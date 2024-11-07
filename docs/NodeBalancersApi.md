# openapi_client.NodeBalancersApi

All URIs are relative to *https://api.linode.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_node_balancer**](NodeBalancersApi.md#delete_node_balancer) | **DELETE** /{apiVersion}/nodebalancers/{nodeBalancerId} | Delete a NodeBalancer
[**delete_node_balancer_config**](NodeBalancersApi.md#delete_node_balancer_config) | **DELETE** /{apiVersion}/nodebalancers/{nodeBalancerId}/configs/{configId} | Delete a config
[**delete_node_balancer_config_node**](NodeBalancersApi.md#delete_node_balancer_config_node) | **DELETE** /{apiVersion}/nodebalancers/{nodeBalancerId}/configs/{configId}/nodes/{nodeId} | Delete a NodeBalancer&#39;s node
[**get_node_balancer**](NodeBalancersApi.md#get_node_balancer) | **GET** /{apiVersion}/nodebalancers/{nodeBalancerId} | Get a NodeBalancer
[**get_node_balancer_config**](NodeBalancersApi.md#get_node_balancer_config) | **GET** /{apiVersion}/nodebalancers/{nodeBalancerId}/configs/{configId} | Get a config
[**get_node_balancer_config_nodes**](NodeBalancersApi.md#get_node_balancer_config_nodes) | **GET** /{apiVersion}/nodebalancers/{nodeBalancerId}/configs/{configId}/nodes | List nodes
[**get_node_balancer_configs**](NodeBalancersApi.md#get_node_balancer_configs) | **GET** /{apiVersion}/nodebalancers/{nodeBalancerId}/configs | List configs
[**get_node_balancer_firewalls**](NodeBalancersApi.md#get_node_balancer_firewalls) | **GET** /{apiVersion}/nodebalancers/{nodeBalancerId}/firewalls | List NodeBalancer firewalls
[**get_node_balancer_node**](NodeBalancersApi.md#get_node_balancer_node) | **GET** /{apiVersion}/nodebalancers/{nodeBalancerId}/configs/{configId}/nodes/{nodeId} | Get a NodeBalancer&#39;s node
[**get_node_balancer_stats**](NodeBalancersApi.md#get_node_balancer_stats) | **GET** /{apiVersion}/nodebalancers/{nodeBalancerId}/stats | Get NodeBalancer statistics
[**get_node_balancer_types**](NodeBalancersApi.md#get_node_balancer_types) | **GET** /{apiVersion}/nodebalancers/types | List NodeBalancer types
[**get_node_balancers**](NodeBalancersApi.md#get_node_balancers) | **GET** /{apiVersion}/nodebalancers | List NodeBalancers
[**post_node_balancer**](NodeBalancersApi.md#post_node_balancer) | **POST** /{apiVersion}/nodebalancers | Create a NodeBalancer
[**post_node_balancer_config**](NodeBalancersApi.md#post_node_balancer_config) | **POST** /{apiVersion}/nodebalancers/{nodeBalancerId}/configs | Create a config
[**post_node_balancer_node**](NodeBalancersApi.md#post_node_balancer_node) | **POST** /{apiVersion}/nodebalancers/{nodeBalancerId}/configs/{configId}/nodes | Create a node
[**post_rebuild_node_balancer_config**](NodeBalancersApi.md#post_rebuild_node_balancer_config) | **POST** /{apiVersion}/nodebalancers/{nodeBalancerId}/configs/{configId}/rebuild | Rebuild a config
[**put_node_balancer**](NodeBalancersApi.md#put_node_balancer) | **PUT** /{apiVersion}/nodebalancers/{nodeBalancerId} | Update a NodeBalancer
[**put_node_balancer_config**](NodeBalancersApi.md#put_node_balancer_config) | **PUT** /{apiVersion}/nodebalancers/{nodeBalancerId}/configs/{configId} | Update a config
[**put_node_balancer_node**](NodeBalancersApi.md#put_node_balancer_node) | **PUT** /{apiVersion}/nodebalancers/{nodeBalancerId}/configs/{configId}/nodes/{nodeId} | Update a node


# **delete_node_balancer**
> object delete_node_balancer(api_version, node_balancer_id)

Delete a NodeBalancer

Deletes a NodeBalancer.  __This is a destructive action and cannot be undone.__  Deleting a NodeBalancer will also delete all associated Configs and Nodes, although the backend servers represented by the Nodes will not be changed or removed. Deleting a NodeBalancer will cause you to lose access to the IP Addresses assigned to this NodeBalancer.   <<LB>>  ---   - __CLI__.      ```     linode-cli nodebalancers delete 12345     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     nodebalancers:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.NodeBalancersApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    node_balancer_id = 56 # int | The ID of the NodeBalancer to access.

    try:
        # Delete a NodeBalancer
        api_response = api_instance.delete_node_balancer(api_version, node_balancer_id)
        print("The response of NodeBalancersApi->delete_node_balancer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeBalancersApi->delete_node_balancer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **node_balancer_id** | **int**| The ID of the NodeBalancer to access. | 

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
**200** | NodeBalancer deleted successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_node_balancer_config**
> object delete_node_balancer_config(api_version, node_balancer_id, config_id)

Delete a config

Deletes the Config for a port of this NodeBalancer.  __This cannot be undone.__  Once completed, this NodeBalancer will no longer respond to requests on the given port. This also deletes all associated NodeBalancerNodes, but the Linodes they were routing traffic to will be unchanged and will not be removed.   <<LB>>  ---   - __CLI__.      ```     linode-cli nodebalancers config-delete \\   12345 4567     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     nodebalancers:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.NodeBalancersApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    node_balancer_id = 56 # int | The ID of the NodeBalancer to access.
    config_id = 56 # int | The ID of the Config to access.

    try:
        # Delete a config
        api_response = api_instance.delete_node_balancer_config(api_version, node_balancer_id, config_id)
        print("The response of NodeBalancersApi->delete_node_balancer_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeBalancersApi->delete_node_balancer_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **node_balancer_id** | **int**| The ID of the NodeBalancer to access. | 
 **config_id** | **int**| The ID of the Config to access. | 

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
**200** | NodeBalancer Config deleted successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_node_balancer_config_node**
> object delete_node_balancer_config_node(api_version, node_balancer_id, config_id, node_id)

Delete a NodeBalancer's node

Deletes a Node from this Config. This backend will no longer receive traffic for the configured port of this NodeBalancer.  This does not change or remove the Linode whose address was used in the creation of this Node.   <<LB>>  ---   - __CLI__.      ```     linode-cli nodebalancers node-delete \\   12345 4567 54321     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     nodebalancers:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.NodeBalancersApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    node_balancer_id = 56 # int | The ID of the NodeBalancer to access.
    config_id = 56 # int | The ID of the Config to access.
    node_id = 'node_id_example' # str | The ID of the Node to access.

    try:
        # Delete a NodeBalancer's node
        api_response = api_instance.delete_node_balancer_config_node(api_version, node_balancer_id, config_id, node_id)
        print("The response of NodeBalancersApi->delete_node_balancer_config_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeBalancersApi->delete_node_balancer_config_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **node_balancer_id** | **int**| The ID of the NodeBalancer to access. | 
 **config_id** | **int**| The ID of the Config to access. | 
 **node_id** | **str**| The ID of the Node to access. | 

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
**200** | Node deleted successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_balancer**
> NodeBalancer get_node_balancer(api_version, node_balancer_id)

Get a NodeBalancer

Returns a single NodeBalancer you can access.   <<LB>>  ---   - __CLI__.      ```     linode-cli nodebalancers view 12345     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     nodebalancers:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.node_balancer import NodeBalancer
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
    api_instance = openapi_client.NodeBalancersApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    node_balancer_id = 56 # int | The ID of the NodeBalancer to access.

    try:
        # Get a NodeBalancer
        api_response = api_instance.get_node_balancer(api_version, node_balancer_id)
        print("The response of NodeBalancersApi->get_node_balancer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeBalancersApi->get_node_balancer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **node_balancer_id** | **int**| The ID of the NodeBalancer to access. | 

### Return type

[**NodeBalancer**](NodeBalancer.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested NodeBalancer object. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_balancer_config**
> GetNodeBalancerConfigs200ResponseDataInner get_node_balancer_config(api_version, node_balancer_id, config_id)

Get a config

Returns configuration information for a single port of this NodeBalancer.   <<LB>>  ---   - __CLI__.      ```     linode-cli nodebalancers config-view \\   12345 4567     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     nodebalancers:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_node_balancer_configs200_response_data_inner import GetNodeBalancerConfigs200ResponseDataInner
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
    api_instance = openapi_client.NodeBalancersApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    node_balancer_id = 56 # int | The ID of the NodeBalancer to access.
    config_id = 56 # int | The ID of the Config to access.

    try:
        # Get a config
        api_response = api_instance.get_node_balancer_config(api_version, node_balancer_id, config_id)
        print("The response of NodeBalancersApi->get_node_balancer_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeBalancersApi->get_node_balancer_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **node_balancer_id** | **int**| The ID of the NodeBalancer to access. | 
 **config_id** | **int**| The ID of the Config to access. | 

### Return type

[**GetNodeBalancerConfigs200ResponseDataInner**](GetNodeBalancerConfigs200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested NodeBalancer config. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_balancer_config_nodes**
> GetNodeBalancerConfigNodes200Response get_node_balancer_config_nodes(api_version, node_balancer_id, config_id, page=page, page_size=page_size)

List nodes

Returns a paginated list of NodeBalancer nodes associated with this Config. These are the backends that will be sent traffic for this port.   <<LB>>  ---   - __CLI__.      ```     linode-cli nodebalancers nodes-list 12345 4567     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     nodebalancers:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_node_balancer_config_nodes200_response import GetNodeBalancerConfigNodes200Response
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
    api_instance = openapi_client.NodeBalancersApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    node_balancer_id = 56 # int | The ID of the NodeBalancer to access.
    config_id = 56 # int | The ID of the NodeBalancer config to access.
    page = 1 # int | The page of a collection to return. (optional) (default to 1)
    page_size = 100 # int | The number of items to return per page. (optional) (default to 100)

    try:
        # List nodes
        api_response = api_instance.get_node_balancer_config_nodes(api_version, node_balancer_id, config_id, page=page, page_size=page_size)
        print("The response of NodeBalancersApi->get_node_balancer_config_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeBalancersApi->get_node_balancer_config_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **node_balancer_id** | **int**| The ID of the NodeBalancer to access. | 
 **config_id** | **int**| The ID of the NodeBalancer config to access. | 
 **page** | **int**| The page of a collection to return. | [optional] [default to 1]
 **page_size** | **int**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetNodeBalancerConfigNodes200Response**](GetNodeBalancerConfigNodes200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of NodeBalancer nodes. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_balancer_configs**
> GetNodeBalancerConfigs200Response get_node_balancer_configs(api_version, node_balancer_id, page=page, page_size=page_size)

List configs

Returns a paginated list of NodeBalancer Configs associated with this NodeBalancer. NodeBalancer Configs represent individual ports that this NodeBalancer will accept traffic on, one Config per port.  For example, if you wanted to accept standard HTTP traffic, you would need a Config listening on port 80.   <<LB>>  ---   - __CLI__.      ```     linode-cli nodebalancers configs-list 12345     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     nodebalancers:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_node_balancer_configs200_response import GetNodeBalancerConfigs200Response
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
    api_instance = openapi_client.NodeBalancersApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    node_balancer_id = 56 # int | The ID of the NodeBalancer to access.
    page = 1 # int | The page of a collection to return. (optional) (default to 1)
    page_size = 100 # int | The number of items to return per page. (optional) (default to 100)

    try:
        # List configs
        api_response = api_instance.get_node_balancer_configs(api_version, node_balancer_id, page=page, page_size=page_size)
        print("The response of NodeBalancersApi->get_node_balancer_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeBalancersApi->get_node_balancer_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **node_balancer_id** | **int**| The ID of the NodeBalancer to access. | 
 **page** | **int**| The page of a collection to return. | [optional] [default to 1]
 **page_size** | **int**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetNodeBalancerConfigs200Response**](GetNodeBalancerConfigs200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of NodeBalancer Configs. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_balancer_firewalls**
> GetNodeBalancerFirewalls200Response get_node_balancer_firewalls(api_version, node_balancer_id)

List NodeBalancer firewalls

View information for Firewalls assigned to this NodeBalancer.   <<LB>>  ---   - __CLI__.      ```     linode-cli nodebalancers firewalls $nodeBalancerId     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     nodebalancers:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_node_balancer_firewalls200_response import GetNodeBalancerFirewalls200Response
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
    api_instance = openapi_client.NodeBalancersApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    node_balancer_id = 56 # int | The ID of the NodeBalancer to access.

    try:
        # List NodeBalancer firewalls
        api_response = api_instance.get_node_balancer_firewalls(api_version, node_balancer_id)
        print("The response of NodeBalancersApi->get_node_balancer_firewalls:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeBalancersApi->get_node_balancer_firewalls: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **node_balancer_id** | **int**| The ID of the NodeBalancer to access. | 

### Return type

[**GetNodeBalancerFirewalls200Response**](GetNodeBalancerFirewalls200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a paginated list of Firewalls assigned to this NodeBalancer. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_balancer_node**
> PostNodeBalancerRequestConfigsInnerNodesInner get_node_balancer_node(api_version, node_balancer_id, config_id, node_id)

Get a NodeBalancer's node

Returns information about a single Node, a backend for this NodeBalancer's configured port.   <<LB>>  ---   - __CLI__.      ```     linode-cli nodebalancers node-view 12345 4567 54321     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     nodebalancers:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.post_node_balancer_request_configs_inner_nodes_inner import PostNodeBalancerRequestConfigsInnerNodesInner
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
    api_instance = openapi_client.NodeBalancersApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    node_balancer_id = 56 # int | The ID of the NodeBalancer to access.
    config_id = 56 # int | The ID of the Config to access.
    node_id = 'node_id_example' # str | The ID of the Node to access.

    try:
        # Get a NodeBalancer's node
        api_response = api_instance.get_node_balancer_node(api_version, node_balancer_id, config_id, node_id)
        print("The response of NodeBalancersApi->get_node_balancer_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeBalancersApi->get_node_balancer_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **node_balancer_id** | **int**| The ID of the NodeBalancer to access. | 
 **config_id** | **int**| The ID of the Config to access. | 
 **node_id** | **str**| The ID of the Node to access. | 

### Return type

[**PostNodeBalancerRequestConfigsInnerNodesInner**](PostNodeBalancerRequestConfigsInnerNodesInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of NodeBalancer nodes. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_balancer_stats**
> GetNodeBalancerStats200Response get_node_balancer_stats(api_version, node_balancer_id)

Get NodeBalancer statistics

Returns detailed statistics about the requested NodeBalancer.   <<LB>>  ---   - __OAuth scopes__.      ```     nodebalancers:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_node_balancer_stats200_response import GetNodeBalancerStats200Response
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
    api_instance = openapi_client.NodeBalancersApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    node_balancer_id = 56 # int | The ID of the NodeBalancer to access.

    try:
        # Get NodeBalancer statistics
        api_response = api_instance.get_node_balancer_stats(api_version, node_balancer_id)
        print("The response of NodeBalancersApi->get_node_balancer_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeBalancersApi->get_node_balancer_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **node_balancer_id** | **int**| The ID of the NodeBalancer to access. | 

### Return type

[**GetNodeBalancerStats200Response**](GetNodeBalancerStats200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested stats. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_balancer_types**
> GetNodeBalancerTypes200Response get_node_balancer_types(api_version)

List NodeBalancer types

Returns NodeBalancer types and prices, including any region-specific rates.   <<LB>>  ---   - __CLI__.      ```     linode-cli nodebalancers types     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)

### Example


```python
import openapi_client
from openapi_client.models.get_node_balancer_types200_response import GetNodeBalancerTypes200Response
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
    api_instance = openapi_client.NodeBalancersApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)

    try:
        # List NodeBalancer types
        api_response = api_instance.get_node_balancer_types(api_version)
        print("The response of NodeBalancersApi->get_node_balancer_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeBalancersApi->get_node_balancer_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]

### Return type

[**GetNodeBalancerTypes200Response**](GetNodeBalancerTypes200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of NodeBalancer types. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_balancers**
> GetLinodeNodeBalancers200Response get_node_balancers(api_version, page=page, page_size=page_size)

List NodeBalancers

Returns a paginated list of NodeBalancers you have access to.   <<LB>>  ---   - __CLI__.      ```     linode-cli nodebalancers list     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     nodebalancers:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_linode_node_balancers200_response import GetLinodeNodeBalancers200Response
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
    api_instance = openapi_client.NodeBalancersApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    page = 1 # int | The page of a collection to return. (optional) (default to 1)
    page_size = 100 # int | The number of items to return per page. (optional) (default to 100)

    try:
        # List NodeBalancers
        api_response = api_instance.get_node_balancers(api_version, page=page, page_size=page_size)
        print("The response of NodeBalancersApi->get_node_balancers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeBalancersApi->get_node_balancers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **page** | **int**| The page of a collection to return. | [optional] [default to 1]
 **page_size** | **int**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetLinodeNodeBalancers200Response**](GetLinodeNodeBalancers200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of NodeBalancers. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_node_balancer**
> NodeBalancer post_node_balancer(api_version, post_node_balancer_request)

Create a NodeBalancer

Creates a NodeBalancer in the requested Region. Only available in [regions](https://techdocs.akamai.com/linode-api/reference/get-regions) with \"NodeBalancers\" in their `capabilities`.  NodeBalancers require a port Config with at least one backend Node to start serving requests.  When using the Linode CLI to create a NodeBalancer, first create a NodeBalancer without any Configs. Then, create Configs and Nodes for that NodeBalancer with the respective [Create a config](https://techdocs.akamai.com/linode-api/reference/post-node-balancer-config) and [Create a node](https://techdocs.akamai.com/linode-api/reference/post-node-balancer-node) operations.   <<LB>>  ---   - __CLI__.      ```     linode-cli nodebalancers create \\   --region us-east \\   --label balancer12345 \\   --client_conn_throttle 0     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     nodebalancers:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.node_balancer import NodeBalancer
from openapi_client.models.post_node_balancer_request import PostNodeBalancerRequest
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
    api_instance = openapi_client.NodeBalancersApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    post_node_balancer_request = openapi_client.PostNodeBalancerRequest() # PostNodeBalancerRequest | Information about the NodeBalancer to create.

    try:
        # Create a NodeBalancer
        api_response = api_instance.post_node_balancer(api_version, post_node_balancer_request)
        print("The response of NodeBalancersApi->post_node_balancer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeBalancersApi->post_node_balancer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **post_node_balancer_request** | [**PostNodeBalancerRequest**](PostNodeBalancerRequest.md)| Information about the NodeBalancer to create. | 

### Return type

[**NodeBalancer**](NodeBalancer.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | NodeBalancer created successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_node_balancer_config**
> GetNodeBalancerConfigs200ResponseDataInner post_node_balancer_config(api_version, node_balancer_id, get_node_balancer_configs200_response_data_inner=get_node_balancer_configs200_response_data_inner)

Create a config

Creates a NodeBalancer Config, which allows the NodeBalancer to accept traffic on a new port. You will need to add NodeBalancer Nodes to the new Config before it can actually serve requests.   <<LB>>  ---   - __CLI__.      ```     linode-cli nodebalancers config-create 12345 \\   --port 443 \\   --protocol https \\   --algorithm roundrobin \\   --stickiness http_cookie \\   --check http_body \\   --check_interval 90 \\   --check_timeout 10 \\   --check_attempts 3 \\   --check_path \"/test\" \\   --check_body \"it works\" \\   --check_passive true \\   --proxy_protocol \"none\" \\   --ssl_cert \"-----BEGIN CERTIFICATE-----               CERTIFICATE_INFORMATION               -----END CERTIFICATE-----\" \\   --ssl_key \"-----BEGIN PRIVATE KEY-----              PRIVATE_KEY_INFORMATION              -----END PRIVATE KEY-----\" \\   --cipher_suite recommended     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     nodebalancers:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_node_balancer_configs200_response_data_inner import GetNodeBalancerConfigs200ResponseDataInner
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
    api_instance = openapi_client.NodeBalancersApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    node_balancer_id = 56 # int | The ID of the NodeBalancer to access.
    get_node_balancer_configs200_response_data_inner = openapi_client.GetNodeBalancerConfigs200ResponseDataInner() # GetNodeBalancerConfigs200ResponseDataInner | Information about the port to configure. (optional)

    try:
        # Create a config
        api_response = api_instance.post_node_balancer_config(api_version, node_balancer_id, get_node_balancer_configs200_response_data_inner=get_node_balancer_configs200_response_data_inner)
        print("The response of NodeBalancersApi->post_node_balancer_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeBalancersApi->post_node_balancer_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **node_balancer_id** | **int**| The ID of the NodeBalancer to access. | 
 **get_node_balancer_configs200_response_data_inner** | [**GetNodeBalancerConfigs200ResponseDataInner**](GetNodeBalancerConfigs200ResponseDataInner.md)| Information about the port to configure. | [optional] 

### Return type

[**GetNodeBalancerConfigs200ResponseDataInner**](GetNodeBalancerConfigs200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Config created successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_node_balancer_node**
> PostNodeBalancerRequestConfigsInnerNodesInner post_node_balancer_node(api_version, node_balancer_id, config_id, post_node_balancer_node_request)

Create a node

Creates a NodeBalancer Node, a backend that can accept traffic for this NodeBalancer Config. Nodes are routed requests on the configured port based on their status.   <<LB>>  ---   - __CLI__.      ```     linode-cli nodebalancers node-create \\   12345 4567 \\   --address 192.168.210.120:80 \\   --label node54321 \\   --weight 50 \\   --mode accept     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     nodebalancers:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.post_node_balancer_node_request import PostNodeBalancerNodeRequest
from openapi_client.models.post_node_balancer_request_configs_inner_nodes_inner import PostNodeBalancerRequestConfigsInnerNodesInner
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
    api_instance = openapi_client.NodeBalancersApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    node_balancer_id = 56 # int | The ID of the NodeBalancer to access.
    config_id = 56 # int | The ID of the NodeBalancer config to access.
    post_node_balancer_node_request = openapi_client.PostNodeBalancerNodeRequest() # PostNodeBalancerNodeRequest | Information about the Node to create.

    try:
        # Create a node
        api_response = api_instance.post_node_balancer_node(api_version, node_balancer_id, config_id, post_node_balancer_node_request)
        print("The response of NodeBalancersApi->post_node_balancer_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeBalancersApi->post_node_balancer_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **node_balancer_id** | **int**| The ID of the NodeBalancer to access. | 
 **config_id** | **int**| The ID of the NodeBalancer config to access. | 
 **post_node_balancer_node_request** | [**PostNodeBalancerNodeRequest**](PostNodeBalancerNodeRequest.md)| Information about the Node to create. | 

### Return type

[**PostNodeBalancerRequestConfigsInnerNodesInner**](PostNodeBalancerRequestConfigsInnerNodesInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Node created successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_rebuild_node_balancer_config**
> GetNodeBalancerConfigs200ResponseDataInner post_rebuild_node_balancer_config(api_version, node_balancer_id, config_id, post_rebuild_node_balancer_config_request)

Rebuild a config

Rebuilds a NodeBalancer Config and its Nodes that you have permission to modify.  Use this operation to update a NodeBalancer's Config and Nodes with a single request.   <<LB>>  ---   - __CLI__.      ```     linode-cli nodebalancers config-rebuild \\   12345 4567 \\   --port 443 \\   --protocol https \\   --algorithm roundrobin \\   --stickiness http_cookie \\   --check http_body \\   --check_interval 90 \\   --check_timeout 10 \\   --check_attempts 3 \\   --check_path \"/test\" \\   --check_body \"it works\" \\   --check_passive true \\   --proxy_protocol \"none\" \\   --ssl_cert \"-----BEGIN CERTIFICATE-----               CERTIFICATE_INFORMATION               -----END CERTIFICATE-----\" \\   --ssl_key \"-----BEGIN PRIVATE KEY-----              PRIVATE_KEY_INFORMATION              -----END PRIVATE KEY-----\" \\   --cipher_suite recommended \\   --nodes '{\"address\":\"192.168.210.120:80\",\"label\":\"node1\",\"weight\":50,\"mode\":\"accept\"}' \\   --nodes '{\"address\":\"192.168.210.122:80\",\"label\":\"node2\",\"weight\":50,\"mode\":\"accept\"}'     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     nodebalancers:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_node_balancer_configs200_response_data_inner import GetNodeBalancerConfigs200ResponseDataInner
from openapi_client.models.post_rebuild_node_balancer_config_request import PostRebuildNodeBalancerConfigRequest
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
    api_instance = openapi_client.NodeBalancersApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    node_balancer_id = 56 # int | The ID of the NodeBalancer to access.
    config_id = 56 # int | The ID of the Config to access.
    post_rebuild_node_balancer_config_request = openapi_client.PostRebuildNodeBalancerConfigRequest() # PostRebuildNodeBalancerConfigRequest | Information about the NodeBalancer Config to rebuild.

    try:
        # Rebuild a config
        api_response = api_instance.post_rebuild_node_balancer_config(api_version, node_balancer_id, config_id, post_rebuild_node_balancer_config_request)
        print("The response of NodeBalancersApi->post_rebuild_node_balancer_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeBalancersApi->post_rebuild_node_balancer_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **node_balancer_id** | **int**| The ID of the NodeBalancer to access. | 
 **config_id** | **int**| The ID of the Config to access. | 
 **post_rebuild_node_balancer_config_request** | [**PostRebuildNodeBalancerConfigRequest**](PostRebuildNodeBalancerConfigRequest.md)| Information about the NodeBalancer Config to rebuild. | 

### Return type

[**GetNodeBalancerConfigs200ResponseDataInner**](GetNodeBalancerConfigs200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | NodeBalancer created successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_node_balancer**
> NodeBalancer put_node_balancer(api_version, node_balancer_id, node_balancer)

Update a NodeBalancer

Updates information about a NodeBalancer you can access.   <<LB>>  ---   - __CLI__.      ```     linode-cli nodebalancers update 12345 \\   --label balancer12345 \\   --client_conn_throttle 0     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     nodebalancers:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.node_balancer import NodeBalancer
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
    api_instance = openapi_client.NodeBalancersApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    node_balancer_id = 56 # int | The ID of the NodeBalancer to access.
    node_balancer = openapi_client.NodeBalancer() # NodeBalancer | The information to update.

    try:
        # Update a NodeBalancer
        api_response = api_instance.put_node_balancer(api_version, node_balancer_id, node_balancer)
        print("The response of NodeBalancersApi->put_node_balancer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeBalancersApi->put_node_balancer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **node_balancer_id** | **int**| The ID of the NodeBalancer to access. | 
 **node_balancer** | [**NodeBalancer**](NodeBalancer.md)| The information to update. | 

### Return type

[**NodeBalancer**](NodeBalancer.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | NodeBalancer updated successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_node_balancer_config**
> GetNodeBalancerConfigs200ResponseDataInner put_node_balancer_config(api_version, node_balancer_id, config_id, get_node_balancer_configs200_response_data_inner)

Update a config

Updates the configuration for a single port on a NodeBalancer.   <<LB>>  ---   - __CLI__.      ```     linode-cli nodebalancers config-update \\   12345 4567 \\   --port 443 \\   --protocol https \\   --algorithm roundrobin \\   --stickiness http_cookie \\   --check http_body \\   --check_interval 90 \\   --check_timeout 10 \\   --check_attempts 3 \\   --check_path \"/test\" \\   --check_body \"it works\" \\   --check_passive true \\   --proxy_protocol \"none\" \\   --ssl_cert \"-----BEGIN CERTIFICATE-----               CERTIFICATE_INFORMATION               -----END CERTIFICATE-----\" \\   --ssl_key \"-----BEGIN PRIVATE KEY-----              PRIVATE_KEY_INFORMATION              -----END PRIVATE KEY-----\" \\   --cipher_suite recommended     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     nodebalancers:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_node_balancer_configs200_response_data_inner import GetNodeBalancerConfigs200ResponseDataInner
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
    api_instance = openapi_client.NodeBalancersApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    node_balancer_id = 56 # int | The ID of the NodeBalancer to access.
    config_id = 56 # int | The ID of the Config to access.
    get_node_balancer_configs200_response_data_inner = openapi_client.GetNodeBalancerConfigs200ResponseDataInner() # GetNodeBalancerConfigs200ResponseDataInner | The fields to update.

    try:
        # Update a config
        api_response = api_instance.put_node_balancer_config(api_version, node_balancer_id, config_id, get_node_balancer_configs200_response_data_inner)
        print("The response of NodeBalancersApi->put_node_balancer_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeBalancersApi->put_node_balancer_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **node_balancer_id** | **int**| The ID of the NodeBalancer to access. | 
 **config_id** | **int**| The ID of the Config to access. | 
 **get_node_balancer_configs200_response_data_inner** | [**GetNodeBalancerConfigs200ResponseDataInner**](GetNodeBalancerConfigs200ResponseDataInner.md)| The fields to update. | 

### Return type

[**GetNodeBalancerConfigs200ResponseDataInner**](GetNodeBalancerConfigs200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Config updated successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_node_balancer_node**
> PostNodeBalancerRequestConfigsInnerNodesInner put_node_balancer_node(api_version, node_balancer_id, config_id, node_id, post_node_balancer_request_configs_inner_nodes_inner)

Update a node

Updates information about a Node, a backend for this NodeBalancer's configured port.   <<LB>>  ---   - __CLI__.      ```     linode-cli nodebalancers node-update \\   12345 4567 54321 \\   --address 192.168.210.120:80 \\   --label node54321 \\   --weight 50 \\   --mode accept     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     nodebalancers:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.post_node_balancer_request_configs_inner_nodes_inner import PostNodeBalancerRequestConfigsInnerNodesInner
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
    api_instance = openapi_client.NodeBalancersApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    node_balancer_id = 56 # int | The ID of the NodeBalancer to access.
    config_id = 56 # int | The ID of the Config to access.
    node_id = 'node_id_example' # str | The ID of the Node to access.
    post_node_balancer_request_configs_inner_nodes_inner = openapi_client.PostNodeBalancerRequestConfigsInnerNodesInner() # PostNodeBalancerRequestConfigsInnerNodesInner | The fields to update.

    try:
        # Update a node
        api_response = api_instance.put_node_balancer_node(api_version, node_balancer_id, config_id, node_id, post_node_balancer_request_configs_inner_nodes_inner)
        print("The response of NodeBalancersApi->put_node_balancer_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeBalancersApi->put_node_balancer_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **node_balancer_id** | **int**| The ID of the NodeBalancer to access. | 
 **config_id** | **int**| The ID of the Config to access. | 
 **node_id** | **str**| The ID of the Node to access. | 
 **post_node_balancer_request_configs_inner_nodes_inner** | [**PostNodeBalancerRequestConfigsInnerNodesInner**](PostNodeBalancerRequestConfigsInnerNodesInner.md)| The fields to update. | 

### Return type

[**PostNodeBalancerRequestConfigsInnerNodesInner**](PostNodeBalancerRequestConfigsInnerNodesInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Node updated successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

