from typing import Dict, Any, List

from mangacollec.genres.converter.genre_converter import GenreConverter
from mangacollec.genres.responses.genres_response import GenresEndpointResponse
from mangacollec.client.interfaces.client_interface import IMangaCollecAPIClient
from mangacollec.genres.interfaces.genre_endpoint_interface import IGenresEndpoint
from mangacollec.genres.entity.genre import Genre


class GenreEndpoint(IGenresEndpoint):
    def __init__(self, client: IMangaCollecAPIClient):
        self.client = client

    def get_all_genres(self) -> Dict[str, Any]:
        return self.client.get("/v1/types")

    def get_all_genres_v2(self) -> GenresEndpointResponse:
        result_endpoint = self.client.get("/v1/types")
        
        genres: List[Genre] = []
        converter = GenreConverter()

        for item_genre in result_endpoint:
            genres.append(converter.deserialize(item_genre))

        return GenresEndpointResponse(genres=genres)