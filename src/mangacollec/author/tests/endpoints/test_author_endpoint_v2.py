from unittest.mock import Mock
from mangacollec.author.endpoint.author_endpoint import AuthorEndpoint
from mangacollec.author.entity.author import Author
from mangacollec.author.responces.author_responce import AuthorEndpointResponce
from mangacollec.author.responces.authors_responce import AuthorsEndpointResponce
from mangacollec.client import IMangaCollecAPIClient


class TestSerieEndpointV2:
    """Tests pour les méthodes v2 de l'endpoint des séries."""

    def setup_method(self):
        """Configuration du mock client pour les tests."""
        self.mock_client = Mock(spec=IMangaCollecAPIClient)
        self.endpoint = AuthorEndpoint(self.mock_client)

    def test_get_all_authors_v2(self):
        """Test de récupération de toutes les author (API v2)."""
        api_response = {
            "authors": [
                {
                    "id": "370ac96c-49e0-4f09-b7c4-662cb1374b21",
                    "name": "Kishimoto",
                    "first_name": "Masashi",
                    "tasks_count": 32
                },
                {
                    "id": "e6cc4590-0b5e-4122-9428-b9b185bdb221",
                    "name": "Oda",
                    "first_name": "Eiichirō",
                    "tasks_count": 29
                }
            ]
        }

        self.mock_client.get.return_value = api_response

        result = self.endpoint.get_all_authors_v2()

        self.mock_client.get.assert_called_once_with("/v2/authors")

        assert isinstance(result, AuthorsEndpointResponce)
        assert len(result.authors) == 2

        assert all(isinstance(author, Author) for author in result.authors)

    def test_get_authors_by_id_v2(self):
        """Test de récupération d'un author (API v2)."""
        api_response = {
            "authors": [
                {
                    "id": "381c5429-93b2-494d-857d-ceb2b701f876",
                    "name": "Yamada",
                    "first_name": "Kanehito",
                    "tasks_count": 3
                }
            ],
            "tasks": [
                {
                    "id": "a8f22260-8048-4b9a-8667-8997fbc009d8",
                    "job_id": "bf39f3fe-ce75-48b0-b557-877da935633b",
                    "series_id": "71c893e9-9b0a-446f-ab1e-588dc7b48c76",
                    "author_id": "381c5429-93b2-494d-857d-ceb2b701f876"
                },
                {
                    "id": "727adc4c-ce1d-4558-abbc-3c5b408f1ada",
                    "job_id": "a3d7a6be-c4e4-405c-8a07-0c3cedfe42c1",
                    "series_id": "8ce919e7-e565-403c-bb87-289e9e039b6b",
                    "author_id": "381c5429-93b2-494d-857d-ceb2b701f876"
                },
                {
                    "id": "ee03a791-f6e5-45cf-b057-ebba8e410ccd",
                    "job_id": "a3d7a6be-c4e4-405c-8a07-0c3cedfe42c1",
                    "series_id": "dc681899-2eb9-4980-b92c-75f45baa29cc",
                    "author_id": "381c5429-93b2-494d-857d-ceb2b701f876"
                }
            ],
            "jobs": [
                {
                    "id": "a3d7a6be-c4e4-405c-8a07-0c3cedfe42c1",
                    "title": "Œuvre originale"
                },
                {
                    "id": "bf39f3fe-ce75-48b0-b557-877da935633b",
                    "title": "Scénario"
                }
            ],
            "series": [
                {
                    "id": "71c893e9-9b0a-446f-ab1e-588dc7b48c76",
                    "title": "Frieren",
                    "type_id": "106f524e-7283-44b8-aa84-25e9a7fb1f7d",
                    "adult_content": False,
                    "editions_count": 4,
                    "tasks_count": 2
                },
                {
                    "id": "dc681899-2eb9-4980-b92c-75f45baa29cc",
                    "title": "Frieren Anthologie",
                    "type_id": "106f524e-7283-44b8-aa84-25e9a7fb1f7d",
                    "adult_content": False,
                    "editions_count": 1,
                    "tasks_count": 2
                },
                {
                    "id": "8ce919e7-e565-403c-bb87-289e9e039b6b",
                    "title": "Frieren Art works",
                    "type_id": "f41d81b0-fca6-4445-a903-da310e0899d2",
                    "adult_content": False,
                    "editions_count": 1,
                    "tasks_count": 2
                }
            ],
            "editions": [
                {
                    "id": "ea0e02bc-c457-46f2-87c4-435f72a73a71",
                    "title": "Jaquette Librairies",
                    "series_id": "71c893e9-9b0a-446f-ab1e-588dc7b48c76",
                    "publisher_id": "74de7d1e-f2e9-44bb-8a5a-1fe84258c7bf",
                    "parent_edition_id": "7413bab2-2abd-4edd-aa4c-fa6f85ccd244",
                    "volumes_count": 1,
                    "last_volume_number": None,
                    "commercial_stop": False,
                    "not_finished": False,
                    "follow_editions_count": 1449
                },
                {
                    "id": "ec11ea40-fe6d-492d-974f-54f493860d6c",
                    "title": None,
                    "series_id": "dc681899-2eb9-4980-b92c-75f45baa29cc",
                    "publisher_id": "74de7d1e-f2e9-44bb-8a5a-1fe84258c7bf",
                    "parent_edition_id": None,
                    "volumes_count": 1,
                    "last_volume_number": 0,
                    "commercial_stop": False,
                    "not_finished": False,
                    "follow_editions_count": 4407
                },
                {
                    "id": "4f983fa3-c048-4e99-91cc-62d72467ea2e",
                    "title": "Prix découverte",
                    "series_id": "71c893e9-9b0a-446f-ab1e-588dc7b48c76",
                    "publisher_id": "74de7d1e-f2e9-44bb-8a5a-1fe84258c7bf",
                    "parent_edition_id": "7413bab2-2abd-4edd-aa4c-fa6f85ccd244",
                    "volumes_count": 1,
                    "last_volume_number": None,
                    "commercial_stop": False,
                    "not_finished": False,
                    "follow_editions_count": 416
                },
                {
                    "id": "e1f602df-61d5-48cc-a446-71d63f2b3ee7",
                    "title": None,
                    "series_id": "8ce919e7-e565-403c-bb87-289e9e039b6b",
                    "publisher_id": "74de7d1e-f2e9-44bb-8a5a-1fe84258c7bf",
                    "parent_edition_id": None,
                    "volumes_count": 1,
                    "last_volume_number": 0,
                    "commercial_stop": False,
                    "not_finished": False,
                    "follow_editions_count": 3303
                },
                {
                    "id": "e1e042a5-32db-46a0-9216-1dce2b9d32d1",
                    "title": "Jaquette alternative",
                    "series_id": "71c893e9-9b0a-446f-ab1e-588dc7b48c76",
                    "publisher_id": "74de7d1e-f2e9-44bb-8a5a-1fe84258c7bf",
                    "parent_edition_id": "7413bab2-2abd-4edd-aa4c-fa6f85ccd244",
                    "volumes_count": 6,
                    "last_volume_number": None,
                    "commercial_stop": False,
                    "not_finished": False,
                    "follow_editions_count": 15357
                },
                {
                    "id": "7413bab2-2abd-4edd-aa4c-fa6f85ccd244",
                    "title": None,
                    "series_id": "71c893e9-9b0a-446f-ab1e-588dc7b48c76",
                    "publisher_id": "74de7d1e-f2e9-44bb-8a5a-1fe84258c7bf",
                    "parent_edition_id": None,
                    "volumes_count": 14,
                    "last_volume_number": None,
                    "commercial_stop": False,
                    "not_finished": False,
                    "follow_editions_count": 42873
                }
            ],
            "volumes": [
                {
                    "id": "486f193a-400b-4307-88bc-451c00b07391",
                    "title": None,
                    "number": 14,
                    "release_date": "2025-07-03",
                    "isbn": None,
                    "asin": None,
                    "edition_id": "e1e042a5-32db-46a0-9216-1dce2b9d32d1",
                    "possessions_count": 4980,
                    "not_sold": True,
                    "image_url": "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWxqWkRRME1UVmlNUzA0TkRobExUUmtZek10WVdZd09TMWxOMlU0WmpCaE1qSXhZV1FHT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--4668d612a628462bbdacc939d8b4588e0e135b6d/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFMMEFXa0M5QUU9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--f4740ce9863997714730d7d28982d4fbc8d883df/486f193a-400b-4307-88bc-451c00b07391.jpg"
                },
                {
                    "id": "964a7712-dee1-4cdd-9311-fa5cae807c82",
                    "title": None,
                    "number": 1,
                    "release_date": "2025-05-07",
                    "isbn": "9791032721117",
                    "asin": "B0DXTPK5L5",
                    "edition_id": "4f983fa3-c048-4e99-91cc-62d72467ea2e",
                    "possessions_count": 334,
                    "not_sold": False,
                    "image_url": "https://m.media-amazon.com/images/I/51S8IImYSqL.jpg"
                },
                {
                    "id": "6ef7588a-aa8e-49be-9f49-1683857c6b80",
                    "title": None,
                    "number": 8,
                    "release_date": "2023-06-08",
                    "isbn": None,
                    "asin": None,
                    "edition_id": "e1e042a5-32db-46a0-9216-1dce2b9d32d1",
                    "possessions_count": 7926,
                    "not_sold": True,
                    "image_url": "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWsyTlRCbE1UVXhNQzFoTnpsaUxUUTRNV0V0WVdNellpMWxNakUyWWpJeVpUZ3dZVEFHT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--ce14ddc5a4dc5c4b84e66cc232089937e678ae7b/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFMMEFXa0M5QUU9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--f4740ce9863997714730d7d28982d4fbc8d883df/6ef7588a-aa8e-49be-9f49-1683857c6b80.jpg"
                },
                {
                    "id": "9343931c-e554-4467-b302-5bc195eb133c",
                    "title": None,
                    "number": 13,
                    "release_date": "2024-12-05",
                    "isbn": None,
                    "asin": None,
                    "edition_id": "ea0e02bc-c457-46f2-87c4-435f72a73a71",
                    "possessions_count": 1203,
                    "not_sold": True,
                    "image_url": "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWsyWmpZNU1ETTROaTFqTm1Ka0xUUmhPR1V0WWprMFppMWhPR1ZpTmpreE5XSXhZV1FHT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--c8e9c9d18fbae8b5bc37c77b1fd4683e4545b3e9/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFMMEFXa0M5QUU9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--f4740ce9863997714730d7d28982d4fbc8d883df/9343931c-e554-4467-b302-5bc195eb133c.jpg"
                },
                {
                    "id": "c793172a-63d2-48fd-8667-9acaf6ddbb17",
                    "title": None,
                    "number": 11,
                    "release_date": "2024-01-04",
                    "isbn": "9791032716076",
                    "asin": "B0CKKQC3LN",
                    "edition_id": "7413bab2-2abd-4edd-aa4c-fa6f85ccd244",
                    "possessions_count": 14854,
                    "not_sold": False,
                    "image_url": "https://m.media-amazon.com/images/I/51s+q6auLWL.jpg"
                },
                {
                    "id": "6366bc93-1101-441a-bc92-3086fa90450d",
                    "title": None,
                    "number": 7,
                    "release_date": "2023-03-02",
                    "isbn": "9791032713105",
                    "asin": "B0BQWX8576",
                    "edition_id": "7413bab2-2abd-4edd-aa4c-fa6f85ccd244",
                    "possessions_count": 18648,
                    "not_sold": False,
                    "image_url": "https://m.media-amazon.com/images/I/51LrLACDZBL.jpg"
                },
                {
                    "id": "3a0f0a84-95a0-4e52-80fa-2d4608fb6384",
                    "title": None,
                    "number": 0,
                    "release_date": "2024-12-05",
                    "isbn": "9791032719060",
                    "asin": "B0D6YDC9DQ",
                    "edition_id": "ec11ea40-fe6d-492d-974f-54f493860d6c",
                    "possessions_count": 3790,
                    "not_sold": False,
                    "image_url": "https://m.media-amazon.com/images/I/51qxpemOv6L.jpg"
                },
                {
                    "id": "62f9c3a8-9f0a-4203-b0eb-b602e6420cdf",
                    "title": None,
                    "number": 0,
                    "release_date": "2024-11-07",
                    "isbn": "9791032719077",
                    "asin": "B0D6YFXPXR",
                    "edition_id": "e1f602df-61d5-48cc-a446-71d63f2b3ee7",
                    "possessions_count": 2524,
                    "not_sold": False,
                    "image_url": "https://m.media-amazon.com/images/I/51-I3d32qRL.jpg"
                },
                {
                    "id": "07bc795f-eb52-418c-85e1-7cbb2c4cdeff",
                    "title": None,
                    "number": 1,
                    "release_date": "2022-03-03",
                    "isbn": None,
                    "asin": None,
                    "edition_id": "e1e042a5-32db-46a0-9216-1dce2b9d32d1",
                    "possessions_count": 7449,
                    "not_sold": False,
                    "image_url": "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWxpTTJGa1lUTm1ZaTB3TURsa0xUUTNaVEF0WVRkaU5DMDVPRFZsTURnMk56WmlOR0VHT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--615e8cf4abcf81138eb80cb5e4813d45471d9d54/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFMMEFXa0M5QUU9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--f4740ce9863997714730d7d28982d4fbc8d883df/07bc795f-eb52-418c-85e1-7cbb2c4cdeff.jpg"
                },
                {
                    "id": "e5e7ca54-42ce-41bd-b9d7-978bb8341de8",
                    "title": None,
                    "number": 5,
                    "release_date": "2022-10-13",
                    "isbn": None,
                    "asin": None,
                    "edition_id": "e1e042a5-32db-46a0-9216-1dce2b9d32d1",
                    "possessions_count": 8288,
                    "not_sold": True,
                    "image_url": "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWsyTVdObU1EUmtNeTB6Wm1KbExUUTBNR1F0T0dOaFpDMDBaVGRsTWpoa1pHVTFZbU1HT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--e17f1bbaea8456837fb00d7d85d71d9b92a938be/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFMMEFXa0M5QUU9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--f4740ce9863997714730d7d28982d4fbc8d883df/e5e7ca54-42ce-41bd-b9d7-978bb8341de8.jpg"
                },
                {
                    "id": "83dde34f-8c96-45ab-8270-40d3a8b1ca4f",
                    "title": None,
                    "number": 12,
                    "release_date": "2024-05-02",
                    "isbn": "9791032716090",
                    "asin": "B0CW61RL3X",
                    "edition_id": "7413bab2-2abd-4edd-aa4c-fa6f85ccd244",
                    "possessions_count": 12743,
                    "not_sold": False,
                    "image_url": "https://m.media-amazon.com/images/I/51UY5YYw1wL.jpg"
                },
                {
                    "id": "c732b645-d60e-48f7-a3be-d0500194d8e9",
                    "title": None,
                    "number": 12,
                    "release_date": "2024-05-02",
                    "isbn": None,
                    "asin": None,
                    "edition_id": "e1e042a5-32db-46a0-9216-1dce2b9d32d1",
                    "possessions_count": 6468,
                    "not_sold": True,
                    "image_url": "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWsxWlRreFlUTTFZUzB4WWpCaUxUUXhaRFl0WVdJM1l5MHhOall3WkdRNU1HSmxOeklHT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--83696c72b4df8b62f8a4b300cdbe68fc9d1d8ac8/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFMMEFXa0M5QUU9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--f4740ce9863997714730d7d28982d4fbc8d883df/c732b645-d60e-48f7-a3be-d0500194d8e9.jpg"
                },
                {
                    "id": "d55bed5a-1315-4055-95d6-b100d5212984",
                    "title": None,
                    "number": 6,
                    "release_date": "2023-01-05",
                    "isbn": "9791032711897",
                    "asin": "B0BHY819CH",
                    "edition_id": "7413bab2-2abd-4edd-aa4c-fa6f85ccd244",
                    "possessions_count": 19474,
                    "not_sold": False,
                    "image_url": "https://m.media-amazon.com/images/I/517DEg+HqOL.jpg"
                },
                {
                    "id": "85d7123b-fdbc-4132-8849-0a5a92fef719",
                    "title": None,
                    "number": 4,
                    "release_date": "2022-07-07",
                    "isbn": "9791032711262",
                    "asin": "B09ND27Q7M",
                    "edition_id": "7413bab2-2abd-4edd-aa4c-fa6f85ccd244",
                    "possessions_count": 23271,
                    "not_sold": False,
                    "image_url": "https://m.media-amazon.com/images/I/51EmSa6bLWL.jpg"
                },
                {
                    "id": "2a591b32-460c-4c91-9bb4-fcc4075068d8",
                    "title": None,
                    "number": 5,
                    "release_date": "2022-10-13",
                    "isbn": "9791032711484",
                    "asin": "B09ND1RPTT",
                    "edition_id": "7413bab2-2abd-4edd-aa4c-fa6f85ccd244",
                    "possessions_count": 20300,
                    "not_sold": False,
                    "image_url": "https://m.media-amazon.com/images/I/511f-x6jCyL.jpg"
                },
                {
                    "id": "87c028d1-2e83-415b-b9d0-1286720cc866",
                    "title": None,
                    "number": 13,
                    "release_date": "2024-12-05",
                    "isbn": "9791032716113",
                    "asin": "B0D223CMPC",
                    "edition_id": "7413bab2-2abd-4edd-aa4c-fa6f85ccd244",
                    "possessions_count": 11873,
                    "not_sold": False,
                    "image_url": "https://m.media-amazon.com/images/I/51Deg0640+L.jpg"
                },
                {
                    "id": "91c7faa3-5431-473e-ba85-f11a7c870b05",
                    "title": None,
                    "number": 8,
                    "release_date": "2023-06-08",
                    "isbn": "9791032713204",
                    "asin": "B0BWHP27Z8",
                    "edition_id": "7413bab2-2abd-4edd-aa4c-fa6f85ccd244",
                    "possessions_count": 16555,
                    "not_sold": False,
                    "image_url": "https://m.media-amazon.com/images/I/51fQfYZQkOL.jpg"
                },
                {
                    "id": "d53df49e-286c-4444-a462-690adb152787",
                    "title": None,
                    "number": 10,
                    "release_date": "2023-09-28",
                    "isbn": None,
                    "asin": None,
                    "edition_id": "e1e042a5-32db-46a0-9216-1dce2b9d32d1",
                    "possessions_count": 5981,
                    "not_sold": True,
                    "image_url": "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWswWkdaaE9UWXlZeTAyTjJVNUxUUTBOR1V0WVRsbE1DMWlNVEV4TVdNelpESTRPVFFHT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--f75bad332496ea841cf64bcd2062d962b9940019/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFMMEFXa0M5QUU9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--f4740ce9863997714730d7d28982d4fbc8d883df/d53df49e-286c-4444-a462-690adb152787.jpg"
                },
                {
                    "id": "4c57986e-3ee9-48f5-a96f-0f70c76c23e3",
                    "title": None,
                    "number": 3,
                    "release_date": "2022-05-05",
                    "isbn": "9791032711125",
                    "asin": "B09ND1X5QS",
                    "edition_id": "7413bab2-2abd-4edd-aa4c-fa6f85ccd244",
                    "possessions_count": 26897,
                    "not_sold": False,
                    "image_url": "https://m.media-amazon.com/images/I/51fmfABtvoL.jpg"
                },
                {
                    "id": "dbf73cef-6371-48dc-b6b1-000d4be0d91b",
                    "title": None,
                    "number": 14,
                    "release_date": "2025-07-03",
                    "isbn": "9791032716137",
                    "asin": "B0D6XWR8F4",
                    "edition_id": "7413bab2-2abd-4edd-aa4c-fa6f85ccd244",
                    "possessions_count": 6133,
                    "not_sold": False,
                    "image_url": "https://m.media-amazon.com/images/I/51sgZfv7FRL.jpg"
                },
                {
                    "id": "e4004f77-f544-4aa5-988b-ef305df817c6",
                    "title": None,
                    "number": 10,
                    "release_date": "2023-09-28",
                    "isbn": "9791032713662",
                    "asin": "B0C2K63T4Y",
                    "edition_id": "7413bab2-2abd-4edd-aa4c-fa6f85ccd244",
                    "possessions_count": 14891,
                    "not_sold": False,
                    "image_url": "https://m.media-amazon.com/images/I/51EhFcRLBKL.jpg"
                },
                {
                    "id": "7d2e75a6-fd0e-4f31-bd83-82c958e48f96",
                    "title": None,
                    "number": 2,
                    "release_date": "2022-03-03",
                    "isbn": "9791032710845",
                    "asin": "B09NCM8ZT1",
                    "edition_id": "7413bab2-2abd-4edd-aa4c-fa6f85ccd244",
                    "possessions_count": 31384,
                    "not_sold": False,
                    "image_url": "https://m.media-amazon.com/images/I/51fEVckJ65L.jpg"
                },
                {
                    "id": "94635426-7ecb-4fcb-865b-d85868d66da9",
                    "title": None,
                    "number": 1,
                    "release_date": "2022-03-03",
                    "isbn": "9791032710838",
                    "asin": "B09NCNYG4J",
                    "edition_id": "7413bab2-2abd-4edd-aa4c-fa6f85ccd244",
                    "possessions_count": 35588,
                    "not_sold": False,
                    "image_url": "https://m.media-amazon.com/images/I/51TPSFO3YoL.jpg"
                },
                {
                    "id": "f29e08bf-c016-48b8-92af-cb0b841e9751",
                    "title": None,
                    "number": 9,
                    "release_date": "2023-08-24",
                    "isbn": "9791032713419",
                    "asin": "B0BWJ8RTSS",
                    "edition_id": "7413bab2-2abd-4edd-aa4c-fa6f85ccd244",
                    "possessions_count": 16459,
                    "not_sold": False,
                    "image_url": "https://m.media-amazon.com/images/I/51z9-3cmAYL.jpg"
                }
            ]
}

        self.mock_client.get.return_value = api_response

        result = self.endpoint.get_author_by_id_v2("381c5429-93b2-494d-857d-ceb2b701f876")

        self.mock_client.get.assert_called_once_with("/v2/authors/381c5429-93b2-494d-857d-ceb2b701f876")
        assert isinstance(result, AuthorEndpointResponce)
        assert len(result.authors) == 1
        assert result.authors[0].id == "381c5429-93b2-494d-857d-ceb2b701f876"
        assert result.authors[0].name == "Yamada"
        assert result.authors[0].first_name == "Kanehito"
        assert result.authors[0].tasks_count == 3

