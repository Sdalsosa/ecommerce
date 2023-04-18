from django.db import models


class ContactUs(models.Model):

    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=False)
    subject = models.CharField(max_length=255, null=True, blank=False)
    message = models.TextField(null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Contact us"

    def __str__(self):
        return self.name
