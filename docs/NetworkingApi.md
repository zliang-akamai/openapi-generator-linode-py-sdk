# openapi_client.NetworkingApi

All URIs are relative to *https://api.linode.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_firewall**](NetworkingApi.md#delete_firewall) | **DELETE** /{apiVersion}/networking/firewalls/{firewallId} | Delete a firewall
[**delete_firewall_device**](NetworkingApi.md#delete_firewall_device) | **DELETE** /{apiVersion}/networking/firewalls/{firewallId}/devices/{deviceId} | Delete a firewall device
[**delete_ipv6_range**](NetworkingApi.md#delete_ipv6_range) | **DELETE** /{apiVersion}/networking/ipv6/ranges/{range} | Delete an IPv6 range
[**get_firewall**](NetworkingApi.md#get_firewall) | **GET** /{apiVersion}/networking/firewalls/{firewallId} | Get a firewall
[**get_firewall_device**](NetworkingApi.md#get_firewall_device) | **GET** /{apiVersion}/networking/firewalls/{firewallId}/devices/{deviceId} | Get a firewall device
[**get_firewall_devices**](NetworkingApi.md#get_firewall_devices) | **GET** /{apiVersion}/networking/firewalls/{firewallId}/devices | List firewall devices
[**get_firewall_rule_version**](NetworkingApi.md#get_firewall_rule_version) | **GET** /{apiVersion}/networking/firewalls/{firewallId}/history/rules/{version} | Get a firewall rule version
[**get_firewall_rule_versions**](NetworkingApi.md#get_firewall_rule_versions) | **GET** /{apiVersion}/networking/firewalls/{firewallId}/history | List firewall rule versions
[**get_firewall_rules**](NetworkingApi.md#get_firewall_rules) | **GET** /{apiVersion}/networking/firewalls/{firewallId}/rules | List firewall rules
[**get_firewalls**](NetworkingApi.md#get_firewalls) | **GET** /{apiVersion}/networking/firewalls | List firewalls
[**get_ip**](NetworkingApi.md#get_ip) | **GET** /{apiVersion}/networking/ips/{address} | Get an IP address
[**get_ips**](NetworkingApi.md#get_ips) | **GET** /{apiVersion}/networking/ips | List IP addresses
[**get_ipv6_pools**](NetworkingApi.md#get_ipv6_pools) | **GET** /{apiVersion}/networking/ipv6/pools | List IPv6 pools
[**get_ipv6_range**](NetworkingApi.md#get_ipv6_range) | **GET** /{apiVersion}/networking/ipv6/ranges/{range} | Get an IPv6 range
[**get_ipv6_ranges**](NetworkingApi.md#get_ipv6_ranges) | **GET** /{apiVersion}/networking/ipv6/ranges | List IPv6 ranges
[**get_vlans**](NetworkingApi.md#get_vlans) | **GET** /{apiVersion}/networking/vlans | List VLANs
[**post_allocate_ip**](NetworkingApi.md#post_allocate_ip) | **POST** /{apiVersion}/networking/ips | Allocate an IP address
[**post_assign_ips**](NetworkingApi.md#post_assign_ips) | **POST** /{apiVersion}/networking/ips/assign | Assign IP addresses
[**post_assign_ipv4s**](NetworkingApi.md#post_assign_ipv4s) | **POST** /{apiVersion}/networking/ipv4/assign | Assign IPv4s to Linodes
[**post_firewall_device**](NetworkingApi.md#post_firewall_device) | **POST** /{apiVersion}/networking/firewalls/{firewallId}/devices | Create a firewall device
[**post_firewalls**](NetworkingApi.md#post_firewalls) | **POST** /{apiVersion}/networking/firewalls | Create a firewall
[**post_ipv6_range**](NetworkingApi.md#post_ipv6_range) | **POST** /{apiVersion}/networking/ipv6/ranges | Create an IPv6 range
[**post_share_ips**](NetworkingApi.md#post_share_ips) | **POST** /{apiVersion}/networking/ips/share | Share IP addresses
[**post_share_ipv4s**](NetworkingApi.md#post_share_ipv4s) | **POST** /{apiVersion}/networking/ipv4/share | Configure IPv4 sharing
[**put_firewall**](NetworkingApi.md#put_firewall) | **PUT** /{apiVersion}/networking/firewalls/{firewallId} | Update a firewall
[**put_firewall_rules**](NetworkingApi.md#put_firewall_rules) | **PUT** /{apiVersion}/networking/firewalls/{firewallId}/rules | Update firewall rules
[**put_ip**](NetworkingApi.md#put_ip) | **PUT** /{apiVersion}/networking/ips/{address} | Update an IP address&#39;s RDNS


# **delete_firewall**
> object delete_firewall(api_version, firewall_id)

Delete a firewall

Delete a Firewall resource by its ID. This removes all of the Firewall's Rules from any services that the Firewall was assigned to.  - Assigned Linodes must not have any ongoing live migrations.  - A `firewall_delete` Event is generated when this operation returns successfully.   <<LB>>  ---   - __CLI__.      ```     linode-cli firewalls delete 123     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     firewall:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.NetworkingApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    firewall_id = 56 # int | ID of the Firewall to access.

    try:
        # Delete a firewall
        api_response = api_instance.delete_firewall(api_version, firewall_id)
        print("The response of NetworkingApi->delete_firewall:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkingApi->delete_firewall: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **firewall_id** | **int**| ID of the Firewall to access. | 

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
**200** | Delete Successful. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_firewall_device**
> object delete_firewall_device(api_version, firewall_id, device_id)

Delete a firewall device

Removes a Firewall Device, which removes a Firewall from the service it was assigned to by the Device. This removes all of the Firewall's Rules from the service. If any other Firewalls have been assigned to the service, then those Rules remain in effect.  - Assigned Linodes must not have any ongoing live migrations.  - A `firewall_device_remove` Event is generated when the Firewall Device is removed successfully.   <<LB>>  ---   - __CLI__.      ```     linode-cli firewalls device-delete 123 456     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     firewall:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.NetworkingApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    firewall_id = 56 # int | ID of the Firewall to access.
    device_id = 56 # int | ID of the Firewall Device to access.

    try:
        # Delete a firewall device
        api_response = api_instance.delete_firewall_device(api_version, firewall_id, device_id)
        print("The response of NetworkingApi->delete_firewall_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkingApi->delete_firewall_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **firewall_id** | **int**| ID of the Firewall to access. | 
 **device_id** | **int**| ID of the Firewall Device to access. | 

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
**200** | Delete Successful. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ipv6_range**
> object delete_ipv6_range(api_version, range)

Delete an IPv6 range

Removes this IPv6 range from your account and disconnects the range from any assigned Linodes.  __Note__. Shared IPv6 ranges cannot be deleted at this time. Please contact Customer Support for assistance.   <<LB>>  ---   - __CLI__.      ```     linode-cli networking v6-range-delete 2001:0db8::     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     ips:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.NetworkingApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    range = 'range_example' # str | The IPv6 range to access. Corresponds to the `range` property of objects returned from the [List IPv6 ranges](https://techdocs.akamai.com/linode-api/reference/get-ipv6-ranges) operation.  __Note__. Omit the prefix length of the IPv6 range.

    try:
        # Delete an IPv6 range
        api_response = api_instance.delete_ipv6_range(api_version, range)
        print("The response of NetworkingApi->delete_ipv6_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkingApi->delete_ipv6_range: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **range** | **str**| The IPv6 range to access. Corresponds to the &#x60;range&#x60; property of objects returned from the [List IPv6 ranges](https://techdocs.akamai.com/linode-api/reference/get-ipv6-ranges) operation.  __Note__. Omit the prefix length of the IPv6 range. | 

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
**200** | IPv6 Range deleted. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firewall**
> GetLinodeFirewalls200ResponseDataInner get_firewall(api_version, firewall_id)

Get a firewall

Get a specific Firewall resource by its ID. The Firewall's Devices will not be returned in the response. Instead, run the [List firewall devices](https://techdocs.akamai.com/linode-api/reference/get-firewall-devices) operation to review them.   <<LB>>  ---   - __CLI__.      ```     linode-cli firewalls view 123     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     firewall:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_linode_firewalls200_response_data_inner import GetLinodeFirewalls200ResponseDataInner
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
    api_instance = openapi_client.NetworkingApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    firewall_id = 56 # int | ID of the Firewall to access.

    try:
        # Get a firewall
        api_response = api_instance.get_firewall(api_version, firewall_id)
        print("The response of NetworkingApi->get_firewall:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkingApi->get_firewall: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **firewall_id** | **int**| ID of the Firewall to access. | 

### Return type

[**GetLinodeFirewalls200ResponseDataInner**](GetLinodeFirewalls200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns information about this Firewall. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firewall_device**
> GetFirewallDevices200ResponseDataInner get_firewall_device(api_version, firewall_id, device_id)

Get a firewall device

Returns information for a Firewall Device, which assigns a Firewall to a service (referred to as the Device's `entity`).   <<LB>>  ---   - __CLI__.      ```     linode-cli firewalls device-view \\   123 456     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     firewall:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_firewall_devices200_response_data_inner import GetFirewallDevices200ResponseDataInner
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
    api_instance = openapi_client.NetworkingApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    firewall_id = 56 # int | ID of the Firewall to access.
    device_id = 56 # int | ID of the Firewall Device to access.

    try:
        # Get a firewall device
        api_response = api_instance.get_firewall_device(api_version, firewall_id, device_id)
        print("The response of NetworkingApi->get_firewall_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkingApi->get_firewall_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **firewall_id** | **int**| ID of the Firewall to access. | 
 **device_id** | **int**| ID of the Firewall Device to access. | 

### Return type

[**GetFirewallDevices200ResponseDataInner**](GetFirewallDevices200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Firewall Device. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firewall_devices**
> GetFirewallDevices200Response get_firewall_devices(api_version, firewall_id, page=page, page_size=page_size)

List firewall devices

Returns a paginated list of a Firewall's Devices. A Firewall Device assigns a Firewall to a service (referred to as the Device's `entity`).   <<LB>>  ---   - __CLI__.      ```     linode-cli firewalls devices-list 123     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     firewall:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_firewall_devices200_response import GetFirewallDevices200Response
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
    api_instance = openapi_client.NetworkingApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    firewall_id = 56 # int | ID of the Firewall to access.
    page = 1 # int | The page of a collection to return. (optional) (default to 1)
    page_size = 100 # int | The number of items to return per page. (optional) (default to 100)

    try:
        # List firewall devices
        api_response = api_instance.get_firewall_devices(api_version, firewall_id, page=page, page_size=page_size)
        print("The response of NetworkingApi->get_firewall_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkingApi->get_firewall_devices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **firewall_id** | **int**| ID of the Firewall to access. | 
 **page** | **int**| The page of a collection to return. | [optional] [default to 1]
 **page_size** | **int**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetFirewallDevices200Response**](GetFirewallDevices200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of Firewall Devices. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firewall_rule_version**
> GetLinodeFirewalls200ResponseDataInner get_firewall_rule_version(api_version, firewall_id, version)

Get a firewall rule version

Get a specific firewall rule version for an `enabled` or `disabled` firewall.   <<LB>>  ---   - __CLI__.      ```     linode-cli firewalls version-view \\   123 2     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     firewall:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_linode_firewalls200_response_data_inner import GetLinodeFirewalls200ResponseDataInner
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
    api_instance = openapi_client.NetworkingApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    firewall_id = 56 # int | ID of the Firewall to access.
    version = 3 # int | The firewall rule version to view.

    try:
        # Get a firewall rule version
        api_response = api_instance.get_firewall_rule_version(api_version, firewall_id, version)
        print("The response of NetworkingApi->get_firewall_rule_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkingApi->get_firewall_rule_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **firewall_id** | **int**| ID of the Firewall to access. | 
 **version** | **int**| The firewall rule version to view. | 

### Return type

[**GetLinodeFirewalls200ResponseDataInner**](GetLinodeFirewalls200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a rule version. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firewall_rule_versions**
> GetLinodeFirewalls200ResponseDataInner get_firewall_rule_versions(api_version, firewall_id)

List firewall rule versions

Lists the current and historical rules of the firewall (that is not deleted), using `version`. Whenever rules update, the `version` increments from `1`.   <<LB>>  ---   - __CLI__.      ```     linode-cli firewalls versions-list 123     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     firewall:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_linode_firewalls200_response_data_inner import GetLinodeFirewalls200ResponseDataInner
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
    api_instance = openapi_client.NetworkingApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    firewall_id = 56 # int | ID of the Firewall to access.

    try:
        # List firewall rule versions
        api_response = api_instance.get_firewall_rule_versions(api_version, firewall_id)
        print("The response of NetworkingApi->get_firewall_rule_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkingApi->get_firewall_rule_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **firewall_id** | **int**| ID of the Firewall to access. | 

### Return type

[**GetLinodeFirewalls200ResponseDataInner**](GetLinodeFirewalls200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns information for all rule versions for this firewall. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firewall_rules**
> GetLinodeFirewalls200ResponseDataInnerRules get_firewall_rules(api_version, firewall_id)

List firewall rules

Returns the inbound and outbound Rules for a Firewall.   <<LB>>  ---   - __CLI__.      ```     linode-cli firewalls rules-list 123     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     firewall:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_linode_firewalls200_response_data_inner_rules import GetLinodeFirewalls200ResponseDataInnerRules
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
    api_instance = openapi_client.NetworkingApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    firewall_id = 56 # int | ID of the Firewall to access.

    try:
        # List firewall rules
        api_response = api_instance.get_firewall_rules(api_version, firewall_id)
        print("The response of NetworkingApi->get_firewall_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkingApi->get_firewall_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **firewall_id** | **int**| ID of the Firewall to access. | 

### Return type

[**GetLinodeFirewalls200ResponseDataInnerRules**](GetLinodeFirewalls200ResponseDataInnerRules.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Firewall Rules. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firewalls**
> GetLinodeFirewalls200Response get_firewalls(api_version, page=page, page_size=page_size)

List firewalls

Returns a paginated list of accessible Firewalls.   <<LB>>  ---   - __CLI__.      ```     linode-cli firewalls list     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     firewall:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_linode_firewalls200_response import GetLinodeFirewalls200Response
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
    api_instance = openapi_client.NetworkingApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    page = 1 # int | The page of a collection to return. (optional) (default to 1)
    page_size = 100 # int | The number of items to return per page. (optional) (default to 100)

    try:
        # List firewalls
        api_response = api_instance.get_firewalls(api_version, page=page, page_size=page_size)
        print("The response of NetworkingApi->get_firewalls:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkingApi->get_firewalls: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **page** | **int**| The page of a collection to return. | [optional] [default to 1]
 **page_size** | **int**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetLinodeFirewalls200Response**](GetLinodeFirewalls200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an array of Firewalls. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ip**
> GetLinodeIps200ResponseIpv4PublicInner get_ip(api_version, address)

Get an IP address

Returns information about a single IP Address on your Account.   <<LB>>  ---   - __CLI__.      ```     linode-cli networking ip-view 97.107.143.141     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     ips:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_linode_ips200_response_ipv4_public_inner import GetLinodeIps200ResponseIpv4PublicInner
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
    api_instance = openapi_client.NetworkingApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    address = 'address_example' # str | The address to operate on.

    try:
        # Get an IP address
        api_response = api_instance.get_ip(api_version, address)
        print("The response of NetworkingApi->get_ip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkingApi->get_ip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **address** | **str**| The address to operate on. | 

### Return type

[**GetLinodeIps200ResponseIpv4PublicInner**](GetLinodeIps200ResponseIpv4PublicInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested IP Address. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ips**
> GetIps200Response get_ips(api_version, skip_ipv6_rdns=skip_ipv6_rdns)

List IP addresses

Returns a paginated list of IP addresses on your account, excluding private addresses.  __Note__. Use the `skip_ipv6_rdns` query string to improve performance if your application frequently accesses this operation and doesn't require IPv6 RDNS data.   <<LB>>  ---   - __CLI__.      ```     linode-cli networking ips-list     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     ips:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_ips200_response import GetIps200Response
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
    api_instance = openapi_client.NetworkingApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    skip_ipv6_rdns = False # bool | When `true`, the `rdns` property for any `ipv6` type addresses always returns `null` regardless of whether RDNS data exists for the address. (optional) (default to False)

    try:
        # List IP addresses
        api_response = api_instance.get_ips(api_version, skip_ipv6_rdns=skip_ipv6_rdns)
        print("The response of NetworkingApi->get_ips:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkingApi->get_ips: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **skip_ipv6_rdns** | **bool**| When &#x60;true&#x60;, the &#x60;rdns&#x60; property for any &#x60;ipv6&#x60; type addresses always returns &#x60;null&#x60; regardless of whether RDNS data exists for the address. | [optional] [default to False]

### Return type

[**GetIps200Response**](GetIps200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of IP Addresses. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ipv6_pools**
> GetIpv6Pools200Response get_ipv6_pools(api_version, page=page, page_size=page_size)

List IPv6 pools

Displays the IPv6 pools on your Account. A pool of IPv6 addresses are routed to all of your Linodes in a single [region](https://techdocs.akamai.com/linode-api/reference/get-regions). Any Linode on your Account may bring up any address in this pool at any time, with no external configuration required.   <<LB>>  ---   - __CLI__.      ```     linode-cli networking v6-pools     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     ips:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_ipv6_pools200_response import GetIpv6Pools200Response
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
    api_instance = openapi_client.NetworkingApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    page = 1 # int | The page of a collection to return. (optional) (default to 1)
    page_size = 100 # int | The number of items to return per page. (optional) (default to 100)

    try:
        # List IPv6 pools
        api_response = api_instance.get_ipv6_pools(api_version, page=page, page_size=page_size)
        print("The response of NetworkingApi->get_ipv6_pools:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkingApi->get_ipv6_pools: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **page** | **int**| The page of a collection to return. | [optional] [default to 1]
 **page_size** | **int**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetIpv6Pools200Response**](GetIpv6Pools200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The IPv6 pools on your Account. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ipv6_range**
> GetIpv6Range200Response get_ipv6_range(api_version, range)

Get an IPv6 range

View IPv6 range information.   <<LB>>  ---   - __CLI__.      ```     linode-cli networking v6-range-view 2001:0db8::     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     ips:read     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_ipv6_range200_response import GetIpv6Range200Response
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
    api_instance = openapi_client.NetworkingApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    range = 'range_example' # str | The IPv6 range to access. Corresponds to the `range` property of objects returned from the [List IPv6 ranges](https://techdocs.akamai.com/linode-api/reference/get-ipv6-ranges) operation.  __Note__. Omit the prefix length of the IPv6 range.

    try:
        # Get an IPv6 range
        api_response = api_instance.get_ipv6_range(api_version, range)
        print("The response of NetworkingApi->get_ipv6_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkingApi->get_ipv6_range: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **range** | **str**| The IPv6 range to access. Corresponds to the &#x60;range&#x60; property of objects returned from the [List IPv6 ranges](https://techdocs.akamai.com/linode-api/reference/get-ipv6-ranges) operation.  __Note__. Omit the prefix length of the IPv6 range. | 

### Return type

[**GetIpv6Range200Response**](GetIpv6Range200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns IPv6 range information. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ipv6_ranges**
> GetIpv6Ranges200Response get_ipv6_ranges(api_version, page=page, page_size=page_size)

List IPv6 ranges

Displays the IPv6 ranges on your Account.    - An IPv6 range is a `/64` or `/56` block of IPv6 addresses routed to a single Linode in a given [region](https://techdocs.akamai.com/linode-api/reference/get-regions).    - Your Linode is responsible for routing individual addresses in the range, or handling traffic for all the addresses in the range.    - Run the [Create an IPv6 range](https://techdocs.akamai.com/linode-api/reference/post-ipv6-range) operation to add a `/64` or `/56` block of IPv6 addresses to your account.   <<LB>>  ---   - __CLI__.      ```     linode-cli networking v6-ranges     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     ips:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_ipv6_ranges200_response import GetIpv6Ranges200Response
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
    api_instance = openapi_client.NetworkingApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    page = 1 # int | The page of a collection to return. (optional) (default to 1)
    page_size = 100 # int | The number of items to return per page. (optional) (default to 100)

    try:
        # List IPv6 ranges
        api_response = api_instance.get_ipv6_ranges(api_version, page=page, page_size=page_size)
        print("The response of NetworkingApi->get_ipv6_ranges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkingApi->get_ipv6_ranges: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **page** | **int**| The page of a collection to return. | [optional] [default to 1]
 **page_size** | **int**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetIpv6Ranges200Response**](GetIpv6Ranges200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The IPv6 ranges on your Account. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vlans**
> GetVlans200Response get_vlans(api_version, page=page, page_size=page_size)

List VLANs

Returns a list of all Virtual Local Area Networks (VLANs) on your Account. VLANs provide a mechanism for secure communication between two or more Linodes that are assigned to the same VLAN and are both within the same Layer 2 broadcast domain.  VLANs are created and attached to Linodes by using the `interfaces` property for the following operations:  - [Create a Linode](https://techdocs.akamai.com/linode-api/reference/post-linode-instance) - [Create a config profile](https://techdocs.akamai.com/linode-api/reference/post-add-linode-config) - [Update a config profile](https://techdocs.akamai.com/linode-api/reference/put-linode-config)  There are several ways to detach a VLAN from a Linode:  - [Update](https://techdocs.akamai.com/linode-api/reference/put-linode-config) the active Configuration Profile to remove the VLAN Interface, then [reboot](https://techdocs.akamai.com/linode-api/reference/post-reboot-linode-instance) the Linode. - [Create a config profile](https://techdocs.akamai.com/linode-api/reference/post-add-linode-config) without the VLAN Interface, then [reboot](https://techdocs.akamai.com/linode-api/reference/post-reboot-linode-instance) the Linode into the new Configuration Profile. - [Delete](https://techdocs.akamai.com/linode-api/reference/delete-linode-instance) the Linode.  __Note__. Only Next Generation Network (NGN) data centers support VLANs. Run the [List regions](https://techdocs.akamai.com/linode-api/reference/get-regions) operation to view the capabilities of data center regions. If a VLAN is attached to your Linode and you attempt to migrate or clone it to a non-NGN data center, the migration or cloning will not initiate. If a Linode cannot be migrated because of an incompatibility, you will be prompted to select a different data center or contact support.  __Note__. See the [VLANs Overview](https://www.linode.com/docs/products/networking/vlans/#technical-specifications) to view additional specifications and limitations.   <<LB>>  ---   - __CLI__.      ```     linode-cli vlans list     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     linodes:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_vlans200_response import GetVlans200Response
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
    api_instance = openapi_client.NetworkingApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    page = 1 # int | The page of a collection to return. (optional) (default to 1)
    page_size = 100 # int | The number of items to return per page. (optional) (default to 100)

    try:
        # List VLANs
        api_response = api_instance.get_vlans(api_version, page=page, page_size=page_size)
        print("The response of NetworkingApi->get_vlans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkingApi->get_vlans: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **page** | **int**| The page of a collection to return. | [optional] [default to 1]
 **page_size** | **int**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetVlans200Response**](GetVlans200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The VLANs available on this Account. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_allocate_ip**
> GetLinodeIps200ResponseIpv4PublicInner post_allocate_ip(api_version, post_allocate_ip_request)

Allocate an IP address

Allocates a new IPv4 Address on your Account. The Linode must be configured to support additional addresses - please [Open a support ticket](https://techdocs.akamai.com/linode-api/reference/post-ticket) requesting additional addresses before attempting allocation.   <<LB>>  ---   - __CLI__.      ```     linode-cli networking ip-add \\   --type ipv4 \\   --public true \\   --linode_id 123     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     ips:read_write linodes:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_linode_ips200_response_ipv4_public_inner import GetLinodeIps200ResponseIpv4PublicInner
from openapi_client.models.post_allocate_ip_request import PostAllocateIpRequest
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
    api_instance = openapi_client.NetworkingApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    post_allocate_ip_request = openapi_client.PostAllocateIpRequest() # PostAllocateIpRequest | Information about the address you are creating.

    try:
        # Allocate an IP address
        api_response = api_instance.post_allocate_ip(api_version, post_allocate_ip_request)
        print("The response of NetworkingApi->post_allocate_ip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkingApi->post_allocate_ip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **post_allocate_ip_request** | [**PostAllocateIpRequest**](PostAllocateIpRequest.md)| Information about the address you are creating. | 

### Return type

[**GetLinodeIps200ResponseIpv4PublicInner**](GetLinodeIps200ResponseIpv4PublicInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | IP Address allocated successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_assign_ips**
> object post_assign_ips(api_version, post_assign_ips_request)

Assign IP addresses

Assign multiple IPv4 addresses and/or IPv6 ranges to multiple Linodes in one Region. This allows swapping, shuffling, or otherwise reorganizing IPs to your Linodes.  The following restrictions apply:  - All Linodes involved must have at least one public IPv4 address after assignment. - Linodes may have no more than one assigned private IPv4 address. - Linodes may have no more than one assigned IPv6 range. - Shared IP addresses cannot be swapped between Linodes.  [Open a support ticket](https://techdocs.akamai.com/linode-api/reference/post-ticket) to request additional IPv4 addresses or IPv6 ranges beyond standard account limits.  __Note__. Removing an IP address that has been set as a Managed Linode's `ssh.ip` causes the Managed Linode's SSH access settings to reset to their default values.  To view and configure Managed Linode SSH settings, use the following operations:  - [Get a Linode's managed settings](https://techdocs.akamai.com/linode-api/reference/get-managed-linode-setting) - [Update a Linode's managed settings](https://techdocs.akamai.com/linode-api/reference/put-managed-linode-setting)  __Note__. Addresses with an active 1:1 NAT to a VPC Interface address cannot be assigned to other Linodes.   <<LB>>  ---   - __CLI__.      ```     linode-cli networking ip-assign \\   --region us-east \\   --assignments.address 192.0.2.1 \\   --assignments.linode_id 123 \\   --assignments.address 2001:db8:3c4d:15::/64 \\   --assignments.linode_id 234     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     ips:read_write linodes:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.post_assign_ips_request import PostAssignIpsRequest
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
    api_instance = openapi_client.NetworkingApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    post_assign_ips_request = openapi_client.PostAssignIpsRequest() # PostAssignIpsRequest | Information about what IPv4 address or IPv6 range to assign, and to which Linode.

    try:
        # Assign IP addresses
        api_response = api_instance.post_assign_ips(api_version, post_assign_ips_request)
        print("The response of NetworkingApi->post_assign_ips:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkingApi->post_assign_ips: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **post_assign_ips_request** | [**PostAssignIpsRequest**](PostAssignIpsRequest.md)| Information about what IPv4 address or IPv6 range to assign, and to which Linode. | 

### Return type

**object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All assignments completed successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_assign_ipv4s**
> object post_assign_ipv4s(api_version, post_assign_ips_request)

Assign IPv4s to Linodes

This operation is equivalent to [Assign IP addresses](https://techdocs.akamai.com/linode-api/reference/post-assign-ips).  Assign multiple IPv4 addresses and/or IPv6 ranges to multiple Linodes in one Region. This allows swapping, shuffling, or otherwise reorganizing IPs to your Linodes.  The following restrictions apply:  - All Linodes involved must have at least one public IPv4 address after assignment. - Linodes may have no more than one assigned private IPv4 address. - Linodes may have no more than one assigned IPv6 range.  [Open a support ticket](https://techdocs.akamai.com/linode-api/reference/post-ticket) to request additional IPv4 addresses or IPv6 ranges beyond standard account limits.  __Note__. Removing an IP address that has been set as a Managed Linode's `ssh.ip` causes the Managed Linode's SSH access settings to reset to their default values.  To view and configure Managed Linode SSH settings, use the following operations: - [Get a Linode's managed settings](https://techdocs.akamai.com/linode-api/reference/get-managed-linode-setting) - [Update a Linode's managed settings](https://techdocs.akamai.com/linode-api/reference/put-managed-linode-setting)   <<LB>>  ---   - __OAuth scopes__.      ```     ips:read_write linodes:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.post_assign_ips_request import PostAssignIpsRequest
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
    api_instance = openapi_client.NetworkingApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    post_assign_ips_request = openapi_client.PostAssignIpsRequest() # PostAssignIpsRequest | Information about what IPv4 address to assign, and to which Linode.

    try:
        # Assign IPv4s to Linodes
        api_response = api_instance.post_assign_ipv4s(api_version, post_assign_ips_request)
        print("The response of NetworkingApi->post_assign_ipv4s:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkingApi->post_assign_ipv4s: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **post_assign_ips_request** | [**PostAssignIpsRequest**](PostAssignIpsRequest.md)| Information about what IPv4 address to assign, and to which Linode. | 

### Return type

**object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All assignments completed successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_firewall_device**
> GetFirewallDevices200ResponseDataInner post_firewall_device(api_version, firewall_id, post_firewall_device_request=post_firewall_device_request)

Create a firewall device

Creates a Firewall Device, which assigns a Firewall to a service (referred to as the Device's `entity`) and applies the Firewall's Rules to the device.  - Currently, Devices with `linode` and `nodebalancer` entity types are accepted.  - Firewalls only apply to inbound TCP traffic to NodeBalancers.  - A Firewall can be assigned to multiple services at a time.  - A service can have one assigned Firewall at a time.  - Assigned Linodes must not have any ongoing live migrations.  - A `firewall_device_add` Event is generated when the Firewall Device is added successfully.   <<LB>>  ---   - __CLI__.      ```     linode-cli firewalls device-create 123 \\   --id 456 \\   --type \"linode\"     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     firewall:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_firewall_devices200_response_data_inner import GetFirewallDevices200ResponseDataInner
from openapi_client.models.post_firewall_device_request import PostFirewallDeviceRequest
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
    api_instance = openapi_client.NetworkingApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    firewall_id = 56 # int | ID of the Firewall to access.
    post_firewall_device_request = openapi_client.PostFirewallDeviceRequest() # PostFirewallDeviceRequest |  (optional)

    try:
        # Create a firewall device
        api_response = api_instance.post_firewall_device(api_version, firewall_id, post_firewall_device_request=post_firewall_device_request)
        print("The response of NetworkingApi->post_firewall_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkingApi->post_firewall_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **firewall_id** | **int**| ID of the Firewall to access. | 
 **post_firewall_device_request** | [**PostFirewallDeviceRequest**](PostFirewallDeviceRequest.md)|  | [optional] 

### Return type

[**GetFirewallDevices200ResponseDataInner**](GetFirewallDevices200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns information about the created Firewall Device. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_firewalls**
> GetLinodeFirewalls200ResponseDataInner post_firewalls(api_version, post_firewalls_request=post_firewalls_request)

Create a firewall

Creates a Firewall to filter network traffic.  - Use `rules` to create inbound and outbound access rules. Rule versions increment from `1` whenever the firewall's `rules` change.  - Use `devices` to assign the firewall to a service and apply its rules to the device. Requires `read_write` [user grant](https://techdocs.akamai.com/linode-api/reference/get-user-grants) to the device. Currently, firewalls can be assigned to Linode compute instances and NodeBalancers.  - A Firewall can be assigned to multiple services at a time.  - Use `firewall_id` to assign a firewall when [creating a Linode](https://techdocs.akamai.com/linode-api/reference/post-linode-instance).  - A service can have one assigned Firewall at a time.  - Firewalls apply to all of a Linode's non-`vlan` purpose Configuration Profile Interfaces.  - Assigned Linodes must not have any ongoing live migrations.  - A `firewall_create` Event is generated when this operation succeeds.   <<LB>>  ---   - __CLI__.      ```     linode-cli firewalls create \\   --label example-firewall \\   --rules.outbound_policy ACCEPT \\   --rules.inbound_policy DROP \\   --rules.inbound '[{\"protocol\": \"TCP\", \"ports\": \"22, 80, 8080, 443\", \"addresses\": {\"ipv4\": [\"192.0.2.0/24\", \"198.51.100.2/32\"], \"ipv6\": [\"2001:DB8::/128\"]}, \"action\": \"ACCEPT\"}]' \\   --rules.outbound '[{\"protocol\": \"TCP\", \"ports\": \"49152-65535\", \"addresses\": {\"ipv4\": [\"192.0.2.0/24\", \"198.51.100.2/32\"],\"ipv6\": [\"2001:DB8::/128\"]}, \"action\": \"DROP\", \"label\": \"outbound-rule123\", \"description\": \"An example outbound rule description.\"}]'     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     firewall:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_linode_firewalls200_response_data_inner import GetLinodeFirewalls200ResponseDataInner
from openapi_client.models.post_firewalls_request import PostFirewallsRequest
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
    api_instance = openapi_client.NetworkingApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    post_firewalls_request = openapi_client.PostFirewallsRequest() # PostFirewallsRequest | Creates a Firewall object that can be applied to a service to filter the service's network traffic. (optional)

    try:
        # Create a firewall
        api_response = api_instance.post_firewalls(api_version, post_firewalls_request=post_firewalls_request)
        print("The response of NetworkingApi->post_firewalls:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkingApi->post_firewalls: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **post_firewalls_request** | [**PostFirewallsRequest**](PostFirewallsRequest.md)| Creates a Firewall object that can be applied to a service to filter the service&#39;s network traffic. | [optional] 

### Return type

[**GetLinodeFirewalls200ResponseDataInner**](GetLinodeFirewalls200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns information about the created Firewall. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ipv6_range**
> PostIpv6Range200Response post_ipv6_range(api_version, post_ipv6_range_request)

Create an IPv6 range

Creates an IPv6 Range and assigns it based on the provided Linode or route target IPv6 SLAAC address. See the `ipv6` property when running the [Get a Linode](https://techdocs.akamai.com/linode-api/reference/get-linode-instance) operation to view a Linode's IPv6 SLAAC address.  - Either `linode_id` or `route_target` is required in a request. - `linode_id` and `route_target` are mutually exclusive. Submitting values for both properties in a request results in an error. - Upon a successful request, an IPv6 range is created in the [region](https://techdocs.akamai.com/linode-api/reference/get-regions) that corresponds to the provided `linode_id` or `route_target`. - Your Linode is responsible for routing individual addresses in the range, or handling traffic for all the addresses in the range. - Run the [Assign IP addresses](https://techdocs.akamai.com/linode-api/reference/post-assign-ips) operation to re-assign IPv6 Ranges to your Linodes.  __Note__. The following restrictions apply:    - A Linode can only have one IPv6 range targeting its SLAAC address.   - An account can only have one IPv6 range in each [region](https://techdocs.akamai.com/linode-api/reference/get-regions).   - [Open a support ticket](https://techdocs.akamai.com/linode-api/reference/post-ticket) to request expansion of these restrictions.   <<LB>>  ---   - __CLI__.      ```     linode-cli networking v6-range-create \\   --linode_id 123 \\   --prefix_length 64     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     ips:read_write linodes:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.post_ipv6_range200_response import PostIpv6Range200Response
from openapi_client.models.post_ipv6_range_request import PostIpv6RangeRequest
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
    api_instance = openapi_client.NetworkingApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    post_ipv6_range_request = openapi_client.PostIpv6RangeRequest() # PostIpv6RangeRequest | Information about the IPv6 range to create.

    try:
        # Create an IPv6 range
        api_response = api_instance.post_ipv6_range(api_version, post_ipv6_range_request)
        print("The response of NetworkingApi->post_ipv6_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkingApi->post_ipv6_range: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **post_ipv6_range_request** | [**PostIpv6RangeRequest**](PostIpv6RangeRequest.md)| Information about the IPv6 range to create. | 

### Return type

[**PostIpv6Range200Response**](PostIpv6Range200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | IPv6 range created successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_share_ips**
> object post_share_ips(api_version, post_share_ips_request)

Share IP addresses

Configure shared IPs.  IP sharing allows IP address reassignment (also referred to as IP failover) from one Linode to another if the primary Linode becomes unresponsive. This means that requests to the primary Linode's IP address can be automatically rerouted to secondary Linodes at the configured shared IP addresses.  IP failover requires configuration of a [BGP based failover service](https://techdocs.akamai.com/cloud-computing/docs/configure-failover-on-a-compute-instance) within the internal system of the primary Linode.  __Note__. A public IPv4 address cannot be shared if it is configured for a 1:1 NAT on a `vpc` purpose Configuration Profile Interface.   <<LB>>  ---   - __CLI__.      ```     linode-cli networking ip-share \\   --linode_id 123 \\   --ips 192.0.2.1 \\   --ips 2001:db8:3c4d:15::     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     ips:read_write linodes:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.post_share_ips_request import PostShareIpsRequest
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
    api_instance = openapi_client.NetworkingApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    post_share_ips_request = openapi_client.PostShareIpsRequest() # PostShareIpsRequest | Information about what IPs to share with which Linode.

    try:
        # Share IP addresses
        api_response = api_instance.post_share_ips(api_version, post_share_ips_request)
        print("The response of NetworkingApi->post_share_ips:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkingApi->post_share_ips: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **post_share_ips_request** | [**PostShareIpsRequest**](PostShareIpsRequest.md)| Information about what IPs to share with which Linode. | 

### Return type

**object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | IP Address sharing successful. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_share_ipv4s**
> object post_share_ipv4s(api_version, post_share_ips_request)

Configure IPv4 sharing

This operation is equivalent to [Share IP addresses](https://techdocs.akamai.com/linode-api/reference/post-share-ips).  Configure shared IPs.  IP sharing allows IP address reassignment (also referred to as IP failover) from one Linode to another if the primary Linode becomes unresponsive. This means that requests to the primary Linode's IP address can be automatically rerouted to secondary Linodes at the configured shared IP addresses.  IP failover requires configuration of a [BGP based failover service](https://techdocs.akamai.com/cloud-computing/docs/configure-failover-on-a-compute-instance) within the internal system of the primary Linode.   <<LB>>  ---   - __OAuth scopes__.      ```     ips:read_write linodes:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.post_share_ips_request import PostShareIpsRequest
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
    api_instance = openapi_client.NetworkingApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    post_share_ips_request = openapi_client.PostShareIpsRequest() # PostShareIpsRequest | Information about what IPs to share with which Linode.

    try:
        # Configure IPv4 sharing
        api_response = api_instance.post_share_ipv4s(api_version, post_share_ips_request)
        print("The response of NetworkingApi->post_share_ipv4s:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkingApi->post_share_ipv4s: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **post_share_ips_request** | [**PostShareIpsRequest**](PostShareIpsRequest.md)| Information about what IPs to share with which Linode. | 

### Return type

**object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sharing configured successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_firewall**
> GetLinodeFirewalls200ResponseDataInner put_firewall(api_version, firewall_id, put_firewall_request=put_firewall_request)

Update a firewall

Updates information for a Firewall.  - Assigned Linodes must not have any ongoing live migrations.  - If a Firewall's status is changed with this operation, a corresponding `firewall_enable` or `firewall_disable` Event will be generated.  Some parts of a Firewall's configuration cannot be manipulated by this operation:  - A Firewall's Devices cannot be set with this operation. Instead, run the [Create a firewall device](https://techdocs.akamai.com/linode-api/reference/post-firewall-device) and [Delete a firewall device](https://techdocs.akamai.com/linode-api/reference/delete-firewall-device) operations to assign and remove this Firewall from services.  - A Firewall's Rules cannot be changed with this operation. Instead, run the [Update firewall rules](https://techdocs.akamai.com/linode-api/reference/put-firewall-rules) operation to update your Rules.  - A Firewall's status can be set to `enabled` or `disabled` by this operation, but it cannot be set to `deleted`. Instead, run the [Delete a firewall](https://techdocs.akamai.com/linode-api/reference/delete-firewall) operation to delete a Firewall.   <<LB>>  ---   - __CLI__.      ```     linode-cli firewalls update 123 \\   --status disabled     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     firewall:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_linode_firewalls200_response_data_inner import GetLinodeFirewalls200ResponseDataInner
from openapi_client.models.put_firewall_request import PutFirewallRequest
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
    api_instance = openapi_client.NetworkingApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    firewall_id = 56 # int | ID of the Firewall to access.
    put_firewall_request = openapi_client.PutFirewallRequest() # PutFirewallRequest | The Firewall information to update. (optional)

    try:
        # Update a firewall
        api_response = api_instance.put_firewall(api_version, firewall_id, put_firewall_request=put_firewall_request)
        print("The response of NetworkingApi->put_firewall:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkingApi->put_firewall: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **firewall_id** | **int**| ID of the Firewall to access. | 
 **put_firewall_request** | [**PutFirewallRequest**](PutFirewallRequest.md)| The Firewall information to update. | [optional] 

### Return type

[**GetLinodeFirewalls200ResponseDataInner**](GetLinodeFirewalls200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Firewall updated successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_firewall_rules**
> GetLinodeFirewalls200ResponseDataInnerRules put_firewall_rules(api_version, firewall_id, put_firewall_rules_request=put_firewall_rules_request)

Update firewall rules

Updates the inbound and outbound Rules for a Firewall.  - Assigned Linodes must not have any ongoing live migrations.  - __Note__. This operation replaces all of a Firewall's `inbound` and `outbound` rulesets with the values specified in your request.   <<LB>>  ---   - __CLI__.      ```     linode-cli firewalls rules-update 123 \\   --inbound '[{\"action\":\"ACCEPT\", \"protocol\": \"TCP\", \"ports\": \"22, 80, 8080, 443\", \"addresses\": {\"ipv4\": [\"192.0.2.0/24\", \"198.51.100.2/32\"], \"ipv6\": [\"2001:DB8::/128\"]}}]' \\   --outbound '[{\"action\":\"DROP\",\"protocol\": \"TCP\", \"ports\": \"49152-65535\", \"addresses\": {\"ipv4\": [\"192.0.2.0/24\", \"198.51.100.2/32\"], \"ipv6\": [\"2001:DB8::/128`\"]}}]'     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     firewall:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_linode_firewalls200_response_data_inner_rules import GetLinodeFirewalls200ResponseDataInnerRules
from openapi_client.models.put_firewall_rules_request import PutFirewallRulesRequest
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
    api_instance = openapi_client.NetworkingApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    firewall_id = 56 # int | ID of the Firewall to access.
    put_firewall_rules_request = openapi_client.PutFirewallRulesRequest() # PutFirewallRulesRequest | The Firewall Rules information to update. (optional)

    try:
        # Update firewall rules
        api_response = api_instance.put_firewall_rules(api_version, firewall_id, put_firewall_rules_request=put_firewall_rules_request)
        print("The response of NetworkingApi->put_firewall_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkingApi->put_firewall_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **firewall_id** | **int**| ID of the Firewall to access. | 
 **put_firewall_rules_request** | [**PutFirewallRulesRequest**](PutFirewallRulesRequest.md)| The Firewall Rules information to update. | [optional] 

### Return type

[**GetLinodeFirewalls200ResponseDataInnerRules**](GetLinodeFirewalls200ResponseDataInnerRules.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Firewall Rules updated successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_ip**
> GetLinodeIps200ResponseIpv4PublicInner put_ip(api_version, address, put_ip_request)

Update an IP address's RDNS

Sets RDNS on an IP Address. Forward DNS must already be set up for reverse DNS to be applied. If you set the RDNS to `null` for public IPv4 addresses, it will be reset to the default _ip.linodeusercontent.com_ RDNS value.   <<LB>>  ---   - __CLI__.      ```     linode-cli networking ip-update \\   203.0.113.1 \\   --rdns \"test.example.org\"     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     ips:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_linode_ips200_response_ipv4_public_inner import GetLinodeIps200ResponseIpv4PublicInner
from openapi_client.models.put_ip_request import PutIpRequest
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
    api_instance = openapi_client.NetworkingApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    address = 'address_example' # str | The address to operate on.
    put_ip_request = openapi_client.PutIpRequest() # PutIpRequest | The information to update.

    try:
        # Update an IP address's RDNS
        api_response = api_instance.put_ip(api_version, address, put_ip_request)
        print("The response of NetworkingApi->put_ip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkingApi->put_ip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **address** | **str**| The address to operate on. | 
 **put_ip_request** | [**PutIpRequest**](PutIpRequest.md)| The information to update. | 

### Return type

[**GetLinodeIps200ResponseIpv4PublicInner**](GetLinodeIps200ResponseIpv4PublicInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RDNS set successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

