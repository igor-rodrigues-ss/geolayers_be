from src.apps.tasks.repository import TasksSaveLayerRepository


class TasksSaveLayer:

    async def list_all(self):
        return await TasksSaveLayerRepository().list_all()