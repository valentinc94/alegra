import logging
import os

from utils import api_resource, schemas

logger = logging.getLogger(__name__)


class AlegraApiConfig:
    def __init__(self, api_version: str = "v1"):
        self.config = schemas.ApiConfig(
            username=os.getenv("ALEGRA_CLIENT_USERNAME", ""),
            token_auth=os.getenv("ALEGRA_CLIENT_TOKEN_AUTH", ""),
            api_base_url=os.getenv("ALEGRA_API_BASE_URL", ""),
            api_version=api_version,
        )


class BankAccounts(
    api_resource.Retrieve,
    api_resource.Listable,
    AlegraApiConfig,
):
    endpoint = "bank-accounts"


class Items(
    api_resource.Retrieve,
    api_resource.Listable,
    AlegraApiConfig,
):
    endpoint = "items"


class Contacts(
    api_resource.Updatable,
    api_resource.Creatable,
    api_resource.Retrieve,
    api_resource.Listable,
    AlegraApiConfig,
):
    endpoint = "contacts"


class Invoices(
    api_resource.Updatable,
    api_resource.Creatable,
    api_resource.Retrieve,
    api_resource.Listable,
    AlegraApiConfig,
):
    endpoint = "invoices"


class Payments(
    api_resource.Updatable,
    api_resource.Creatable,
    api_resource.Retrieve,
    api_resource.Listable,
    AlegraApiConfig,
):
    endpoint = "payments"


class Alegra:
    @property
    def bank_accounts(self) -> BankAccounts:
        return BankAccounts()

    @property
    def items(self) -> Items:
        return Items()

    @property
    def contacts(self) -> Contacts:
        return Contacts()

    @property
    def invoices(self) -> Invoices:
        return Invoices()

    @property
    def payments(self) -> Payments:
        return Payments()
