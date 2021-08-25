from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel


class BaseProfile(BaseModel):
    fields: Optional[dict] = None


class Profile(BaseProfile):
    id: UUID = None


user_profile_data = dict((profile.id, profile) for profile in [
    Profile(id=uuid4(), **_.dict()) for _ in [
        BaseProfile(
            fields=dict(
                name='donald duck',
                address='132 Pond Lane, Disneyland'
            )),
        BaseProfile(
            fields=dict(
                name='mickey mouse',
                address='15 Brie Avenue, Disneyland'
            )),
        BaseProfile(
            fields=dict(
                name='scrooge',
                address='13 Revenue Road, Disneyland'
            ))
        ]
    ])