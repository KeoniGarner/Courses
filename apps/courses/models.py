from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def validations(self, postData):
        errors = {}
        if len(postData["name"]) < 5:
            errors["name"] = "Course name should be longer than 5 characters!"
        if len(postData["desc"]) < 15:
            errors["desc"] = "Course description should be longer than 15 characters!"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    objects = CourseManager()