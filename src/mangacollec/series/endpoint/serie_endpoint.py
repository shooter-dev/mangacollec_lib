from typing import Dict, Any, List

from mangacollec.series.converter.serie_converter import SerieConverter
from mangacollec.series.converter.type_converter import TypeConverter
from mangacollec.series.converter.task_converter import TaskConverter
from mangacollec.series.converter.box_edition_converter import BoxEditionConverter
from mangacollec.series.converter.box_converter import BoxConverter
from mangacollec.series.converter.box_volume_converter import BoxVolumeConverter
from mangacollec.series.responses.serie_response import SerieEndpointResponse
from mangacollec.series.responses.series_response import SeriesEndpointResponse
from mangacollec.client.interfaces.client_interface import IMangaCollecAPIClient
from mangacollec.series.interfaces.serie_endpoint_interface import ISeriesEndpoint
from mangacollec.series.entity.serie import Serie
from mangacollec.kinds.converter.kind_converter import KindConverter
from mangacollec.job.converter.job_converter import JobConverter
from mangacollec.author.converter.author_converter import AuthorConverter
from mangacollec.editions.converter.edition_converter import EditionConverter
from mangacollec.publishers.converter.publisher_converter import PublisherConverter
from mangacollec.volumes.converter.volume_converter import VolumeConverter


class SerieEndpoint(ISeriesEndpoint):
    def __init__(self, client: IMangaCollecAPIClient):
        self.client = client

    def get_all_series(self) -> Dict[str, Any]:
        return self.client.get("/v1/series")

    def get_serie_by_id(self, serie_id: str) -> Dict[str, Any]:
        return self.client.get(f"/v1/series/{serie_id}")

    def get_all_series_v2(self) -> SeriesEndpointResponse:
        result_endpoint = self.client.get("/v2/series")
        
        series: List[Serie] = []
        converter = SerieConverter()

        for item_serie in result_endpoint['series']:
            series.append(converter.deserialize(item_serie))

        return SeriesEndpointResponse(series=series)

    def get_serie_by_id_v2(self, serie_id: str) -> SerieEndpointResponse:
        result_endpoint = self.client.get(f"/v2/series/{serie_id}")

        # Initialisation des convertisseurs
        serie_converter = SerieConverter()
        type_converter = TypeConverter()
        kind_converter = KindConverter()
        task_converter = TaskConverter()
        job_converter = JobConverter()
        author_converter = AuthorConverter()
        edition_converter = EditionConverter()
        publisher_converter = PublisherConverter()
        volume_converter = VolumeConverter()
        box_edition_converter = BoxEditionConverter()
        box_converter = BoxConverter()
        box_volume_converter = BoxVolumeConverter()

        # Conversion des données
        series = []
        if 'series' in result_endpoint and result_endpoint['series']:
            for item in result_endpoint['series']:
                series.append(serie_converter.deserialize(item))

        types = []
        if 'types' in result_endpoint and result_endpoint['types']:
            for item in result_endpoint['types']:
                types.append(type_converter.deserialize(item))

        kinds = []
        if 'kinds' in result_endpoint and result_endpoint['kinds']:
            for item in result_endpoint['kinds']:
                kinds.append(kind_converter.deserialize(item))

        tasks = []
        if 'tasks' in result_endpoint and result_endpoint['tasks']:
            for item in result_endpoint['tasks']:
                tasks.append(task_converter.deserialize(item))

        jobs = []
        if 'jobs' in result_endpoint and result_endpoint['jobs']:
            for item in result_endpoint['jobs']:
                jobs.append(job_converter.deserialize(item))

        authors = []
        if 'authors' in result_endpoint and result_endpoint['authors']:
            for item in result_endpoint['authors']:
                authors.append(author_converter.deserialize(item))

        editions = []
        if 'editions' in result_endpoint and result_endpoint['editions']:
            for item in result_endpoint['editions']:
                editions.append(edition_converter.deserialize(item))

        publishers = []
        if 'publishers' in result_endpoint and result_endpoint['publishers']:
            for item in result_endpoint['publishers']:
                publishers.append(publisher_converter.deserialize(item))

        volumes = []
        if 'volumes' in result_endpoint and result_endpoint['volumes']:
            for item in result_endpoint['volumes']:
                volumes.append(volume_converter.deserialize(item))

        box_editions = []
        if 'box_editions' in result_endpoint and result_endpoint['box_editions']:
            for item in result_endpoint['box_editions']:
                box_editions.append(box_edition_converter.deserialize(item))

        boxes = []
        if 'boxes' in result_endpoint and result_endpoint['boxes']:
            for item in result_endpoint['boxes']:
                boxes.append(box_converter.deserialize(item))

        box_volumes = []
        if 'box_volumes' in result_endpoint and result_endpoint['box_volumes']:
            for item in result_endpoint['box_volumes']:
                box_volumes.append(box_volume_converter.deserialize(item))

        return SerieEndpointResponse(
            series=series,
            types=types,
            kinds=kinds,
            tasks=tasks,
            jobs=jobs,
            authors=authors,
            editions=editions,
            publishers=publishers,
            volumes=volumes,
            box_editions=box_editions,
            boxes=boxes,
            box_volumes=box_volumes
        )