from abc import ABC, abstractmethod
from typing import List, Optional
from mangacollec.author.entity.author import Author


class IGetAuthorUseCase(ABC):
    """
    Interface pour le use case de récupération d'un auteur par ID.
    """
    
    @abstractmethod
    def execute(self, author_id: str) -> Author:
        """
        Récupère un auteur par son ID.
        
        :param author_id: Identifiant de l'auteur
        :return: L'auteur trouvé
        :raises AuthorValidationError: Si l'ID est invalide
        :raises AuthorNotFoundError: Si l'auteur n'existe pas
        """
        pass


class IListAuthorsUseCase(ABC):
    """
    Interface pour le use case de listage des auteurs.
    """
    
    @abstractmethod
    def execute(self, name_filter: Optional[str] = None, min_tasks: Optional[int] = None) -> List[Author]:
        """
        Récupère la liste des auteurs avec filtres optionnels.
        
        :param name_filter: Filtre optionnel sur le nom
        :param min_tasks: Nombre minimum de tâches
        :return: Liste des auteurs filtrés
        :raises AuthorError: En cas d'erreur
        """
        pass