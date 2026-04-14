import pytest


pytestmark = pytest.mark.smoke


def test_products_list_returns_catalog_page(catalog_page: dict) -> None:
    assert catalog_page["current_page"] == 1
    assert catalog_page["total"] >= len(catalog_page["data"]) > 0

    sample = catalog_page["data"][0]
    for field in ("id", "name", "price", "in_stock", "category", "brand"):
        assert field in sample


def test_product_details_return_expected_fields(client, first_in_stock_product: dict) -> None:
    response = client.get(f"/products/{first_in_stock_product['id']}")

    assert response.status_code == 200
    payload = response.json()

    assert payload["id"] == first_in_stock_product["id"]
    assert payload["name"] == first_in_stock_product["name"]
    assert isinstance(payload["specs"], list)
    assert payload["category"]["id"]
    assert payload["brand"]["id"]


def test_brands_endpoint_returns_items(client) -> None:
    response = client.get("/brands")

    assert response.status_code == 200
    payload = response.json()

    assert isinstance(payload, list)
    assert len(payload) > 0
    assert {"id", "name", "slug"}.issubset(payload[0].keys())


def test_categories_tree_returns_nested_structure(client) -> None:
    response = client.get("/categories/tree")

    assert response.status_code == 200
    payload = response.json()

    assert isinstance(payload, list)
    assert len(payload) > 0
    assert "sub_categories" in payload[0]


def test_login_returns_bearer_token(login_payload: dict) -> None:
    assert login_payload["token_type"] == "bearer"
    assert login_payload["expires_in"] > 0
    assert len(login_payload["access_token"]) > 20


def test_users_me_returns_demo_account(client, auth_headers: dict[str, str], demo_credentials: dict[str, str]) -> None:
    response = client.get("/users/me", headers=auth_headers)

    assert response.status_code == 200
    payload = response.json()

    assert payload["email"] == demo_credentials["email"]
    assert payload["first_name"]
    assert payload["last_name"]


def test_cart_can_be_created_and_read(client, auth_headers: dict[str, str], empty_cart_id: str) -> None:
    response = client.get(f"/carts/{empty_cart_id}", headers=auth_headers)

    assert response.status_code == 200
    payload = response.json()

    assert payload["id"] == empty_cart_id
    assert "cart_items" in payload
    assert isinstance(payload["cart_items"], list)
