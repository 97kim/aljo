from django.db import models
#from django.contrib.auth.models import User
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.urls import reverse
from django.utils.text import slugify
from taggit.managers import TaggableManager

# Create your models here.
class Aljoadmin(models.Model):
    foodname = models.CharField('FOOD_NAME', max_length=50, blank=False)
    slug = models.SlugField('SLUG', unique=True, null=True, allow_unicode=True, help_text='one word for title alias.')
    recipe = models.CharField('RECIPE', max_length=100, blank=False)
    brand = models.CharField('BRAND', max_length=30, blank=False, null=True)
    image = models.ImageField('IMAGE', blank=True, null=True, upload_to='images/%Y/%m')
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(359,359)], format='JPEG')
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)
    tags = TaggableManager(blank=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts', blank=True)

    class Meta:
        verbose_name = 'aljoadmin'
        verbose_name_plural = 'aljoadmins'
        db_table = 'aljoadmin'
        ordering = ('-modify_dt',)

    def get_absolute_url(self):
        return reverse('aljoadmin:detail', args=[self.slug])

    def count_like_users(self):
        return self.like_users.count()

    def __str__(self):
        return self.foodname

    def save(self, *args, **kwargs):
        self.slug = slugify(self.foodname, allow_unicode=True)
        super().save(*args, **kwargs)

class Comment(models.Model):
    aljo = models.ForeignKey(Aljoadmin, on_delete=models.CASCADE)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    content = models.CharField('COMMENT', max_length=200)
    create_dt = models.DateTimeField("CREATE DATE", auto_now_add=True, null=True)
    modify_dt = models.DateTimeField("MODIFY DATE", auto_now=True, null=True)

    class Meta:
        ordering = ['-create_dt']

    def __str__(self):
        return self.content