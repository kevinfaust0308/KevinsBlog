from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='media/')
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_pretty_pub_date(self):
        return self.pub_date.strftime('%B %d %Y')

    def get_summary(self):
        summary = self.body[:100]
        if len(self.body) > 100:
            summary += '...'
        return summary
