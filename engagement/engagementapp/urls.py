from rest_framework.routers import DefaultRouter
from engagementapp.views import (EngagementPostViewSet, EngagementPostProductViewSet, CollectionViewSet, 
                    TopViewedPostsAPIView, TopViewedProductsAPIView)

router = DefaultRouter()
router.register(r'posts', EngagementPostViewSet, basename='engagementpost')
router.register(r'products', EngagementPostProductViewSet, basename='product')
router.register(r'collections', CollectionViewSet, basename='collection')