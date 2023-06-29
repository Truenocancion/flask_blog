import pytest
import allure
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@allure.title("Check Home Page Response Code")
@allure.description("Verify that the home page returns a 200 status code")
def test_home_page_response_code(client):
    response = client.get()
    assert response.status_code == 200


@pytest.mark.parametrize("url", ["/create"])
@allure.title("Check Add Post Page Response Code")
@allure.description("Verify that the Add Post page returns a 200 status code")
def test_add_post_button_exists(client, url):
    response = client.get(url)
    assert response.status_code == 200
