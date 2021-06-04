from src.apps.tasks.repository import LayerTasksRepository


class TasksSaveLayer:

    async def list_all(self):
        return await LayerTasksRepository().list_all()