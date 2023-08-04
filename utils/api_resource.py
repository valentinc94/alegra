from requests import models
from utils import api_requestor, schemas


class APIResource:
    """
    Represents a generic API resource.
    Subclasses should specify the 'endpoint' class variable to define the API endpoint.
    """

    endpoint = ""
    config = schemas.ApiConfig(username="", token_auth="", api_version="", api_base_url="")


class Creatable(APIResource):
    def create(self, **json) -> models.Response:
        requestor = api_requestor.APIRequestor(
            username=self.config.username,
            token_auth=self.config.token_auth,
            api_base_url=self.config.api_base_url,
            api_version=self.config.api_version,
        )
        url = self.endpoint
        return requestor.request(
            method="post",
            url=url,
            json=json,
        )


class Listable(APIResource):
    def list(self, **params) -> models.Response:
        requestor = api_requestor.APIRequestor(
            username=self.config.username,
            token_auth=self.config.token_auth,
            api_base_url=self.config.api_base_url,
            api_version=self.config.api_version,
        )
        url = self.endpoint
        return requestor.request(
            method="get",
            url=url,
            params=params,
        )


class Updatable(APIResource):
    def update(self, resource_id: int, **json) -> models.Response:
        requestor = api_requestor.APIRequestor(
            username=self.config.username,
            token_auth=self.config.token_auth,
            api_base_url=self.config.api_base_url,
            api_version=self.config.api_version,
        )
        url = f"{self.endpoint}/{resource_id}"
        return requestor.request(
            method="put",
            url=url,
            json=json,
        )


class Retrieve(APIResource):
    def retrieve(self, resource_id: int, **params) -> models.Response:
        requestor = api_requestor.APIRequestor(
            username=self.config.username,
            token_auth=self.config.token_auth,
            api_base_url=self.config.api_base_url,
            api_version=self.config.api_version,
        )
        url = f"{self.endpoint}/{resource_id}"
        return requestor.request(
            method="get",
            url=url,
            params=params,
        )
