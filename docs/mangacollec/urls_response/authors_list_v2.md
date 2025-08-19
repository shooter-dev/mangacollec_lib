# Endpoint Authors 

- **url** : `https://api.mangacollecc.com/v2/authors
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
    "authors": [
        {
            "id": "370ac96c-49e0-4f09-b7c4-662cb1374b21",
            "name": "Kishimoto",
            "first_name": "Masashi",
            "tasks_count": 32
        },
        {
            "id": "e6cc4590-0b5e-4122-9428-b9b185bdb221",
            "name": "Oda",
            "first_name": "Eiichirō",
            "tasks_count": 29
        },
        {
            "id": "edad2d63-cc34-42b8-9bc2-ca9e210b670d",
            "name": "Horikoshi",
            "first_name": "Kôhei",
            "tasks_count": 16
        }
    ]
}
```