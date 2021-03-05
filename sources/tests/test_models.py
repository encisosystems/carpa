from django.test import TestCase, tag
from sources.models import ParcelOwner, Parcel, Driver, Vehicle


@tag('vehicles')
class TestVehicles(TestCase):
    fixtures = ['test/vehicles.json']

    def setUp(self):
        self.queryset = Vehicle.objects.all()
        self.vehicle = Vehicle.objects.get(pk=10000)

    def test_query_vehicle(self):
        vehicle_status = self.vehicle.is_active
        self.assertIs(vehicle_status, True)

    def create_vehicle(self):
        new_vehicle = Vehicle.objects.create(
            is_active=True,
            plate='T24680',
            model=2005,
            brand='Ford',
            details='it´s a particular vehicle'
        )
        self.assertEqual(new_vehicle.plate, 'T23680')

    def delete_vehicle(self):
        self.vehicle.delete()
        self.assertNotIn(self.vehicle, self.queryset)
