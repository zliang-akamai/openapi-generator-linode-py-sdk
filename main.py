import openapi_client
import os
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.linode.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.linode.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: personalAccessToken
configuration = openapi_client.Configuration(
    access_token = "9111e0afb99c46a3d7dbeabd007da9a244fa2391c2bddc1adecc17e1442850ba"
)

# onfiguration.access_token = os.environ["ACCESS_TOKEN"]


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    
    api_instance = openapi_client.AccountApi(api_client)
    api_version = "v4" # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    #client_id = 'client_id_example' # str | The OAuth Client ID to look up.

    print(api_instance.get_account(api_version))