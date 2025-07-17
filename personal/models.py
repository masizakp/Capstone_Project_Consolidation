from django.db import models

class Contact(models.Model):
    """
    Model representing a contact/order entry.

    :param name: First name of the contact
    :type name: str
    :param lastname: Last name of the contact
    :type lastname: str
    :param email: Email address of the contact
    :type email: str
    :param address: Physical address of the contact
    :type address: str
    :param product: Product ordered
    :type product: str
    :param payment_slip: Optional file upload of the payment slip
    :type payment_slip: File, optional

    :return: String representation combining name, lastname, and product
    :rtype: str
    """
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    product = models.CharField(max_length=200)
    payment_slip = models.FileField(upload_to='payments/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.lastname} – {self.product}"
