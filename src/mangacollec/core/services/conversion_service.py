from typing import Dict, Any, List, TypeVar, Generic
from mangacollec.core.interfaces.converter_interface import IConverterEntity

T = TypeVar('T')


class ConversionService:
    """
    Service générique pour la conversion de données API en objets typés.
    
    Ce service centralise la logique de conversion pour éviter la duplication
    de code entre les différents endpoints du projet.
    """
    
    @staticmethod
    def convert_items(items: List[Dict[str, Any]], converter: IConverterEntity[T]) -> List[T]:
        """
        Convertit une liste d'éléments avec le convertisseur fourni.
        
        :param items: Liste des éléments à convertir
        :param converter: Convertisseur à utiliser
        :return: Liste des éléments convertis
        """
        return [converter.deserialize(item) for item in items]
    
    @staticmethod
    def convert_response_data(
        result_endpoint: Dict[str, Any], 
        converter_mapping: Dict[str, IConverterEntity]
    ) -> Dict[str, List[Any]]:
        """
        Convertit les données de réponse API en utilisant un mapping de convertisseurs.
        
        :param result_endpoint: Réponse brute de l'API
        :param converter_mapping: Mapping des clés vers leurs convertisseurs
        :return: Dictionnaire des données converties
        """
        converted_data: Dict[str, List[Any]] = {}
        
        for key, converter in converter_mapping.items():
            items = result_endpoint.get(key, [])
            converted_data[key] = ConversionService.convert_items(items, converter)
            
        return converted_data