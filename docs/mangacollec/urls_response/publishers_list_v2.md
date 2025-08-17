# Endpoint Publishers List

- **url** : `https://api.mangacollec.com/v2/publishers`
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
        },
        {
            "id": "4c9547ff-2ef6-439a-80b8-ea705a385b76",
            "title": "Kana",
            "closed": false,
            "editions_count": 592,
            "no_amazon": false
        },
        {
            "id": "5e961f4c-9954-452a-961f-4d3d922c370d",
            "title": "Glénat",
            "closed": false,
            "editions_count": 518,
            "no_amazon": false
        }
    ]
}
```