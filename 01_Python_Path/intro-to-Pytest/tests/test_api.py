import pytest
import requests

@pytest.mark.duckduckgo
@pytest.mark.api
@pytest.mark.skip #issue with status_code ==200 but browser answer 202 because of botting suspicion could add headers to prevent
def test_duckduckgo_instant_answer_api():
    # Arrange
    url = 'https://api.duckduckgo.com/?q=python+programming&format=json'
    # Act
    response = requests.get(url)
    body = response.json()
    # Assert
    assert response.status_code == 200
    assert 'Python' in body['AbstractText']