# Endpoint User Collection (Public) `shooterdev`

- **url** : `https://api.mangacollec.com/v2/user/{username}/collection`
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
            "id": "aa0f2403-cc92-45fb-9ace-438eb242d21c",
            "title": null,
            "series_id": "ba90fa8d-5cec-43c3-ba68-e0189d2ea7de",
            "publisher_id": "e92bb57e-3fa1-4cc0-bd69-44f2f89e502c",
            "parent_edition_id": null,
            "volumes_count": 12,
            "last_volume_number": 12,
            "commercial_stop": false,
            "not_finished": false,
            "follow_editions_count": 6138
        },
        {
            "id": "af8a923a-13e5-4233-8a4f-6609c8e3e336",
            "title": null,
            "series_id": "7e1fd99e-bae9-4e67-adc5-0401d45074cd",
            "publisher_id": "2f064f84-a653-48c1-b1f6-27a694bb7ec6",
            "parent_edition_id": null,
            "volumes_count": 10,
            "last_volume_number": 10,
            "commercial_stop": false,
            "not_finished": false,
            "follow_editions_count": 1515
        },
        {
            "id": "c3dee740-1708-45ea-843d-c0f588c28576",
            "title": null,
            "series_id": "b175251f-41e5-4299-a94a-f41cee4c6a0a",
            "publisher_id": "122e0ec3-f072-4c5d-b40d-3eba4a82fe1e",
            "parent_edition_id": null,
            "volumes_count": 36,
            "last_volume_number": null,
            "commercial_stop": false,
            "not_finished": false,
            "follow_editions_count": 62736
        }
    ],
    "series": [
        {
            "id": "ba90fa8d-5cec-43c3-ba68-e0189d2ea7de",
            "title": "Mirai Nikki",
            "type_id": "106f524e-7283-44b8-aa84-25e9a7fb1f7d",
            "adult_content": false,
            "editions_count": 1,
            "tasks_count": 1,
            "kinds_ids": []
        },
        {
            "id": "7e1fd99e-bae9-4e67-adc5-0401d45074cd",
            "title": "The Civilization Blaster - Zetsuen no Tempest",
            "type_id": "106f524e-7283-44b8-aa84-25e9a7fb1f7d",
            "adult_content": false,
            "editions_count": 1,
            "tasks_count": 3,
            "kinds_ids": [
                "5f2df76f-b8d1-4db6-9e36-506cabdbb1db",
                "eb5eb1b3-9f89-43ab-b0fa-0ef61f10d633",
                "9d6a131c-4b4e-4cf6-a9aa-de78087d672d",
                "1c608d8c-7cc0-408d-b2ab-09cf0e6c7b1d",
                "2b38ee99-9539-49b5-a0bb-b7dfbd495764",
                "d5a3385a-cfcd-45f6-8f82-0c80956b084d",
                "805f36d4-88bb-42af-b586-1b9764d54208",
                "9d621a26-4842-4b1f-a69a-d916dbb04b1b",
                "131af2d8-4342-49df-91bc-dae1628d70c8"
            ]
        },
        {
            "id": "b175251f-41e5-4299-a94a-f41cee4c6a0a",
            "title": "Black Clover",
            "type_id": "106f524e-7283-44b8-aa84-25e9a7fb1f7d",
            "adult_content": false,
            "editions_count": 3,
            "tasks_count": 1,
            "kinds_ids": [
                "5f2df76f-b8d1-4db6-9e36-506cabdbb1db",
                "7673ab04-ceca-4388-b52b-7b4d2af58e45",
                "b19c9c05-2e40-4821-bf87-3bf9822ea6eb",
                "59a6ad18-392a-4e22-98ad-61fe58f0fee5",
                "1c608d8c-7cc0-408d-b2ab-09cf0e6c7b1d",
                "d5a3385a-cfcd-45f6-8f82-0c80956b084d"
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
        },
        {
            "id": "f41d81b0-fca6-4445-a903-da310e0899d2",
            "title": "Artbook",
            "to_display": true
        }
    ],
    "kinds": [
        {
            "id": "5f2df76f-b8d1-4db6-9e36-506cabdbb1db",
            "title": "Action"
        },
        {
            "id": "eb5eb1b3-9f89-43ab-b0fa-0ef61f10d633",
            "title": "Enquête"
        },
        {
            "id": "9d6a131c-4b4e-4cf6-a9aa-de78087d672d",
            "title": "Fantastique"
        }
    ],
    "volumes": [
        {
            "id": "2f688404-8bb0-44ff-807a-e6712d1ed937",
            "title": null,
            "number": 11,
            "release_date": "2011-06-25",
            "isbn": "9782203038424",
            "asin": "220303842X",
            "edition_id": "aa0f2403-cc92-45fb-9ace-438eb242d21c",
            "possessions_count": 1984,
            "not_sold": false,
            "image_url": "https://images-eu.ssl-images-amazon.com/images/I/516hrzPRk1L.jpg"
        },
        {
            "id": "99da0c7e-f316-468c-bdc0-6245caa47fe8",
            "title": null,
            "number": 3,
            "release_date": "2009-09-09",
            "isbn": "9782203022393",
            "asin": "2203022396",
            "edition_id": "aa0f2403-cc92-45fb-9ace-438eb242d21c",
            "possessions_count": 2997,
            "not_sold": false,
            "image_url": "https://images-eu.ssl-images-amazon.com/images/I/511cM6MsnaL.jpg"
        },
        {
            "id": "f781b5cf-a971-464e-9ed6-dad8e5992fa6",
            "title": null,
            "number": 8,
            "release_date": "2010-09-08",
            "isbn": "9782203035201",
            "asin": "220303520X",
            "edition_id": "aa0f2403-cc92-45fb-9ace-438eb242d21c",
            "possessions_count": 2159,
            "not_sold": false,
            "image_url": "https://images-eu.ssl-images-amazon.com/images/I/51L-V1lie1L.jpg"
        }
    ],
    "box_volumes": [
        {
            "id": "85772fc7-fa25-424b-b1a9-30d38c26625f",
            "box_id": "1e9aa5ea-e919-423e-82ae-10bc1bc3e4a8",
            "volume_id": "45ef316f-f99c-4adb-8f7f-eacec79c52a5",
            "included": true
        },
        {
            "id": "e239a454-c47b-4e0b-b823-616a837be87e",
            "box_id": "d22b1b50-2f04-4a4c-90d4-7a47ceee2703",
            "volume_id": "7dc7a7f8-c53d-4845-8d92-c673cb101a7a",
            "included": true
        },
        {
            "id": "a97200f7-ad48-49a2-aed6-866bd1d0e69c",
            "box_id": "d22b1b50-2f04-4a4c-90d4-7a47ceee2703",
            "volume_id": "27dcc589-ae21-43f1-a6e8-cf8aba11f169",
            "included": true
        }
    ],
    "possessions": [
        {
            "id": "c917d0ab-b851-4797-86da-4b4910438549",
            "volume_id": "99da0c7e-f316-468c-bdc0-6245caa47fe8",
            "user_id": "1f32e2fc-c7c3-4dd3-9f18-e0fcdb075295",
            "created_at": "2019-03-07T15:34:48.337Z"
        },
        {
            "id": "4ad2d87b-d435-4007-acb1-b47bf8021088",
            "volume_id": "ee025c0b-4e9f-4ad6-bd43-75dd60225a09",
            "user_id": "1f32e2fc-c7c3-4dd3-9f18-e0fcdb075295",
            "created_at": "2019-03-07T15:36:54.266Z"
        },
        {
            "id": "df54e91d-ce0e-4e41-9ee3-bfd33a5c2dd5",
            "volume_id": "21c7b979-c6cb-4b36-b3c1-533b69410295",
            "user_id": "1f32e2fc-c7c3-4dd3-9f18-e0fcdb075295",
            "created_at": "2019-03-07T15:36:54.291Z"
        }
    ],
    "box_follow_editions": [
        {
            "id": "378db86b-c684-4716-9285-1d826c044821",
            "box_edition_id": "7c983ccc-a2f9-40b3-b566-7ee6a0e23b12",
            "user_id": "1f32e2fc-c7c3-4dd3-9f18-e0fcdb075295",
            "following": true,
            "created_at": "2023-06-06T17:33:50.157Z",
            "updated_at": "2023-06-06T17:33:50.157Z"
        },
        {
            "id": "8659b2a3-15a2-447f-8aa6-c1ac5a315e10",
            "box_edition_id": "090584e3-9033-4aaf-8d2f-49bc3c8ac9eb",
            "user_id": "1f32e2fc-c7c3-4dd3-9f18-e0fcdb075295",
            "following": true,
            "created_at": "2023-12-05T21:28:55.091Z",
            "updated_at": "2023-12-05T21:28:55.091Z"
        },
        {
            "id": "d79894f8-f5d5-43b9-a901-ba701e10fabb",
            "box_edition_id": "0d3a7a29-fc4c-40e2-80d4-03e0777e1cd8",
            "user_id": "1f32e2fc-c7c3-4dd3-9f18-e0fcdb075295",
            "following": true,
            "created_at": "2024-04-20T06:15:39.864Z",
            "updated_at": "2024-04-20T06:15:39.864Z"
        }
    ],
    "box_possessions": [
        {
            "id": "0024c8a5-ef20-4851-aca2-419ba8e75c94",
            "box_id": "1e9aa5ea-e919-423e-82ae-10bc1bc3e4a8",
            "user_id": "1f32e2fc-c7c3-4dd3-9f18-e0fcdb075295",
            "created_at": "2023-06-06T17:33:50.140Z"
        },
        {
            "id": "34faeab7-2f9a-445f-b13b-1c2d483c2583",
            "box_id": "c6c57add-3d32-4618-8b80-fef03d50a29c",
            "user_id": "1f32e2fc-c7c3-4dd3-9f18-e0fcdb075295",
            "created_at": "2023-12-05T21:28:55.080Z"
        },
        {
            "id": "922ae8f4-f3a5-47fb-8efc-0152ca65b8c3",
            "box_id": "53024c1e-51be-4dce-8db8-40ac7d97c01b",
            "user_id": "1f32e2fc-c7c3-4dd3-9f18-e0fcdb075295",
            "created_at": "2023-10-11T13:19:03.606Z"
        }
    ]
}
```
