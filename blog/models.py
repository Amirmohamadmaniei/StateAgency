from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from account.models import CustomUser


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self):
        self.slug = slugify(self.title)
        super(Category, self).save()


class Blog(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img/blog')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='blogs')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blogs')
    description = models.TextField()
    view = models.IntegerField(default=0)
    slug = models.SlugField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self):
        self.slug = slugify(self.title)
        super(Blog, self).save()

    def get_absolute_url(self):
        return reverse('blog:detail_blog', kwargs={'slug': self.slug})

    def get_date_created(self):
        return f'{self.created.day} {self.created.month}. {self.created.year}'


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    description = models.TextField()
    pattern = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
