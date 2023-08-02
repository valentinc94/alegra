import unittest
from unittest.mock import patch

from client import Alegra
from utils import api_requestor


class TestAlegraApi(unittest.TestCase):
    def setUp(self):
        self.alegra = Alegra()

    @patch.object(api_requestor.APIRequestor, "request")
    def test_list_bank_accounts_successful(self, mock_request):
        # Simulate a successful API response with status 200
        expected_response = [
            {
                "id": 3,
                "name": "Banco 1",
                "number": "100294",
                "description": "Banco principal",
                "type": "bank",
                "status": "active",
                "initialBalance": 200,
                "initialBalanceDate": "2022-04-01",
            },
            {
                "id": 1,
                "name": "Tarjeta de credito",
                "number": "3849939393939393",
                "description": "Tarjeta coorporativa",
                "type": "credit-card",
                "status": "active",
                "initialBalance": -100,
                "initialBalanceDate": "2022-02-01",
            },
        ]
        mock_request.return_value.status_code = 200
        mock_request.return_value.json.return_value = expected_response

        # Call the method to be tested
        result = self.alegra.bank_accounts.list().json()

        # Assertions
        self.assertEqual(result, expected_response)
        mock_request.assert_called_once()

    @patch.object(api_requestor.APIRequestor, "request")
    def test_list_bank_accounts_return_response_with_error_data(self, mock_request):
        # Simulate an error API response with status 400
        error_response = {"error": 903, "code": "Límite sobrepasa máximo permitido"}
        mock_request.return_value.status_code = 400
        mock_request.return_value.json.return_value = error_response

        data = self.alegra.bank_accounts.list().json()

        # Assertions
        self.assertEqual(data["error"], error_response["error"])
        self.assertEqual(data["code"], error_response["code"])

    @patch.object(api_requestor.APIRequestor, "request")
    def test_list_bank_accounts_timeout(self, mock_request):
        # Simulate a timeout when making the API request
        mock_request.side_effect = api_requestor.UnableToMakeRequest("Request timeout")

        # Call the method to be tested
        with self.assertRaises(api_requestor.UnableToMakeRequest) as cm:
            self.alegra.bank_accounts.list().json()

        # Assertions
        self.assertEqual(str(cm.exception), "Request timeout")
        mock_request.assert_called_once()


if __name__ == "__main__":
    unittest.main()
