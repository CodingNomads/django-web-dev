from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User,
                             related_name='posts',
                             on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    # this Meta setting allows you to display the posts in order of newest post first
    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return "{0} at {1}: {2}...".format(self.user,
                                           self.created_at,
                                           self.body[:20])
