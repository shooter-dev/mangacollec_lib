from abc import ABC, abstractmethod
from typing import List, Optional
from mangacollec.author.entity.author import Author


class IAuthorService(ABC):
    """
    Interface pour le service de gestion des auteurs.
    
    Cette interface définit le contrat public du service AuthorService
    et permet l'injection de dépendances et les tests.
    """
    
    @abstractmethod
    def get_author_by_id(self, author_id: str) -> Author:
        """
        Récupère un auteur spécifique par son ID.
        
        :param author_id: Identifiant de l'auteur
        :return: L'auteur trouvé
        :raises AuthorValidationError: Si l'ID est invalide
        :raises AuthorNotFoundError: Si l'auteur n'existe pas
        """
        pass
    
    @abstractmethod
    def get_all_authors(self, name_filter: Optional[str] = None, min_tasks: Optional[int] = None) -> List[Author]:
        """
        Récupère la liste de tous les auteurs avec filtres optionnels.
        
        :param name_filter: Filtre optionnel sur le nom de l'auteur
        :param min_tasks: Nombre minimum de tâches pour filtrer
        :return: Liste des auteurs correspondant aux critères
        :raises AuthorError: En cas d'erreur lors de la récupération
        """
        pass
    
    @abstractmethod
    def search_authors_by_name(self, search_term: str) -> List[Author]:
        """
        Recherche des auteurs par nom ou prénom.
        
        :param search_term: Terme de recherche
        :return: Liste des auteurs correspondant à la recherche
        :raises AuthorError: En cas d'erreur lors de la recherche
        """
        pass
    
    @abstractmethod
    def get_active_authors(self, min_tasks: int = 1) -> List[Author]:
        """
        Récupère les auteurs actifs (ayant au moins un certain nombre de tâches).
        
        :param min_tasks: Nombre minimum de tâches (défaut: 1)
        :return: Liste des auteurs actifs
        :raises AuthorError: En cas d'erreur lors de la récupération
        """
        pass
    
    @abstractmethod
    def get_author_display_name(self, author_id: str) -> str:
        """
        Récupère le nom d'affichage complet d'un auteur.
        
        :param author_id: Identifiant de l'auteur
        :return: Nom d'affichage (nom + prénom si disponible)
        :raises AuthorValidationError: Si l'ID est invalide
        :raises AuthorNotFoundError: Si l'auteur n'existe pas
        """
        pass
    
    @abstractmethod
    def count_authors(self) -> int:
        """
        Compte le nombre total d'auteurs.
        
        :return: Nombre d'auteurs
        :raises AuthorError: En cas d'erreur lors du comptage
        """
        pass