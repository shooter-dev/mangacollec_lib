# Endpoint Publisher for ID `bdef8c9e-7395-465d-8175-a1b985d4aa92`

- **url** : `https://api.mangacollec.com/v2/publishers/{id}`
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
    "publishers": [
        {
            "id": "bdef8c9e-7395-465d-8175-a1b985d4aa92",
            "title": "Pika",
            "closed": false,
            "editions_count": 682,
            "no_amazon": false
        }
    ],
    "editions": [
        {
            "id": "59507c98-7ba0-4249-bb36-7bcb0e3a6ed0",
            "title": "Jaquette Anime",
            "series_id": "4629f6b2-db53-4a24-9e15-16be1365b86d",
            "publisher_id": "bdef8c9e-7395-465d-8175-a1b985d4aa92",
            "parent_edition_id": "2449720e-1698-4f42-ba89-d239ef316a35",
            "volumes_count": 1,
            "last_volume_number": null,
            "commercial_stop": false,
            "not_finished": false,
            "follow_editions_count": 126
        },
        {
            "id": "c531d4fd-ebd4-4286-8db9-21d5d0e0ae23",
            "title": null,
            "series_id": "cc309ede-770c-49b3-a04c-09cceb1723eb",
            "publisher_id": "bdef8c9e-7395-465d-8175-a1b985d4aa92",
            "parent_edition_id": null,
            "volumes_count": 1,
            "last_volume_number": null,
            "commercial_stop": false,
            "not_finished": false,
            "follow_editions_count": 100
        },
        {
            "id": "b506e5af-e2c3-45e0-9ef2-a9a10dcd8060",
            "title": null,
            "series_id": "0b0c0fdc-b6f2-4732-9580-74e82c1811f4",
            "publisher_id": "bdef8c9e-7395-465d-8175-a1b985d4aa92",
            "parent_edition_id": null,
            "volumes_count": 2,
            "last_volume_number": 8,
            "commercial_stop": false,
            "not_finished": false,
            "follow_editions_count": 857
        }
    ],
    "box_editions": [
        {
            "id": "3a10742e-3f8d-48d3-a5c3-0b8a797ff44d",
            "title": "Blue Lock",
            "publisher_id": "bdef8c9e-7395-465d-8175-a1b985d4aa92",
            "boxes_count": 2,
            "adult_content": false,
            "box_follow_editions_count": 1746
        },
        {
            "id": "c2f033b9-cc35-4e52-956c-c5d2d6ff83e3",
            "title": "Criminelles Fiançailles",
            "publisher_id": "bdef8c9e-7395-465d-8175-a1b985d4aa92",
            "boxes_count": 1,
            "adult_content": false,
            "box_follow_editions_count": 991
        },
        {
            "id": "b8df1de4-a658-49e9-a470-b494b40eaa98",
            "title": "Kaguya-sama: Love is War",
            "publisher_id": "bdef8c9e-7395-465d-8175-a1b985d4aa92",
            "boxes_count": 1,
            "adult_content": false,
            "box_follow_editions_count": 315
        }
    ],
    "series": [
        {
            "id": "4629f6b2-db53-4a24-9e15-16be1365b86d",
            "title": "Gachiakuta",
            "type_id": "106f524e-7283-44b8-aa84-25e9a7fb1f7d",
            "adult_content": false,
            "editions_count": 6,
            "tasks_count": 1
        },
        {
            "id": "cc309ede-770c-49b3-a04c-09cceb1723eb",
            "title": "Cervin - Le roi oublié",
            "type_id": "106f524e-7283-44b8-aa84-25e9a7fb1f7d",
            "adult_content": false,
            "editions_count": 1,
            "tasks_count": 1
        },
        {
            "id": "0b0c0fdc-b6f2-4732-9580-74e82c1811f4",
            "title": "Marriage of Convenience",
            "type_id": "fcb5dd8c-b28f-467d-9858-df52dd24e555",
            "adult_content": false,
            "editions_count": 1,
            "tasks_count": 3
        }
    ],
    "types": [
        {
            "id": "106f524e-7283-44b8-aa84-25e9a7fb1f7d",
            "title": "Manga",
            "to_display": false
        },
        {
            "id": "fcb5dd8c-b28f-467d-9858-df52dd24e555",
            "title": "Manhwa",
            "to_display": false
        },
        {
            "id": "3c009f18-811d-4b07-8dde-8249e422ec9e",
            "title": "Global Manga",
            "to_display": false
        }
    ],
    "volumes": [
        {
            "id": "1df96e31-8d77-4d1c-b458-c540771a7e64",
            "title": null,
            "number": 13,
            "release_date": "2025-08-20",
            "isbn": "9791043303753",
            "asin": "B0FH1MNNKX",
            "edition_id": "59507c98-7ba0-4249-bb36-7bcb0e3a6ed0",
            "possessions_count": 4,
            "not_sold": false,
            "image_url": "https://m.media-amazon.com/images/I/51Y+qGTdE4L.jpg"
        },
        {
            "id": "e8197873-894f-4654-8935-256454deeb7a",
            "title": null,
            "number": 1,
            "release_date": "2025-10-15",
            "isbn": "9782811692438",
            "asin": "2811692436",
            "edition_id": "c531d4fd-ebd4-4286-8db9-21d5d0e0ae23",
            "possessions_count": 2,
            "not_sold": false,
            "image_url": "https://m.media-amazon.com/images/I/51GmUfGoX3L.jpg"
        },
        {
            "id": "0dd7b2db-3731-4382-89d4-4070ab6f64dc",
            "title": null,
            "number": 1,
            "release_date": "2025-07-02",
            "isbn": "9782811699642",
            "asin": "2811699643",
            "edition_id": "b506e5af-e2c3-45e0-9ef2-a9a10dcd8060",
            "possessions_count": 499,
            "not_sold": false,
            "image_url": "https://m.media-amazon.com/images/I/51dZcjhgqgL.jpg"
        }
    ],
    "boxes": []
}
```