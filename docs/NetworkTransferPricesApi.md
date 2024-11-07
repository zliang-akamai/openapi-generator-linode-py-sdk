# openapi_client.NetworkTransferPricesApi

All URIs are relative to *https://api.linode.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_network_transfer_prices**](NetworkTransferPricesApi.md#get_network_transfer_prices) | **GET** /{apiVersion}/network-transfer/prices | List network transfer prices


# **get_network_transfer_prices**
> GetNetworkTransferPrices200Response get_network_transfer_prices(api_version)

List network transfer prices

Returns collection of network transfer prices, including any region-specific rates.   <<LB>>  ---   - __CLI__.      ```     linode-cli network-transfer prices     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)

### Example


```python
import openapi_client
from openapi_client.models.get_network_transfer_prices200_response import GetNetworkTransferPrices200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.linode.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.linode.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.NetworkTransferPricesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)

    try:
        # List network transfer prices
        api_response = api_instance.get_network_transfer_prices(api_version)
        print("The response of NetworkTransferPricesApi->get_network_transfer_prices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkTransferPricesApi->get_network_transfer_prices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]

### Return type

[**GetNetworkTransferPrices200Response**](GetNetworkTransferPrices200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of network transfer prices. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

