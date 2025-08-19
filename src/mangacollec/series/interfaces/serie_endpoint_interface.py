from abc import ABC, abstractmethod
from typing import Dict, Any
from mangacollec.series.responses.serie_response import SerieEndpointResponse
from mangacollec.series.responses.series_response import SeriesEndpointResponse


class ISeriesEndpoint(ABC):
    @abstractmethod
    def get_all_series(self) -> Dict[str, Any]:
        pass

    @abstractmethod
    def get_serie_by_id(self, serie_id: str) -> Dict[str, Any]:
        pass

    @abstractmethod
    def get_all_series_v2(self) -> SeriesEndpointResponse:
        pass

    @abstractmethod
    def get_serie_by_id_v2(self, serie_id: str) -> SerieEndpointResponse:
        pass