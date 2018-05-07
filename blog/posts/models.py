from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField()
    image = models.ImageField(upload_to='media/')
    text = models.TextField()

    def __str__(self):
        return self.title

    def pub_date(self):
        return self.created_at.strftime('%d-%m-%Y %H-%M')

    def text_150(self):
        return self.text[:150]
