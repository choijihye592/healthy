from rest_framework import serializers
from .models import Jbnu

class JbnuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jbnu
        fields = ['id', 'title', 'belt', 'date', 'jurl']