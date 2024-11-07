# openapi_client.LinodeKubernetesEngineLKEApi

All URIs are relative to *https://api.linode.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_lke_cluster**](LinodeKubernetesEngineLKEApi.md#delete_lke_cluster) | **DELETE** /{apiVersion}/lke/clusters/{clusterId} | Delete a Kubernetes cluster
[**delete_lke_cluster_acl**](LinodeKubernetesEngineLKEApi.md#delete_lke_cluster_acl) | **DELETE** /{apiVersion}/lke/clusters/{clusterId}/control_plane_acl | Delete the control plane access control list
[**delete_lke_cluster_kubeconfig**](LinodeKubernetesEngineLKEApi.md#delete_lke_cluster_kubeconfig) | **DELETE** /{apiVersion}/lke/clusters/{clusterId}/kubeconfig | Delete a Kubeconfig
[**delete_lke_cluster_node**](LinodeKubernetesEngineLKEApi.md#delete_lke_cluster_node) | **DELETE** /{apiVersion}/lke/clusters/{clusterId}/nodes/{nodeId} | Delete a node
[**delete_lke_node_pool**](LinodeKubernetesEngineLKEApi.md#delete_lke_node_pool) | **DELETE** /{apiVersion}/lke/clusters/{clusterId}/pools/{poolId} | Delete a node pool
[**delete_lke_service_token**](LinodeKubernetesEngineLKEApi.md#delete_lke_service_token) | **DELETE** /{apiVersion}/lke/clusters/{clusterId}/servicetoken | Delete a service token
[**get_lke_cluster**](LinodeKubernetesEngineLKEApi.md#get_lke_cluster) | **GET** /{apiVersion}/lke/clusters/{clusterId} | Get a Kubernetes cluster
[**get_lke_cluster_acl**](LinodeKubernetesEngineLKEApi.md#get_lke_cluster_acl) | **GET** /{apiVersion}/lke/clusters/{clusterId}/control_plane_acl | Get the control plane access control list
[**get_lke_cluster_api_endpoints**](LinodeKubernetesEngineLKEApi.md#get_lke_cluster_api_endpoints) | **GET** /{apiVersion}/lke/clusters/{clusterId}/api-endpoints | List Kubernetes API endpoints
[**get_lke_cluster_dashboard**](LinodeKubernetesEngineLKEApi.md#get_lke_cluster_dashboard) | **GET** /{apiVersion}/lke/clusters/{clusterId}/dashboard | Get a Kubernetes cluster dashboard URL
[**get_lke_cluster_kubeconfig**](LinodeKubernetesEngineLKEApi.md#get_lke_cluster_kubeconfig) | **GET** /{apiVersion}/lke/clusters/{clusterId}/kubeconfig | Get a Kubeconfig
[**get_lke_cluster_node**](LinodeKubernetesEngineLKEApi.md#get_lke_cluster_node) | **GET** /{apiVersion}/lke/clusters/{clusterId}/nodes/{nodeId} | Get a node
[**get_lke_cluster_pools**](LinodeKubernetesEngineLKEApi.md#get_lke_cluster_pools) | **GET** /{apiVersion}/lke/clusters/{clusterId}/pools | List node pools
[**get_lke_clusters**](LinodeKubernetesEngineLKEApi.md#get_lke_clusters) | **GET** /{apiVersion}/lke/clusters | List Kubernetes clusters
[**get_lke_node_pool**](LinodeKubernetesEngineLKEApi.md#get_lke_node_pool) | **GET** /{apiVersion}/lke/clusters/{clusterId}/pools/{poolId} | Get a node pool
[**get_lke_types**](LinodeKubernetesEngineLKEApi.md#get_lke_types) | **GET** /{apiVersion}/lke/types | List Kubernetes types
[**get_lke_version**](LinodeKubernetesEngineLKEApi.md#get_lke_version) | **GET** /{apiVersion}/lke/versions/{version} | Get a Kubernetes version
[**get_lke_versions**](LinodeKubernetesEngineLKEApi.md#get_lke_versions) | **GET** /{apiVersion}/lke/versions | List Kubernetes versions
[**post_lke_cluster**](LinodeKubernetesEngineLKEApi.md#post_lke_cluster) | **POST** /{apiVersion}/lke/clusters | Create a Kubernetes cluster
[**post_lke_cluster_node_recycle**](LinodeKubernetesEngineLKEApi.md#post_lke_cluster_node_recycle) | **POST** /{apiVersion}/lke/clusters/{clusterId}/nodes/{nodeId}/recycle | Recycle a node
[**post_lke_cluster_pool_recycle**](LinodeKubernetesEngineLKEApi.md#post_lke_cluster_pool_recycle) | **POST** /{apiVersion}/lke/clusters/{clusterId}/pools/{poolId}/recycle | Recycle a node pool
[**post_lke_cluster_pools**](LinodeKubernetesEngineLKEApi.md#post_lke_cluster_pools) | **POST** /{apiVersion}/lke/clusters/{clusterId}/pools | Create a node pool
[**post_lke_cluster_recycle**](LinodeKubernetesEngineLKEApi.md#post_lke_cluster_recycle) | **POST** /{apiVersion}/lke/clusters/{clusterId}/recycle | Recycle cluster nodes
[**post_lke_cluster_regenerate**](LinodeKubernetesEngineLKEApi.md#post_lke_cluster_regenerate) | **POST** /{apiVersion}/lke/clusters/{clusterId}/regenerate | Regenerate a Kubernetes cluster
[**put_lke_cluster**](LinodeKubernetesEngineLKEApi.md#put_lke_cluster) | **PUT** /{apiVersion}/lke/clusters/{clusterId} | Update a Kubernetes cluster
[**put_lke_cluster_acl**](LinodeKubernetesEngineLKEApi.md#put_lke_cluster_acl) | **PUT** /{apiVersion}/lke/clusters/{clusterId}/control_plane_acl | Update the control plane access control list
[**put_lke_node_pool**](LinodeKubernetesEngineLKEApi.md#put_lke_node_pool) | **PUT** /{apiVersion}/lke/clusters/{clusterId}/pools/{poolId} | Update a node pool


# **delete_lke_cluster**
> object delete_lke_cluster(api_version, cluster_id)

Delete a Kubernetes cluster

Deletes a Cluster you have permission to `read_write`.  __Deleting a Cluster is a destructive action and cannot be undone.__  Deleting a Cluster:  - Deletes all Linodes in all pools within this Kubernetes cluster - Deletes all supporting Kubernetes services for this Kubernetes cluster (API server, etcd, etc) - Deletes all NodeBalancers created by this Kubernetes cluster - Does not delete any of the volumes created by this Kubernetes cluster   <<LB>>  ---   - __CLI__.      ```     linode-cli lke cluster-delete 12345     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     lke:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.LinodeKubernetesEngineLKEApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    cluster_id = 56 # int | ID of the Kubernetes cluster to look up.

    try:
        # Delete a Kubernetes cluster
        api_response = api_instance.delete_lke_cluster(api_version, cluster_id)
        print("The response of LinodeKubernetesEngineLKEApi->delete_lke_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinodeKubernetesEngineLKEApi->delete_lke_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **cluster_id** | **int**| ID of the Kubernetes cluster to look up. | 

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
**200** | Delete successful. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_lke_cluster_acl**
> object delete_lke_cluster_acl(api_version, cluster_id)

Delete the control plane access control list

Disable control plane access controls and deletes all rules. This has the same effect as calling `PUT` with an acl json map value of `{“enabled” : false}`. __Note__: control plane ACLs may not currently be available to all users.   <<LB>>  ---   - __CLI__.      ```     linode-cli lke cluster-acl-delete 12345     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     lke:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.LinodeKubernetesEngineLKEApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    cluster_id = 56 # int | ID of the Kubernetes cluster to look up.

    try:
        # Delete the control plane access control list
        api_response = api_instance.delete_lke_cluster_acl(api_version, cluster_id)
        print("The response of LinodeKubernetesEngineLKEApi->delete_lke_cluster_acl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinodeKubernetesEngineLKEApi->delete_lke_cluster_acl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **cluster_id** | **int**| ID of the Kubernetes cluster to look up. | 

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
**200** | Delete successful. |  -  |
**400** | If the cluster was not created or updated to enable the ACL feature, this request returns a 400 (Bad Request) error with an appropriate message, such as &#x60;Cluster does not support Control Plane ACL&#x60;. |  -  |
**404** | If the cluster does not exist, this request returns a 404 (Not Found) error. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_lke_cluster_kubeconfig**
> object delete_lke_cluster_kubeconfig(api_version, cluster_id)

Delete a Kubeconfig

Delete and regenerate the Kubeconfig file for a Cluster.   <<LB>>  ---   - __CLI__.      ```     linode-cli lke kubeconfig-delete 12345     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     lke:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.LinodeKubernetesEngineLKEApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    cluster_id = 56 # int | ID of the Kubernetes cluster to look up.

    try:
        # Delete a Kubeconfig
        api_response = api_instance.delete_lke_cluster_kubeconfig(api_version, cluster_id)
        print("The response of LinodeKubernetesEngineLKEApi->delete_lke_cluster_kubeconfig:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinodeKubernetesEngineLKEApi->delete_lke_cluster_kubeconfig: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **cluster_id** | **int**| ID of the Kubernetes cluster to look up. | 

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
**200** | Kubeconfig file deleted and regenerated successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_lke_cluster_node**
> object delete_lke_cluster_node(api_version, cluster_id, node_id)

Delete a node

Deletes a specific Node from a Node Pool.  __Deleting a Node is a destructive action and cannot be undone.__  Deleting a Node will reduce the size of the Node Pool it belongs to.   <<LB>>  ---   - __CLI__.      ```     linode-cli lke node-delete 12345 12345-6aa78910bc     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     lke:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.LinodeKubernetesEngineLKEApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    cluster_id = 56 # int | ID of the Kubernetes cluster containing the Node.
    node_id = 'node_id_example' # str | The ID of the Node to access.

    try:
        # Delete a node
        api_response = api_instance.delete_lke_cluster_node(api_version, cluster_id, node_id)
        print("The response of LinodeKubernetesEngineLKEApi->delete_lke_cluster_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinodeKubernetesEngineLKEApi->delete_lke_cluster_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **cluster_id** | **int**| ID of the Kubernetes cluster containing the Node. | 
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
**200** | Delete successful. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_lke_node_pool**
> object delete_lke_node_pool(api_version, cluster_id, pool_id)

Delete a node pool

Delete a specific Node Pool from a Kubernetes cluster.  __Deleting a Node Pool is a destructive action and cannot be undone.__  Deleting a Node Pool will delete all Linodes within that Pool.   <<LB>>  ---   - __CLI__.      ```     linode-cli lke pool-delete 12345 456     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     lke:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.LinodeKubernetesEngineLKEApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    cluster_id = 56 # int | ID of the Kubernetes cluster to look up.
    pool_id = 56 # int | ID of the Pool to look up.

    try:
        # Delete a node pool
        api_response = api_instance.delete_lke_node_pool(api_version, cluster_id, pool_id)
        print("The response of LinodeKubernetesEngineLKEApi->delete_lke_node_pool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinodeKubernetesEngineLKEApi->delete_lke_node_pool: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **cluster_id** | **int**| ID of the Kubernetes cluster to look up. | 
 **pool_id** | **int**| ID of the Pool to look up. | 

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
**200** | Delete successful. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_lke_service_token**
> object delete_lke_service_token(api_version, cluster_id)

Delete a service token

Delete and regenerate the service account token for a Cluster.  __Note__. When regenerating a service account token, the Cluster's control plane components and Linode CSI drivers are also restarted and configured with the new token. High Availability Clusters should not experience any disruption, while standard Clusters may experience brief control plane downtime while components are restarted.   <<LB>>  ---   - __CLI__.      ```     linode-cli lke service-token-delete 12345     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     lke:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.LinodeKubernetesEngineLKEApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    cluster_id = 56 # int | ID of the target Kubernetes cluster.

    try:
        # Delete a service token
        api_response = api_instance.delete_lke_service_token(api_version, cluster_id)
        print("The response of LinodeKubernetesEngineLKEApi->delete_lke_service_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinodeKubernetesEngineLKEApi->delete_lke_service_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **cluster_id** | **int**| ID of the target Kubernetes cluster. | 

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
**200** | Service token deleted and regenerated successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lke_cluster**
> GetLkeClusters200ResponseDataInner get_lke_cluster(api_version, cluster_id)

Get a Kubernetes cluster

Get a specific Cluster by ID.   <<LB>>  ---   - __CLI__.      ```     linode-cli lke cluster-view 12345     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     lke:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_lke_clusters200_response_data_inner import GetLkeClusters200ResponseDataInner
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
    api_instance = openapi_client.LinodeKubernetesEngineLKEApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    cluster_id = 56 # int | ID of the Kubernetes cluster to look up.

    try:
        # Get a Kubernetes cluster
        api_response = api_instance.get_lke_cluster(api_version, cluster_id)
        print("The response of LinodeKubernetesEngineLKEApi->get_lke_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinodeKubernetesEngineLKEApi->get_lke_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **cluster_id** | **int**| ID of the Kubernetes cluster to look up. | 

### Return type

[**GetLkeClusters200ResponseDataInner**](GetLkeClusters200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single Kubernetes cluster. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lke_cluster_acl**
> GetLkeClusterAcl200Response get_lke_cluster_acl(api_version, cluster_id)

Get the control plane access control list

Get a specific cluster's control plane access control List. __Note__: control plane ACLs may not currently be available to all users.   <<LB>>  ---   - __CLI__.      ```     linode-cli lke cluster-acl-view 12345     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     lke:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_lke_cluster_acl200_response import GetLkeClusterAcl200Response
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
    api_instance = openapi_client.LinodeKubernetesEngineLKEApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    cluster_id = 56 # int | ID of the Kubernetes cluster to look up.

    try:
        # Get the control plane access control list
        api_response = api_instance.get_lke_cluster_acl(api_version, cluster_id)
        print("The response of LinodeKubernetesEngineLKEApi->get_lke_cluster_acl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinodeKubernetesEngineLKEApi->get_lke_cluster_acl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **cluster_id** | **int**| ID of the Kubernetes cluster to look up. | 

### Return type

[**GetLkeClusterAcl200Response**](GetLkeClusterAcl200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single cluster&#39;s control plane access control list. The optional field &#x60;revision-id&#x60; provided will be reflected on GET response when (and only after) the ACL stanza is verified as enforced. |  -  |
**400** | If the cluster was not created or updated to enable the ACL feature, this request returns a 400 (Bad Request) error with an appropriate message, such as &#x60;Cluster does not support Control Plane ACL&#x60;. |  -  |
**404** | If the cluster does not exist, this request returns a 404 (Not Found) error. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lke_cluster_api_endpoints**
> GetLkeClusterApiEndpoints200Response get_lke_cluster_api_endpoints(api_version, cluster_id)

List Kubernetes API endpoints

List the Kubernetes API server endpoints for this cluster. Please note that it often takes 2-5 minutes before the endpoint is ready after first [creating a new cluster](https://techdocs.akamai.com/linode-api/reference/post-lke-cluster).   <<LB>>  ---   - __CLI__.      ```     linode-cli lke api-endpoints-list 12345     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     lke:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_lke_cluster_api_endpoints200_response import GetLkeClusterApiEndpoints200Response
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
    api_instance = openapi_client.LinodeKubernetesEngineLKEApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    cluster_id = 56 # int | ID of the Kubernetes cluster to look up.

    try:
        # List Kubernetes API endpoints
        api_response = api_instance.get_lke_cluster_api_endpoints(api_version, cluster_id)
        print("The response of LinodeKubernetesEngineLKEApi->get_lke_cluster_api_endpoints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinodeKubernetesEngineLKEApi->get_lke_cluster_api_endpoints: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **cluster_id** | **int**| ID of the Kubernetes cluster to look up. | 

### Return type

[**GetLkeClusterApiEndpoints200Response**](GetLkeClusterApiEndpoints200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the Kubernetes API server endpoints for this cluster. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lke_cluster_dashboard**
> GetLkeClusterDashboard200Response get_lke_cluster_dashboard(api_version, cluster_id)

Get a Kubernetes cluster dashboard URL

Get a [Kubernetes Dashboard](https://github.com/kubernetes/dashboard) access URL for this Cluster, which enables performance of administrative tasks through a web interface.  Dashboards are installed for Clusters by default.  To access the Cluster Dashboard login prompt, enter the URL in a web browser. Select either __Token__ or __Kubeconfig__ authentication, then select __Sign in__.  For additional guidance on using the Cluster Dashboard, see the [Navigating the Cluster Dashboard](https://www.linode.com/docs/guides/using-the-kubernetes-dashboard-on-lke/#navigating-the-cluster-dashboard) section of our guide on [Using the Kubernetes Dashboard on LKE](https://www.linode.com/docs/guides/using-the-kubernetes-dashboard-on-lke/).   <<LB>>  ---   - __CLI__.      ```     linode-cli lke cluster-dashboard-url 12345     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     lke:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_lke_cluster_dashboard200_response import GetLkeClusterDashboard200Response
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
    api_instance = openapi_client.LinodeKubernetesEngineLKEApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    cluster_id = 56 # int | ID of the Kubernetes cluster to look up.

    try:
        # Get a Kubernetes cluster dashboard URL
        api_response = api_instance.get_lke_cluster_dashboard(api_version, cluster_id)
        print("The response of LinodeKubernetesEngineLKEApi->get_lke_cluster_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinodeKubernetesEngineLKEApi->get_lke_cluster_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **cluster_id** | **int**| ID of the Kubernetes cluster to look up. | 

### Return type

[**GetLkeClusterDashboard200Response**](GetLkeClusterDashboard200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Kubernetes Cluster Dashboard URL. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lke_cluster_kubeconfig**
> GetLkeClusterKubeconfig200Response get_lke_cluster_kubeconfig(api_version, cluster_id)

Get a Kubeconfig

Get the Kubeconfig file for a Cluster. Please note that it often takes 2-5 minutes before the Kubeconfig file is ready after first [creating a new cluster](https://techdocs.akamai.com/linode-api/reference/post-lke-cluster).   <<LB>>  ---   - __CLI__.      ```     linode-cli lke kubeconfig-view 12345     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     lke:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_lke_cluster_kubeconfig200_response import GetLkeClusterKubeconfig200Response
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
    api_instance = openapi_client.LinodeKubernetesEngineLKEApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    cluster_id = 56 # int | ID of the Kubernetes cluster to look up.

    try:
        # Get a Kubeconfig
        api_response = api_instance.get_lke_cluster_kubeconfig(api_version, cluster_id)
        print("The response of LinodeKubernetesEngineLKEApi->get_lke_cluster_kubeconfig:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinodeKubernetesEngineLKEApi->get_lke_cluster_kubeconfig: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **cluster_id** | **int**| ID of the Kubernetes cluster to look up. | 

### Return type

[**GetLkeClusterKubeconfig200Response**](GetLkeClusterKubeconfig200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the Base64-encoded Kubeconfig file for this Kubernetes cluster. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lke_cluster_node**
> GetLkeClusterNode200Response get_lke_cluster_node(api_version, cluster_id, node_id)

Get a node

Returns the values for a specified node object.   <<LB>>  ---   - __CLI__.      ```     linode-cli lke node-view 123456 12345-6aa78910bc     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     lke:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_lke_cluster_node200_response import GetLkeClusterNode200Response
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
    api_instance = openapi_client.LinodeKubernetesEngineLKEApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    cluster_id = 56 # int | ID of the Kubernetes cluster containing the Node.
    node_id = 'node_id_example' # str | The ID of the Node to access.

    try:
        # Get a node
        api_response = api_instance.get_lke_cluster_node(api_version, cluster_id, node_id)
        print("The response of LinodeKubernetesEngineLKEApi->get_lke_cluster_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinodeKubernetesEngineLKEApi->get_lke_cluster_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **cluster_id** | **int**| ID of the Kubernetes cluster containing the Node. | 
 **node_id** | **str**| The ID of the Node to access. | 

### Return type

[**GetLkeClusterNode200Response**](GetLkeClusterNode200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the values of a node object in the form that it appears currently in the node pool array. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lke_cluster_pools**
> GetLkeClusterPools200Response get_lke_cluster_pools(api_version, cluster_id)

List node pools

Returns all active Node Pools on a Kubernetes cluster.   <<LB>>  ---   - __CLI__.      ```     linode-cli lke pools-list 12345     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     lke:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_lke_cluster_pools200_response import GetLkeClusterPools200Response
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
    api_instance = openapi_client.LinodeKubernetesEngineLKEApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    cluster_id = 56 # int | ID of the Kubernetes cluster to look up.

    try:
        # List node pools
        api_response = api_instance.get_lke_cluster_pools(api_version, cluster_id)
        print("The response of LinodeKubernetesEngineLKEApi->get_lke_cluster_pools:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinodeKubernetesEngineLKEApi->get_lke_cluster_pools: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **cluster_id** | **int**| ID of the Kubernetes cluster to look up. | 

### Return type

[**GetLkeClusterPools200Response**](GetLkeClusterPools200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an array of all Pools in this Kubernetes cluster. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lke_clusters**
> GetLkeClusters200Response get_lke_clusters(api_version)

List Kubernetes clusters

Lists current Kubernetes clusters available on your account.   <<LB>>  ---   - __CLI__.      ```     linode-cli lke clusters-list     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     lke:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_lke_clusters200_response import GetLkeClusters200Response
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
    api_instance = openapi_client.LinodeKubernetesEngineLKEApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)

    try:
        # List Kubernetes clusters
        api_response = api_instance.get_lke_clusters(api_version)
        print("The response of LinodeKubernetesEngineLKEApi->get_lke_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinodeKubernetesEngineLKEApi->get_lke_clusters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]

### Return type

[**GetLkeClusters200Response**](GetLkeClusters200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an array of all Kubernetes clusters on your Account. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lke_node_pool**
> GetLkeClusterPools200ResponseDataInner get_lke_node_pool(api_version, cluster_id, pool_id)

Get a node pool

Get a specific Node Pool by ID.   <<LB>>  ---   - __CLI__.      ```     linode-cli lke pool-view 12345 456     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     lke:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_lke_cluster_pools200_response_data_inner import GetLkeClusterPools200ResponseDataInner
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
    api_instance = openapi_client.LinodeKubernetesEngineLKEApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    cluster_id = 56 # int | ID of the Kubernetes cluster to look up.
    pool_id = 56 # int | ID of the Pool to look up.

    try:
        # Get a node pool
        api_response = api_instance.get_lke_node_pool(api_version, cluster_id, pool_id)
        print("The response of LinodeKubernetesEngineLKEApi->get_lke_node_pool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinodeKubernetesEngineLKEApi->get_lke_node_pool: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **cluster_id** | **int**| ID of the Kubernetes cluster to look up. | 
 **pool_id** | **int**| ID of the Pool to look up. | 

### Return type

[**GetLkeClusterPools200ResponseDataInner**](GetLkeClusterPools200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the requested Node Pool. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lke_types**
> GetLkeTypes200Response get_lke_types(api_version)

List Kubernetes types

Returns Kubernetes types and prices, including any region-specific rates.   <<LB>>  ---   - __CLI__.      ```     linode-cli lke types     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)

### Example


```python
import openapi_client
from openapi_client.models.get_lke_types200_response import GetLkeTypes200Response
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
    api_instance = openapi_client.LinodeKubernetesEngineLKEApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)

    try:
        # List Kubernetes types
        api_response = api_instance.get_lke_types(api_version)
        print("The response of LinodeKubernetesEngineLKEApi->get_lke_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinodeKubernetesEngineLKEApi->get_lke_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]

### Return type

[**GetLkeTypes200Response**](GetLkeTypes200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of Kubernetes types. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lke_version**
> GetLkeVersions200ResponseDataInner get_lke_version(api_version, version)

Get a Kubernetes version

View a Kubernetes version available for deployment to a Kubernetes cluster.   <<LB>>  ---   - __CLI__.      ```     linode-cli lke version-view 1.27     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     lke:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_lke_versions200_response_data_inner import GetLkeVersions200ResponseDataInner
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
    api_instance = openapi_client.LinodeKubernetesEngineLKEApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    version = 'version_example' # str | The LKE version to view.

    try:
        # Get a Kubernetes version
        api_response = api_instance.get_lke_version(api_version, version)
        print("The response of LinodeKubernetesEngineLKEApi->get_lke_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinodeKubernetesEngineLKEApi->get_lke_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **version** | **str**| The LKE version to view. | 

### Return type

[**GetLkeVersions200ResponseDataInner**](GetLkeVersions200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Kubernetes version object that is available for deployment to a Kubernetes cluster. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lke_versions**
> GetLkeVersions200Response get_lke_versions(api_version)

List Kubernetes versions

List the Kubernetes versions available for deployment to a Kubernetes cluster.   <<LB>>  ---   - __CLI__.      ```     linode-cli lke versions-list     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     lke:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_lke_versions200_response import GetLkeVersions200Response
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
    api_instance = openapi_client.LinodeKubernetesEngineLKEApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)

    try:
        # List Kubernetes versions
        api_response = api_instance.get_lke_versions(api_version)
        print("The response of LinodeKubernetesEngineLKEApi->get_lke_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinodeKubernetesEngineLKEApi->get_lke_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]

### Return type

[**GetLkeVersions200Response**](GetLkeVersions200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of Kubernetes versions available for deployment to a Kubernetes cluster. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_lke_cluster**
> PostLkeCluster200Response post_lke_cluster(api_version, post_lke_cluster_request=post_lke_cluster_request)

Create a Kubernetes cluster

Creates a Kubernetes cluster. The Kubernetes cluster will be created asynchronously. You can use the events system to determine when the Kubernetes cluster is ready to use. Please note that it often takes 2-5 minutes before the [Kubernetes API endpoints](https://techdocs.akamai.com/linode-api/reference/get-lke-cluster-api-endpoints) and the [Kubeconfig file](https://techdocs.akamai.com/linode-api/reference/get-lke-cluster-kubeconfig) for the new cluster are ready.   <<LB>>  ---   - __CLI__.      ```     linode-cli lke cluster-create \\   --label cluster12345 \\   --region us-central \\   --k8s_version 1.27 \\   --control_plane.high_availability true \\   --node_pools.type g6-standard-4 --node_pools.count 6 \\   --node_pools.type g6-standard-8 --node_pools.count 3 \\   --node_pools.autoscaler.enabled true \\   --node_pools.autoscaler.max 12 \\   --node_pools.autoscaler.min 3 \\   --tags ecomm     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     lke:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.post_lke_cluster200_response import PostLkeCluster200Response
from openapi_client.models.post_lke_cluster_request import PostLkeClusterRequest
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
    api_instance = openapi_client.LinodeKubernetesEngineLKEApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    post_lke_cluster_request = openapi_client.PostLkeClusterRequest() # PostLkeClusterRequest | Configuration for the Kubernetes cluster. (optional)

    try:
        # Create a Kubernetes cluster
        api_response = api_instance.post_lke_cluster(api_version, post_lke_cluster_request=post_lke_cluster_request)
        print("The response of LinodeKubernetesEngineLKEApi->post_lke_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinodeKubernetesEngineLKEApi->post_lke_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **post_lke_cluster_request** | [**PostLkeClusterRequest**](PostLkeClusterRequest.md)| Configuration for the Kubernetes cluster. | [optional] 

### Return type

[**PostLkeCluster200Response**](PostLkeCluster200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Kubernetes cluster creation has started. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_lke_cluster_node_recycle**
> object post_lke_cluster_node_recycle(api_version, cluster_id, node_id)

Recycle a node

Recycles an individual Node in the designated Kubernetes Cluster. The Node will be deleted and replaced with a new Linode, which may take a few minutes. Replacement Nodes are installed with the latest available patch for the Cluster's Kubernetes Version.  __Any local storage on deleted Linodes (such as `hostPath` and `emptyDir` volumes, or `local` PersistentVolumes) will be erased.__   <<LB>>  ---   - __CLI__.      ```     linode-cli lke node-recycle 12345 12345-6aa78910bc     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     lke:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.LinodeKubernetesEngineLKEApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    cluster_id = 56 # int | ID of the Kubernetes cluster containing the Node.
    node_id = 'node_id_example' # str | ID of the Node to be recycled.

    try:
        # Recycle a node
        api_response = api_instance.post_lke_cluster_node_recycle(api_version, cluster_id, node_id)
        print("The response of LinodeKubernetesEngineLKEApi->post_lke_cluster_node_recycle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinodeKubernetesEngineLKEApi->post_lke_cluster_node_recycle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **cluster_id** | **int**| ID of the Kubernetes cluster containing the Node. | 
 **node_id** | **str**| ID of the Node to be recycled. | 

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
**200** | Recycle request succeeded and is in progress. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_lke_cluster_pool_recycle**
> object post_lke_cluster_pool_recycle(api_version, cluster_id, pool_id)

Recycle a node pool

Recycles a Node Pool for the designated Kubernetes Cluster. All Linodes within the Node Pool will be deleted and replaced with new Linodes on a rolling basis, which may take several minutes. Replacement Nodes are installed with the latest available patch for the Cluster's Kubernetes Version.  __Any local storage on deleted Linodes (such as `hostPath` and `emptyDir` volumes, or `local` PersistentVolumes) will be erased.__   <<LB>>  ---   - __CLI__.      ```     linode-cli lke pool-recycle 12345 456     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     lke:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.LinodeKubernetesEngineLKEApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    cluster_id = 56 # int | ID of the Kubernetes cluster this Node Pool is attached to.
    pool_id = 56 # int | ID of the Node Pool to be recycled.

    try:
        # Recycle a node pool
        api_response = api_instance.post_lke_cluster_pool_recycle(api_version, cluster_id, pool_id)
        print("The response of LinodeKubernetesEngineLKEApi->post_lke_cluster_pool_recycle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinodeKubernetesEngineLKEApi->post_lke_cluster_pool_recycle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **cluster_id** | **int**| ID of the Kubernetes cluster this Node Pool is attached to. | 
 **pool_id** | **int**| ID of the Node Pool to be recycled. | 

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
**200** | Recycle request succeeded and is in progress. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_lke_cluster_pools**
> GetLkeClusterPools200ResponseDataInner post_lke_cluster_pools(api_version, cluster_id, post_lke_cluster_pools_request)

Create a node pool

Creates a new Node Pool for the designated Kubernetes cluster.   <<LB>>  ---   - __CLI__.      ```     linode-cli lke pool-create 12345 \\   --type g6-standard-4 \\   --count 6 \\   --tags example-tag \\   --autoscaler.enabled true \\   --autoscaler.max 12 \\   --autoscaler.min 3 \\   --labels.key \"example.com/my-app\" \\   --labels.value \"teams\" \\   --taints.effect \"NoSchedule\" \\   --taints.key \"example.com/my-app\" \\   --taints.value \"teamA\"     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     lke:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_lke_cluster_pools200_response_data_inner import GetLkeClusterPools200ResponseDataInner
from openapi_client.models.post_lke_cluster_pools_request import PostLkeClusterPoolsRequest
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
    api_instance = openapi_client.LinodeKubernetesEngineLKEApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    cluster_id = 56 # int | ID of the Kubernetes cluster to look up.
    post_lke_cluster_pools_request = openapi_client.PostLkeClusterPoolsRequest() # PostLkeClusterPoolsRequest | Configuration for the Node Pool.

    try:
        # Create a node pool
        api_response = api_instance.post_lke_cluster_pools(api_version, cluster_id, post_lke_cluster_pools_request)
        print("The response of LinodeKubernetesEngineLKEApi->post_lke_cluster_pools:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinodeKubernetesEngineLKEApi->post_lke_cluster_pools: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **cluster_id** | **int**| ID of the Kubernetes cluster to look up. | 
 **post_lke_cluster_pools_request** | [**PostLkeClusterPoolsRequest**](PostLkeClusterPoolsRequest.md)| Configuration for the Node Pool. | 

### Return type

[**GetLkeClusterPools200ResponseDataInner**](GetLkeClusterPools200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Node Pool has been created. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_lke_cluster_recycle**
> object post_lke_cluster_recycle(api_version, cluster_id)

Recycle cluster nodes

Recycles all nodes in all pools of a designated Kubernetes Cluster. All Linodes within the Cluster will be deleted and replaced with new Linodes on a rolling basis, which may take several minutes. Replacement Nodes are installed with the latest available patch version for the Cluster's current Kubernetes minor release.  __Any local storage on deleted Linodes (such as `hostPath` and `emptyDir` volumes, or `local` PersistentVolumes) will be erased.__   <<LB>>  ---   - __CLI__.      ```     linode-cli lke cluster-nodes-recycle 12345     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     lke:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.LinodeKubernetesEngineLKEApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    cluster_id = 56 # int | ID of the Kubernetes cluster which contains nodes to be recycled.

    try:
        # Recycle cluster nodes
        api_response = api_instance.post_lke_cluster_recycle(api_version, cluster_id)
        print("The response of LinodeKubernetesEngineLKEApi->post_lke_cluster_recycle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinodeKubernetesEngineLKEApi->post_lke_cluster_recycle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **cluster_id** | **int**| ID of the Kubernetes cluster which contains nodes to be recycled. | 

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
**200** | Recycle request succeeded and is in progress. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_lke_cluster_regenerate**
> object post_lke_cluster_regenerate(api_version, cluster_id, post_lke_cluster_regenerate_request=post_lke_cluster_regenerate_request)

Regenerate a Kubernetes cluster

Regenerate the Kubeconfig file and/or the service account token for a Cluster.  This is a helper operation that allows performing both the [Delete a Kubeconfig](https://techdocs.akamai.com/linode-api/reference/delete-lke-cluster-kubeconfig) and the [Delete a service token](https://techdocs.akamai.com/linode-api/reference/delete-lke-service-token) operations with a single request.  When using this operation, at least one of `kubeconfig` or `servicetoken` is required.  __Note__. When regenerating a service account token, the Cluster's control plane components and Linode CSI drivers are also restarted and configured with the new token. High Availability Clusters should not experience any disruption, while standard Clusters may experience brief control plane downtime while components are restarted.   <<LB>>  ---   - __CLI__.      ```     linode-cli lke regenerate 12345 \\     --kubeconfig true \\     --servicetoken true     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     lke:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.post_lke_cluster_regenerate_request import PostLkeClusterRegenerateRequest
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
    api_instance = openapi_client.LinodeKubernetesEngineLKEApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    cluster_id = 56 # int | ID of the target Kubernetes cluster.
    post_lke_cluster_regenerate_request = openapi_client.PostLkeClusterRegenerateRequest() # PostLkeClusterRegenerateRequest | The Kubernetes Cluster Regenerate request object. (optional)

    try:
        # Regenerate a Kubernetes cluster
        api_response = api_instance.post_lke_cluster_regenerate(api_version, cluster_id, post_lke_cluster_regenerate_request=post_lke_cluster_regenerate_request)
        print("The response of LinodeKubernetesEngineLKEApi->post_lke_cluster_regenerate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinodeKubernetesEngineLKEApi->post_lke_cluster_regenerate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **cluster_id** | **int**| ID of the target Kubernetes cluster. | 
 **post_lke_cluster_regenerate_request** | [**PostLkeClusterRegenerateRequest**](PostLkeClusterRegenerateRequest.md)| The Kubernetes Cluster Regenerate request object. | [optional] 

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
**200** | Regenerate request successful. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_lke_cluster**
> PostLkeCluster200Response put_lke_cluster(api_version, cluster_id, put_lke_cluster_request=put_lke_cluster_request)

Update a Kubernetes cluster

Updates a Kubernetes cluster.   <<LB>>  ---   - __CLI__.      ```     linode-cli lke cluster-update 12345 \\   --label lkecluster54321 \\   --control_plane.high_availability true \\   --k8s_version 1.27 \\   --tags ecomm \\   --tags blog \\   --tags prod \\   --tags monitoring     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     lke:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.post_lke_cluster200_response import PostLkeCluster200Response
from openapi_client.models.put_lke_cluster_request import PutLkeClusterRequest
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
    api_instance = openapi_client.LinodeKubernetesEngineLKEApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    cluster_id = 56 # int | ID of the Kubernetes cluster to look up.
    put_lke_cluster_request = openapi_client.PutLkeClusterRequest() # PutLkeClusterRequest | The fields to update the Kubernetes cluster. (optional)

    try:
        # Update a Kubernetes cluster
        api_response = api_instance.put_lke_cluster(api_version, cluster_id, put_lke_cluster_request=put_lke_cluster_request)
        print("The response of LinodeKubernetesEngineLKEApi->put_lke_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinodeKubernetesEngineLKEApi->put_lke_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **cluster_id** | **int**| ID of the Kubernetes cluster to look up. | 
 **put_lke_cluster_request** | [**PutLkeClusterRequest**](PutLkeClusterRequest.md)| The fields to update the Kubernetes cluster. | [optional] 

### Return type

[**PostLkeCluster200Response**](PostLkeCluster200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single Kubernetes cluster. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_lke_cluster_acl**
> GetLkeClusterAcl200Response put_lke_cluster_acl(api_version, cluster_id, put_lke_cluster_acl_request=put_lke_cluster_acl_request)

Update the control plane access control list

Updates a specific cluster's control plane access control list. __Note__: control plane ACLs may not currently be available to all users.   <<LB>>  ---   - __CLI__.      ```     linode-cli lke cluster-acl-update 12345 \\       --acl.enabled true \\       --acl.addresses.ipv4 \"203.0.113.1\" \\       --acl.addresses.ipv6 \"2001:db8:1234:abcd::/64\"     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     lke:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_lke_cluster_acl200_response import GetLkeClusterAcl200Response
from openapi_client.models.put_lke_cluster_acl_request import PutLkeClusterAclRequest
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
    api_instance = openapi_client.LinodeKubernetesEngineLKEApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    cluster_id = 56 # int | ID of the Kubernetes cluster to look up.
    put_lke_cluster_acl_request = openapi_client.PutLkeClusterAclRequest() # PutLkeClusterAclRequest | The fields to update the cluster. (optional)

    try:
        # Update the control plane access control list
        api_response = api_instance.put_lke_cluster_acl(api_version, cluster_id, put_lke_cluster_acl_request=put_lke_cluster_acl_request)
        print("The response of LinodeKubernetesEngineLKEApi->put_lke_cluster_acl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinodeKubernetesEngineLKEApi->put_lke_cluster_acl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **cluster_id** | **int**| ID of the Kubernetes cluster to look up. | 
 **put_lke_cluster_acl_request** | [**PutLkeClusterAclRequest**](PutLkeClusterAclRequest.md)| The fields to update the cluster. | [optional] 

### Return type

[**GetLkeClusterAcl200Response**](GetLkeClusterAcl200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single cluster&#39;s control plane access control list. The optional field &#x60;revision-id&#x60; provided will be reflected on GET response when (and only after) the ACL stanza is verified as enforced. |  -  |
**400** | If the cluster was not created or updated to enable the ACL feature, this request returns a 400 (Bad Request) error with an appropriate message, such as &#x60;Cluster does not support Control Plane ACL&#x60;. |  -  |
**404** | If the cluster does not exist, this request returns a 404 (Not Found) error. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_lke_node_pool**
> GetLkeClusterPools200ResponseDataInner put_lke_node_pool(api_version, cluster_id, pool_id, put_lke_node_pool_request=put_lke_node_pool_request)

Update a node pool

Updates a node pool's count, labels and taints, and autoscaler configuration.  Linodes are created or deleted to match changes to the Node Pool's count.  Specifying labels or taints on update overwrites any previous values, and updates existing nodes with the new values without a recycle.  __Any local storage on deleted Linodes (such as `hostPath` and `emptyDir` volumes, or `local` PersistentVolumes) will be erased.__   <<LB>>  ---   - __CLI__.      ```     linode-cli lke pool-update 12345 456 \\   --count 6 \\   --autoscaler.enabled true \\   --autoscaler.max 12 \\   --autoscaler.min 3 \\   --labels.key \"example.com/my-app\" \\   --labels.value \"teams\" \\   --taints.effect \"NoSchedule\" \\   --taints.key \"example.com/my-app\" \\   --taints.value \"teamA\"     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     lke:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_lke_cluster_pools200_response_data_inner import GetLkeClusterPools200ResponseDataInner
from openapi_client.models.put_lke_node_pool_request import PutLkeNodePoolRequest
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
    api_instance = openapi_client.LinodeKubernetesEngineLKEApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    cluster_id = 56 # int | ID of the Kubernetes cluster to look up.
    pool_id = 56 # int | ID of the Pool to look up.
    put_lke_node_pool_request = openapi_client.PutLkeNodePoolRequest() # PutLkeNodePoolRequest | The fields to update. (optional)

    try:
        # Update a node pool
        api_response = api_instance.put_lke_node_pool(api_version, cluster_id, pool_id, put_lke_node_pool_request=put_lke_node_pool_request)
        print("The response of LinodeKubernetesEngineLKEApi->put_lke_node_pool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinodeKubernetesEngineLKEApi->put_lke_node_pool: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **cluster_id** | **int**| ID of the Kubernetes cluster to look up. | 
 **pool_id** | **int**| ID of the Pool to look up. | 
 **put_lke_node_pool_request** | [**PutLkeNodePoolRequest**](PutLkeNodePoolRequest.md)| The fields to update. | [optional] 

### Return type

[**GetLkeClusterPools200ResponseDataInner**](GetLkeClusterPools200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Node Pool was successfully modified. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

