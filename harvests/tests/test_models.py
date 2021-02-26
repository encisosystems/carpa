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
