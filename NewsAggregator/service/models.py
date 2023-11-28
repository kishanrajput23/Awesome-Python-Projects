from django.db import models


class NewsSourceModel(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    code = models.CharField(max_length=3, null=False, blank=False, unique=True)

    top_stories_url = models.URLField(null=False, blank=False)
    sports_url = models.URLField(null=False, blank=False)
    entertainment_url = models.URLField(null=False, blank=False)
    business_url = models.URLField(null=False, blank=False)
    tech_url = models.URLField(null=False, blank=False)

    def __str__(self):
        return f'{self.name} - {self.code}'


class UrlModel(models.Model):
    url = models.URLField(null=False, blank=False)
    news_source = models.ForeignKey(NewsSourceModel, on_delete=models.CASCADE, null=False, blank=False)

    keywords = models.TextField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    title = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return f'{self.news_source.name} - {self.url}'


class CategoryUrlsModel(models.Model):
    NEWS_CAT_CHOICES = (
        ('TPS', 'Top Stories'),
        ('TCH', 'Technology'),
        ('SPR', 'Sports'),
        ('BSN', 'Business'),
        ('ENT', 'Entertainment'),
    )
    news_cat = models.CharField(max_length=3, choices=NEWS_CAT_CHOICES, null=False, blank=False, \
        unique=True)
    urls = models.ManyToManyField(UrlModel, blank=False)

    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.news_cat