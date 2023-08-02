# Alegra API Client

This is a Python client for the Alegra API. It provides convenient methods for interacting with the Alegra API endpoints.

### Installation

To install the Alegra API client and its dependencies, follow these steps:

1.  Clone the repository to your local machine:

```sh
   git clone https://github.com/valentinc94/alegra.git
```

2.  Change into the project directory:

```sh
   cd alegra
```

3.  Create a virtual environment (optional, but recommended):

```sh
   python -m venv venv
```

4.  Activate the virtual environment:

-   On Windows:

```sh
   venv\Scripts\activate
```

-   On macOS and Linux:

```sh
   source venv/bin/activate
```

5.  Install the required packages:

```sh
   pip install -r requirements/local.txt
```

### Running the Tests

To run the unit tests, make sure you are in the project directory and the virtual environment is activated.

```sh
   python -m unittest discover tests
```

### Usage

To use the Alegra API client in your own project, you can import the necessary classes from the `client` and `utils` modules.

Here's an example of how to list bank accounts using the client:

```sh
from alegra.client import Alegra

# Create an instance of the Alegra client
alegra = Alegra()

# List bank accounts
bank_accounts = alegra.bank_accounts.list().json()
print(bank_accounts)
```

### Features!

If you want to interact with the taxes API endpoint from the Alegra documentation (), you can easily do so by using the Taxes class. This class provides the necessary methods to retrieve and list taxes, making them readily available for use in your application.

```sh
from alegra import api_resource

class Taxes(
    api_resource.Retrieve,
    api_resource.Listable,
    AlegraApiConfig,
):
    endpoint = "taxes"
```

Make sure to configure the environment variables `ALEGRA_CLIENT_USERNAME`, `ALEGRA_CLIENT_TOKEN_AUTH`, and `ALEGRA_API_BASE_URL` with your Alegra API credentials before running the client.

For more details on how to use the client and its methods, refer to the source code and the API documentation.

### Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.

Happy coding!