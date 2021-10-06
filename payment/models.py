from django.db import models

# Create your models here.
class Payment(models.Model):
    method = models.CharField(max_length=200)
    account_number = models.CharField(max_length=200)
    account_name = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"

