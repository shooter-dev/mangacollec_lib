"""
Exemple d'utilisation simplifiée avec le pattern singleton.
"""

from mangacollec.client.singleton_client import get_mangacollec_client
from mangacollec.author.endpoint.author_endpoint import AuthorEndpoint
from mangacollec.series.endpoint.serie_endpoint import SerieEndpoint


def example_simple_usage():
    """Exemple d'utilisation ultra-simple."""
    print("=== Exemple Usage Simple avec Singleton ===")
    
    # Configuration UNIQUE du client au début de l'application
    client = get_mangacollec_client(
        client_id="your_client_id",
        client_secret="your_client_secret",
        email="your_email@example.com",  # optionnel
        password="your_password"          # optionnel
    )
    
    print(f"✅ Client configuré: {client}")
    
    # Maintenant tous les endpoints peuvent être utilisés sans paramètres !
    try:
        # Utilisation directe des endpoints
        authors_endpoint = AuthorEndpoint()  # ← Pas de paramètres nécessaires !
        series_endpoint = SerieEndpoint()    # ← Le client est automatiquement injecté !
        
        # Appels API simples
        authors_v1 = authors_endpoint.get_all()
        print(f"📚 Auteurs V1: {len(authors_v1)} trouvés")
        
        authors_v2 = authors_endpoint.get_all_v2()
        print(f"📚 Auteurs V2: {len(authors_v2.authors)} trouvés")
        
        series_v2 = series_endpoint.get_all_series_v2()
        print(f"📖 Séries V2: {len(series_v2.series)} trouvées")
        
    except Exception as e:
        print(f"❌ Erreur: {e}")


def example_error_handling():
    """Exemple de gestion d'erreur quand le singleton n'est pas initialisé."""
    print("\n=== Exemple Gestion d'Erreur ===")
    
    # Reset du singleton pour simuler un état non-initialisé
    from mangacollec.client.singleton_client import SingletonMangaCollecClient
    SingletonMangaCollecClient.reset_instance()
    
    try:
        # Tentative d'utilisation sans initialisation
        authors_endpoint = AuthorEndpoint()
        print("❌ Ceci ne devrait pas s'afficher")
        
    except RuntimeError as e:
        print(f"✅ Erreur attendue: {e}")
        print("💡 Solution: Appelez get_mangacollec_client(client_id, client_secret) d'abord")


def example_mixed_usage():
    """Exemple montrant l'usage mixte : singleton + injection manuelle."""
    print("\n=== Exemple Usage Mixte ===")
    
    # Configuration du singleton
    singleton_client = get_mangacollec_client(
        client_id="your_client_id", 
        client_secret="your_client_secret"
    )
    
    # Usage avec singleton (automatique)
    authors_auto = AuthorEndpoint()
    print(f"🤖 Endpoint avec singleton: {authors_auto.client is singleton_client}")
    
    # Usage avec injection manuelle (pour cas spéciaux)
    from mangacollec.client.client import MangaCollecAPIClient
    
    manual_client = MangaCollecAPIClient(
        client_id="another_client_id",
        client_secret="another_client_secret"
    )
    
    authors_manual = AuthorEndpoint(client=manual_client)
    print(f"🔧 Endpoint avec client manuel: {authors_manual.client is manual_client}")
    print(f"🔄 Clients différents: {authors_auto.client is not authors_manual.client}")


def example_real_world_usage():
    """Exemple d'utilisation dans une vraie application."""
    print("\n=== Exemple Application Réelle ===")
    
    # 1. Configuration au démarrage de l'app (dans main.py ou __init__.py)
    def configure_mangacollec_api():
        """Configuration globale de l'API au démarrage."""
        return get_mangacollec_client(
            client_id="your_client_id",
            client_secret="your_client_secret",
            email="user@example.com",
            password="password"
        )
    
    # 2. Utilisation dans n'importe quel module de l'app
    def get_latest_manga_releases():
        """Fonction business qui récupère les dernières sorties."""
        volumes_endpoint = VolumeEndpoint()  # ← Simplicité maximale !
        try:
            volumes = volumes_endpoint.get_volumes_news_v2()
            return [v for v in volumes.volumes if not v.not_sold]
        except Exception as e:
            print(f"Erreur lors de la récupération: {e}")
            return []
    
    def search_series_by_author(author_name: str):
        """Fonction business qui cherche les séries d'un auteur."""
        authors_endpoint = AuthorEndpoint()  # ← Simplicité maximale !
        series_endpoint = SerieEndpoint()    # ← Simplicité maximale !
        
        try:
            # Récupération des auteurs
            authors_response = authors_endpoint.get_all_v2()
            
            # Recherche de l'auteur par nom
            target_author = None
            for author in authors_response.authors:
                if author_name.lower() in author.name.lower():
                    target_author = author
                    break
            
            if target_author:
                print(f"✅ Auteur trouvé: {target_author.name}")
                # Ici on pourrait faire d'autres appels pour récupérer ses séries
                return target_author
            else:
                print(f"❌ Auteur '{author_name}' non trouvé")
                return None
                
        except Exception as e:
            print(f"Erreur lors de la recherche: {e}")
            return None
    
    # Configuration
    configure_mangacollec_api()
    
    # Utilisation dans l'application
    print("🔍 Recherche de 'Oda'...")
    result = search_series_by_author("Oda")
    
    print("📅 Récupération des dernières sorties...")
    # latest = get_latest_manga_releases()
    # print(f"📚 {len(latest)} nouveaux volumes disponibles")


if __name__ == "__main__":
    print("⚠️  Remplacez les credentials par vos vraies valeurs pour tester")
    
    example_simple_usage()
    example_error_handling()
    example_mixed_usage()
    example_real_world_usage()
    
    print("\n🎉 Le pattern Singleton simplifie grandement l'utilisation de l'API !")
    print("💡 Plus besoin de passer le client partout dans votre code.")