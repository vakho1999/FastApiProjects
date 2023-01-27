import json

from fastapi_pagination import Page
from sqlalchemy.orm import Session

from fastapi.testclient import TestClient
from app.src.app import app
from app.src.schemas.requests.TransactionPageSchema import TransactionPageFilter, DealPageFilter
from app.src.schemas.requests.TransactionSettings import TransactionSettings, DealSettings
from app.tests.samples import fake_token, transaction, FAKE_DEAL_SETTINGS, FAKE_TRANSACTION_SETTINGS
from app.tests.samples import fake_filters
from app.src.schemas.requests.enums.types import TransactionOrDeal

# if __name__ == "__main__":
#     from app.src.main import app
#
#     client = TestClient(app)
client = TestClient(app)
headers = {
    "Authorization": "Bearer " + fake_token
}
def test_app():
    resp = client.get("/")
    assert resp.status_code == 200

def test_creating_database_configuration():
    from app.src.config.settings import Settings
    setting = Settings()
    assert setting.SQLALCHEMY_DATABASE_URL is not None

def test_creating_database_session():
    from app.src.db.utils import get_db

    session: Session = next(get_db())
    assert isinstance(session, Session)


def test_deals_list():
    resp = client.post("/transaction/deals?page=1&size=50",headers=headers)
    assert Page(**resp.json())

def test_transactions_list():

    resp = client.post("/transaction/transactions?page=1&size=50", headers=headers)
    print(resp.json())
    assert Page(**resp.json())

def test_save_transaction_filters():

    resp = client.post("/transaction/transactions?page=1&size=50", json=fake_filters, headers=headers)
    assert resp.status_code == 200
    assert Page(**resp.json())

def test_save_deal_filters():

    resp = client.post("/transaction/deals?page=1&size=50", json=fake_filters, headers=headers)
    assert resp.status_code == 200
    assert Page(**resp.json())


def test_parse_keycloak_token():
    # sub
    from jose import jwt

    data = jwt.get_unverified_claims(fake_token)
    assert data["sub"] is not None


def test_get_transaction_filters():
    resp = client.post("/transaction/filters", headers=headers, params={"transaction_type": TransactionOrDeal.TRANSACTION.value})
    assert resp.status_code == 200
    assert resp.json() == [] or TransactionPageFilter(**resp.json())

def test_get_deal_filters():
    resp = client.post("/transaction/filters", headers=headers, params={"transaction_type": TransactionOrDeal.DEAL.value})
    assert resp.status_code == 200
    assert resp.json() == [] or DealPageFilter(**resp.json())

def test_save_transaction():

    resp = client.post("/transaction/create_resource", data=json.dumps(transaction))
    assert resp.status_code == 201
    assert resp.json() == "CREATED"


def test_save_deal_datatable_parameters():

    resp = client.post("/datatable/save_settings", headers=headers, params={"transaction_type": TransactionOrDeal.DEAL.value},
                       data=FAKE_DEAL_SETTINGS.json())
    assert resp.status_code == 201
    assert resp.json() == "CREATED"
    
def test_save_transaction_datatable_parameters():

    resp = client.post("/datatable/save_settings", headers=headers,
                       params={"transaction_type": TransactionOrDeal.TRANSACTION.value},
                      data=FAKE_TRANSACTION_SETTINGS.json())
    assert resp.status_code == 201
    assert resp.json() == "CREATED"

def test_get_deal_datatable_parameters():
    type = TransactionOrDeal.DEAL.value
    resp = client.get("/datatable/get_settings?transaction_type=" + type, headers=headers)
    assert resp.status_code == 200
    assert DealSettings(**resp.json())


def test_get_transaction_datatable_parameters():
    type = TransactionOrDeal.TRANSACTION.value
    resp = client.get("/datatable/get_settings?transaction_type=" + type, headers=headers)
    assert resp.status_code == 200
    assert TransactionSettings(**resp.json())
