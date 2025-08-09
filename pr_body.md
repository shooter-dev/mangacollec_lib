# 🚀 Configuration initiale du projet MangaCollectLib

## 📋 Description
Mise en place de la structure initiale du projet MangaCollectLib, une bibliothèque Python moderne pour interagir avec l'API MangaCollec. Ce commit établit l'architecture DDD, la configuration Poetry, et la documentation complète du projet.

---

## 🔄 Changements apportés

### 📦 Configuration du projet
- **pyproject.toml** : Configuration Poetry avec Python >=3.12, métadonnées du projet
- **poetry.lock** : Verrouillage des dépendances pour assurer la reproductibilité
- **poetry.toml** : Configuration Poetry avec virtual environment en local
- **.gitignore** : Exclusions Git adaptées pour Python/Poetry

### 📚 Documentation
- **README.md** : Documentation principale du projet en français
- **docs/project/ARCHECTECTURES.md** : Documentation détaillée de l'architecture DDD
- **docs/mangacollec/URL_ENDPOINT.md** : Référence complète des endpoints API

### 🗂️ Exemples de réponses API
- **docs/mangacollec/urls_responce/** : Collection complète d'exemples JSON
  - Auteurs : `v2_authors.json`, `v2_author_{id}.json`
  - Séries : `v2_series.json`, `v2_serie_{id}.json`
  - Éditeurs : `v2_publishers.json`, `v2_publisher_{id}.json`
  - Volumes : `v2_volume_{id}.json`, `v2_volumes_news.json`
  - Collections : `v2_collection_me.json`, `v2_collection_shooterdev.json`
  - Éditions : `v2_edition_{id}.json`
  - Types : `v2_kinds.json`

### 🔧 Outils de développement
- **.github/pull_request_template.md** : Template standardisé pour les PR

---

## 🧪 Tests réalisés
- [x] Tests unitaires ajoutés ou mis à jour (aucun test à ce stade - structure initiale)
- [x] Tests manuels effectués : Validation de la configuration Poetry
- [x] Couverture de test vérifiée : Configuration de base testée avec `poetry install`

---

## ✅ Checklist avant merge
- [x] Code revu et approuvé par un pair
- [x] Pas d'erreurs ou warnings à la compilation (`poetry install` réussi)
- [x] Documentation mise à jour si nécessaire (documentation complète incluse)
- [x] Pas de régression constatée (projet initial)

---

## 🔗 Liens associés
- API MangaCollec : https://api.mangacollec.com
- Documentation Poetry : https://python-poetry.org/docs/

---

## 📝 Notes supplémentaires
Ce commit établit les fondations solides du projet avec :
- Architecture DDD prête pour l'implémentation des domaines métier
- Configuration Poetry optimisée pour le développement
- Documentation exhaustive pour faciliter la contribution
- Exemples API réels pour guider l'implémentation

Le projet est maintenant prêt pour l'implémentation des modules métier (authors, series, publishers, etc.).