from django.db import models
from django import forms


class Contact(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    patronymic = models.CharField(max_length=40, null=True)
    birth_date = models.DateField(null=True)
    citizenship = models.CharField(max_length=40, null=True)
    website = models.CharField(max_length=40, null=True)
    email = models.CharField(max_length=40, null=True)
    place_of_work = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    street = models.CharField(max_length=50, null=True)
    zip_code = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = "contact"


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    note = models.CharField(max_length=50, null=True)
    country_code = models.CharField(max_length=5, null=True)
    operator_code = models.CharField(max_length=5, null=True)

    def __str__(self):
        return self.phone_number

    class Meta:
        db_table = "phone"


class Attachment(models.Model):
    id = models.IntegerField(primary_key=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=50)
    upload_date = models.DateField()
    note = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.file_name

    class Meta:
        db_table = "attachment"


class Group(models.Model):
    id = models.IntegerField(primary_key=True)
    group_name = models.CharField(max_length=50)
    contacts = models.ManyToManyField(Contact)


class ContactForm(forms.ModelForm):
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'patronymic', 'birth_date', 'city', 'country', 'citizenship']