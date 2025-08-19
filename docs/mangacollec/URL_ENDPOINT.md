# URLS

---

**url_base** https://api.mangacollecc.com

---

| [–] |                      **Name** | Ver | **Methode** | **Domain** | **Endpoint**                                         | **Details**                                                 |
|:---:|------------------------------:|:---:|:-----------:|:----------:|:-----------------------------------------------------|:------------------------------------------------------------|
| [ ] |                      **auth** | --  |    POST     |    auth    | **url_base**/oauth/token/                            | docs/mangacollec/urls_response/auth_token.md                |
| --- |                           --- | --  |     ---     |            | ---                                                  | ---                                                         |
| [ ] |             **edition by id** | V1  |     GET     |  edition   | **url_base**/v1/editions/{id}/                       | -                                                           |
| [ ] |             **edition by id** | V2  |     GET     |  edition   | **url_base**/v2/editions/{id}/                       | docs/mangacollec/urls_response/edition_for_id_v2.md         |
| --- |                           --- | --  |     ---     |            | ---                                                  | ---                                                         |
| [ ] |              **series liste** | V1  |     GET     |   series   | **url_base**/v1/series/                              | -                                                           |
| [ ] |               **serie by id** | V1  |     GET     |   series   | **url_base**/v1/series/{id}/                         | -                                                           |
| [ ] |              **series liste** | V2  |     GET     |   series   | **url_base**/v2/series/                              | docs/mangacollec/urls_response/series_list_v2.md            |
| [ ] |               **serie by id** | V2  |     GET     |   series   | **url_base**/v2/series/{id}/                         | docs/mangacollec/urls_response/serie_for_id_v2.md           |
| --- |                           --- | --  |     ---     |            | ---                                                  | ---                                                         |
| [ ] |          **publishers liste** | V1  |     GET     | publisher  | **url_base**/v1/publishers/                          | -                                                           |
| [ ] |           **publisher by id** | V1  |     GET     | publisher  | **url_base**/v1/publishers/{id}/                     | -                                                           |
| --- |                           --- | --  |     ---     |            | ---                                                  | ---                                                         |
| [ ] |           **publishers list** | V2  |     GET     | publisher  | **url_base**/v2/publishers                           | docs/mangacollec/urls_response/publishers_list_v2.md        |
| [ ] |           **publisher by id** | V2  |     GET     | publisher  | **url_base**/v2/publishers/{id}/                     | docs/mangacollec/urls_response/publisher_for_id_v2.md       |
| --- |                           --- | --  |     ---     |            | ---                                                  | ---                                                         |
| [ ] |              **genres liste** | V1  |     GET     |    type    | **url_base**/v1/types/                               | -                                                           |
| --- |                           --- | --  |     ---     |            | ---                                                  | ---                                                         |
| [ ] |                **jobs liste** | V1  |     GET     |    job     | **url_base**/v1/jobs/                                | -                                                           |
| --- |                           --- | --  |     ---     |            | ---                                                  | ---                                                         |
| [ ] |               **kinds liste** | V1  |     GET     |    kind    | **url_base**/v1/kinds/                               | -                                                           |
| [ ] |               **kinds liste** | V2  |     GET     |    kind    | **url_base**/v2/kinds/                               | docs_mangacollec/urls_response/v2_kinds.json                |
| --- |                           --- | --  |     ---     |            | ---                                                  | ---                                                         |
| [ ] |             **authors liste** | V1  |     GET     |   author   | **url_base**/v1/authors/                             | -                                                           |
| [ ] |              **author by id** | V1  |     GET     |   author   | **url_base**/v1/authors/{id}/                        | -                                                           |
| --- |                           --- | --  |     ---     |            | ---                                                  | ---                                                         |
| [ ] |             **authors liste** | V2  |     GET     |   author   | **url_base**/v2/authors/                             | docs/mangacollec/urls_response/authors_list_v2.md           |
| [ ] |              **author by id** | V2  |     GET     |   author   | **url_base**/v2/authors/{id}/                        | docs/mangacollec/urls_response/author_for_id_v2.md          |
| --- |                           --- | --  |     ---     |            | ---                                                  | ---                                                         |
| [ ] |              **volume by id** | V1  |     GET     |   volume   | **url_base**/v1/volumes/{id}/                        | -                                                           |
| [ ] |              **volumes news** | V1  |     GET     |   volume   | **url_base**/v1/volumes/news/                        | -                                                           |
| --- |                           --- | --  |     ---     |            | ---                                                  | ---                                                         |
| [ ] |              **volume by id** | V2  |     GET     |   volume   | **url_base**/v2/volumes/{id}/                        | docs/mangacollec/urls_response/volume_for_id_v2.md          |
| [ ] |              **volumes news** | V2  |     GET     |   volume   | **url_base**/v2/volumes/news/                        | docs/mangacollec/urls_response/volumes_news_v2.md           |
| --- |                           --- | --  |     ---     |            | ---                                                  | ---                                                         |
| [ ] |          **volumes planning** | V2  |     GET     |   volume   | **url_base**/v2/planning?month={year}-{month}-{day}/ |                                                             |
| --- |                           --- | --  |     ---     |            | ---                                                  | ---                                                         |
| [ ] |     **user colection public** | V1  |     GET     |    user    | **url_base**/v1/user/{username}/collection/          |                                                             |
| [ ] |     **user colection public** | V2  |     GET     |    user    | **url_base**/v2/user/{username}/collection/          | docs/mangacollec/urls_response/user_collection_public_v2.md |
| --- |                           --- | --  |     ---     |            | ---                                                  | ---                                                         |
| [ ] |       **user recommendation** | V1  |     GET     |    user    | **url_base**/v1/users/me/recommendation/             | -                                                           |
| --- |                           --- | --  |     ---     |            | ---                                                  | ---                                                         |
| [ ] |         **user parm private** | V1  |     GET     |    user    | **url_base**/v1/users/me/                            | -                                                           |
| [ ] |          **user parm public** | V1  |     GET     |    user    | **url_base**/v1/users/{username}/                    | -                                                           |
| --- |                           --- | --  |     ---     |            | ---                                                  | ---                                                         |
| [ ] | **user possessions multiple** | V1  |    POST     |    user    | **url_base**/v1/possessions_multiple/                | docs/mangacollec/urls_response/possessions_multiple.md      |
| [ ] |   **user unpossess_multiple** | V1  |   DELETE    |    user    | **url_base**/v1/possessions_multiple/                | docs/mangacollec/urls_response/unpossess_multiple.md        |
| --- |                           --- | --  |     ---     |            | ---                                                  | ---                                                         |
| [ ] |      **user follow_editions** | V1  |    POST     |    user    | **url_base**/v1/follow_editions/                     | docs/mangacollec/urls_response/follow_editions.md           |
| [ ] |    **user unfollow_editions** | V1  |   DELETE    |    user    | **url_base**/v1/follow_editions/{id}/                | docs/mangacollec/urls_response/unfollow_editions.md         |
| --- |                           --- | --  |     ---     |            | ---                                                  | ---                                                         |
| [ ] |       **user read_multiples** | V1  |    POST     |    user    | **url_base**/v1/reads_multiple/                      | docs/mangacollec/urls_response/reads_multiple.md            |
| [ ] |     **user unread_multiples** | V1  |   DELETE    |    user    | **url_base**/v1/reads_multiple/                      | docs/mangacollec/urls_response/unreads_multiple.md          |
| --- |                           --- | --  |     ---     |            | ---                                                  | ---                                                         |
| [ ] |        **amazon_offer by id** | V1  |     GET     |            | **url_base**/v1/amazon_offer/{id}/                   | -                                                           |
| --- |                           --- | --  |     ---     |            | ---                                                  | ---                                                         |
| [ ] |       **bdfugue_offer by id** | V1  |     GET     |            | **url_base**/v1/bdfugue_offer/{id}/                  | -                                                           |
| --- |                           --- | --  |     ---     |            | ---                                                  | ---                                                         |
