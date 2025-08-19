# Endpoint Reads volumes for id `dcf1f103-48d0-4a0a-b20a-acc20f656f04`

- **url** : `https://api.mangacollec.com/v1/reads_multiple`
- **methodes** : `POST`

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
[
  {"volume_id":"5224808b-e085-4140-9f67-33c11697424a"}
]
```

---

## Response `200`

```json
{
    "reads": [
        {
            "id": "739f5f3b-f3e4-4889-877c-5b4f17c877c3",
            "user_id": "1f32e2fc-c7c3-4dd3-9f18-e0fcdb075295",
            "volume_id": "dcf1f103-48d0-4a0a-b20a-acc20f656f04",
            "created_at": "2025-08-17T13:15:35.542Z"
        }
    ],
    "read_editions": [
        {
            "id": "4d042a7d-ddb9-47ae-b898-c45dde568be9",
            "user_id": "1f32e2fc-c7c3-4dd3-9f18-e0fcdb075295",
            "edition_id": "1e68b837-be95-4baa-a38f-09c082777c04",
            "reading": true,
            "created_at": "2025-08-17T13:15:35.536Z"
        }
    ]
}
```