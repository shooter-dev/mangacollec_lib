# 🏛️ Architecture

Ce projet suit une **architecture Domain-Driven Design (DDD)** 
avec une séparation claire des responsabilités :

### Structure générale

```
src/mangacollec_api/         # Project
├── core/                    # Infrastructure centrale
│   ├── exceptions/          # Exceptions de base
│   └── interfaces/          # Interfaces centralisées
│
├── client/                  # Client API et authentification
├── auth/                    # Gestion OAuth2
└── {domain}/                # Domaines métier
    │
    ├── endpoint/            # Points d'accès API
    ├── interfaces/          # Interface
    ├── entity/              # Entités métier
    ├── converter/           # Transformation de données
    ├── exceptions/          # Exceptions spécifiques
    └── tests/               # Test unitaires du domaine
        │
        ├── test_endpoint    # Test points d'accès API
        ├── test_entity      # Test entités métier
        ├── test_converter   # Test converter
        └── test_exceptions  # Tests exceptions
```