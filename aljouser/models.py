from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.
class Aljouser(models.Model):
    foodname = models.CharField('FOOD_NAME', max_length=50, blank=False)
    recipe = models.TextField('RECIPE', blank=False)
    brand = models.CharField('BRAND', max_length=30, blank=False, null=True)
    role = models.CharField('ROLE', max_length=10, blank=False, null=True)
    image = models.ImageField('IMAGE', blank=False, null=True, upload_to='images/%Y/%m')
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(359,359)], format='JPEG')
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)
    tags = TaggableManager(blank=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_postsUser', blank=True)

    class Meta:
        verbose_name = 'aljouser'
        verbose_name_plural = 'aljousers'
        db_table = 'aljouser'
        ordering = ('-create_dt',)

    def get_absolute_url(self):
        return reverse('aljouser:detail', args=[self.id])

    @property
    def count_like_users(self):
        return self.like_users.count()

    def __str__(self):
        return self.foodname

class CommentUser(models.Model):
    aljo = models.ForeignKey(Aljouser, on_delete=models.CASCADE)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    content = models.CharField('COMMENT', max_length=200)
    create_dt = models.DateTimeField("CREATE DATE", auto_now_add=True, null=True)
    modify_dt = models.DateTimeField("MODIFY DATE", auto_now=True, null=True)

    class Meta:
        ordering = ['-create_dt']

    def __str__(self):
        return self.content