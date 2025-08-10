"""
Module client pour l'API MangaCollec.

Ce module expose les classes principales pour interagir avec l'API MangaCollec.
"""

from .client import MangaCollecAPIClient
from .interfaces.client_interface import IMangaCollecAPIClient

__all__ = ["MangaCollecAPIClient", "IMangaCollecAPIClient"]