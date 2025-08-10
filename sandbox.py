import os

from mangacollec.author.endpoint.author_endpoint import AuthorEndpoint
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

    api_password = AuthorEndpoint(client_password)

    print(api_password.get_all_authors_v2())