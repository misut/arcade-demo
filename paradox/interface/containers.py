from dependency_injector import containers, providers

from paradox.infrastructure.unit_of_work import FileWorldUnitOfWork


class WorldEditContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    uow = providers.Factory(
        FileWorldUnitOfWork,
        path="assets/worlds.pkl"
    )
