# openapi_client.BetaProgramsApi

All URIs are relative to *https://api.linode.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_beta_program**](BetaProgramsApi.md#get_beta_program) | **GET** /{apiVersion}/betas/{betaId} | Get a Beta program
[**get_beta_programs**](BetaProgramsApi.md#get_beta_programs) | **GET** /{apiVersion}/betas | List Beta programs


# **get_beta_program**
> GetBetaPrograms200ResponseAllOfDataInner get_beta_program(api_version, beta_id)

Get a Beta program

Display information about a Beta Program. This operation can be used to access inactive as well as active Beta Programs.  Only unrestricted Users can access this operation.   <<LB>>  ---   - __CLI__.      ```     linode-cli betas view $betaId     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_beta_programs200_response_all_of_data_inner import GetBetaPrograms200ResponseAllOfDataInner
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
    access_token = os.environ["BEARER_TOKEN"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.BetaProgramsApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    beta_id = 'beta_id_example' # str | The ID of the Beta Program.

    try:
        # Get a Beta program
        api_response = api_instance.get_beta_program(api_version, beta_id)
        print("The response of BetaProgramsApi->get_beta_program:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BetaProgramsApi->get_beta_program: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **beta_id** | **str**| The ID of the Beta Program. | 

### Return type

[**GetBetaPrograms200ResponseAllOfDataInner**](GetBetaPrograms200ResponseAllOfDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a paginated list of all available Beta Program objects. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_beta_programs**
> GetBetaPrograms200Response get_beta_programs(api_version, page=page, page_size=page_size)

List Beta programs

Display all active Beta Programs.  Only unrestricted Users can access this operation.   <<LB>>  ---   - __CLI__.      ```     linode-cli betas list     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_beta_programs200_response import GetBetaPrograms200Response
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
    access_token = os.environ["BEARER_TOKEN"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.BetaProgramsApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    page = 1 # int | The page of a collection to return. (optional) (default to 1)
    page_size = 100 # int | The number of items to return per page. (optional) (default to 100)

    try:
        # List Beta programs
        api_response = api_instance.get_beta_programs(api_version, page=page, page_size=page_size)
        print("The response of BetaProgramsApi->get_beta_programs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BetaProgramsApi->get_beta_programs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **page** | **int**| The page of a collection to return. | [optional] [default to 1]
 **page_size** | **int**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetBetaPrograms200Response**](GetBetaPrograms200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a paginated list of all available Beta Program objects. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

