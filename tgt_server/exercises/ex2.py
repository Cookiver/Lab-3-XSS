#  The functions below access the user profiles using the REST api provided by the web application
#  defined in the module tgt_server.main

import uuid

from fastapi import testclient
from fastapi.openapi.models import Response


def get_profile_id(client: testclient.TestClient, name: str) -> uuid.UUID:
    """
        Retrieves all profiles from the REST API and finds the UUID that uniquely
        identifies the first profile that contains the provided name.

    :param client: A rest API client implemented by fastapi providing
                   methods like post(), get(), put(), and delete()

    :param name:   The name of the user that the desired profile describes
    :return:       The UUID that uniquely identifies the first profile that contains the
                   provided name
    """
    pass


def update_profile(client: testclient.TestClient, _id: uuid.UUID, updated_profile: dict) -> Response:
    """
        Uses the REST API to update the user profile having the given uuid with the
        new profile given.  The response object returned back from the client is
        passed by back as the result of this function.

    :param client: a rest API client providing methods like post(), get(), put(), and delete()
    :param _id:
    :param updated_profile:
    :return:
    """
    pass