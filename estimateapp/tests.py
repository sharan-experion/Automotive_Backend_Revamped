from django.test import TestCase
import os
from rest_framework.test import APITestCase
from rest_framework import status


class TestProduct(APITestCase):
     def setUp(self):
        super(TestProduct, self).setUp()
        self.authenticate()
    
        def test_products(self):
            response = self.client.get("/getestimateproducts/")
            print("response", response.status_code)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
# Create your tests here.
