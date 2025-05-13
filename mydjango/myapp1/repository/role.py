from myapp1.models import Role
from myapp1.repository.basic import BaseRepository


class RoleRepository(BaseRepository):
    model = Role