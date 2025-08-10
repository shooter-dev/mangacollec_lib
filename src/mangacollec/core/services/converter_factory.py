from typing import Dict, Any
from mangacollec.core.interfaces.converter_interface import IConverterEntity


class ConverterFactory:
    """
    Factory pour créer et gérer les convertisseurs de données.
    
    Cette factory centralise la création des convertisseurs pour éviter
    la duplication et faciliter la maintenance.
    """
    
    @staticmethod
    def get_author_converters() -> Dict[str, IConverterEntity]:
        """
        Retourne les convertisseurs nécessaires pour les endpoints d'auteurs.
        
        :return: Dictionnaire des convertisseurs pour le domaine author
        """
        from mangacollec.author.converter.author_converter import AuthorConverter
        
        return {
            'authors': AuthorConverter()
        }
    
    @staticmethod
    def get_serie_converters() -> Dict[str, IConverterEntity]:
        """
        Retourne les convertisseurs nécessaires pour les endpoints de séries.
        
        :return: Dictionnaire des convertisseurs pour le domaine serie
        """
        from mangacollec.author.converter.author_converter import AuthorConverter
        from mangacollec.serie.converter.serie_converter import SerieConverter
        from mangacollec.edition.converter.edition_converter import EditionConverter
        from mangacollec.volume.converter.volume_converter import VolumeConverter
        
        return {
            'authors': AuthorConverter(),
            'series': SerieConverter(),
            'editions': EditionConverter(),
            'volumes': VolumeConverter()
        }
    
    @staticmethod
    def get_edition_converters() -> Dict[str, IConverterEntity]:
        """
        Retourne les convertisseurs nécessaires pour les endpoints d'éditions.
        
        :return: Dictionnaire des convertisseurs pour le domaine edition
        """
        from mangacollec.author.converter.author_converter import AuthorConverter
        from mangacollec.edition.converter.edition_converter import EditionConverter
        from mangacollec.genre.converter.genre_converter import GenreConverter
        from mangacollec.job.converter.job_converter import JobConverter
        from mangacollec.kind.converter.kind_converter import KindConverter
        from mangacollec.publisher.converter.publisher_converter import PublisherConverter
        from mangacollec.serie.converter.serie_converter import SerieConverter
        from mangacollec.task.converter.task_converter import TaskConverter
        from mangacollec.volume.converter.volume_converter import VolumeConverter
        
        return {
            'editions': EditionConverter(),
            'series': SerieConverter(),
            'types': GenreConverter(),
            'kinds': KindConverter(),
            'tasks': TaskConverter(),
            'jobs': JobConverter(),
            'authors': AuthorConverter(),
            'publishers': PublisherConverter(),
            'volumes': VolumeConverter()
        }