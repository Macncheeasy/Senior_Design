import time
import datetime
import sqlite3
import spidev #tightdev.net/SpiDev_Doc.pdf for info 
			  #~ https://www.raspberrypi-spy.co.uk/2013/10/analogue-sensors-on-the-raspberry-pi-using-an-mcp3008/
import RPi.GPIO as GPIO

# Initialize SQLite
con = sqlite3.connect('db.sqlite3') #connecting to the database, this is called 'db.sqlite3'
cur = con.cursor() #this is used to perform SQL commands, by calling cur, connectiong to the "con" database and writing or reading from it

# LDR channel on MCP3008

#LIGHT_CHANNEL = 0

# GPIO Setup
GPIO.setmode(GPIO.BOARD) #this sets the board up in BCM mode which will be the way to identify the pins within the program
						#https://raspberrypi.stackexchange.com/questions/12966/what-is-the-difference-between-board-and-bcm-for-gpio-pin-numbering
						#look at numbers after GPIO
LIGHT_PIN = 13

# Open SPI bus #SPI or Serial Peripheral Interface is a communication protocol used to transfer data between micro-computers
#this data can be either sensors or actuators, an example could be to use an analog to digital converter

#~ spi = spidev.SpiDev()
#~ spi.open(0, 0) #open SPI port 0, device 0

#~ # Light Level Threshold
#~ threshold = 100

# Function to read LDR connected to MCP3008

#~ def readLDR():
    #~ light_level = ReadChannel(LIGHT_CHANNEL)
    #~ lux = ConvertLux(light_level, 2)
    #~ return lux

# Function to convert LDR reading to Lux
#~ def ConvertLux(data, places):
    #~ R = 10 #10k-ohm resistor connected to LDR
    #~ volts = (data * 3.3) / 1023
    #~ volts = round(volts, places) #rounds a value 'volts' , to a certain amount of decimal places 'places' is called in when using the function
    #~ lux = 500 * (3.3 - volts) / (R * volts)
    #~ return lux

# Function to read SPI data from MCP3008 chip

#~ def ReadChannel(channel):
    #~ adc = spi.xfer2([1, (8 + channel) << 4, 0]) #transfer one byte
    #~ data = ((adc[1]&3) << 8) + adc[2]
    #~ return data


# Get current mode from DB
def getsugarpref():
    print('getsugarpref')
    cur.execute('SELECT * FROM myapp_profiles') #this selects all of the fields available in the table, if want specific use SELECT column1, column2 FROM table_name
    data = cur.fetchone()  # (1, u'auto') #This method retrieves the next row of a query result set and returns a single sequence or None if no more rows available
    return data[2]

# Get current state from DB
def getmilkpref():
    print('getmilkpref')
    cur.execute('SELECT * FROM myapp_profiles')
    data = cur.fetchone()  # (1, u'on')
    return data[1]

#~ this is designed to get the value, either 0 or 1, which is whether or not to "Make the coffee"
def getRun():
    print('getRun')
    cur.execute('SELECT * FROM myapp_profiles') #this selects all of the fields available in the table, if want specific use SELECT column1, column2 FROM table_name
    data = cur.fetchone()# (1, u'on')
    #~ print(data)
    return data[3]

#~ This is used to reset the counter 'Run' back to zero after the process has been done
#~ the reason for this is so after someone "orders coffee" the product will not dispense again until
#it has to or is prompted by the API
def setRun():
    query = 'UPDATE myapp_profiles set run = 0'
    cur.execute(query)
    #~ dont really need just a check (code below)
    #~ For these databases the 1 i.e. the first entry takes the place holder for the [0]


# Store current state in DB
def setCurrentState(val):
    query = 'UPDATE myapp_profiles set name = "'+val+'"' #Update statement updates columns of existing rows in the named table
													#set clause indicated which columns to modify and the values they should be given
    cur.execute(query)   #Executes this query, makes it happen!

def switchOnLight(PIN):
    GPIO.setup(PIN, GPIO.OUT) #Similar to arduino this declares what the pin is for, in this case Pin number "PIN" will be set as an Output
    GPIO.output(PIN, 1) #This sets the Pin to a HIGH or on poisition, you can also use GPIO.High instead of True or 1

def switchOffLight(PIN):
    GPIO.setup(PIN, GPIO.OUT)
    GPIO.output(PIN, 0)

    # Controller main function
def runController():
    run = getRun();
     
    if run == 1:
    #~ if the count is 1 run this 
		milkpref = getmilkpref()
		if milkpref == 'yes':
			print 'Yes Milk'
		elif milkpref == 'no':
			print 'No Milk'
		sugarpref = getsugarpref()
		if sugarpref == 'yes':
			print('Yes Sugar')
			#~ setRun() #issue with this function wont let other buttons write to DB, causes error in home
			#~ make the count equal to zero
		elif sugarpref == 'no':
			print('No Sugar')
			#~ setRun()
			#~ make the count equal to zero

	
    return True

while True:
    try:
        runController()
        time.sleep(5)
    except KeyboardInterrupt:
        
        #~ spi.close() #disconnects the object from the interface
        
        GPIO.cleanup() #clean up all the ports used, however only affects any ports that I have set in the current program, resets back to input mode
						#this makes it safe because if u have a port set to HIGH as an output and accidently connect to ground, would short the circuit and possibly fry it
						#Inputs can handle either 0V or 3.3V so its safer to leave ports as inputs
        exit()
