# Endpoint Series List

- **url** : `https://api.mangacollec.com/v2/series`
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
    "series": [
        {
            "id": "a02cf154-af6c-4f08-9a7a-32f7bc229ac8",
            "title": "One Piece",
            "type_id": "106f524e-7283-44b8-aa84-25e9a7fb1f7d",
            "adult_content": false,
            "editions_count": 5,
            "tasks_count": 1
        },
        {
            "id": "2f70bcbc-756b-4db3-8159-bb30b602c5b7",
            "title": "My Hero Academia",
            "type_id": "106f524e-7283-44b8-aa84-25e9a7fb1f7d",
            "adult_content": false,
            "editions_count": 7,
            "tasks_count": 1
        },
        {
            "id": "a320ac19-4318-4471-9e4e-eb017f4584d5",
            "title": "Demon Slayer",
            "type_id": "106f524e-7283-44b8-aa84-25e9a7fb1f7d",
            "adult_content": false,
            "editions_count": 5,
            "tasks_count": 1
        }
    ]
}
```