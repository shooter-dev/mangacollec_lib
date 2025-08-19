from typing import Dict, Any, List

from mangacollec.job.converter.job_converter import JobConverter
from mangacollec.job.responses.jobs_response import JobsEndpointResponse
from mangacollec.client.interfaces.client_interface import IMangaCollecAPIClient
from mangacollec.job.interfaces.job_endpoint_interface import IJobsEndpoint
from mangacollec.job.entity.job import Job


class JobEndpoint(IJobsEndpoint):
    """
    Implémentation des opérations pour les jobs dans l'API MangaCollec.
    """
    
    def __init__(self, client: IMangaCollecAPIClient):
        """
        Initialise le endpoint des jobs.
        
        :param client: Client API MangaCollec
        """
        self.client = client

    def get_all_jobs(self) -> List[Job]:
        """
        Récupère la liste complète des jobs disponibles sur MangaCollec.

        :return: Liste des jobs
        """
        result_endpoint = self.client.get("/v1/jobs")

        jobs: List[Job] = []

        converter = JobConverter()

        for item_job in result_endpoint:
            print(item_job)
            #jobs.append(converter.deserialize(item_job))

        return JobsEndpointResponse(jobs=jobs)

    def get_all_jobs_v2(self) -> JobsEndpointResponse:
        """
        Récupère la liste complète des jobs disponibles sur MangaCollec (API v2).

        :return: JobsEndpointResponse
        """
        result_endpoint = self.client.get("/v2/jobs")

        jobs: List[Job] = []

        converter = JobConverter()

        for item_job in result_endpoint['jobs']:
            jobs.append(converter.deserialize(item_job))

        return JobsEndpointResponse(jobs=jobs)
