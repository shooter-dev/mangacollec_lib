# Endpoint token `password`

- **url** : `https://api.mangacollec.com/oauth/token`
- **methodes** : `POST`
`
---

## Header

```json
{
  "Accept" : "application/json",
  "Content-Type" : "application/json",
  "User-Agent" : ""
}
```

---

## Body

```json
{
    "client_id":"client_id",
    "client_secret": "client_secret",
    "grant_type": "password",
    "password": "mot de pass",
    "username": "email"
}
```

---

## Response

```json
{
    "access_token": "access_token",
    "token_type": "Bearer",
    "expires_in": 7200,
    "refresh_token": "refresh_token",
    "created_at": 1755364883
}
```

---

# Endpoint token `client_credentials` 

- **url** : `https://api.mangacollec.com/oauth/token`
- **methodes** : `POST`

---

## Header

```json
{
  "Accept" : "application/json",
  "Content-Type" : "application/json",
  "User-Agent" : ""
}
````

---

## Body

```json
{
    "client_id":"client_id",
    "client_secret": "client_secret",
    "grant_type": "client_credentials"
}
```

---

## Response

```json
{
    "access_token": "access_token",
    "token_type": "Bearer",
    "expires_in": 7200,
    "refresh_token": "refresh_token",
    "created_at": 1755364883
}
```