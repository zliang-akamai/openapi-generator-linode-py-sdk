# openapi_client.RegionsApi

All URIs are relative to *https://api.linode.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_region**](RegionsApi.md#get_region) | **GET** /{apiVersion}/regions/{regionId} | Get a region
[**get_region_availability**](RegionsApi.md#get_region_availability) | **GET** /{apiVersion}/regions/{regionId}/availability | Get a region&#39;s availability
[**get_regions**](RegionsApi.md#get_regions) | **GET** /{apiVersion}/regions | List regions
[**get_regions_availability**](RegionsApi.md#get_regions_availability) | **GET** /{apiVersion}/regions/availability | List regions&#39; availability


# **get_region**
> GetRegions200ResponseDataInner get_region(api_version, region_id)

Get a region

Returns a single Region.   <<LB>>  ---   - __CLI__.      ```     linode-cli regions view us-east     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)

### Example


```python
import openapi_client
from openapi_client.models.get_regions200_response_data_inner import GetRegions200ResponseDataInner
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
    api_instance = openapi_client.RegionsApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    region_id = 'region_id_example' # str | ID of the Region to look up.

    try:
        # Get a region
        api_response = api_instance.get_region(api_version, region_id)
        print("The response of RegionsApi->get_region:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegionsApi->get_region: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **region_id** | **str**| ID of the Region to look up. | 

### Return type

[**GetRegions200ResponseDataInner**](GetRegions200ResponseDataInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single Region object. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_region_availability**
> List[GetRegionsAvailability200ResponseAllOfDataInner] get_region_availability(api_version, region_id)

Get a region's availability

Returns availability data for a single Region.   <<LB>>  ---   - __CLI__.      ```     linode-cli regions view-avail us-east     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)

### Example


```python
import openapi_client
from openapi_client.models.get_regions_availability200_response_all_of_data_inner import GetRegionsAvailability200ResponseAllOfDataInner
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
    api_instance = openapi_client.RegionsApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    region_id = 'region_id_example' # str | ID of the Region to look up.

    try:
        # Get a region's availability
        api_response = api_instance.get_region_availability(api_version, region_id)
        print("The response of RegionsApi->get_region_availability:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegionsApi->get_region_availability: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **region_id** | **str**| ID of the Region to look up. | 

### Return type

[**List[GetRegionsAvailability200ResponseAllOfDataInner]**](GetRegionsAvailability200ResponseAllOfDataInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The availability data for a single Region. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_regions**
> GetRegions200Response get_regions(api_version)

List regions

Lists the Regions available for Linode services. Not all services are guaranteed to be available in all Regions.   <<LB>>  ---   - __CLI__.      ```     linode-cli regions list     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)

### Example


```python
import openapi_client
from openapi_client.models.get_regions200_response import GetRegions200Response
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
    api_instance = openapi_client.RegionsApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)

    try:
        # List regions
        api_response = api_instance.get_regions(api_version)
        print("The response of RegionsApi->get_regions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegionsApi->get_regions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]

### Return type

[**GetRegions200Response**](GetRegions200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an array of Regions. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_regions_availability**
> GetRegionsAvailability200Response get_regions_availability(api_version)

List regions' availability

Returns availability data for all Regions.  Currently, this operation returns availability of select premium and GPU plans for select regions.   <<LB>>  ---   - __CLI__.      ```     linode-cli regions list-avail     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)

### Example


```python
import openapi_client
from openapi_client.models.get_regions_availability200_response import GetRegionsAvailability200Response
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
    api_instance = openapi_client.RegionsApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)

    try:
        # List regions' availability
        api_response = api_instance.get_regions_availability(api_version)
        print("The response of RegionsApi->get_regions_availability:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegionsApi->get_regions_availability: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]

### Return type

[**GetRegionsAvailability200Response**](GetRegionsAvailability200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Region Availability object. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

