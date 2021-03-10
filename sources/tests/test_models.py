from django.test import TestCase, tag
from sources.models import ParcelOwner, Parcel, Driver, Vehicle



@tag('parcel')
class TestParcel(TestCase):
    fixtures = ['test/sources.json']

    def setUp(self):
        self.queryset = Parcel.objects.all()
        self.parcel = Parcel.objects.get(pk=10000)

    def test_query_owner(self):
        owner_status = self.parcel.owner.is_active
        self.assertEqual(owner_status, True)

    def test_create_parcel(self):
        new_parcel = Parcel.objects.create(
            is_active=True,
            name='acienda las mercedes',
            owner_id=10000
        )
        self.assertEqual(new_parcel.name, 'acienda las mercedes')

    def test_update_parce(self):
        self.parcel.name='fina buenavista'
        self.parcel.save()
        self.assertEqual(self.parcel.name, 'fina buenavista')

    def test_delete_parcel(self):
        self.parcel.delete()
        self.assertNotIn(self.parcel, self.queryset)


@tag('driver')
class TestDriver(TestCase):
    fixtures = ['test/sourcesDriver.json']

    def setUp(self):
        self.queryset = Driver.objects.all()
        self.driver = Driver.objects.get(pk=10000)

    def test_query_driver(self):
        driver_status = self.driver.is_active
        self.assertEqual(driver_status, True)

    def test_create_driver(self):
        new_driver = Driver.objects.create(
            is_active=True,
            name='Señor X',
            address='742 Evergreen Terrace',
            email='amantedelacomida53@aol.com',
            phone='0',
            web='compumundohypermegared.net'
        )
        self.assertEqual(new_driver.name, 'Señor X')

    def test_update_driver(self):
        self.driver.name = 'El baron de la cerveza'
        self.driver.save()
        self.assertEqual(self.driver.name, 'El baron de la cerveza')

    def test_delete_driver(self):
        self.driver.delete()
        self.assertNotIn(self.driver, self.queryset)


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

    def test_update_driver(self):
        self.vehicle.plate = 'MQTT09'
        self.vehicle.save()
        self.assertEqual(self.vehicle.plate, 'MQTT09')
