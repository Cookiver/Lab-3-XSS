import uuid
from typing import Optional

from config import settings
from data import user_profile_data, Profile

malicious_url = f'http://{settings.api_host}:{settings.api_port}/static/hacked.html'

# The Cross-site Script:
malicious_xss = f'document.location=http://{settings.api_host}:{settings.api_port}/static/hacked.html'

#  The functions below manipulate the in-memory data structure from the module tgt_server.data
#  in which user profiles are stored.


async def update_user_profile(_id: uuid.UUID, address: str, name: str) -> Profile:
    """
    Update the address and name in the profile identified by the given uuid

    :param _id: the uuid of the profile to be updated
    :param address: the new address
    :param name: the new name

    :return: the updated user profile
    """
    pass


def search_profiles(*, name: Optional[str] = None) -> dict[uuid.UUID, Profile]:
    """
    Look for those profiles that have a name that contains the value passed in
    as the name parameter.

    The returned profiles satisfy the following psuedo predicate:
    name in profile.fields.get('name', '')

    :param name: the name to be found

    :return: A dictionary containing profiles whose names contain the name given
    as a parameter.
    """
    pass
