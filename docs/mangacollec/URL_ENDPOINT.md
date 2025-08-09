# URLS

---

**url_base** https://api.mangacollecc.com

---

|                          **Name** | Ver | **Methode**  | **Endpoint**                                         | **Responce url**                                                                      |
|----------------------------------:|:---:|:------------:|:-----------------------------------------------------|:--------------------------------------------------------------------------------------|
|                          **auth** | --  |     POST     | **url_base**/oauth/token/                            |                                                                                       |
|                 **edition by id** | V1  |     GET      | **url_base**/v1/editions/{id}/                       |                                                                                       |
|                 **edition by id** | V2  |     GET      | **url_base**/v2/editions/{id}/                       | docs/mangacollec/urls_responce/v2_edition_333eb14c-5f0a-4130-99fe-d2842cd06349.json   |
|                  **series liste** | V1  |     GET      | **url_base**/v1/series/                              |                                                                                       |
|                   **serie by id** | V1  |     GET      | **url_base**/v1/series/{id}/                         |                                                                                       |
|                  **series liste** | V2  |     GET      | **url_base**/v2/series/                              | docs/mangacollec/urls_responce/v2_series.json                                         |
|                   **serie by id** | V2  |     GET      | **url_base**/v2/series/{id}/                         | docs/mangacollec/urls_responce/v2_serie_a320ac19-4318-4471-9e4e-eb017f4584d5.json     |
|              **publishers liste** | V1  |     GET      | **url_base**/v1/publishers/                          |                                                                                       |
|               **publisher by id** | V1  |     GET      | **url_base**/v1/publishers/{id}/                     |                                                                                       |
|               **publishers list** | V2  |     GET      | **url_base**/v2/publishers                           | docs/mangacollec/urls_responce/v2_publishers.json                                     |
|               **publisher by id** | V2  |     GET      | **url_base**/v2/publishers/{id}/                     | docs/mangacollec/urls_responce/v2_publisher_bdef8c9e-7395-465d-8175-a1b985d4aa92.json |
|                  **genres liste** | V1  |     GET      | **url_base**/v1/types/                               |                                                                                       |
|                    **jobs liste** | V1  |     GET      | **url_base**/v1/jobs/                                |                                                                                       |
|                   **kinds liste** | V1  |     GET      | **url_base**/v1/kinds/                               |                                                                                       |
|                 **authors liste** | V1  |     GET      | **url_base**/v1/authors/                             |                                                                                       |
|                  **author by id** | V1  |     GET      | **url_base**/v1/authors/{id}/                        |                                                                                       |
|                 **authors liste** | V2  |     GET      | **url_base**/v2/authors/                             | docs/mangacollec/urls_responce/v2_authors.json                                        |
|                  **author by id** | V2  |     GET      | **url_base**/v2/authors/{id}/                        | docs/mangacollec/urls_responce/v2_author_381c5429-93b2-494d-857d-ceb2b701f876.json    |
|                  **volume by id** | V1  |     GET      | **url_base**/v1/volumes/{id}/                        |                                                                                       |
|                  **volumes news** | V1  |     GET      | **url_base**/v1/volumes/news/                        |                                                                                       |
|              **volumes planning** | V2  |     GET      | **url_base**/v2/planning?month={year}-{month}-{day}/ |                                                                                       |
|                  **volume by id** | V2  |     GET      | **url_base**/v2/volumes/{id}/                        | docs/mangacollec/urls_responce/v2_volume_6e22eae9-2afd-45ba-8c26-d10d4224d5bf.json    |
|                  **volumes news** | V2  |     GET      | **url_base**/v2/volumes/news/                        | docs/mangacollec/urls_responce/v2_volumes_news.json                                   |
|         **user colection public** | V1  |     GET      | **url_base**/v1/user/{username}/collection/          | docs/mangacollec/urls_responce/v2_collection_shooterdev.json                          |
|        **user colection private** | V1  |     GET      | **url_base**/v1/users/me/collection/                 |                                                                                       |
|         **user colection public** | V2  |     GET      | **url_base**/v2/user/{username}/collection/          |                                                                                       |
|          **user colectio public** | V2  |     GET      | **url_base**/v2/users/me/collection/                 | docs/mangacollec/urls_responce/v2_collection_me.json                                  |
|           **user recommendation** | V1  |     GET      | **url_base**/v1/users/me/recommendation/             |                                                                                       |
|             **user parm private** | V1  |     GET      | **url_base**/v1/users/me/                            |                                                                                       |
|              **user parm public** | V1  |     GET      | **url_base**/v1/users/{username}/                    |                                                                                       |
| **user possessions multiple add** | V1  | POST, DELETE | **url_base**/v1/possessions_multiple/                |                                                                                       |
|      **user follow_editions add** | V1  | POST, DELETE | **url_base**/v1/follow_editions/                     |                                                                                       |
|            **amazon_offer by id** | V1  |     GET      | **url_base**/v1/amazon_offer/{id}/                   |                                                                                       |
|           **bdfugue_offer by id** | V1  |     GET      | **url_base**/v1/bdfugue_offer/{id}/                  |                                                                                       |
|                   **kinds liste** | V2  |     GET      | **url_base**/v2/kinds/                               | docs_mangacollecc/urls_responce/v2_kinds.json                                         |
