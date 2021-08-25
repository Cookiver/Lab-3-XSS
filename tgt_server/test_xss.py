from fastapi import testclient

from exercises import ex1, ex2, ex3
from main import app

client = testclient.TestClient(app)


def test_user_profiles():
    response = client.get("/user-profiles?name=donald", headers=dict(accept='application/json'))
    assert response.status_code == 200
    assert all(_['fields']['address'].startswith('132') for _ in response.json().values())


def test_api_update_user_profile():
    #  Get Target's profile_id
    _id = ex2.get_profile_id(client, 'scrooge')
    response = ex2.update_profile(client, _id, dict(
        name='scrooge',
        address='Transient'
    ))
    assert response.status_code == 200
    assert response.json()['fields']['address'] == 'Transient'


def test_reflect_xss():
    """
    Check that the reflection XSS penetration workflow implementation works as expected.

    This test as provided does not include all assertions that will be used to
    assess the method persistent_xss.

    Those that are there are intended to provide immediate feedback.
    """
    response = ex3.reflect_xss(client)

    # Confirm exploit:
    assert ex1.malicious_url in response.text


def test_persistent_xss():
    """
    Check that the persistent XSS workflow implementation works as expected.

    This test as provided does not include all assertions that will be used to
    assess the method persistent_xss.

    Those that are there are intended to provide immediate feedback.
    """

    _id, response = ex3.persistent_xss(client, 'scrooge')

    # Confirm exploit:
    response = client.get(f"/user-profiles/{_id}")
    assert ex1.malicious_url in response.text


def test_officially_xss_hack_user_profile():
    _id, response = ex3.persistent_xss(client, 'scrooge')

    assert response.status_code == 200
    assert ex1.malicious_xss == response.json()['fields']['address']

    # Confirm exploit:
    response = client.get(f"/user-profiles/{_id}")
    assert ex1.malicious_url in response.text
