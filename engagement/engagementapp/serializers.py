from rest_framework import serializers
from engagementapp.models import (EngagementPost, EngagementPostContent, EngagementPostProduct,
                     Collection, EngagementPostCollection, EngagementPostProductMapping)

class EngagementPostSerializer(serializers.ModelSerializer):
    contents = serializers.StringRelatedField(many=True)
    products = serializers.StringRelatedField(many=True)

    class Meta:
        model = EngagementPost
        fields = ['id', 'title', 'post_type', 'description', 'tenant_id', 'contents', 'products']

class EngagementPostProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngagementPostProduct
        fields = '__all__'

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'

class EngagementPostContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngagementPostContent
        fields = ['post', 'content_url']

class EngagementPostCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngagementPostCollection
        fields = ['collection', 'post', 'duration_in_seconds']

class EngagementPostProductMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngagementPostProductMapping
        fields = ['post', 'product']
