from django.db import models

# 1. Engagement Post Model
class EngagementPost(models.Model):
    POST_TYPES = (
        ('video', 'Video Reel'),
        ('story', 'Story'),
    )

    tenant_id = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    post_type = models.CharField(max_length=50, choices=POST_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title} ({self.post_type})'


# 2. Engagement Post Content Model
class EngagementPostContent(models.Model):
    post = models.ForeignKey(EngagementPost, on_delete=models.CASCADE, related_name='contents')
    content_url = models.URLField(max_length=500)

    def __str__(self):
        return f'Content for {self.post.title}'


# 3. Engagement Post Product Model
class EngagementPostProduct(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.URLField(max_length=500)
    sku = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# 4. Engagement Post Product Mapping Model
class EngagementPostProductMapping(models.Model):
    post = models.ForeignKey(EngagementPost, on_delete=models.CASCADE, related_name='products')
    product = models.ForeignKey(EngagementPostProduct, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return f'{self.product.name} in {self.post.title}'


# 5. Collection Model
class Collection(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# 6. Engagement Post Collection Mapping Model
class EngagementPostCollection(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='posts')
    post = models.ForeignKey(EngagementPost, on_delete=models.CASCADE, related_name='collections')
    duration_in_seconds = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.post.title} in {self.collection.name}'
