import base64

import requests.exceptions
from requests import models, request


class InvalidUrl(Exception):
    """Custom exception to indicate an invalid URL."""

    pass


class UnableToMakeRequest(Exception):
    """Exception raised when unable to make an HTTP request to the API."""

    pass


class APIRequestor(object):
    def __init__(self, username: str, token_auth: str, api_base_url: str, api_version=""):
        """
        Initializes an APIRequestor object with the credentials and API information.
        Args:
            username (str): Username for basic authentication.
            token_auth (str): Authentication token for basic authentication.
            api_base_url (str): Base URL of the API.
            api_version (str): API version to use.
        """
        self.username = username
        self.token_auth = token_auth
        self.api_base_url = api_base_url
        self.api_version = api_version
        self.api_url = f"{self.api_base_url}/{self.api_version}"

    def authorization_header(self) -> str:
        """
        Generates the authorization header for basic authentication.
        Returns:
            str: Authorization header in the format "Basic <token>".
        """
        user_token = f"{self.username}:{self.token_auth}".encode()
        authorization_code = base64.b64encode(user_token).decode("utf-8")
        return f"Basic {authorization_code}"

    def request(self, method: str, url: str, **kwargs) -> models.Response:
        """
        Makes an HTTP request to the API with basic authentication.
        Args:
            method (str): HTTP method of the request (e.g., "GET", "POST", etc.).
            url (str): Relative URL of the resource to which the request will be sent.
            **kwargs: Additional arguments to customize the request (optional).
        Returns:
            requests.models.Response: Response object of the HTTP request.
        """
        headers = {
            "Authorization": self.authorization_header(),
            "content-type": "application/json",
        }
        headers.update(kwargs.pop("headers", {}))
        try:
            return request(method, url=f"{self.api_url}/{url}", headers=headers, **kwargs)
        except (requests.exceptions.MissingSchema, requests.exceptions.InvalidURL) as e:
            raise InvalidUrl(f"Invalid url: {e}")
        except (
            requests.exceptions.Timeout,
            requests.exceptions.ConnectionError,
            requests.ConnectTimeout,
        ):
            raise UnableToMakeRequest(
                f"Unable to make request with method {method} for {self.api_url}/{url} service not available"
            )
