from rest_framework import serializers
from .models import Dummy
class DummySerializer(serializers.ModelSerializer):
    dummy = serializers.SerializerMethodField()
    class Meta:
        fields = ["title","content","price","getDiscount","dummy"]
        model = Dummy
        
    def get_dummy(self,obj):
        return obj.price