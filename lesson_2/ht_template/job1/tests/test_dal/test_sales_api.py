"""
Tests sales_api.py module.
# TODO: write tests
"""
from unittest import TestCase, mock

# NB: avoid relative imports when you will write your code:
from lesson_2.ht_template.job1.dal.sales_api import get_sales


class GetSalesTestCase(TestCase):
    """
    Test sales_api.get_sales function.
    # TODO: implement
    """
    def test_get_sales_valid_date(self):
        """Test get_sales function."""
        print(get_sales('2022-08-09')[0])

    def test_get_sales_invalid_date(self):
        """Test get_sales function."""
        print(get_sales('2022-009')[0])

    def test_get_sales_no_date(self):
        """Test get_sales function."""
        print(get_sales('')[0])

    def test_get_sales_no_page(self):
        """Test get_sales function."""
        print(get_sales('2022-08-09', page=0)[0])

    def test_get_sales_invalid_page(self):
        """Test get_sales function."""
        print(get_sales('2022-08-09', page='')[0])
