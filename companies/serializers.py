from rest_framework import serializers
from .models import Stock

class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model=Stock
        # to return specific data -> fields=('ticker','volume')
        fields = '__all__'
