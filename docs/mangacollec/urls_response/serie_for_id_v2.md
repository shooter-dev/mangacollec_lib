# Endpoint Serie for ID `a320ac19-4318-4471-9e4e-eb017f4584d5`

- **url** : `https://api.mangacollec.com/v2/series/{id}`
- **methodes** : `GET`

---

## Header

```json
{
  "Authorization" : "Bearer {token}",
  "Accept" : "application/json",
  "Content-Type" : "application/json",
  "User-Agent" : ""
}
```

---

## Body

```json
{}
```

---

## Response

```json
{
    "series": [
        {
            "id": "a320ac19-4318-4471-9e4e-eb017f4584d5",
            "title": "Demon Slayer",
            "type_id": "106f524e-7283-44b8-aa84-25e9a7fb1f7d",
            "adult_content": false,
            "editions_count": 5,
            "tasks_count": 1,
            "kinds_ids": [
                "5f2df76f-b8d1-4db6-9e36-506cabdbb1db",
                "7673ab04-ceca-4388-b52b-7b4d2af58e45",
                "05e9dc5b-bad9-4fb6-be5c-66925d58b911",
                "acd6bec9-507d-46ab-a1de-f18f8b8ca83c",
                "9d6a131c-4b4e-4cf6-a9aa-de78087d672d",
                "4b028255-c92e-4ff7-a732-7754bcf4afe6",
                "d5a3385a-cfcd-45f6-8f82-0c80956b084d"
            ]
        }
    ],
    "types": [
        {
            "id": "106f524e-7283-44b8-aa84-25e9a7fb1f7d",
            "title": "Manga",
            "to_display": false
        }
    ],
    "kinds": [
        {
            "id": "5f2df76f-b8d1-4db6-9e36-506cabdbb1db",
            "title": "Action"
        },
        {
            "id": "7673ab04-ceca-4388-b52b-7b4d2af58e45",
            "title": "Aventure"
        },
        {
            "id": "05e9dc5b-bad9-4fb6-be5c-66925d58b911",
            "title": "Démon"
        }
    ],
    "tasks": [
        {
            "id": "5c522a92-899f-4c44-b9ef-719b8aa111d7",
            "job_id": "dc7b6062-6aae-49ee-87a2-95d47ab52600",
            "series_id": "a320ac19-4318-4471-9e4e-eb017f4584d5",
            "author_id": "95919709-c155-4a04-9525-e06d81025a62"
        }
    ],
    "jobs": [
        {
            "id": "dc7b6062-6aae-49ee-87a2-95d47ab52600",
            "title": "Auteur"
        }
    ],
    "authors": [
        {
            "id": "95919709-c155-4a04-9525-e06d81025a62",
            "name": "Gotouge",
            "first_name": "Koyoharu",
            "tasks_count": 15
        }
    ],
    "editions": [
        {
            "id": "17090559-1f60-478a-9993-98de13643a10",
            "title": "Edition Pilier",
            "series_id": "a320ac19-4318-4471-9e4e-eb017f4584d5",
            "publisher_id": "df4bb56a-de70-48ed-a507-b946f7ae2c0e",
            "parent_edition_id": null,
            "volumes_count": 8,
            "last_volume_number": 8,
            "commercial_stop": false,
            "not_finished": false,
            "follow_editions_count": 6208
        },
        {
            "id": "56a08fea-5f6b-44ab-8daf-5cee677f6cf2",
            "title": null,
            "series_id": "a320ac19-4318-4471-9e4e-eb017f4584d5",
            "publisher_id": "df4bb56a-de70-48ed-a507-b946f7ae2c0e",
            "parent_edition_id": null,
            "volumes_count": 23,
            "last_volume_number": 23,
            "commercial_stop": false,
            "not_finished": false,
            "follow_editions_count": 146011
        },
        {
            "id": "d65cbaab-54f1-418c-9378-cb698321605c",
            "title": "Edition Collector Noël",
            "series_id": "a320ac19-4318-4471-9e4e-eb017f4584d5",
            "publisher_id": "df4bb56a-de70-48ed-a507-b946f7ae2c0e",
            "parent_edition_id": "56a08fea-5f6b-44ab-8daf-5cee677f6cf2",
            "volumes_count": 1,
            "last_volume_number": null,
            "commercial_stop": false,
            "not_finished": false,
            "follow_editions_count": 3080
        }
    ],
    "publishers": [
        {
            "id": "df4bb56a-de70-48ed-a507-b946f7ae2c0e",
            "title": "Panini",
            "closed": false,
            "editions_count": 429,
            "no_amazon": false
        }
    ],
    "volumes": [
        {
            "id": "cfd7d6e5-0e4f-47b7-8031-6eaab5be7139",
            "title": null,
            "number": 10,
            "release_date": "2020-08-12",
            "isbn": "9782809488289",
            "asin": "2809488282",
            "edition_id": "56a08fea-5f6b-44ab-8daf-5cee677f6cf2",
            "possessions_count": 84270,
            "not_sold": false,
            "image_url": "https://m.media-amazon.com/images/I/51KpvC4rrgL.jpg"
        },
        {
            "id": "e8bc74d5-3afb-4eee-a344-421b9c9f4c05",
            "title": null,
            "number": 17,
            "release_date": "2021-05-12",
            "isbn": "9782809496987",
            "asin": "2809496986",
            "edition_id": "56a08fea-5f6b-44ab-8daf-5cee677f6cf2",
            "possessions_count": 74529,
            "not_sold": false,
            "image_url": "https://m.media-amazon.com/images/I/51BOH-Ays2L.jpg"
        },
        {
            "id": "72f73c6e-3d3d-43ed-9cd6-dabbcfbd6c75",
            "title": null,
            "number": 18,
            "release_date": "2021-07-15",
            "isbn": "9782809498103",
            "asin": "2809498105",
            "edition_id": "56a08fea-5f6b-44ab-8daf-5cee677f6cf2",
            "possessions_count": 69958,
            "not_sold": false,
            "image_url": "https://m.media-amazon.com/images/I/51vrKY6Eg4S.jpg"
        }
    ],
    "box_editions": [
        {
            "id": "2d011677-903a-4adf-a1b8-abef4882c97b",
            "title": "Demon Slayer",
            "publisher_id": "df4bb56a-de70-48ed-a507-b946f7ae2c0e",
            "boxes_count": 6,
            "adult_content": false,
            "box_follow_editions_count": 881
        },
        {
            "id": "b6df9e4d-c62c-4314-8460-158f4bfc06b8",
            "title": "Demon Slayer",
            "publisher_id": "df4bb56a-de70-48ed-a507-b946f7ae2c0e",
            "boxes_count": 1,
            "adult_content": false,
            "box_follow_editions_count": 7216
        },
        {
            "id": "67ffba62-913e-48a3-95c8-82175a609b0d",
            "title": "Demon Slayer",
            "publisher_id": "df4bb56a-de70-48ed-a507-b946f7ae2c0e",
            "boxes_count": 3,
            "adult_content": false,
            "box_follow_editions_count": 1200
        }
    ],
    "boxes": [
        {
            "id": "13595d56-cf87-4fe3-9e58-4afc60e476b9",
            "title": "Pack découverte",
            "number": 0,
            "release_date": "2025-01-22",
            "isbn": "9791039133609",
            "asin": "B0DHGCJCN3",
            "commercial_stop": false,
            "box_edition_id": "67ffba62-913e-48a3-95c8-82175a609b0d",
            "box_possessions_count": 75,
            "image_url": "https://m.media-amazon.com/images/I/512s9dwAUWL.jpg"
        },
        {
            "id": "892225b9-dfa0-47b2-a7a0-6a25230830fa",
            "title": "Coffret collector Tome 19 ",
            "number": 0,
            "release_date": "2021-10-13",
            "isbn": "9791039101424",
            "asin": "B0948KS7BW",
            "commercial_stop": false,
            "box_edition_id": "9d0f2d77-5829-412e-852b-0a76fdd5b02b",
            "box_possessions_count": 8299,
            "image_url": "https://m.media-amazon.com/images/I/51fCKdbw6SL.jpg"
        },
        {
            "id": "02284b39-2b33-41fd-a36c-327819dcc6b8",
            "title": "Coffret Tomes 4 à 6",
            "number": 2,
            "release_date": "2020-11-25",
            "isbn": "9782809492507",
            "asin": "2809492506",
            "commercial_stop": false,
            "box_edition_id": "c3993c87-2bf5-434d-bd62-442a36b2744e",
            "box_possessions_count": 1292,
            "image_url": "https://m.media-amazon.com/images/I/512iAkZGt6L.jpg"
        }
    ],
    "box_volumes": [
        {
            "id": "ef2eb005-6ed9-4958-918f-f0e0b4ba334c",
            "box_id": "c00b7e0e-dd6d-435c-8266-601de7977400",
            "volume_id": "35240bc6-b618-4a74-9511-3a0f60f2bc2e",
            "included": true
        },
        {
            "id": "60d768aa-68c1-40e0-a762-adabb089af18",
            "box_id": "c00b7e0e-dd6d-435c-8266-601de7977400",
            "volume_id": "664aa063-8aef-4aea-a6da-44e2effa7134",
            "included": true
        },
        {
            "id": "47fca3ac-8b30-4033-81d7-afc0b78b913c",
            "box_id": "c00b7e0e-dd6d-435c-8266-601de7977400",
            "volume_id": "da22139c-910c-4bdd-8622-20f7122cb60d",
            "included": true
        }
    ]
}
```