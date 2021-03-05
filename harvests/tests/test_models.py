from django.test import TestCase, tag
from harvests.models import Bunch, BunchBatch, CategoryBunch, Harvester
from sources.models import Parcel, Vehicle


@tag('categories')
class TestCategories(TestCase):
    fixtures = ['test/harvests.json']

    def setUp(self):
        self.category = CategoryBunch.objects.get(pk=10000)
        self.queryset = CategoryBunch.objects.all()

    def test_query_category(self):
        category_name = self.category.name
        self.assertEqual(category_name, 'maturity : green')

    def test_create_category(self):
        test_category = CategoryBunch.objects.create(
            name='test-category',
        )
        self.assertIsInstance(test_category, CategoryBunch)

    def test_update_category(self):
        self.category.name = 'new name'
        self.category.save()
        self.assertEqual(self.category.name, 'new name')

    def test_delete_category(self):
        self.category.delete()
        self.assertNotIn(self.category, self.queryset)


@tag('harvesters')
class TestHarvesters(TestCase):
    fixtures = ['test/harvesters.json']

    def setUp(self):
        self.queryset = Harvester.objects.all()
        self.harvester = Harvester.objects.get(pk=10000)

    def test_query_harvester(self):
        harvester_status = self.harvester.is_active
        self.assertIs(harvester_status, True)

    def test_create_harvester(self):
        new_harvester = Harvester.objects.create(
            is_active=True,
            name='Ricardo',
            address='Calle 4 #25-04'
        )
        self.assertEqual(new_harvester.name, 'Ricardo')

    def test_delete_harvester(self):
        self.harvester.delete()
        self.assertNotIn(self.harvester, self.queryset)


@tag('bunchbatch')
class TestBunchBatch(TestCase):
    fixtures = ['test/BunchBatch.json']

    def setUp(self):
        self.queryset = BunchBatch.objects.all()
        self.bunchbatch= BunchBatch.objects.get(pk=10000)
        self.parcel = Parcel.objects.get(pk=10000)
        self.vehicle = Vehicle.objects.get(pk=10000)
        self.bunch= Bunch.objects.get(pk=10000)     
        self.harvester = Harvester.objects.get(pk=10000)

    def test_query_bunchbatch(self):
        bunchbatch_status = self.bunchbatch.is_active
        self.assertIs(bunchbatch_status, True)

    def test_create_bunchbatch(self):
        new_bunchbatch = BunchBatch.objects.create(            
        	notes="test-create",
        	delivery_time= "2021-03-01T17:00:00Z",
        	parcel= self.parcel,
        	vehicle= self.vehicle,        	
        )
        new_bunchbatch.bunches.add(self.bunch);
        new_bunchbatch.harvesters.add(self.harvester);
        self.assertEqual( new_bunchbatch.harvesters.get(pk=10000).name, 'Andres Cabanzo')

    def test_delete_bunchbatch(self):
        self.bunchbatch.delete()
        self.assertNotIn(self.bunchbatch, self.queryset)


           

