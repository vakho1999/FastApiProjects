from faker import Faker

from app.src.schemas.requests.TransactionSettings import DealSettings, TransactionSettings, TransactionProperty, \
  DealProperty, BaseEnum, DealSettingsEnum, TransactionSettingsEnum
from app.src.schemas.requests.enums.types import CurrencyType

fake = Faker()

def generate_fake_transaction_settings():
    data = []
    for e in BaseEnum:
        width = fake.random_int(min=20, max=200)
        name = e.value
        data.append(TransactionProperty(width=width, name=name))
        for e in TransactionSettingsEnum:
            width = fake.random_int(min=20, max=200)
            name = e.value
            data.append(TransactionProperty(width=width, name=name))
    return TransactionSettings(data=data)

def generate_fake_deal_settings():
    data = []
    for e in BaseEnum:
        width = fake.random_int(min=20, max=200)
        name = e.value
        data.append(DealProperty(width=width, name=name))
        for e in DealSettingsEnum:
            width = fake.random_int(min=20, max=200)
            name = e.value
            data.append(DealProperty(width=width, name=name))
    return DealSettings(data=data)


fake_token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJaa09rUGFpQWhaQmZJaDNTNWVkekVWT3hqSzVEQ3BIV2ZvaXJpX0RSeHE4In0.eyJleHAiOjE2NzMzNTcxNDMsImlhdCI6MTY3MzM1NTM0MywianRpIjoiMzgzMTA1ODktZjY2OC00ZjFlLWJmMzYtMzljNzMyNWFiN2FhIiwiaXNzIjoiaHR0cDovL2F1dGg6ODA4MC9hdXRoL3JlYWxtcy90cmFuc2d1YXJkIiwic3ViIjoiNWQyZmNmNzUtY2FmNi00NGNkLWFlNjUtYjg0NTg2OTU2MDc4IiwidHlwIjoiQmVhcmVyIiwiYXpwIjoidGctYmxzIiwic2Vzc2lvbl9zdGF0ZSI6ImQ4ZTMzNzQyLThlMDEtNGVjYS1iNWY3LWY5OWZmNmUzODFlZSIsImFjciI6IjEiLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiIsInRnLWN1c3RvbWVyIl19LCJzY29wZSI6ImVtYWlsIHByb2ZpbGUiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsIlJvbGVzIjpbIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iLCJ0Zy1jdXN0b21lciJdLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJjcmVkby10ZXN0In0.Q_drckC6JbgOE2Yq__v3CLQ2t49QJbptKQ9COpZNeJsZPZzlYLwjuwZX9y4joB19yl-XhkjcAEYRaYzvMPQPLYEvyQGHT1WdHXMMN0O854fLyf2vBRBoJCOiimGV-6za3ZEaZVZJk_PuBqTXpkv27Tx7GqVESSqlqOKzjr8oH_fskWHHuMWMK9Wl362cy8uCzgd7hqixX8Lzgs0JYKL7mfOTB9PWkQhZba1tzvK_sSIqCiLb8FDhwmFLrkaxPIkKNEp7942YdHinFYqogFw78jFiemwSYmFr_6VJ0ahBsfiJlSLiEF83_pFCcWH6FWAGVCWtKGDprbZF43y34xqCkg"

