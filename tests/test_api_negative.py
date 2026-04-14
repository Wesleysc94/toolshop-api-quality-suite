import pytest


pytestmark = pytest.mark.negative


def test_users_me_requires_auth(client) -> None:
    response = client.get("/users/me")

    assert response.status_code == 401
    payload = response.json()
    assert payload.get("error") == "Unauthorized" or payload.get("message") == "Unauthorized"


def test_login_rejects_invalid_credentials(client, demo_credentials: dict[str, str]) -> None:
    response = client.post(
        "/users/login",
        json={"email": demo_credentials["email"], "password": "senha-invalida"},
    )

    assert response.status_code == 401
    payload = response.json()
    assert payload.get("error") == "Unauthorized" or payload.get("message") == "Unauthorized"


def test_nonexistent_product_returns_404(client) -> None:
    response = client.get("/products/nao-existe")

    assert response.status_code == 404


def test_nonexistent_cart_returns_404(client, auth_headers: dict[str, str]) -> None:
    response = client.get("/carts/nao-existe", headers=auth_headers)

    assert response.status_code == 404
    assert response.json()["message"] == "Requested item not found"
