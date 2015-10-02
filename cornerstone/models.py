from django.db import models
from mptt.models import MPTTModel,TreeForeignKey


class CornerstoneUserProfile(MPTTModel):
    GUID = models.UUIDField()
    User_ID = models.IntegerField()
    First_Name = models.CharField(max_length=50)
    Last_Name  = models.CharField(max_length=50)
    Manager_ID = models.IntegerField(null=True)
    parent = TreeForeignKey('self', null=True, blank=True, db_index=True, related_name='children')# parent is nothing but manager guid
    def __str__(self):
        return self.First_Name

