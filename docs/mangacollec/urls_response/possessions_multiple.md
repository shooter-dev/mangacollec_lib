# Endpoint Possession Multiple Volumes for id `5224808b-e085-4140-9f67-33c11697424a`

- **url** : `https://api.mangacollec.com/v1/possessions_multiple`
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
    "possessions": [
        {
            "id": "15e58a38-373c-44f3-8b44-a0938078e2ef",
            "user_id": "a0f0de04-9cd7-421e-b416-6929e0915b2c",
            "volume_id": "5224808b-e085-4140-9f67-33c11697424a",
            "created_at": "2025-08-17T12:56:05.718Z"
        }
    ],
    "follow_editions": [
        {
            "id": "aab0e2e2-36ba-4153-aba5-8592507695c5",
            "user_id": "a0f0de04-9cd7-421e-b416-6929e0915b2c",
            "edition_id": "5d2e24ce-1147-43eb-a499-35431c32705d",
            "following": true,
            "created_at": "2025-08-17T12:56:05.713Z"
        }
    ]
}
```