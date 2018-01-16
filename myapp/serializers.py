from myapp.models import Mode
from rest_framework import serializers

#Serializers allow complex data such as querysets and model instances to be 
#converted to native python datatypes that can then be rendered into JSON or XML files

#HyperlinkedModelSerializer uses hyperlinks to represent relationships

class ModeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mode
        fields = ('url','name', 'milk','sugar', 'run')

