# Endpoint Kinds List

- **url** : `https://api.mangacollec.com/v2/kinds`
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
    "kinds": [
        {
            "id": "5f2df76f-b8d1-4db6-9e36-506cabdbb1db",
            "title": "Action",
            "series_ids": [
                "b95afc4d-45a4-46d5-bc36-dd40a1f31822",
                "ddacaa94-ccfd-431d-93f4-21975abd304f",
                "0f585dea-1bac-47b2-959d-f894304017f2",
                "a7f16247-6308-4455-991c-1afbf940c621"
            ]
        },
        {
            "id": "7673ab04-ceca-4388-b52b-7b4d2af58e45",
            "title": "Aventure",
            "series_ids": [
                "9a8f7908-ef7a-4ec0-a63b-29b80c2a7a19",
                "b9be3112-2ca5-4f1f-a73d-940b1c852131",
                "e9ae8ef7-7931-472c-bc16-55d5aa4e8c54"
            ]
        },
        {
            "id": "05e9dc5b-bad9-4fb6-be5c-66925d58b911",
            "title": "Démon",
            "series_ids": [
                "a320ac19-4318-4471-9e4e-eb017f4584d5"
            ]
        }
    ]
}
```