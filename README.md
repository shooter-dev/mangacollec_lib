# MangaCollecLib

---

## Context

Une bibliothèque Python moderne pour interagir avec l'API MangaCollec, 
suivant les principes du Domain-Driven Design (DDD) avec une architecture modulaire
et une couverture de tests complète.

---

## 🚀 Installation

### Avec Poetry (recommandé)

```bash
poetry add mangacollec_api
```

### Avec pip

```bash
pip install git+https://github.com/shooter-dev/mangacollec_lib.git
```

---

## Utilisation

### Creation d'un client

#### Client Anonyme
```python
from mangacollec.client import MangaCollecAPIClient
import os

client = MangaCollecAPIClient(
    client_id=os.environ.get("CLIENT_ID"),
    client_secret=os.environ.get("CLIENT_SECRET")
)
```

#### Client auth password
```python
from mangacollec.client import MangaCollecAPIClient
import os

client = MangaCollecAPIClient(
    client_id=os.environ.get("CLIENT_ID"),
    client_secret=os.environ.get("CLIENT_SECRET"),
    email=os.environ.get("USERNAME_TEST"),
    password=os.environ.get("PASSWORD")
)
```

### Utilisation de l'enpoint: `Author` **V2**

#### Authors

```python
from mangacollec.author import AuthorEndpoint, AuthorsEndpointResponce


endpoint_author = AuthorEndpoint(client)

result: AuthorsEndpointResponce = endpoint_author.get_all_authors_v2()
```
##### Responce:

```python

```
#### Author

```python
from mangacollec.author import AuthorEndpoint, AuthorEndpointResponce

endpoint_author = AuthorEndpoint(client)

result: AuthorEndpointResponce = endpoint_author.get_by_id_v2("7b785193-5f0d-4306-9c7e-d4e97ddd7571")
```
##### Responce:

```python

```

---


