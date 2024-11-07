# openapi_client.PlacementGroupsApi

All URIs are relative to *https://api.linode.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_placement_group**](PlacementGroupsApi.md#delete_placement_group) | **DELETE** /{apiVersion}/placement/groups/{groupId} | Delete a placement group
[**get_placement_group**](PlacementGroupsApi.md#get_placement_group) | **GET** /{apiVersion}/placement/groups/{groupId} | Get a placement group
[**get_placement_groups**](PlacementGroupsApi.md#get_placement_groups) | **GET** /{apiVersion}/placement/groups | List placement groups
[**post_group_add_linode**](PlacementGroupsApi.md#post_group_add_linode) | **POST** /{apiVersion}/placement/groups/{groupId}/assign | Assign a placement group
[**post_group_unassign**](PlacementGroupsApi.md#post_group_unassign) | **POST** /{apiVersion}/placement/groups/{groupId}/unassign | Unassign a placement group
[**post_placement_group**](PlacementGroupsApi.md#post_placement_group) | **POST** /{apiVersion}/placement/groups | Create placement group
[**put_placement_group**](PlacementGroupsApi.md#put_placement_group) | **PUT** /{apiVersion}/placement/groups/{groupId} | Update a placement group


# **delete_placement_group**
> object delete_placement_group(api_version, group_id)

Delete a placement group

Deletes a placement group you have permission to `read_write`.  - Deleting a placement group can't be undone. - All compute instances need to be [removed](https://techdocs.akamai.com/linode-api/reference/post-group-unassign) before you can delete a placement group. - If your placement group is non-compliant, you can't delete it. You need to wait for our help to bring it [compliant](https://www.linode.com/docs/products/compute/compute-instances/guides/placement-groups/#non-compliance-precedence).   <<LB>>  ---   - __CLI__.      ```     linode-cli placement group-delete 528     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     linodes:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.PlacementGroupsApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    group_id = 56 # int | ID of the placement group to look up. Run the [List placement groups](https://techdocs.akamai.com/linode-api/reference/get-placement-groups) operation and store the `id` for the applicable placement group.

    try:
        # Delete a placement group
        api_response = api_instance.delete_placement_group(api_version, group_id)
        print("The response of PlacementGroupsApi->delete_placement_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlacementGroupsApi->delete_placement_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **group_id** | **int**| ID of the placement group to look up. Run the [List placement groups](https://techdocs.akamai.com/linode-api/reference/get-placement-groups) operation and store the &#x60;id&#x60; for the applicable placement group. | 

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

# **get_placement_group**
> GetPlacementGroups200ResponseDataInner get_placement_group(api_version, group_id)

Get a placement group

View a specific placement group by ID.   <<LB>>  ---   - __CLI__.      ```     linode-cli placement group-view 528     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     linodes:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_placement_groups200_response_data_inner import GetPlacementGroups200ResponseDataInner
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
    api_instance = openapi_client.PlacementGroupsApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    group_id = 56 # int | ID of the placement group to look up. Run the [List placement groups](https://techdocs.akamai.com/linode-api/reference/get-placement-groups) operation and store the `id` for the applicable placement group.

    try:
        # Get a placement group
        api_response = api_instance.get_placement_group(api_version, group_id)
        print("The response of PlacementGroupsApi->get_placement_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlacementGroupsApi->get_placement_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **group_id** | **int**| ID of the placement group to look up. Run the [List placement groups](https://techdocs.akamai.com/linode-api/reference/get-placement-groups) operation and store the &#x60;id&#x60; for the applicable placement group. | 

### Return type

[**GetPlacementGroups200ResponseDataInner**](GetPlacementGroups200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single placement group object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_placement_groups**
> GetPlacementGroups200Response get_placement_groups(api_version, page=page, page_size=page_size)

List placement groups

Returns a paginated list of placement groups you have permission to view.   <<LB>>  ---   - __CLI__.      ```     linode-cli placement groups-list     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     placement:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_placement_groups200_response import GetPlacementGroups200Response
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
    api_instance = openapi_client.PlacementGroupsApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    page = 1 # int | The page of a collection to return. (optional) (default to 1)
    page_size = 100 # int | The number of items to return per page. (optional) (default to 100)

    try:
        # List placement groups
        api_response = api_instance.get_placement_groups(api_version, page=page, page_size=page_size)
        print("The response of PlacementGroupsApi->get_placement_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlacementGroupsApi->get_placement_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **page** | **int**| The page of a collection to return. | [optional] [default to 1]
 **page_size** | **int**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetPlacementGroups200Response**](GetPlacementGroups200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an array of all placement groups on your Account. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_group_add_linode**
> PostPlacementGroup200Response post_group_add_linode(api_version, group_id, post_group_add_linode_request)

Assign a placement group

Add one or more compute instances to your placement group. Check out our [example API workflow](https://www.linode.com/docs/products/compute/compute-instances/guides/placement-groups/#create-a-placement-group) to create a placement group and add compute instances.   <<LB>>  ---   - __CLI__.      ```     linode-cli placement assign-linode 528 \\   --linodes 123 456 \\   --non-compliant true     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     linodes:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.post_group_add_linode_request import PostGroupAddLinodeRequest
from openapi_client.models.post_placement_group200_response import PostPlacementGroup200Response
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
    api_instance = openapi_client.PlacementGroupsApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    group_id = 56 # int | ID of the placement group to look up. Run the [List placement groups](https://techdocs.akamai.com/linode-api/reference/get-placement-groups) operation and store the `id` for the applicable placement group.
    post_group_add_linode_request = openapi_client.PostGroupAddLinodeRequest() # PostGroupAddLinodeRequest | The compute instances you want to add to your placement group.

    try:
        # Assign a placement group
        api_response = api_instance.post_group_add_linode(api_version, group_id, post_group_add_linode_request)
        print("The response of PlacementGroupsApi->post_group_add_linode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlacementGroupsApi->post_group_add_linode: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **group_id** | **int**| ID of the placement group to look up. Run the [List placement groups](https://techdocs.akamai.com/linode-api/reference/get-placement-groups) operation and store the &#x60;id&#x60; for the applicable placement group. | 
 **post_group_add_linode_request** | [**PostGroupAddLinodeRequest**](PostGroupAddLinodeRequest.md)| The compute instances you want to add to your placement group. | 

### Return type

[**PostPlacementGroup200Response**](PostPlacementGroup200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The compute instance was added successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_group_unassign**
> PostPlacementGroup200Response post_group_unassign(api_version, group_id, post_group_add_linode_request)

Unassign a placement group

Remove one or more compute instances from your placement group.   <<LB>>  ---   - __CLI__.      ```     linode-cli placement unassign-linode 528 \\   --linode 123 456     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     linodes:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.post_group_add_linode_request import PostGroupAddLinodeRequest
from openapi_client.models.post_placement_group200_response import PostPlacementGroup200Response
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
    api_instance = openapi_client.PlacementGroupsApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    group_id = 56 # int | ID of the placement group to look up. Run the [List placement groups](https://techdocs.akamai.com/linode-api/reference/get-placement-groups) operation and store the `id` for the applicable placement group.
    post_group_add_linode_request = openapi_client.PostGroupAddLinodeRequest() # PostGroupAddLinodeRequest | The compute instances you want to remove from your placement group.

    try:
        # Unassign a placement group
        api_response = api_instance.post_group_unassign(api_version, group_id, post_group_add_linode_request)
        print("The response of PlacementGroupsApi->post_group_unassign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlacementGroupsApi->post_group_unassign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **group_id** | **int**| ID of the placement group to look up. Run the [List placement groups](https://techdocs.akamai.com/linode-api/reference/get-placement-groups) operation and store the &#x60;id&#x60; for the applicable placement group. | 
 **post_group_add_linode_request** | [**PostGroupAddLinodeRequest**](PostGroupAddLinodeRequest.md)| The compute instances you want to remove from your placement group. | 

### Return type

[**PostPlacementGroup200Response**](PostPlacementGroup200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The compute instance was removed successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_placement_group**
> PostPlacementGroup200Response post_placement_group(api_version, post_placement_group_request)

Create placement group

Creates a placement group on your account. Placement groups disperse your compute instances across physical machines (hosts) in one of our compute regions. Depending on your workload requirements, you may need your compute instances to follow specific strategies:  - __Grouped together__. You may want them placed close together to reduce latency between compute instances that are used for an application or workload. - __Spread apart__. You may want to disperse them across several hosts to support high availability, for example when required for failover.  <<LB>>  > 📘 > > - For this request to complete successfully, your user needs to have the `add_placement` grant. > - We offer an [example API workflow](https://www.linode.com/docs/products/compute/compute-instances/guides/placement-groups/#create-a-placement-group) you can follow to create a placement group.   <<LB>>  ---   - __CLI__.      ```     linode-cli placement group-create \\   --label PG_Miami_failover \\   --region us-mia \\   --placement_group_type \"anti-affinity:local\" \\   --placement_group_policy strict     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     linodes:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.post_placement_group200_response import PostPlacementGroup200Response
from openapi_client.models.post_placement_group_request import PostPlacementGroupRequest
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
    api_instance = openapi_client.PlacementGroupsApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    post_placement_group_request = openapi_client.PostPlacementGroupRequest() # PostPlacementGroupRequest | The requested initial state of the new placement group.

    try:
        # Create placement group
        api_response = api_instance.post_placement_group(api_version, post_placement_group_request)
        print("The response of PlacementGroupsApi->post_placement_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlacementGroupsApi->post_placement_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **post_placement_group_request** | [**PostPlacementGroupRequest**](PostPlacementGroupRequest.md)| The requested initial state of the new placement group. | 

### Return type

[**PostPlacementGroup200Response**](PostPlacementGroup200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A new placement group is being created. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_placement_group**
> PostPlacementGroup200Response put_placement_group(api_version, group_id, put_placement_group_request)

Update a placement group

Change the `label` for a specific placement group. This is the only value you can update. However, you can [add](https://techdocs.akamai.com/linode-api/reference/post-group-add-linode) more compute instances or [remove](https://techdocs.akamai.com/linode-api/reference/post-group-unassign) existing ones.   <<LB>>  ---   - __CLI__.      ```     linode-cli placement group-update 528 \\   --label PG_Miami_failover_update     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     linodes:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.post_placement_group200_response import PostPlacementGroup200Response
from openapi_client.models.put_placement_group_request import PutPlacementGroupRequest
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
    api_instance = openapi_client.PlacementGroupsApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    group_id = 56 # int | ID of the placement group to look up. Run the [List placement groups](https://techdocs.akamai.com/linode-api/reference/get-placement-groups) operation and store the `id` for the applicable placement group.
    put_placement_group_request = openapi_client.PutPlacementGroupRequest() # PutPlacementGroupRequest | Include the `label` parameter to update the name of your placement group.

    try:
        # Update a placement group
        api_response = api_instance.put_placement_group(api_version, group_id, put_placement_group_request)
        print("The response of PlacementGroupsApi->put_placement_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlacementGroupsApi->put_placement_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **group_id** | **int**| ID of the placement group to look up. Run the [List placement groups](https://techdocs.akamai.com/linode-api/reference/get-placement-groups) operation and store the &#x60;id&#x60; for the applicable placement group. | 
 **put_placement_group_request** | [**PutPlacementGroupRequest**](PutPlacementGroupRequest.md)| Include the &#x60;label&#x60; parameter to update the name of your placement group. | 

### Return type

[**PostPlacementGroup200Response**](PostPlacementGroup200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated placement group. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

