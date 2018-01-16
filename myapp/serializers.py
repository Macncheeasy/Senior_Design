
from myapp.models import Profiles
from rest_framework import serializers

#Serializers allow complex data such as querysets and model instances to be 
#converted to native python datatypes that can then be rendered into JSON or XML files

#HyperlinkedModelSerializer uses hyperlinks to represent relationships

class ProfilesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profiles
        fields = ('url','name', 'milk','sugar', 'run')
