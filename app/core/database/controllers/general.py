from app.core.database.models import Task, User
from app.core.database.tables_managers import Table


class DatabaseController:
    @property
    def tasks(self) -> Table[Task]:
        return Table[Task](Task())
    
    @property
    def users(self) -> Table[User]:
        return Table[User](User())


main_controller = DatabaseController()
