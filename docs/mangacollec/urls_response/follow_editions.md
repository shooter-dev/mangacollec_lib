# Endpoint Follow editions for id `bd982e24-525d-47cc-a152-7582e5f8236d`

- **url** : `https://api.mangacollec.com/v1/follow_editions/`
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
{
    "edition_id": "bd982e24-525d-47cc-a152-7582e5f8236d",
    "following": true
}
```

---

## Response

```json
{
    "id": "3dca1d8f-7a69-4c9d-af33-a9ecc46e79c5",
    "user_id": "a0f0de04-9cd7-421e-b416-6929e0915b2c",
    "edition_id": "bd982e24-525d-47cc-a152-7582e5f8236d",
    "following": true,
    "created_at": "2025-08-17T12:36:15.593Z",
    "updated_at": "2025-08-17T12:36:15.593Z"
}
```