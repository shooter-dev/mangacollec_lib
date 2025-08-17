# Endpoint Volumes News

- **url** : `https://api.mangacollec.com/v2/volumes/news`
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
    "volumes": [
        {
            "id": "60558312-44fd-4b0c-89f6-59cf48162976",
            "title": null,
            "number": 42,
            "release_date": "2025-06-05",
            "isbn": "9791032719657",
            "asin": "B0DXTTH8HT",
            "edition_id": "10c5a50a-21fd-405f-a846-1c1d5949e8e1",
            "possessions_count": 13011,
            "not_sold": false,
            "image_url": "https://m.media-amazon.com/images/I/51Imn07QC+L.jpg"
        },
        {
            "id": "acdda842-df5a-4ce6-934d-b3ec779c8e51",
            "title": null,
            "number": 27,
            "release_date": "2025-07-03",
            "isbn": "9791032719572",
            "asin": "B0DXTZ1FX8",
            "edition_id": "1a39a08f-aba5-4c7f-8dc7-36eaea8f6354",
            "possessions_count": 7430,
            "not_sold": false,
            "image_url": "https://m.media-amazon.com/images/I/51TE4HjBfjL.jpg"
        },
        {
            "id": "7bfa41bc-1e96-45b3-acc9-164e6e9a2cc7",
            "title": null,
            "number": 1,
            "release_date": "2025-06-04",
            "isbn": "9782344067802",
            "asin": "2344067809",
            "edition_id": "da737ff1-fc24-4c41-8090-8123c5b5d2c0",
            "possessions_count": 6909,
            "not_sold": false,
            "image_url": "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWxsTW1FME5qVmhaUzB4TnpnMUxUUmlPV1V0WVRsbE9TMWtORGd3TldabE1XVXpNbUlHT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--2a15d74434df37e01804d85e74371879d3542224/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJY0c1bkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFMMEFXa0M5QUU9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--7c73e8a32db9248865f33012a40f867d228b3b7c/7bfa41bc-1e96-45b3-acc9-164e6e9a2cc7.png"
        }
    ],
    "editions": [
        {
            "id": "10c5a50a-21fd-405f-a846-1c1d5949e8e1",
            "title": null,
            "series_id": "2f70bcbc-756b-4db3-8159-bb30b602c5b7",
            "publisher_id": "74de7d1e-f2e9-44bb-8a5a-1fe84258c7bf",
            "parent_edition_id": null,
            "volumes_count": 42,
            "last_volume_number": 42,
            "commercial_stop": false,
            "not_finished": false,
            "follow_editions_count": 147416
        },
        {
            "id": "1a39a08f-aba5-4c7f-8dc7-36eaea8f6354",
            "title": null,
            "series_id": "544df61b-edcf-45ec-9ae5-cdf8341a84ca",
            "publisher_id": "74de7d1e-f2e9-44bb-8a5a-1fe84258c7bf",
            "parent_edition_id": null,
            "volumes_count": 28,
            "last_volume_number": 30,
            "commercial_stop": false,
            "not_finished": false,
            "follow_editions_count": 143547
        },
        {
            "id": "da737ff1-fc24-4c41-8090-8123c5b5d2c0",
            "title": "Edition Prestige",
            "series_id": "f41a928c-8450-40e9-805b-3ccf3ac49705",
            "publisher_id": "5e961f4c-9954-452a-961f-4d3d922c370d",
            "parent_edition_id": null,
            "volumes_count": 3,
            "last_volume_number": null,
            "commercial_stop": false,
            "not_finished": false,
            "follow_editions_count": 10181
        }
    ],
    "series": [
        {
            "id": "2f70bcbc-756b-4db3-8159-bb30b602c5b7",
            "title": "My Hero Academia",
            "type_id": "106f524e-7283-44b8-aa84-25e9a7fb1f7d",
            "adult_content": false,
            "editions_count": 7,
            "tasks_count": 1
        },
        {
            "id": "544df61b-edcf-45ec-9ae5-cdf8341a84ca",
            "title": "Jujutsu Kaisen",
            "type_id": "106f524e-7283-44b8-aa84-25e9a7fb1f7d",
            "adult_content": false,
            "editions_count": 6,
            "tasks_count": 1
        },
        {
            "id": "f41a928c-8450-40e9-805b-3ccf3ac49705",
            "title": "Berserk",
            "type_id": "106f524e-7283-44b8-aa84-25e9a7fb1f7d",
            "adult_content": false,
            "editions_count": 6,
            "tasks_count": 1
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
    "boxes": [
        {
            "id": "5980a4ed-eafe-43a5-9213-2af25e01ed2c",
            "title": "Plus Ultra Collector Tome 42",
            "number": 0,
            "release_date": "2025-06-05",
            "isbn": "9791032719862",
            "asin": "B0DXTDPFG1",
            "commercial_stop": false,
            "box_edition_id": "a890d54a-b60d-4a82-be75-06b7d29bf294",
            "box_possessions_count": 5985,
            "image_url": "https://m.media-amazon.com/images/I/512HzrPZ6cL.jpg"
        },
        {
            "id": "3f051d4a-2233-4cce-a970-29b6fe989124",
            "title": "Edition collector Tome 38",
            "number": 0,
            "release_date": "2025-07-04",
            "isbn": "3701580713812",
            "asin": "B0DYJDQS44",
            "commercial_stop": false,
            "box_edition_id": "5d7f884e-449d-4be3-8790-7ccbd9d78f13",
            "box_possessions_count": 4352,
            "image_url": "https://m.media-amazon.com/images/I/41TytYXcK1L.jpg"
        },
        {
            "id": "975c6671-3806-48f7-a617-20e785b22639",
            "title": "Edition collector Tome 14",
            "number": 0,
            "release_date": "2025-07-03",
            "isbn": "9791032724811",
            "asin": "B0DXV83BSD",
            "commercial_stop": false,
            "box_edition_id": "fe5facde-af3d-4f3d-9a95-cf252851fe7f",
            "box_possessions_count": 3976,
            "image_url": "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWxqTWpNME5tUTVOeTFsTlRNNUxUUXpObVV0WVRnM1pDMDNNR1l4TWpnNU4yRmxNVGdHT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--320bc5f877a95f81b6886c53553992f6fe83144a/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFMMEFXa0M5QUU9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--f4740ce9863997714730d7d28982d4fbc8d883df/71Z1EPU+lRL._SL1128_.jpg"
        }
    ],
    "box_editions": [
        {
            "id": "a890d54a-b60d-4a82-be75-06b7d29bf294",
            "title": "My Hero Academia",
            "publisher_id": "74de7d1e-f2e9-44bb-8a5a-1fe84258c7bf",
            "boxes_count": 1,
            "adult_content": false,
            "box_follow_editions_count": 6400
        },
        {
            "id": "5d7f884e-449d-4be3-8790-7ccbd9d78f13",
            "title": "Hunter X Hunter",
            "publisher_id": "4c9547ff-2ef6-439a-80b8-ea705a385b76",
            "boxes_count": 1,
            "adult_content": false,
            "box_follow_editions_count": 4745
        },
        {
            "id": "fe5facde-af3d-4f3d-9a95-cf252851fe7f",
            "title": "Frieren",
            "publisher_id": "74de7d1e-f2e9-44bb-8a5a-1fe84258c7bf",
            "boxes_count": 1,
            "adult_content": false,
            "box_follow_editions_count": 4125
        }
    ],
    "box_volumes": []
}
```