transaction = {
  "amount": 0,
  "iso": "TEST",
  "purpose": "string",
  "location": "string",
  "dealId": "444222",
  "recId": None,
  "bankIdentifier": "string",
  "docDate": "2023-01-05",
  "transactionType": "CashDeposit",
  "amountEqu": 0,
  "credit": {
    "resident": {
      "iso2": "string",
      "iso3": "string"
    },
    "balance": 0,
    "clientId": "string",
    "altNames": [
      {
        "id": 0,
        "createTime": "2023-01-05T08:07:42.495Z",
        "updateTime": "2023-01-05T08:07:42.495Z",
        "name": "string"
      }
    ],
    "note": "string",
    "clientNo": 0,
    "juridical": True,
    "citizenship": {
      "iso2": "string",
      "iso3": "string"
    },
    "bankRegDate": "2023-01-05",
    "mail": "string",
    "phone": "string",
    "georgianIdNumber": "string",
    "passportId": "string",
    "address": "string",
    "gender": "string",
    "birthDate": "2023-01-05",
    "birthCountry": "string",
    "birthPlace": "string",
    "documentType": "GeorgianPassport",
    "issuerName": "string",
    "firstName": "string",
    "lastName": "string",
    "serie": "string",
    "number": "string",
    "after": "2023-01-05",
    "before": "2023-01-05",
    "documentIdentifier": "string",
    "issuingCountry": "string",
    "jobTitle": "string",
    "fullName": "string",
    "legalForm": "LLC",
    "regNumber": "string",
    "regDate": "2023-01-05",
    "regOrganization": "string",
    "regCountry": "string",
    "legalAddress": "string",
    "actualAddress": "string",
    "taxPayerId": "string",
    "accountNumber": "string",
    "accountType": "Current",
    "bankName": "string",
    "bic": "string",
    "bankCountry": "string",
    "bankPlace": "string",
    "accountOpeningDate": "2023-01-05",
    "accountClosingDate": "2023-01-05",
    "riskLevel": "GREEN",
    "pep": True,
    "swift50": "string",
    "ITRS": "string",
    "taxPayerRegCountry": "string",
    "relatedPeople": [
      {
        "relatedId": "string",
        "fullName": "string",
        "address": "string",
        "resident": {
          "iso2": "string",
          "iso3": "string"
        },
        "citizenship": {
          "iso2": "string",
          "iso3": "string"
        },
        "passportId": "string",
        "documentId": "string",
        "georgianIdNumber": "string",
        "legalAddress": "string",
        "actualAddress": "string",
        "passportIssuerAddress": "string",
        "identificationIssuerAddress": "string",
        "taxPayerRegCountry": "string",
        "bic": "string",
        "birthDate": "2023-01-05",
        "keywords": [
          "string"
        ],
        "percentShare": 0,
        "juridical": True,
        "relatedType": "FOUNDER",
        "pep": True
      }
    ]
  },
  "debit": {
    "resident": {
      "iso2": "string",
      "iso3": "string"
    },
    "balance": 0,
    "clientId": "string",
    "altNames": [
      {
        "id": 0,
        "createTime": "2023-01-05T08:07:42.495Z",
        "updateTime": "2023-01-05T08:07:42.495Z",
        "name": "string"
      }
    ],
    "note": "string",
    "clientNo": 0,
    "juridical": True,
    "citizenship": {
      "iso2": "string",
      "iso3": "string"
    },
    "bankRegDate": "2023-01-05",
    "mail": "string",
    "phone": "string",
    "georgianIdNumber": "string",
    "passportId": "string",
    "address": "string",
    "gender": "string",
    "birthDate": "2023-01-05",
    "birthCountry": "string",
    "birthPlace": "string",
    "documentType": "GeorgianPassport",
    "issuerName": "string",
    "firstName": "string",
    "lastName": "string",
    "serie": "string",
    "number": "string",
    "after": "2023-01-05",
    "before": "2023-01-05",
    "documentIdentifier": "string",
    "issuingCountry": "string",
    "jobTitle": "string",
    "fullName": "string",
    "legalForm": "LLC",
    "regNumber": "string",
    "regDate": "2023-01-05",
    "regOrganization": "string",
    "regCountry": "string",
    "legalAddress": "string",
    "actualAddress": "string",
    "taxPayerId": "string",
    "accountNumber": "string",
    "accountType": "Current",
    "bankName": "string",
    "bic": "string",
    "bankCountry": "string",
    "bankPlace": "string",
    "accountOpeningDate": "2023-01-05",
    "accountClosingDate": "2023-01-05",
    "riskLevel": "GREEN",
    "pep": True,
    "swift50": "string",
    "ITRS": "string",
    "taxPayerRegCountry": "string",
    "relatedPeople": [
      {
        "relatedId": "string",
        "fullName": "string",
        "address": "string",
        "resident": {
          "iso2": "string",
          "iso3": "string"
        },
        "citizenship": {
          "iso2": "string",
          "iso3": "string"
        },
        "passportId": "string",
        "documentId": "string",
        "georgianIdNumber": "string",
        "legalAddress": "string",
        "actualAddress": "string",
        "passportIssuerAddress": "string",
        "identificationIssuerAddress": "string",
        "taxPayerRegCountry": "string",
        "bic": "string",
        "birthDate": "2023-01-05",
        "keywords": [
          "string"
        ],
        "percentShare": 0,
        "juridical": True,
        "relatedType": "FOUNDER",
        "pep": True
      }
    ]
  },
  "cashPayment": False,
  "extraPurpose": "string",
  "nbgTransactionType": "CurrencyWithCash",
  "transactionSubType": "SWIFT",
  "dealdesc": "string",
  "distance": False,
  "intBank": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}

FAKE_TRANSACTION_SETTINGS = generate_fake_transaction_settings()
FAKE_DEAL_SETTINGS = generate_fake_deal_settings()


fake_filters = {
      "amount_end": {"value":fake.random_int(),"name": "თანხამდე"},
      "amount_to_gel_end": {"value": fake.random_int(),"name": "ექვივალენტი თანხამდე"},
      # "insert_date_end": fake.date_time().isoformat(),
      # "insert_date_start": fake.date_time().isoformat(),
      # "amount_eq": fake.random_int(),
      # "amount_to_gel_eq": fake.random_int(),
      # "insert_date_eq": fake.date_time().isoformat(),
      # "amount_to_gel_not_eq": fake.random_int(),
      # "DealType_in": fake.text(15),
      # "DealForm_not_in": fake.text(10),
    }