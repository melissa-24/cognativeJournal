from django.db import models
from django.db.models.deletion import CASCADE

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=45)

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, unique=True, default=0, on_delete=CASCADE)
    image = models.ImageField(upload_to='profileImgs', default='initial.jpg')
    def __str__(self):
        return f'{self.user.username} Profile'

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        User.objects.create(user=instance)
        post_save.connect(create_user_profile, sender=User)

class Category(models.Model):
    category = models.CharField(max_length=45, unique=True)

class Scale(models.Model):
    type = models.IntegerField()
    scaleImg = models.ImageField(upload_to='moods', default='initial.jpg')

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, default=True)
    author = models.ForeignKey(User, related_name='poster', on_delete=CASCADE)
    content = models.TextField()
    depression = models.ForeignKey(Scale, related_name='depressionLevel', on_delete=CASCADE)
    anxiety = models.ForeignKey(Scale, related_name='anxietyLevel', on_delete=CASCADE)
    pain = models.ForeignKey(Scale, related_name='painLevel', on_delete=CASCADE)
    type = models.ManyToManyField(Category, related_name='categories')
    createdOn = models.DateField(auto_now_add=True)
    updatedOn = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-createdOn']

    def __str__(self):
        return self.title