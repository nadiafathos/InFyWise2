from typing import Generic, TypeVar, List, Optional, Any

DIn = TypeVar('DIn')   # DTO d'entrée
DOut = TypeVar('DOut') # DTO de sortie
Model = TypeVar('Model')

class BaseService(Generic[DIn, DOut, Model]):
    """
    Service générique fournissant CRUD complet pour un modèle donné.
    - le repo doit implémenter create, get_by_id, list, update, delete.
    - DIn  : dataclass d'entrée
    - dOut : dataclass de sortie
    - Model: modèle SQLAlchemy
    """
    def __init__(self, repo):
        self.repo = repo

    def create(self, data: DIn) -> DOut:
        if isinstance(data, dict):
            payload = data
        elif hasattr(data, '__dict__'):
            payload = data.__dict__
        else:
            payload = vars(data)

        model = self.repo.create(**payload)
        return self._to_out(model)

    def get(self, id: int) -> Optional[DOut]:
        model = self.repo.get_by_id(id)
        return self._to_out(model) if model else None

    def get_by(self, column_name: str, value: Any) -> Optional[DOut]:
        model = self.repo.get_by(column_name, value)
        return self._to_out(model) if model else None


    def get_all(self) -> List[DOut]:
        return [self._to_out(m) for m in self.repo.get_all()]

    def update(self, id: int, data: DIn) -> Optional[DOut]:
        model = self.repo.get_by_id(id)
        if not model:
            return None

        if isinstance(data, dict):
            payload = data
        elif hasattr(data, '__dict__'):
            payload = data.__dict__
        else:
            payload = vars(data)

        for key, val in payload.items():
            setattr(model, key, val)
        return self._to_out(model)

    def delete(self, id: int) -> bool:
        model = self.repo.get_by_id(id)
        if not model:
            return False
        self.repo.delete(model)
        return True

    def _to_out(self, model: Model) -> DOut:
        """À implémenter dans la sous-classe pour convertir Model → DTO de sortie."""
        raise NotImplementedError