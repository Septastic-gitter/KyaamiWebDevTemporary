from sre_constants import CATEGORY
from unicodedata import category
from django.db import models
import uuid
#from ..User.models import User

# Create your models here.
class Admin(models.Model):
    ROLES = (
        ('System Admin', 'System Admin'), 
        ('Management Team','Management Team'), 
        ('Site Admin','Site Admin'),
    )

    admin_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    role = models.CharField(max_length=200, default=0, choices=ROLES)
    cell_no = models.CharField(max_length=16)
    email = models.EmailField(max_length=32)
    admin= models.CharField(max_length=16)

class Log_Record(models.Model):
    location = models.CharField(max_length=16)
    device = models.CharField(max_length=16)
    username = models.CharField(max_length=16)
    time = models.DateTimeField()
#    user_id= models.ForeignKey(User, on_delete=models.CASCADE)
    login_no = models.UUIDField(primary_key=True,default = uuid.uuid4)

class Purchase(models.Model):
    distributor = models.CharField(max_length=16)
    provider = models.CharField(max_length=16)
    purchase_time = models.DateTimeField()
    purchase_details = models.TextField()
#    user_id= models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_id = models.UUIDField(primary_key=True,default = uuid.uuid4)

class Comment(models.Model):
    reference = models.URLField()
    comment = models.TextField()
#    commenter_id= models.ForeignKey(User, on_delete=models.CASCADE)
    comment_id = models.UUIDField(primary_key=True,default = uuid.uuid4)

class Order(models.Model):
    #item = models.ImageField()#dont know blob field
    link = models.URLField()
    provider = models.CharField(max_length=16)
    recipient = models.CharField(max_length=16)
    order_id = models.UUIDField(primary_key=True,default = uuid.uuid4)

class To_do_list(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4)
    text = models.CharField(max_length=64)
    deadline = models.DateField()
    done = models.BooleanField(default=False)

class Abuse_reports(models.Model):
    VIOLATION=( 
        ('Spam', 'Spam'),
        ('Copyright Violation', 'Copyright Violation'),
        ('Flagged Content', 'Flagged Content'),
    )
    id = models.UUIDField(primary_key=True, default = uuid.uuid4)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    date =  models.DateField()
    violation = models.CharField(max_length=200, default = 0, choices=VIOLATION)
    by_user = models.BooleanField()
    by_system = models.BooleanField()

class Bug_reports(models.Model):
    CATEGORY = (
        ('Data Loss', 'Data Loss'),
        ('Profile Registration', 'Profile Registration'),
        ('Messaging', 'Messaging'),
    )

    id = models.UUIDField(primary_key=True, default = uuid.uuid4)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    category = models.CharField(max_length=300, default=0, choices=CATEGORY)
    detail = models.TextField()
    