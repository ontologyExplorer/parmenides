import json

import requests

query_token = "https://smt.esante.gouv.fr/ans/sso/auth/realms/ANS/protocol/openid-connect/token"
headers = {"Content-Type": "application/x-www-form-urlencoded"}


def getToken(mail, password):
    data={
    "grant_type": "password",
    "client_id": "user-api",
    "username": f"{mail}",
    "password": f"{password}",
    "refresh_token": "ey...",
    }

    r = requests.post(
        query_token,
        headers=headers,
        data=data,
        )

    result = json.loads(r.text)

    return result["access_token"]