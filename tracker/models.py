from django.db import models
import uuid

# Create your models here.

class BaseModel(models.Model):
    uuid = models.UUIDFIELD(default = uuid.uuid4, editable=False, unique=True)
    created_at = models.DateField(auto_created=True)
    updated_at = models.DateField(auto_now_add= True)

    class Meta:
        abstract = True

class Transaction(BaseModel):
    description = models.CharField(max_length = 100)
    





