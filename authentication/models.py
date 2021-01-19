from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class ModelBase(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(ModelBase, AbstractUser):
    role = models.CharField(max_length=152)
    relation = models.ForeignKey("self", on_delete=models.DO_NOTHING, null=True, blank=True)

    class Meta:
        db_table = "user"
        verbose_name = "user"
        verbose_name_plural = "users"


class UserDetails(ModelBase):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    roll_no = models.BigIntegerField()
    phone = models.BigIntegerField()