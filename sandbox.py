import os

from mangacollec.author import AuthorEndpoint
from mangacollec.client import MangaCollecAPIClient

if __name__ == '__main__':
    client_anonyme = MangaCollecAPIClient(
        client_id=os.environ.get("CLIENT_ID"),
        client_secret=os.environ.get("CLIENT_SECRET")
    )

    print(client_anonyme)

    client_password = MangaCollecAPIClient(
        client_id=os.environ.get("CLIENT_ID"),
        client_secret=os.environ.get("CLIENT_SECRET"),
        email=os.environ.get("USERNAME_TEST"),
        password=os.environ.get("PASSWORD")
    )

    print(client_password)

    api_anonyme = AuthorEndpoint(client_anonyme)

    api_author_password = AuthorEndpoint(client_password)

    print(api_author_password.get_all_authors_v2())

    print(api_author_password.get_author_by_id_v2("7b785193-5f0d-4306-9c7e-d4e97ddd7571"))