from django.test import TestCase
from .models import *


class UserTestCase(TestCase):
    def setUp(self):
        Profile.objects.create(first_name="Testname", last_name="Testname",
                               username="Tester", email="Tester@testmail.com",
                               phone_number="02171353244", is_admin=True,
                               is_active=True, is_staff=True, is_superadmin=True)

# AFTER MIGRATION
#    def test_user_delivery_address(self):
#        address = User_Delivery_Address.objects.create(user=Profile.objects.get(username="Tester"),
#                                                       delivery_street="TestStraße", delivery_house_number="99",
#                                                       delivery_city="TestStadt", delivery_zip_code="53225")
#        self.assertEqual(address.__str__(), "Testname")

#    def test_user_payment_address(self):
#        address = User_Payment_Address.objects.create(user=Profile.objects.get(username="Tester"),
#                                                      delivery_street="ZahlStraße", delivery_house_number="99",
#                                                      delivery_city="TestStadt", delivery_zip_code="53225")
#        self.assertEqual(address.__str__(), "Testname")

    def test_user_credit_card(self):
        creditcard = User_Credit_Card.objects.create(user=Profile.objects.get(username="Tester"),
                                                     owner_first_name="Testfname", owner_last_name="Testfname",
                                                     card_number="647283756482936", expiration_date_month="03",
                                                     expiration_date_year="25", security_code="321")
        self.assertEqual(creditcard.__str__(), "Testname")

    def test_user_paypal(self):
        paypal = User_PayPal.objects.create(user=Profile.objects.get(username="Tester"),
                                            paypal_mail="testpal@paypal.com", paypal_password="testpass")
        self.assertEqual(paypal.__str__(), "Testname")

    def test_user_debit(self):
        debit = User_Debit.objects.create(user=Profile.objects.get(username="Tester"),
                                          debit_first_name="Testfname", debit_last_name="Testlname",
                                          iban="DE4768490010048375453", bic="VR5649604")
        self.assertEqual(debit.__str__(), "Testname")
