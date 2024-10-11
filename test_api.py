import pytest
import requests
from jsonschema import validate, ValidationError

schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "address": {"type": "string"},
        "zip": {"type": "string"},
        "country": {"type": "string"},
        "employeeCount": {"type": "integer"},
        "industry": {"type": "string"},
        "marketCap": {"type": "integer"},
        "domain": {"type": "string"},
        "logo": {"type": "string"},
        "ceoName": {"type": "string"}
    },
    "required": ["id", "name", "industry", "address", "zip", "country", "employeeCount", "marketCap", "domain", "logo", "ceoName"]
}

@pytest.mark.api_test
def test_api_response():
    url = "https://fake-json-api.mock.beeceptor.com/companies"
    response = requests.get(url)
    print(response)
    # Verificar que la respuesta tenga un código de estado de 200
    assert response.status_code == 200, f"Expected status code is 200, but it was {response.status_code}"
    response_json = response.json()
    assert isinstance(response_json, list), "Expected response to be a list"
    #Validar que la respuesta se ajuste al esquema JSON esperado.
    for element in response_json:
        try:
            validate(instance=element, schema=schema)
        except ValidationError as e:
            assert False, f"Schema validation failed for company {element.get('name', 'Unknown')}: {e.message}"

