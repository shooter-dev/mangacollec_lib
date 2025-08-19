# Endpoint UnReads Multiple Volumes for ids `739f5f3b-f3e4-4889-877c-5b4f17c877c3`

- **url** : `https://api.mangacollec.com/v1/reads_multiple`
- **methodes** : `DELETE`

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
  {"id":"739f5f3b-f3e4-4889-877c-5b4f17c877c3"}
]
```

---

## Response `200`

```json
{
    "reads": [
        {
            "id": "739f5f3b-f3e4-4889-877c-5b4f17c877c3",
            "deleted": true
        }
    ],
    "read_editions": [
        {
            "id": "4d042a7d-ddb9-47ae-b898-c45dde568be9",
            "deleted": true
        }
    ]
}
```