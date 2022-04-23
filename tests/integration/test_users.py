# -*- coding: utf-8 -*-
import json
import pytest
from django.urls import reverse

from tests import factories as f
from users import models

pytestmark = pytest.mark.django_db

##############################
## Create user
##############################

def test_users_create_through_standard_api(client):
    user = f.UserFactory.create(is_superuser=True)

    url = reverse('users-list')
    data = {}

    response = client.post(url, json.dumps(data), content_type="application/json")
    assert response.status_code == 405

    client.login(user)

    response = client.post(url, json.dumps(data), content_type="application/json")
    assert response.status_code == 405


##############################
## Test sanitize full name
##############################

INVALID_NAMES = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod",
    "an <script>evil()</script> example",
    "http://testdomain.com",
    "https://testdomain.com",
    "Visit http://testdomain.com",
]

@pytest.mark.parametrize("full_name", INVALID_NAMES)
def test_sanitize_invalid_user_full_name(client, full_name):
    user = f.UserFactory.create(full_name="test_name")
    url = reverse('users-detail', kwargs={"pk": user.pk})

    client.login(user)
    data = {"full_name": full_name}
    response = client.patch(url, json.dumps(data), content_type="application/json")
    assert response.status_code == 400

VALID_NAMES = [
    "martin seamus mcfly"
]

@pytest.mark.parametrize("full_name", VALID_NAMES)
def test_sanitize_valid_user_full_name(client, full_name):
    user = f.UserFactory.create(full_name="test_name")
    url = reverse('users-detail', kwargs={"pk": user.pk})

    client.login(user)
    data = {"full_name": full_name}
    response = client.patch(url, json.dumps(data), content_type="application/json")
    assert response.status_code == 200


