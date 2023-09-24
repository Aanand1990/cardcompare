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
    annual_fees = models.FloatField()
    welcome_benefit = models.TextField(max_length=500, blank = True)
