from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    product = models.CharField(max_length=200)
    payment_slip = models.FileField(upload_to='payments/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.lastname} – {self.product}"
