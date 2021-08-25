#  The methods below demonstrate various techniques by which the tgt_server
#  have be attacked using Cross-site scripting

import uuid
from typing import Tuple

from fastapi.openapi.models import Response
from fastapi import testclient

from exercises import malicious_xss


def persistent_xss(client: testclient.TestClient, target_name: str) -> Tuple[uuid.UUID, Response]:
    """
    Implement the sequence of one or more steps needed to use persistence xss exploit.

    :param client:
    :param target_name:
    :return: (
        id of the profile exploited,
        the response of the last http request made by persistent_xss()
    )
    """
    pass


def reflect_xss(client: testclient.TestClient) -> Response:
    """
    Implement the sequence of one or more steps needed to use persistence xss exploit.

    :return: (
        the malicious_url to which the unknowing victim is redirected,
        the malicious_xss by which the victim is redirected,
        the response of the last http request made by reflect_xss()
    )
    """
    pass
