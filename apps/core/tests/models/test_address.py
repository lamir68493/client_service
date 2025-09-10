import unittest

from apps.core.models import Address


class AddressTests(unittest.TestCase):
    def setUp(self):
        self.address_data = {
            'region': 'Kyivska',
            'district': 'Shevchenkivskyi',
            'city': 'Kyiv',
            'street': 'Street1',
            'house': '10',
            'apartment': '3'
        }
        self.address = Address.objects.create(**self.address_data)

    def test_create_address(self):
        address = Address.objects.get(id=self.address.id)
        #
        for field, value in self.address_data.items():
            self.assertEqual(getattr(address, field), value)

    def test_update_address(self):
        new_data = {
            'region': 'Cherkaska',
            'district': 'Sosnivskyi',
            'city': 'Cherkasy',
            'street': 'Street2',
            'house': '20',
            'apartment': '5'
        }
        #
        for field, value in new_data.items():
            setattr(self.address, field, value)
        self.address.save()
        #
        address_updated = Address.objects.get(id=self.address.id)
        for field, value in new_data.items():
            self.assertEqual(getattr(address_updated, field), value)

    def test_delete_address(self):
        address_id = self.address.id
        self.address.delete()
        with self.assertRaises(Address.DoesNotExist):
            Address.objects.get(id=address_id)

    def tearDown(self):
        Address.objects.all().delete()
