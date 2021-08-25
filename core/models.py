from django.db import models
from django.contrib.auth.models import User


class History(models.Model):
    input_expression = models.CharField(max_length=100)
    output_result = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'histories'

