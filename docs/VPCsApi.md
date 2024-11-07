# openapi_client.VPCsApi

All URIs are relative to *https://api.linode.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_vpc**](VPCsApi.md#delete_vpc) | **DELETE** /{apiVersion}/vpcs/{vpcId} | Delete a VPC
[**delete_vpc_subnet**](VPCsApi.md#delete_vpc_subnet) | **DELETE** /{apiVersion}/vpcs/{vpcId}/subnets/{vpcSubnetId} | Delete a VPC subnet
[**get_vpc**](VPCsApi.md#get_vpc) | **GET** /{apiVersion}/vpcs/{vpcId} | Get a VPC
[**get_vpc_ips**](VPCsApi.md#get_vpc_ips) | **GET** /{apiVersion}/vpcs/{vpcId}/ips | List a VPC&#39;s IP addresses
[**get_vpc_subnet**](VPCsApi.md#get_vpc_subnet) | **GET** /{apiVersion}/vpcs/{vpcId}/subnets/{vpcSubnetId} | Get a VPC subnet
[**get_vpc_subnets**](VPCsApi.md#get_vpc_subnets) | **GET** /{apiVersion}/vpcs/{vpcId}/subnets | List VPC subnets
[**get_vpcs**](VPCsApi.md#get_vpcs) | **GET** /{apiVersion}/vpcs | List VPCs
[**get_vpcs_ips**](VPCsApi.md#get_vpcs_ips) | **GET** /{apiVersion}/vpcs/ips | List VPC IP addresses
[**post_vpc**](VPCsApi.md#post_vpc) | **POST** /{apiVersion}/vpcs | Create a VPC
[**post_vpc_subnet**](VPCsApi.md#post_vpc_subnet) | **POST** /{apiVersion}/vpcs/{vpcId}/subnets | Create a VPC subnet
[**put_vpc**](VPCsApi.md#put_vpc) | **PUT** /{apiVersion}/vpcs/{vpcId} | Update a VPC
[**put_vpc_subnet**](VPCsApi.md#put_vpc_subnet) | **PUT** /{apiVersion}/vpcs/{vpcId}/subnets/{vpcSubnetId} | Update a VPC subnet


# **delete_vpc**
> object delete_vpc(api_version, vpc_id)

Delete a VPC

Delete a single VPC and all of its Subnets.  - The User accessing this operation must have `read_write` grants to the VPC. - A successful request triggers a `vpc_delete` event and `subnet_delete` events for each deleted VPC Subnet. - All of the VPC's Subnets must be eligible for deletion. Accordingly, all Configuration Profile Interfaces that each Subnet is assigned to must first be deleted. If those Interfaces are active, the associated Linodes must first be shut down before they can be removed. If any Subnet cannot be deleted, then neither the VPC nor any of its Subnets are deleted.   <<LB>>  ---   - __CLI__.      ```     linode-cli vpcs delete $vpcId     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     vpc:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
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
    api_instance = openapi_client.VPCsApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    vpc_id = 56 # int | The `id` of the VPC.

    try:
        # Delete a VPC
        api_response = api_instance.delete_vpc(api_version, vpc_id)
        print("The response of VPCsApi->delete_vpc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPCsApi->delete_vpc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **vpc_id** | **int**| The &#x60;id&#x60; of the VPC. | 

### Return type

**object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete request successful. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vpc_subnet**
> object delete_vpc_subnet(api_version, vpc_id, vpc_subnet_id)

Delete a VPC subnet

Delete a single VPC Subnet.  The user accessing this operation must have `read_write` grants to the VPC. A successful request triggers a `subnet_delete` event.  __Note__. You need to delete all the Configuration Profile Interfaces that this Subnet is assigned to before you can delete it. If those Interfaces are active, the associated Linode needs to be shut down before they can be removed.   <<LB>>  ---   - __CLI__.      ```     linode-cli vpcs subnet-delete $vpcId $vpcSubnetId     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     vpc:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
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
    api_instance = openapi_client.VPCsApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    vpc_id = 56 # int | The `id` of the VPC.
    vpc_subnet_id = 56 # int | The `id` of the VPC Subnet.

    try:
        # Delete a VPC subnet
        api_response = api_instance.delete_vpc_subnet(api_version, vpc_id, vpc_subnet_id)
        print("The response of VPCsApi->delete_vpc_subnet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPCsApi->delete_vpc_subnet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **vpc_id** | **int**| The &#x60;id&#x60; of the VPC. | 
 **vpc_subnet_id** | **int**| The &#x60;id&#x60; of the VPC Subnet. | 

### Return type

**object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete request successful. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vpc**
> GetVpcs200ResponseAllOfDataInner get_vpc(api_version, vpc_id)

Get a VPC

Get information about a single VPC.   <<LB>>  ---   - __CLI__.      ```     linode-cli vpcs view $vpcId     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_vpcs200_response_all_of_data_inner import GetVpcs200ResponseAllOfDataInner
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
    api_instance = openapi_client.VPCsApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    vpc_id = 56 # int | The `id` of the VPC.

    try:
        # Get a VPC
        api_response = api_instance.get_vpc(api_version, vpc_id)
        print("The response of VPCsApi->get_vpc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPCsApi->get_vpc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **vpc_id** | **int**| The &#x60;id&#x60; of the VPC. | 

### Return type

[**GetVpcs200ResponseAllOfDataInner**](GetVpcs200ResponseAllOfDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A VPC object. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vpc_ips**
> GetVpcsIps200Response get_vpc_ips(api_version, vpc_id, page=page, page_size=page_size)

List a VPC's IP addresses

Returns a paginated list of IP addresses for a single VPC.   <<LB>>  ---   - __CLI__.      ```     linode-cli vpcs ip-list 123     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     ips:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_vpcs_ips200_response import GetVpcsIps200Response
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
    api_instance = openapi_client.VPCsApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    vpc_id = 56 # int | The `id` of the VPC.
    page = 1 # int | The page of a collection to return. (optional) (default to 1)
    page_size = 100 # int | The number of items to return per page. (optional) (default to 100)

    try:
        # List a VPC's IP addresses
        api_response = api_instance.get_vpc_ips(api_version, vpc_id, page=page, page_size=page_size)
        print("The response of VPCsApi->get_vpc_ips:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPCsApi->get_vpc_ips: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **vpc_id** | **int**| The &#x60;id&#x60; of the VPC. | 
 **page** | **int**| The page of a collection to return. | [optional] [default to 1]
 **page_size** | **int**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetVpcsIps200Response**](GetVpcsIps200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The IP addresses for the requested VPC. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vpc_subnet**
> GetVpcs200ResponseAllOfDataInnerSubnetsInner get_vpc_subnet(api_version, vpc_id, vpc_subnet_id)

Get a VPC subnet

Get information about a single VPC Subnet.   <<LB>>  ---   - __CLI__.      ```     linode-cli vpcs subnet-view $vpcId $vpcSubnetId     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_vpcs200_response_all_of_data_inner_subnets_inner import GetVpcs200ResponseAllOfDataInnerSubnetsInner
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
    api_instance = openapi_client.VPCsApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    vpc_id = 56 # int | The `id` of the VPC.
    vpc_subnet_id = 56 # int | The `id` of the VPC Subnet.

    try:
        # Get a VPC subnet
        api_response = api_instance.get_vpc_subnet(api_version, vpc_id, vpc_subnet_id)
        print("The response of VPCsApi->get_vpc_subnet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPCsApi->get_vpc_subnet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **vpc_id** | **int**| The &#x60;id&#x60; of the VPC. | 
 **vpc_subnet_id** | **int**| The &#x60;id&#x60; of the VPC Subnet. | 

### Return type

[**GetVpcs200ResponseAllOfDataInnerSubnetsInner**](GetVpcs200ResponseAllOfDataInnerSubnetsInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A VPC Subnet object. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vpc_subnets**
> GetVpcSubnets200Response get_vpc_subnets(api_version, vpc_id, page=page, page_size=page_size)

List VPC subnets

Get information about all VPC Subnets associated with a VPC.   <<LB>>  ---   - __CLI__.      ```     linode-cli vpcs subnets-list $vpcId     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_vpc_subnets200_response import GetVpcSubnets200Response
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
    api_instance = openapi_client.VPCsApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    vpc_id = 56 # int | The `id` of the VPC.
    page = 1 # int | The page of a collection to return. (optional) (default to 1)
    page_size = 100 # int | The number of items to return per page. (optional) (default to 100)

    try:
        # List VPC subnets
        api_response = api_instance.get_vpc_subnets(api_version, vpc_id, page=page, page_size=page_size)
        print("The response of VPCsApi->get_vpc_subnets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPCsApi->get_vpc_subnets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **vpc_id** | **int**| The &#x60;id&#x60; of the VPC. | 
 **page** | **int**| The page of a collection to return. | [optional] [default to 1]
 **page_size** | **int**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetVpcSubnets200Response**](GetVpcSubnets200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of VPC Subnet objects. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vpcs**
> GetVpcs200Response get_vpcs(api_version, page=page, page_size=page_size)

List VPCs

Display all VPCs on your account.   <<LB>>  ---   - __CLI__.      ```     linode-cli vpcs list     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_vpcs200_response import GetVpcs200Response
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
    api_instance = openapi_client.VPCsApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    page = 1 # int | The page of a collection to return. (optional) (default to 1)
    page_size = 100 # int | The number of items to return per page. (optional) (default to 100)

    try:
        # List VPCs
        api_response = api_instance.get_vpcs(api_version, page=page, page_size=page_size)
        print("The response of VPCsApi->get_vpcs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPCsApi->get_vpcs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **page** | **int**| The page of a collection to return. | [optional] [default to 1]
 **page_size** | **int**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetVpcs200Response**](GetVpcs200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of VPC objects. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vpcs_ips**
> GetVpcsIps200Response get_vpcs_ips(api_version, page=page, page_size=page_size)

List VPC IP addresses

Returns a paginated list of all VPC IP addresses and address ranges on your account.  __Note__. If a Linode has several configuration profiles that include a VPC interface, address information for all of them is listed in the response. Since VPCs can use the same address space, you may see duplicate IP addresses.   <<LB>>  ---   - __CLI__.      ```     linode-cli vpcs ips-all-list     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     ips:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_vpcs_ips200_response import GetVpcsIps200Response
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
    api_instance = openapi_client.VPCsApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    page = 1 # int | The page of a collection to return. (optional) (default to 1)
    page_size = 100 # int | The number of items to return per page. (optional) (default to 100)

    try:
        # List VPC IP addresses
        api_response = api_instance.get_vpcs_ips(api_version, page=page, page_size=page_size)
        print("The response of VPCsApi->get_vpcs_ips:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPCsApi->get_vpcs_ips: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **page** | **int**| The page of a collection to return. | [optional] [default to 1]
 **page_size** | **int**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetVpcsIps200Response**](GetVpcsIps200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of VPC interface IP addresses. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_vpc**
> GetVpcs200ResponseAllOfDataInner post_vpc(api_version, post_vpc_request)

Create a VPC

Create a new VPC and optionally associated VPC Subnets.  - Users must have the `add_vpc` grant to access this operation. - A successful request triggers a `vpc_create` event and `subnet_create` events for any created VPC Subnets.  Once a VPC is created, it can be attached to a Linode by assigning a VPC Subnet to one of the Linode's Configuration Profile Interfaces. This step can be accomplished with the following operations:  - [Create a Linode](https://techdocs.akamai.com/linode-api/reference/post-linode-instance) - [Create a config profile](https://techdocs.akamai.com/linode-api/reference/post-add-linode-config) - [Update a config profile](https://techdocs.akamai.com/linode-api/reference/put-linode-config) - [Add a configuration profile interface](https://techdocs.akamai.com/linode-api/reference/post-linode-config-interface)   <<LB>>  ---   - __CLI__.      ```     linode-cli vpcs create \\   --description \"A description of my VPC.\" \\   --label cool-vpc \\   --region us-east \\   --subnets.label cool-vpc-subnet \\   --subnets.ipv4 10.0.1.0/24     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     vpc:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_vpcs200_response_all_of_data_inner import GetVpcs200ResponseAllOfDataInner
from openapi_client.models.post_vpc_request import PostVpcRequest
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
    api_instance = openapi_client.VPCsApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    post_vpc_request = openapi_client.PostVpcRequest() # PostVpcRequest | VPC Create request object.

    try:
        # Create a VPC
        api_response = api_instance.post_vpc(api_version, post_vpc_request)
        print("The response of VPCsApi->post_vpc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPCsApi->post_vpc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **post_vpc_request** | [**PostVpcRequest**](PostVpcRequest.md)| VPC Create request object. | 

### Return type

[**GetVpcs200ResponseAllOfDataInner**](GetVpcs200ResponseAllOfDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The new VPC. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_vpc_subnet**
> GetVpcs200ResponseAllOfDataInnerSubnetsInner post_vpc_subnet(api_version, vpc_id, post_vpc_subnet_request)

Create a VPC subnet

Create a VPC Subnet.  - The User accessing this operation must have `read_write` grants to the VPC. - A successful request triggers a `subnet_create` event.  Once a VPC Subnet is created, it can be attached to a Linode by assigning the Subnet to one of the Linode's Configuration Profile Interfaces. This step can be accomplished with the following operations:  - [Create a Linode](https://techdocs.akamai.com/linode-api/reference/post-linode-instance) - [Create a config profile](https://techdocs.akamai.com/linode-api/reference/post-add-linode-config) - [Update a config profile](https://techdocs.akamai.com/linode-api/reference/put-linode-config) - [Add a configuration profile interface](https://techdocs.akamai.com/linode-api/reference/post-linode-config-interface)   <<LB>>  ---   - __CLI__.      ```     linode-cli vpcs subnet-create $vpcId \\   --label cool-vpc-subnet \\   --ipv4 10.0.1.0/24     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     vpc:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_vpcs200_response_all_of_data_inner_subnets_inner import GetVpcs200ResponseAllOfDataInnerSubnetsInner
from openapi_client.models.post_vpc_subnet_request import PostVpcSubnetRequest
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
    api_instance = openapi_client.VPCsApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    vpc_id = 56 # int | The `id` of the VPC.
    post_vpc_subnet_request = openapi_client.PostVpcSubnetRequest() # PostVpcSubnetRequest | VPC Subnet Create request object.

    try:
        # Create a VPC subnet
        api_response = api_instance.post_vpc_subnet(api_version, vpc_id, post_vpc_subnet_request)
        print("The response of VPCsApi->post_vpc_subnet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPCsApi->post_vpc_subnet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **vpc_id** | **int**| The &#x60;id&#x60; of the VPC. | 
 **post_vpc_subnet_request** | [**PostVpcSubnetRequest**](PostVpcSubnetRequest.md)| VPC Subnet Create request object. | 

### Return type

[**GetVpcs200ResponseAllOfDataInnerSubnetsInner**](GetVpcs200ResponseAllOfDataInnerSubnetsInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The new VPC Subnet. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_vpc**
> GetVpcs200ResponseAllOfDataInner put_vpc(api_version, vpc_id, put_vpc_request)

Update a VPC

Update an existing VPC.  - The User accessing this operation must have `read_write` grants to the VPC. - A successful request triggers a `vpc_update` event.  To update a VPC's Subnet, run the [Update a VPC subnet](https://techdocs.akamai.com/linode-api/reference/put-vpc-subnet) operation.   <<LB>>  ---   - __CLI__.      ```     linode-cli vpcs update $vpcId \\   --description \"A description of my VPC.\"   --label cool-vpc     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     vpc:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_vpcs200_response_all_of_data_inner import GetVpcs200ResponseAllOfDataInner
from openapi_client.models.put_vpc_request import PutVpcRequest
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
    api_instance = openapi_client.VPCsApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    vpc_id = 56 # int | The `id` of the VPC.
    put_vpc_request = openapi_client.PutVpcRequest() # PutVpcRequest | VPC Update request object.

    try:
        # Update a VPC
        api_response = api_instance.put_vpc(api_version, vpc_id, put_vpc_request)
        print("The response of VPCsApi->put_vpc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPCsApi->put_vpc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **vpc_id** | **int**| The &#x60;id&#x60; of the VPC. | 
 **put_vpc_request** | [**PutVpcRequest**](PutVpcRequest.md)| VPC Update request object. | 

### Return type

[**GetVpcs200ResponseAllOfDataInner**](GetVpcs200ResponseAllOfDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated VPC. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_vpc_subnet**
> GetVpcs200ResponseAllOfDataInnerSubnetsInner put_vpc_subnet(api_version, vpc_id, vpc_subnet_id, put_vpc_subnet_request)

Update a VPC subnet

Update a VPC Subnet.  - The User accessing this operation must have `read_write` grants to the VPC. - A successful request triggers a `subnet_update` event.   <<LB>>  ---   - __CLI__.      ```     linode-cli vpcs subnet-update $vpcId \\   --label cool-vpc-subnet     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     vpc:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_vpcs200_response_all_of_data_inner_subnets_inner import GetVpcs200ResponseAllOfDataInnerSubnetsInner
from openapi_client.models.put_vpc_subnet_request import PutVpcSubnetRequest
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
    api_instance = openapi_client.VPCsApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    vpc_id = 56 # int | The `id` of the VPC.
    vpc_subnet_id = 56 # int | The `id` of the VPC Subnet.
    put_vpc_subnet_request = openapi_client.PutVpcSubnetRequest() # PutVpcSubnetRequest | VPC Update request object.

    try:
        # Update a VPC subnet
        api_response = api_instance.put_vpc_subnet(api_version, vpc_id, vpc_subnet_id, put_vpc_subnet_request)
        print("The response of VPCsApi->put_vpc_subnet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPCsApi->put_vpc_subnet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **vpc_id** | **int**| The &#x60;id&#x60; of the VPC. | 
 **vpc_subnet_id** | **int**| The &#x60;id&#x60; of the VPC Subnet. | 
 **put_vpc_subnet_request** | [**PutVpcSubnetRequest**](PutVpcSubnetRequest.md)| VPC Update request object. | 

### Return type

[**GetVpcs200ResponseAllOfDataInnerSubnetsInner**](GetVpcs200ResponseAllOfDataInnerSubnetsInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated VPC Subnet. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

