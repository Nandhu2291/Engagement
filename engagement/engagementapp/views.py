from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from engagementapp.models import EngagementPost, EngagementPostProductMapping
from engagementapp.serializers import EngagementPostSerializer
from engagementapp.models import EngagementPostProduct
from engagementapp.serializers import EngagementPostProductSerializer
from engagementapp.models import Collection, EngagementPostCollection
from engagementapp.serializers import CollectionSerializer, EngagementPostCollectionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from engagementapp.models import EngagementPostCollection
from engagementapp.serializers import EngagementPostContentSerializer
from engagementapp.models import EngagementPostProductMapping
from engagementapp.serializers import EngagementPostProductMappingSerializer

class EngagementPostViewSet(viewsets.ViewSet):
    def list(self, request):
        tenant_id = request.query_params.get('tenant_id')
        if not tenant_id:
            return Response({"error": "tenant_id parameter is required"}, status=400)
        
        posts = EngagementPost.objects.filter(tenant_id=tenant_id)
        serializer = EngagementPostSerializer(posts, many=True)
        return Response(serializer.data)
    

class EngagementPostProductViewSet(viewsets.ModelViewSet):
    queryset = EngagementPostProduct.objects.all()
    serializer_class = EngagementPostProductSerializer

class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

    def perform_create(self, serializer):
        collection = serializer.save()
        post_ids = self.request.data.get('post_ids', [])
        for post_id in post_ids:
            EngagementPostCollection.objects.create(collection=collection, post_id=post_id)

class TopViewedPostsAPIView(APIView):
    def get(self, request):
        tenant_id = request.query_params.get('tenant_id')
        top_posts = EngagementPostCollection.objects.filter(post__tenant_id=tenant_id).order_by('-duration_in_seconds')[:5]
        serializer = EngagementPostContentSerializer(top_posts, many=True)
        return Response(serializer.data)
    
class TopViewedProductsAPIView(APIView):
    def get(self, request):
        tenant_id = request.query_params.get('tenant_id')
        top_products = EngagementPostProductMapping.objects.filter(post__tenant_id=tenant_id).order_by('-post__collections__duration_in_seconds')[:5]
        serializer = EngagementPostProductMappingSerializer(top_products, many=True)
        return Response(serializer.data)
