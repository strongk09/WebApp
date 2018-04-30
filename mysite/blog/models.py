from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=40)
    body = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=40)

    class Meta:
        db_table = 'POSTFIX'


class Storage_Location(models.Model):
    Store_local = models.CharField(max_length=40, verbose_name='Storage Location Name')
    Store_add = models.CharField(max_length=40, verbose_name='Storage Location Address')
    Store_room = models.CharField(max_length=40, verbose_name='Storage Location Room')

    class Meta:
        db_table = 'storage_location'


YESNO = (
    ('YES', 'YES'),
    ('NO', 'NO')
)


class Item(models.Model):
    Tag_num = models.CharField(max_length=5, verbose_name='Tag Number')
    NOA_num = models.CharField(max_length=100, verbose_name='Aproval Bill Number')
    Item_name = models.CharField(max_length=100, verbose_name='Item Name')
    Item_des = models.TextField(verbose_name='Item Description')
    Manf_name = models.CharField(max_length=100, verbose_name='Manufaturer Name')
    Model_num = models.CharField(max_length=100, verbose_name='Model Number')
    Ser_num = models.CharField(max_length=100, verbose_name='Serial Number')
    Item_pic = models.CharField(max_length=100, verbose_name='Item Picture')  # upload picture
    Seller_name = models.CharField(max_length=100, verbose_name='Seller Name')
    Pur_date = models.DateTimeField(verbose_name='Purchase Date')
    Pur_price = models.CharField(max_length=100, verbose_name='Purchase Price')  # dollar ammount
    Warranty = models.CharField(max_length=100, choices=YESNO, verbose_name='Warranty')  # drop down
    War_end_date = models.DateTimeField(max_length=100, verbose_name='Warranty End Date')
    FOC_cat = models.CharField(max_length=100, verbose_name='FOC Replacement')

    class Meta:
        db_table = 'items'


class RSO(models.Model):
    RSO_name = models.CharField(max_length=40, verbose_name='RSO Name')
    RSO_prez = models.CharField(max_length=40, verbose_name='RSO President')
    Prez_ph = models.CharField(max_length=12, verbose_name='President Phone Number')
    Prez_email = models.CharField(max_length=40, verbose_name='President Email')
    RSO_advisor = models.CharField(max_length=40, verbose_name='RSO Advisor')
    Advisor_ph = models.CharField(max_length=40, verbose_name='Advisor Phone Number')
    Advisor_email = models.CharField(max_length=40, verbose_name='Advisor Email')

    class Meta:
        db_table = 'RSO'


def __str__(self):
    return self.title
