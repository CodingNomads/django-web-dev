from django.db import models
from django.contrib.auth.models import User


# This Profile class extends the default Django User model.
# If you want to learn more about it, read the tutorial, otherwise accept and move on :)
class DjeeterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    follows = models.ManyToManyField('self',
                                     related_name='followed_by',
                                     symmetrical=False)

    def __str__(self):
        return self.user.username


User.djeeterprofile = property(lambda u: DjeeterProfile.objects.get_or_create(user=u)[0])
