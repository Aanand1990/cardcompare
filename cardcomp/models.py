from django.db import models


class Card(models.Model):
    card_name = models.CharField(max_length=200)
    bank_list = (('Axis_Bank', 'Axis_Bank'),
                 ('ICICI_Bank', 'ICICI_Bank'),
                 ('HDFC_Bank', 'HDFC_Bank'),
                 ('SBI_Bank', 'SBI_Bank'),
                 ('KOTAK_Bank', 'KOTAK_Bank'),
                 ('AMERICAN_EXPRESS_Bank', 'AMERICAN_EXPRESS_Bank'),
                 ('YES_Bank', 'YES_Bank'),
                 ('Standard_Chartered_Bank', 'Standard_Chartered_Bank'),
                 ('IndusInd_Bank', 'IndusInd_Bank'),
                 ('RBL_Bank', 'RBL_Bank'),
                 ('PNB_Bank', 'PNB_Bank'),
                 ('IDFC_First_Bank', 'IDFC_First_Bank'),
                 ('Indian_Bank', 'Indian_Bank'),
                 ('BOI_Bank', 'BOI_Bank'),
                 ('IDBI_Bank', 'IDBI_Bank'),
                 ('CITI_Bank', 'CITI_Bank'),
                 ('Canara_Bank', 'Canara_Bank'))
    bank = models.CharField(max_length=200, choices=bank_list, default='sbi')
    joining_fees = models.FloatField()
    joining_fees_remark = models.CharField(max_length=200, blank=True)
    annual_fees = models.FloatField()
    annual_fees_remark = models.CharField(max_length=200, blank=True)
    welcome_benefit = models.TextField(max_length=500, blank=True)


class Offer(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    offer_type = (
        ('Grocery', 'Grocery'),
        ('food', 'food'),
        ('online_shopping', 'online_shopping'),
        ('utility_bill', 'utility_bill'),
        ('fuel', 'fuel'),
        ('movies', 'movies'),
        ('airline', 'airline'),
        ('other_features', 'other_features'),
    )
    offer_spec = models.CharField(max_length=200, choices=offer_type, default='other_features')
    offer_spec_abt = models.CharField(max_length=200, blank=True)
    offer_spec_per = models.FloatField()
    offer_spec_max_upto = models.FloatField()
    offer_spec_freq = models.FloatField()
    offer_spec_remark = models.TextField(max_length=500, blank=True)
