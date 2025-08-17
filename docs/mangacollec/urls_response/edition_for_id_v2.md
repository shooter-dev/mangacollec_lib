# Endpoint Edition for id `333eb14c-5f0a-4130-99fe-d2842cd06349`

- **url** : `https://api.mangacollec.com/v2/editions/{id}`
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
            "id": "333eb14c-5f0a-4130-99fe-d2842cd06349",
            "title": null,
            "series_id": "0fdb6b55-6b5c-4d2a-8afa-530f58bf3203",
            "publisher_id": "122e0ec3-f072-4c5d-b40d-3eba4a82fe1e",
            "parent_edition_id": null,
            "volumes_count": 16,
            "last_volume_number": null,
            "commercial_stop": false,
            "not_finished": false,
            "follow_editions_count": 81044
        },
        {
            "id": "f0f6e66f-4374-4938-945f-6424c3300275",
            "title": "Jaquette alternative",
            "series_id": "0fdb6b55-6b5c-4d2a-8afa-530f58bf3203",
            "publisher_id": "122e0ec3-f072-4c5d-b40d-3eba4a82fe1e",
            "parent_edition_id": "333eb14c-5f0a-4130-99fe-d2842cd06349",
            "volumes_count": 2,
            "last_volume_number": null,
            "commercial_stop": false,
            "not_finished": false,
            "follow_editions_count": 11655
        }
    ],
    "publishers": [
        {
            "id": "122e0ec3-f072-4c5d-b40d-3eba4a82fe1e",
            "title": "Crunchyroll / Kazé",
            "closed": false,
            "editions_count": 324,
            "no_amazon": false
        }
    ],
    "series": [
        {
            "id": "0fdb6b55-6b5c-4d2a-8afa-530f58bf3203",
            "title": "Kaiju n°8",
            "type_id": "106f524e-7283-44b8-aa84-25e9a7fb1f7d",
            "adult_content": false,
            "editions_count": 4,
            "tasks_count": 1
        }
    ],
    "types": [
        {
            "id": "106f524e-7283-44b8-aa84-25e9a7fb1f7d",
            "title": "Manga",
            "to_display": false
        }
    ],
    "volumes": [
        {
            "id": "722a5b33-b61d-4f88-81b5-e4614cef8b9c",
            "title": null,
            "number": 16,
            "release_date": "2025-12-03",
            "isbn": "9782820353443",
            "asin": "2820353444",
            "edition_id": "333eb14c-5f0a-4130-99fe-d2842cd06349",
            "possessions_count": 30,
            "not_sold": false,
            "image_url": null
        },
        {
            "id": "1ce5735f-20be-40f1-a32e-a987926129bf",
            "title": null,
            "number": 14,
            "release_date": "2025-03-26",
            "isbn": "9782820351814",
            "asin": "2820351816",
            "edition_id": "333eb14c-5f0a-4130-99fe-d2842cd06349",
            "possessions_count": 13000,
            "not_sold": false,
            "image_url": "https://m.media-amazon.com/images/I/51VZQjt9JRL.jpg"
        },
        {
            "id": "f0555350-65f7-439b-92f7-4fc1a9e07194",
            "title": null,
            "number": 8,
            "release_date": "2023-03-29",
            "isbn": "9782820347343",
            "asin": "2820347347",
            "edition_id": "54a94112-d5b6-4448-a3f7-2ba675410d14",
            "possessions_count": 8803,
            "not_sold": false,
            "image_url": "https://m.media-amazon.com/images/I/51pSvk+u3+L.jpg"
        }
    ]
}
```