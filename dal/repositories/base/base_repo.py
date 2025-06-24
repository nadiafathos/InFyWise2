from typing import Type, TypeVar, Generic, List, Optional, Any
from sqlalchemy.orm import Session, InstrumentedAttribute

T = TypeVar('T') # Type générique

class BaseRepository(Generic[T]):
    """
    Repository générique fournissant les opérations CRUD de base
    pour n'importe quel modèle SQLAlchemy.
    """
    def __init__(self, model: Type[T], session: Session):
        self.model   = model
        self.session = session

    def create(self, **data) -> T:
        """
        Crée et persiste une nouvelle instance du modèle.
        """
        obj = self.model(**data)
        self.session.add(obj)
        self.session.commit()
        return obj

    def get_by_id(self, id: any) -> Optional[T]:
        """
        Retourne l'instance du modèle par sa clé primaire, ou None.
        """
        return self.session.get(self.model, id)

    def get_by(self, column_name: str, value: Any) -> Optional[T]:
        """
        Recherche dynamique selon le nom de colonne et la valeur.
        Ex : repo.get_by('username', 'michel')
        """
        column = getattr(self.model, column_name, None)
        if not isinstance(column, InstrumentedAttribute):
            raise AttributeError(f"{self.model.__name__}.{column_name} n'est pas une colonne SQLAlchemy")
        return (
            self.session
            .query(self.model)
            .filter(column == value)
            .first()
        )

    def get_all(self) -> List[T]:
        """
        Retourne toutes les instances du modèle.
        """
        return self.session.query(self.model).all()

    def update(self, instance: T, **data) -> T:
        """
        Met à jour l'instance avec les champs fournis.
        """
        for key, val in data.items():
            setattr(instance, key, val)
        self.session.commit()
        return instance

    def delete(self, instance: T) -> None:
        """
        Supprime l'instance donnée.
        """
        self.session.delete(instance)
        self.session.commit()