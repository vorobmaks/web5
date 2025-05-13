from myapp1.models import Manager
from myapp1.repository.basic import BaseRepository


class ManagerRepository(BaseRepository):
    model = Manager