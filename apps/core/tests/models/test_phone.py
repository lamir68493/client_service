import unittest

from apps.core.models import Phone


class PhoneTests(unittest.TestCase):
    def setUp(self):
        self.phone_data = {
            'phone': '111',
        }
        self.phone = Phone.objects.create(**self.phone_data)

    def test_create_phone(self):
        phone = Phone.objects.get(id=self.phone.id)
        for field, value in self.phone_data.items():
            self.assertEqual(getattr(phone, field), value)

    def test_update_phone(self):
        new_data = {
            'phone': '222',
        }
        #
        for field, value in new_data.items():
            setattr(self.phone, field, value)
        self.phone.save()
        #
        phone_updated = Phone.objects.get(id=self.phone.id)
        for field, value in new_data.items():
            self.assertEqual(getattr(phone_updated, field), value)

    def test_delete_phone(self):
        phone_id = self.phone.id
        self.phone.delete()
        with self.assertRaises(Phone.DoesNotExist):
            Phone.objects.get(id=phone_id)

    def tearDown(self):
        Phone.objects.all().delete()
