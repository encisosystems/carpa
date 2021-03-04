from django.test import TestCase, tag
from harvests.models import Bunch, BunchBatch, CategoryBunch, Harvester


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

@tag('bunch')
class TestHarvesters(TestCase):
    fixtures = ['test/harvests.json']

    def setUp(self):
        self.queryset = Bunch.objects.all()
        self.bunch = Bunch.objects.get(pk=10000)
        self.category = CategoryBunch.objects.get(pk=10000)

    def test_query_bunch(self):
        bunch_is_active = self.bunch.is_active
        self.assertEqual(bunch_is_active, True)

    def test_create_bunch(self):
        new_bunch = Bunch.objects.create(
            is_active=True,
            category=self.category,
            weight=20.5
        )
        self.assertEqual(new_bunch.is_active, True)

    def test_update_bunch(self):
        self.bunch.weight = 20.5
        self.bunch.save()
        self.assertEqual(self.bunch.weight, 20.5)

    def test_delete_bunch(self):
        self.bunch.delete()
        self.assertNotIn(self.bunch, self.queryset)
