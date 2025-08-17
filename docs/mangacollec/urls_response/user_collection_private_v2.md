# Endpoint User Collection (Private)

- **url** : `https://api.mangacollec.com/v2/users/me/collection`
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
    "editions": [
        {
            "id": "89ca1d5b-f4c0-4e2f-8ca3-54f68b50432e",
            "title": null,
            "series_id": "6738a67b-adcd-43e8-9473-16ecd27b0b87",
            "publisher_id": "2f064f84-a653-48c1-b1f6-27a694bb7ec6",
            "parent_edition_id": null,
            "volumes_count": 15,
            "last_volume_number": null,
            "commercial_stop": false,
            "not_finished": false,
            "follow_editions_count": 128524
        },
        {
            "id": "4d717eae-a59d-4f93-af51-2cd02c0b0ab0",
            "title": "Jaquette alternative",
            "series_id": "cbc376d9-130c-4e17-9954-752c20133aa2",
            "publisher_id": "74de7d1e-f2e9-44bb-8a5a-1fe84258c7bf",
            "parent_edition_id": "ec5a4e23-5ca8-4707-89bc-cdcb9fb4cc3f",
            "volumes_count": 3,
            "last_volume_number": null,
            "commercial_stop": false,
            "not_finished": false,
            "follow_editions_count": 12659
        },
        {
            "id": "92079a47-7191-4b8b-b8d2-9f467d2dc5af",
            "title": null,
            "series_id": "ed782ee9-465a-4357-9ef7-8447fa843068",
            "publisher_id": "c5b95b3c-5657-44df-a960-e2cb17bcd0f7",
            "parent_edition_id": null,
            "volumes_count": 4,
            "last_volume_number": null,
            "commercial_stop": false,
            "not_finished": false,
            "follow_editions_count": 2231
        }
    ],
    "series": [
        {
            "id": "6738a67b-adcd-43e8-9473-16ecd27b0b87",
            "title": "Spy x Family",
            "type_id": "106f524e-7283-44b8-aa84-25e9a7fb1f7d",
            "adult_content": false,
            "editions_count": 8,
            "tasks_count": 1,
            "kinds_ids": [
                "5f2df76f-b8d1-4db6-9e36-506cabdbb1db",
                "eb84f0d1-680d-4127-a416-3bb78c365d9d",
                "d5a3385a-cfcd-45f6-8f82-0c80956b084d",
                "820abc9c-f616-437f-9f7e-d0f9a387072c"
            ]
        },
        {
            "id": "cbc376d9-130c-4e17-9954-752c20133aa2",
            "title": "Les Carnets de l'Apothicaire",
            "type_id": "106f524e-7283-44b8-aa84-25e9a7fb1f7d",
            "adult_content": false,
            "editions_count": 4,
            "tasks_count": 3,
            "kinds_ids": [
                "acd6bec9-507d-46ab-a1de-f18f8b8ca83c",
                "4b028255-c92e-4ff7-a732-7754bcf4afe6",
                "fc8b3d02-6e73-4354-b0e1-7d361b6c64d5",
                "820abc9c-f616-437f-9f7e-d0f9a387072c",
                "83558195-a5ee-4acb-a392-9da6f625ad7f"
            ]
        },
        {
            "id": "ed782ee9-465a-4357-9ef7-8447fa843068",
            "title": "Villainess level 99",
            "type_id": "106f524e-7283-44b8-aa84-25e9a7fb1f7d",
            "adult_content": false,
            "editions_count": 1,
            "tasks_count": 3,
            "kinds_ids": [
                "7673ab04-ceca-4388-b52b-7b4d2af58e45",
                "59a6ad18-392a-4e22-98ad-61fe58f0fee5",
                "8ad5487a-46e8-4d4b-b0e7-f903f57bb092",
                "1c608d8c-7cc0-408d-b2ab-09cf0e6c7b1d",
                "36a16e6e-9003-42a3-95b1-2af5b13c62b3",
                "ad1cbbc7-4ee3-441f-a34a-176fdbc7757b"
            ]
        }
    ],
    "types": [
        {
            "id": "106f524e-7283-44b8-aa84-25e9a7fb1f7d",
            "title": "Manga",
            "to_display": false
        },
        {
            "id": "bb3d92a9-020a-4d3f-adec-77bebe9980db",
            "title": "Roman",
            "to_display": true
        }
    ],
    "kinds": [],
    "volumes": [
        {
            "id": "804b8800-e8c7-47a8-b3cd-02e13e81fb16",
            "title": null,
            "number": 15,
            "release_date": "2025-10-09",
            "isbn": "9791042018733",
            "asin": "B0FC21FF2K",
            "edition_id": "89ca1d5b-f4c0-4e2f-8ca3-54f68b50432e",
            "possessions_count": 41,
            "not_sold": false,
            "image_url": "https://m.media-amazon.com/images/I/418Ruv8+AeL.jpg"
        },
        {
            "id": "9fd97b53-bbba-4149-a2b6-d731660f9476",
            "title": null,
            "number": 2,
            "release_date": "2020-11-12",
            "isbn": "9782380710250",
            "asin": "2380710252",
            "edition_id": "89ca1d5b-f4c0-4e2f-8ca3-54f68b50432e",
            "possessions_count": 106117,
            "not_sold": false,
            "image_url": "https://m.media-amazon.com/images/I/41TI9+CXNxL.jpg"
        },
        {
            "id": "3bd20d49-37bf-4d65-b9f0-1f2574d1f77b",
            "title": null,
            "number": 13,
            "release_date": "2024-10-10",
            "isbn": "9791042014704",
            "asin": "B0D6Y7KJFT",
            "edition_id": "89ca1d5b-f4c0-4e2f-8ca3-54f68b50432e",
            "possessions_count": 24040,
            "not_sold": false,
            "image_url": "https://m.media-amazon.com/images/I/41Lix5y-wAL.jpg"
        }
    ],
    "box_editions": [
        {
            "id": "ca91fd0b-65d4-4a0d-8282-c199e2cd2bd3",
            "title": "Tokyo Revengers",
            "publisher_id": "5e961f4c-9954-452a-961f-4d3d922c370d",
            "boxes_count": 1,
            "adult_content": false,
            "box_follow_editions_count": 10283
        }
    ],
    "boxes": [
        {
            "id": "5879aa24-d033-47b2-b34a-7858d5da717a",
            "title": "Coffret collector Tome 23",
            "number": 0,
            "release_date": "2023-03-01",
            "isbn": "9782344056943",
            "asin": "2344056947",
            "commercial_stop": false,
            "box_edition_id": "ca91fd0b-65d4-4a0d-8282-c199e2cd2bd3",
            "box_possessions_count": 9985,
            "image_url": "https://m.media-amazon.com/images/I/41EA-ngt7gL.jpg"
        }
    ],
    "box_volumes": [
        {
            "id": "f7095e3b-3539-40e3-8439-27496dfd6e49",
            "box_id": "5879aa24-d033-47b2-b34a-7858d5da717a",
            "volume_id": "cb700641-c306-4e70-81a2-e750f706864a",
            "included": true
        },
        {
            "id": "bffe5580-6fe4-4198-ad54-becbe2cd5bb2",
            "box_id": "5879aa24-d033-47b2-b34a-7858d5da717a",
            "volume_id": "659fdd94-cdd0-48e9-ba50-4f91d2dd1624",
            "included": true
        }
    ],
    "follow_editions": [
        {
            "id": "b09eed30-dcc4-4ec7-bec1-06df80228f98",
            "edition_id": "89ca1d5b-f4c0-4e2f-8ca3-54f68b50432e",
            "user_id": "a0f0de04-9cd7-421e-b416-6929e0915b2c",
            "following": true,
            "created_at": "2024-08-26T19:58:28.539Z",
            "updated_at": "2024-08-26T19:58:28.539Z"
        },
        {
            "id": "230e1e39-64b7-45a8-8673-e4e95309f141",
            "edition_id": "4d717eae-a59d-4f93-af51-2cd02c0b0ab0",
            "user_id": "a0f0de04-9cd7-421e-b416-6929e0915b2c",
            "following": true,
            "created_at": "2024-08-26T19:58:28.549Z",
            "updated_at": "2024-08-26T19:58:28.549Z"
        },
        {
            "id": "14260ba7-33ca-40e6-8ed2-90b90388f9d4",
            "edition_id": "92079a47-7191-4b8b-b8d2-9f467d2dc5af",
            "user_id": "a0f0de04-9cd7-421e-b416-6929e0915b2c",
            "following": true,
            "created_at": "2024-08-26T19:58:28.555Z",
            "updated_at": "2024-08-26T19:58:28.555Z"
        }
    ],
    "possessions": [
        {
            "id": "1259853c-8711-4099-b8b1-856cfb204c24",
            "volume_id": "add762e6-0af7-4618-a1ab-9ff911bec222",
            "user_id": "a0f0de04-9cd7-421e-b416-6929e0915b2c",
            "created_at": "2024-08-26T19:58:28.638Z"
        },
        {
            "id": "08bd4ac9-cd77-440d-8676-ea34bead73f3",
            "volume_id": "1c1cc1a8-5f47-4c07-ac93-94a0f2b9e706",
            "user_id": "a0f0de04-9cd7-421e-b416-6929e0915b2c",
            "created_at": "2024-08-26T19:58:28.644Z"
        },
        {
            "id": "b4b22557-ed09-4f96-8f77-f213bd7d946e",
            "volume_id": "b16dcea0-079b-42f9-b2b1-5e303362db72",
            "user_id": "a0f0de04-9cd7-421e-b416-6929e0915b2c",
            "created_at": "2024-08-26T19:58:28.656Z"
        }
    ],
    "box_follow_editions": [
        {
            "id": "85fc7599-3d40-4be9-b3ec-28500a608497",
            "box_edition_id": "ca91fd0b-65d4-4a0d-8282-c199e2cd2bd3",
            "user_id": "a0f0de04-9cd7-421e-b416-6929e0915b2c",
            "following": true,
            "created_at": "2023-04-11T17:24:51.073Z",
            "updated_at": "2023-04-11T17:24:51.073Z"
        }
    ],
    "box_possessions": [
        {
            "id": "0dd56669-d8bc-4e5b-a8aa-0b99100bdb9b",
            "box_id": "5879aa24-d033-47b2-b34a-7858d5da717a",
            "user_id": "a0f0de04-9cd7-421e-b416-6929e0915b2c",
            "created_at": "2023-04-11T17:24:51.056Z"
        }
    ],
    "read_editions": [],
    "reads": []
}
```