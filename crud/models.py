from django.db import models


class Contact(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    patronymic = models.CharField(max_length=40)
    birth_date = models.DateField()

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = "contact"


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    note = models.CharField(max_length=50)
    country_code = models.CharField(max_length=5)
    operator_code = models.CharField(max_length=5)

    def __str__(self):
        return self.phone_number

    class Meta:
        db_table = "phone"


class Attachment(models.Model):
    id = models.IntegerField(primary_key=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=50)
    upload_date = models.DateField()
    note = models.CharField(max_length=50)

    def __str__(self):
        return self.file_name

    class Meta:
        db_table = "attachment"