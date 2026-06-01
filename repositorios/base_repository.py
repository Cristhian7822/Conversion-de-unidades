from abc import ABC, abstractmethod

class BaseRepository(ABC):
    """Clase base abstracta para repositorios de datos."""

    _path: str

    @abstractmethod
    def load(self):
        """Cargar datos del repositorio desde la fuente configurada."""
        raise NotImplementedError
