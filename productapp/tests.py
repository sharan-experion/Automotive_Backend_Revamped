from django.test import TestCase
import pytest
from django.urls import reverse

# Create your tests here.
@pytest.mark.django_db
def test_product(client):
    url=reverse('category1')
    response=client.get(url)
    assert response.status_code ==201