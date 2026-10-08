from django.db import models
class Job(models.Model):
    title = models.CharField(max_length = 200)
    company = models.CharField(max_length=200)
    salary = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        indexes = [
            models.Index(fields = ['created_at']),
        ]

    def __str__ (self):
        return f"{self.title}-{self.company}"
# Create your models here.
