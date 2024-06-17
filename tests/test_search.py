import pytest
from unittest.mock import patch

from search import search_nearby_places


# Mock API response for successful request
mock_success_response = {
    "results": [
        {"displayName": "Place 1"},
        {"displayName": "Place 2"},
        {"displayName": "Place 3"},
    ]
}

# Mock API response for failed request
mock_error_response = {"error_message": "API key is invalid"}


@pytest.fixture
def mock_api_key():
    return "mock_api_key"


@pytest.fixture
def mock_location():
    return 37.7749, -122.4194  # San Francisco coordinates


@pytest.fixture
def mock_radius():
    return 1000  # 1 km radius


@pytest.fixture
def mock_types():
    return ["restaurant"]


@patch("search.requests.post")
def test_search_nearby_places_success(
    mock_post, mock_api_key, mock_location, mock_radius, mock_types
):
    latitude, longitude = mock_location
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = mock_success_response

    response = search_nearby_places(
        mock_api_key, latitude, longitude, mock_radius, mock_types
    )

    assert response == mock_success_response
    mock_post.assert_called_once()


@patch("search.requests.post")
def test_search_nearby_places_failure(
    mock_post, mock_api_key, mock_location, mock_radius, mock_types
):
    latitude, longitude = mock_location
    mock_post.return_value.status_code = 400
    mock_post.return_value.text = mock_error_response

    response = search_nearby_places(
        mock_api_key, latitude, longitude, mock_radius, mock_types
    )

    assert response == (400, mock_error_response)
    mock_post.assert_called_once()
