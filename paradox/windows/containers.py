from dependency_injector import containers, providers

from paradox.domain.enum import Language
from paradox.infrastructure.repository import FileTextRepository
from paradox.infrastructure.unit_of_work import FileWorldUnitOfWork


class WorldEditContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    texts = providers.Singleton(
        FileTextRepository,
        text_path=config.TEXTS_PATH,
        language=Language.KOREAN,
    )

    uow = providers.Factory(
        FileWorldUnitOfWork,
        world_path=config.WORLDS_PATH,
    )
