from abc import ABC, abstractmethod
from typing import Dict, Any

from mangacollec.job.responses.jobs_response import JobsEndpointResponse


class IJobsEndpoint(ABC):
    """
    Interface pour les opérations sur les jobs dans l'API MangaCollec.
    """

    @abstractmethod
    def get_all_jobs(self) -> Dict[str, Any]:
        """
        Récupère la liste complète des jobs disponibles sur MangaCollec.

        :return: Liste des jobs
        """
        pass

    @abstractmethod
    def get_all_jobs_v2(self) -> JobsEndpointResponse:
        """
        Récupère la liste complète des jobs disponibles sur MangaCollec (API v2).

        :return: JobsEndpointResponse
        """
        pass