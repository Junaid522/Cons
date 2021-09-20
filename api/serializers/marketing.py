from rest_framework import serializers
from constructor import models


class MarketingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MarketingCard
        fields = ['id', 'card_type', 'card_img', 'heading', 'short_description']


class MarketingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MarketingCard
        fields = ['id', 'card_type', 'card_img', 'heading', 'short_description', 'content']
