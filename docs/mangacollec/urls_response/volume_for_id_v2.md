# Endpoint Volume for ID `6e22eae9-2afd-45ba-8c26-d10d4224d5bf`

- **url** : `https://api.mangacollec.com/v2/volumes/{id}`
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
            "id": "6e22eae9-2afd-45ba-8c26-d10d4224d5bf",
            "title": null,
            "number": 1,
            "release_date": "2016-06-01",
            "isbn": "9782818936238",
            "asin": "2818936233",
            "edition_id": "aa4da196-ccda-4b33-af3f-6f4b75145c6b",
            "possessions_count": 18110,
            "not_sold": false,
            "image_url": "https://images-eu.ssl-images-amazon.com/images/I/51pTipXj2mL.jpg",
            "nb_pages": 160,
            "content": "<p><strong>Trahison, monstres et rivalités : comment survivre dans un RPG avec juste un bouclier ?</strong></p>\r\n<p>Naofumi est projeté dans un monde proche en tout lieu d’un jeu de rôle d’heroic fantasy. Mais alors que d’autres héros ont été dotés d’armes offensives redoutables, Naofumi hérite d’un bouclier aux capacités limitées pour progresser dans ce jeu où le danger peut surgir à chaque instant. Trahi par sa partenaire et vilipendé par la population, le jeune homme ne peut désormais compter que sur lui-même pour survivre dans cet univers hostile… et peut-être sur une jeune fille désœuvrée aux ressources insoupçonnées.</p>"
        },
        {
            "id": "b3421c48-cd75-4149-8109-1b0000083cd3",
            "title": null,
            "number": 1,
            "release_date": "2021-04-07",
            "isbn": "9782818985946",
            "asin": "2818985943",
            "edition_id": "dd8d1962-a1a0-45e1-a2b1-12b74a49fb2f",
            "possessions_count": 1168,
            "not_sold": false,
            "image_url": "https://m.media-amazon.com/images/I/51I4eJU47JL.jpg",
            "nb_pages": null,
            "content": null
        }
    ],
    "editions": [
        {
            "id": "aa4da196-ccda-4b33-af3f-6f4b75145c6b",
            "title": null,
            "series_id": "3ce0e5bb-77ea-4186-b0d1-f335e851c313",
            "publisher_id": "c1866645-afb4-44dd-bdce-420606488352",
            "parent_edition_id": null,
            "volumes_count": 27,
            "last_volume_number": null,
            "commercial_stop": false,
            "not_finished": false,
            "follow_editions_count": 21646
        },
        {
            "id": "dd8d1962-a1a0-45e1-a2b1-12b74a49fb2f",
            "title": "Prix découverte",
            "series_id": "3ce0e5bb-77ea-4186-b0d1-f335e851c313",
            "publisher_id": "c1866645-afb4-44dd-bdce-420606488352",
            "parent_edition_id": "aa4da196-ccda-4b33-af3f-6f4b75145c6b",
            "volumes_count": 1,
            "last_volume_number": null,
            "commercial_stop": true,
            "not_finished": false,
            "follow_editions_count": 1235
        }
    ],
    "publishers": [
        {
            "id": "c1866645-afb4-44dd-bdce-420606488352",
            "title": "Doki Doki",
            "closed": false,
            "editions_count": 211,
            "no_amazon": false
        }
    ],
    "series": [
        {
            "id": "3ce0e5bb-77ea-4186-b0d1-f335e851c313",
            "title": "The Rising of the Shield Hero",
            "type_id": "106f524e-7283-44b8-aa84-25e9a7fb1f7d",
            "adult_content": false,
            "editions_count": 5,
            "tasks_count": 2
        }
    ],
    "types": [
        {
            "id": "106f524e-7283-44b8-aa84-25e9a7fb1f7d",
            "title": "Manga",
            "to_display": false
        }
    ],
    "box_volumes": [
        {
            "id": "14924bcc-b6ee-4db1-9908-ed79b681583f",
            "box_id": "a8832564-df86-4ba2-8447-846a8f4a0e4f",
            "volume_id": "6e22eae9-2afd-45ba-8c26-d10d4224d5bf",
            "included": true
        },
        {
            "id": "ee854c8e-a38a-4c45-8c8d-8bd01c341239",
            "box_id": "3eadb9f3-51e2-46ff-bdb1-d8733766a084",
            "volume_id": "6e22eae9-2afd-45ba-8c26-d10d4224d5bf",
            "included": true
        },
        {
            "id": "afb6ed50-3f88-4284-ab7e-96433c9963dd",
            "box_id": "c4760ffd-0e9b-4bee-ad7b-49386eefd892",
            "volume_id": "6e22eae9-2afd-45ba-8c26-d10d4224d5bf",
            "included": true
        }
    ],
    "boxes": [
        {
            "id": "3eadb9f3-51e2-46ff-bdb1-d8733766a084",
            "title": "Pack découverte",
            "number": 0,
            "release_date": "2023-06-28",
            "isbn": "9791041103959",
            "asin": "B0C42N9NP2",
            "commercial_stop": false,
            "box_edition_id": "6991f796-6c25-4a13-b44c-44d01cdda3c4",
            "box_possessions_count": 41,
            "image_url": "https://m.media-amazon.com/images/I/51RnWgc3bNL.jpg"
        },
        {
            "id": "9f86e823-18d7-434a-a709-6e9e161b1d22",
            "title": "Pack promo",
            "number": 0,
            "release_date": "2020-08-05",
            "isbn": "9782818978825",
            "asin": "2818978823",
            "commercial_stop": true,
            "box_edition_id": "dd7b6ebc-f372-4968-934f-6c8f7cd95e76",
            "box_possessions_count": 116,
            "image_url": "https://m.media-amazon.com/images/I/51lwBQQN75L.jpg"
        },
        {
            "id": "7d545edf-99f3-4c8a-afe0-6450a0425f01",
            "title": "Pack promo",
            "number": 0,
            "release_date": "2019-02-06",
            "isbn": "9782818966303",
            "asin": "2818966302",
            "commercial_stop": true,
            "box_edition_id": "dd7b6ebc-f372-4968-934f-6c8f7cd95e76",
            "box_possessions_count": 60,
            "image_url": "https://images-eu.ssl-images-amazon.com/images/I/51tOW5Sil%2BL.jpg"
        }
    ],
    "box_editions": [
        {
            "id": "7e12aff0-98c9-46d1-b152-adc1e485bca5",
            "title": "The Rising of the Shield Hero",
            "publisher_id": "c1866645-afb4-44dd-bdce-420606488352",
            "boxes_count": 1,
            "adult_content": false,
            "box_follow_editions_count": 242
        },
        {
            "id": "37a6683d-3ad4-45ec-b921-65726fc2ee35",
            "title": "The Rising of the Shield Hero",
            "publisher_id": "c1866645-afb4-44dd-bdce-420606488352",
            "boxes_count": 1,
            "adult_content": false,
            "box_follow_editions_count": 64
        },
        {
            "id": "dd7b6ebc-f372-4968-934f-6c8f7cd95e76",
            "title": "The Rising of the Shield Hero",
            "publisher_id": "c1866645-afb4-44dd-bdce-420606488352",
            "boxes_count": 3,
            "adult_content": false,
            "box_follow_editions_count": 240
        }
    ]
}
```