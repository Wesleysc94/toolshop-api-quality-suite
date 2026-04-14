import os

import httpx
import pytest


BASE_URL = os.getenv("PST_API_BASE_URL", "https://api.practicesoftwaretesting.com")
DEMO_EMAIL = os.getenv("PST_API_EMAIL", "customer@practicesoftwaretesting.com")
DEMO_PASSWORD = os.getenv("PST_API_PASSWORD", "welcome01")
DEFAULT_PRODUCTS_PARAMS = {
    "page": 1,
    "between": "price,1,100",
    "is_rental": "false",
}


@pytest.fixture(scope="session")
def client() -> httpx.Client:
    with httpx.Client(
        base_url=BASE_URL,
        timeout=20.0,
        headers={"Accept": "application/json"},
    ) as api_client:
        yield api_client


@pytest.fixture(scope="session")
def demo_credentials() -> dict[str, str]:
    return {"email": DEMO_EMAIL, "password": DEMO_PASSWORD}


@pytest.fixture(scope="session")
def login_payload(client: httpx.Client, demo_credentials: dict[str, str]) -> dict:
    response = client.post("/users/login", json=demo_credentials)
    assert response.status_code == 200, response.text

    payload = response.json()
    assert payload["token_type"] == "bearer"
    assert payload["expires_in"] > 0
    assert payload["access_token"]
    return payload


@pytest.fixture(scope="session")
def auth_headers(login_payload: dict) -> dict[str, str]:
    return {"Authorization": f"Bearer {login_payload['access_token']}"}


@pytest.fixture(scope="session")
def catalog_page(client: httpx.Client) -> dict:
    response = client.get("/products", params=DEFAULT_PRODUCTS_PARAMS)
    assert response.status_code == 200, response.text
    return response.json()


@pytest.fixture(scope="session")
def first_in_stock_product(catalog_page: dict) -> dict:
    return next(product for product in catalog_page["data"] if product["in_stock"])


@pytest.fixture
def empty_cart_id(client: httpx.Client, auth_headers: dict[str, str]) -> str:
    response = client.post("/carts", headers=auth_headers, json={})
    assert response.status_code == 201, response.text
    return response.json()["id"]
