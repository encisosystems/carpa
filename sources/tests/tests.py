from sources.tests.test_models import *
from sources.models import ParcelOwner



@tag('parcelowner')
class TestParcelOwner(TestCase):
    fixtures = ['test/parcelown.json']

    def setUp(self):
        self.parcel_owner = ParcelOwner.objects.get(pk=10000)
        self.queryset = ParcelOwner.objects.all()

    def test_query_parcel_own(self):
        parcel_owner_first_name = self.parcel_owner.first_name
        self.assertEqual(parcel_owner_first_name, 'Juan')

    def test_create_parcel_own(self):
        test_parcel_owner = ParcelOwner.objects.create(
            first_name='Luz',
            last_name='Posada',
            organization='Organization 2',
            address_1='calle falsa 123',
            address_2='calle false 234',
            email='c@g.com',
            phone='22553665',
            website='www.g.com'
        )
        self.assertIsInstance(test_parcel_owner, ParcelOwner)

    def test_update_parcel_own(self):
        self.parcel_owner.first_name = 'Luis'
        self.parcel_owner.save()
        self.assertEqual(self.parcel_owner.first_name, 'Luis')

    def test_delete_category(self):
        self.parcel_owner.delete()
        self.assertNotIn(self.parcel_owner, self.queryset)
