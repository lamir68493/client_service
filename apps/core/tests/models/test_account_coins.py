import unittest

from apps.core.models import AccountCoins


class AccountCoinsTests(unittest.TestCase):
    def setUp(self):
        self.client_data = {
            'amount': 100,
        }
        self.account = AccountCoins.objects.create(**self.client_data)

    def test_create_account_coins(self):
        account = AccountCoins.objects.get(id=self.account.id)
        #
        self.assertEqual(account.amount, self.client_data['amount'])

    def test_update_account_coins(self):
        self.account.amount = 150
        self.account.save()
        account = AccountCoins.objects.get(id=self.account.id)
        self.assertEqual(account.amount, 150)

    def test_delete_account_coins(self):
        account_id = self.account.id
        self.account.delete()
        with self.assertRaises(AccountCoins.DoesNotExist):
            AccountCoins.objects.get(id=account_id)

    def tearDown(self):
        AccountCoins.objects.all().delete()
