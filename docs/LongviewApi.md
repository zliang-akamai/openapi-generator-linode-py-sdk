# openapi_client.LongviewApi

All URIs are relative to *https://api.linode.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_longview_client**](LongviewApi.md#delete_longview_client) | **DELETE** /{apiVersion}/longview/clients/{clientId} | Delete a Longview client
[**get_longview_client**](LongviewApi.md#get_longview_client) | **GET** /{apiVersion}/longview/clients/{clientId} | Get a Longview client
[**get_longview_clients**](LongviewApi.md#get_longview_clients) | **GET** /{apiVersion}/longview/clients | List Longview clients
[**get_longview_plan**](LongviewApi.md#get_longview_plan) | **GET** /{apiVersion}/longview/plan | Get a Longview plan
[**get_longview_subscription**](LongviewApi.md#get_longview_subscription) | **GET** /{apiVersion}/longview/subscriptions/{subscriptionId} | Get a Longview subscription
[**get_longview_subscriptions**](LongviewApi.md#get_longview_subscriptions) | **GET** /{apiVersion}/longview/subscriptions | List Longview subscriptions
[**get_longview_types**](LongviewApi.md#get_longview_types) | **GET** /{apiVersion}/longview/types | List Longview types
[**post_longview_client**](LongviewApi.md#post_longview_client) | **POST** /{apiVersion}/longview/clients | Create a Longview client
[**put_longview_client**](LongviewApi.md#put_longview_client) | **PUT** /{apiVersion}/longview/clients/{clientId} | Update a Longview client
[**put_longview_plan**](LongviewApi.md#put_longview_plan) | **PUT** /{apiVersion}/longview/plan | Update a Longview plan


# **delete_longview_client**
> object delete_longview_client(api_version, client_id)

Delete a Longview client

Deletes a Longview Client from your Account.  __All information stored for this client will be lost.__  This _does not_ uninstall the Longview Client application for your Linode - you must do that manually.   <<LB>>  ---   - __CLI__.      ```     linode-cli longview delete 789     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     longview:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.LongviewApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    client_id = 56 # int | The Longview Client ID to access.

    try:
        # Delete a Longview client
        api_response = api_instance.delete_longview_client(api_version, client_id)
        print("The response of LongviewApi->delete_longview_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LongviewApi->delete_longview_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **client_id** | **int**| The Longview Client ID to access. | 

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
**200** | Longview Client deleted successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_longview_client**
> GetLongviewClients200ResponseDataInner get_longview_client(api_version, client_id)

Get a Longview client

Returns a single Longview Client you can access.   <<LB>>  ---   - __CLI__.      ```     linode-cli longview view 789     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     longview:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_longview_clients200_response_data_inner import GetLongviewClients200ResponseDataInner
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
    api_instance = openapi_client.LongviewApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    client_id = 56 # int | The Longview Client ID to access.

    try:
        # Get a Longview client
        api_response = api_instance.get_longview_client(api_version, client_id)
        print("The response of LongviewApi->get_longview_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LongviewApi->get_longview_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **client_id** | **int**| The Longview Client ID to access. | 

### Return type

[**GetLongviewClients200ResponseDataInner**](GetLongviewClients200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Longview Client. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_longview_clients**
> GetLongviewClients200Response get_longview_clients(api_version, page=page, page_size=page_size)

List Longview clients

Returns a paginated list of Longview Clients you have access to. Longview Client is used to monitor stats on your Linode with the help of the Longview Client application.   <<LB>>  ---   - __CLI__.      ```     linode-cli longview list     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     longview:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_longview_clients200_response import GetLongviewClients200Response
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
    api_instance = openapi_client.LongviewApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    page = 1 # int | The page of a collection to return. (optional) (default to 1)
    page_size = 100 # int | The number of items to return per page. (optional) (default to 100)

    try:
        # List Longview clients
        api_response = api_instance.get_longview_clients(api_version, page=page, page_size=page_size)
        print("The response of LongviewApi->get_longview_clients:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LongviewApi->get_longview_clients: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **page** | **int**| The page of a collection to return. | [optional] [default to 1]
 **page_size** | **int**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetLongviewClients200Response**](GetLongviewClients200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of Longview Clients. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_longview_plan**
> GetLongviewPlan200Response get_longview_plan(api_version)

Get a Longview plan

Get the details of your current Longview plan. This returns a `LongviewSubscription` object for your current Longview Pro plan, or an empty set `{}` if your current plan is Longview Free.  You must have at least one of the following `global` [List a user's grants](https://techdocs.akamai.com/linode-api/reference/get-user-grants) in order to run this operation:    - `\"account_access\": read_write`   - `\"account_access\": read_only`   - `\"longview_subscription\": true`   - `\"add_longview\": true`  To update your subscription plan, send a request to [Update a Longview plan](https://techdocs.akamai.com/linode-api/reference/put-longview-plan).   <<LB>>  ---   - __CLI__.      ```     linode-cli longview plan-view     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     longview:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_longview_plan200_response import GetLongviewPlan200Response
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
    api_instance = openapi_client.LongviewApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)

    try:
        # Get a Longview plan
        api_response = api_instance.get_longview_plan(api_version)
        print("The response of LongviewApi->get_longview_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LongviewApi->get_longview_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]

### Return type

[**GetLongviewPlan200Response**](GetLongviewPlan200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Longview plan details for this account. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_longview_subscription**
> GetLongviewPlan200Response get_longview_subscription(api_version, subscription_id)

Get a Longview subscription

Get the Longview plan details as a single `LongviewSubscription` object for the provided subscription ID. This is a public endpoint and requires no authentication.   <<LB>>  ---   - __CLI__.      ```     linode-cli longview subscription-view     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)

### Example


```python
import openapi_client
from openapi_client.models.get_longview_plan200_response import GetLongviewPlan200Response
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
    api_instance = openapi_client.LongviewApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    subscription_id = 'subscription_id_example' # str | The Longview Subscription to look up.

    try:
        # Get a Longview subscription
        api_response = api_instance.get_longview_subscription(api_version, subscription_id)
        print("The response of LongviewApi->get_longview_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LongviewApi->get_longview_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **subscription_id** | **str**| The Longview Subscription to look up. | 

### Return type

[**GetLongviewPlan200Response**](GetLongviewPlan200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Longview Subscription details. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_longview_subscriptions**
> GetLongviewSubscriptions200Response get_longview_subscriptions(api_version, page=page, page_size=page_size)

List Longview subscriptions

Returns a paginated list of available Longview Subscriptions. This is a public endpoint and requires no authentication.   <<LB>>  ---   - __CLI__.      ```     linode-cli longview subscriptions-list     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)

### Example


```python
import openapi_client
from openapi_client.models.get_longview_subscriptions200_response import GetLongviewSubscriptions200Response
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
    api_instance = openapi_client.LongviewApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    page = 1 # int | The page of a collection to return. (optional) (default to 1)
    page_size = 100 # int | The number of items to return per page. (optional) (default to 100)

    try:
        # List Longview subscriptions
        api_response = api_instance.get_longview_subscriptions(api_version, page=page, page_size=page_size)
        print("The response of LongviewApi->get_longview_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LongviewApi->get_longview_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **page** | **int**| The page of a collection to return. | [optional] [default to 1]
 **page_size** | **int**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetLongviewSubscriptions200Response**](GetLongviewSubscriptions200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of Longview Subscriptions. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_longview_types**
> GetLongviewTypes200Response get_longview_types(api_version)

List Longview types

Returns Longview types and prices, including any region-specific rates.   <<LB>>  ---   - __CLI__.      ```     linode-cli longview types     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)

### Example


```python
import openapi_client
from openapi_client.models.get_longview_types200_response import GetLongviewTypes200Response
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
    api_instance = openapi_client.LongviewApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)

    try:
        # List Longview types
        api_response = api_instance.get_longview_types(api_version)
        print("The response of LongviewApi->get_longview_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LongviewApi->get_longview_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]

### Return type

[**GetLongviewTypes200Response**](GetLongviewTypes200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of Longview types. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_longview_client**
> GetLongviewClients200ResponseDataInner post_longview_client(api_version, get_longview_clients200_response_data_inner)

Create a Longview client

Creates a Longview Client.  This Client will not begin monitoring the status of your server until you configure the Longview Client application on your Linode using the returning `install_code` and `api_key`.   <<LB>>  ---   - __CLI__.      ```     linode-cli longview create \\   --label client789     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     longview:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_longview_clients200_response_data_inner import GetLongviewClients200ResponseDataInner
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
    api_instance = openapi_client.LongviewApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    get_longview_clients200_response_data_inner = openapi_client.GetLongviewClients200ResponseDataInner() # GetLongviewClients200ResponseDataInner | Information about the LongviewClient to create.

    try:
        # Create a Longview client
        api_response = api_instance.post_longview_client(api_version, get_longview_clients200_response_data_inner)
        print("The response of LongviewApi->post_longview_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LongviewApi->post_longview_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **get_longview_clients200_response_data_inner** | [**GetLongviewClients200ResponseDataInner**](GetLongviewClients200ResponseDataInner.md)| Information about the LongviewClient to create. | 

### Return type

[**GetLongviewClients200ResponseDataInner**](GetLongviewClients200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Longview Client created successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_longview_client**
> GetLongviewClients200ResponseDataInner put_longview_client(api_version, client_id, get_longview_clients200_response_data_inner)

Update a Longview client

Updates a Longview Client.  This cannot update how it monitors your server; use the Longview Client application on your Linode for monitoring configuration.   <<LB>>  ---   - __CLI__.      ```     linode-cli longview update 789 \\   --label client789     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     longview:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_longview_clients200_response_data_inner import GetLongviewClients200ResponseDataInner
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
    api_instance = openapi_client.LongviewApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    client_id = 56 # int | The Longview Client ID to access.
    get_longview_clients200_response_data_inner = openapi_client.GetLongviewClients200ResponseDataInner() # GetLongviewClients200ResponseDataInner | The fields to update.

    try:
        # Update a Longview client
        api_response = api_instance.put_longview_client(api_version, client_id, get_longview_clients200_response_data_inner)
        print("The response of LongviewApi->put_longview_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LongviewApi->put_longview_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **client_id** | **int**| The Longview Client ID to access. | 
 **get_longview_clients200_response_data_inner** | [**GetLongviewClients200ResponseDataInner**](GetLongviewClients200ResponseDataInner.md)| The fields to update. | 

### Return type

[**GetLongviewClients200ResponseDataInner**](GetLongviewClients200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Longview Client updated successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_longview_plan**
> GetLongviewPlan200Response put_longview_plan(api_version, put_longview_plan_request)

Update a Longview plan

Update your Longview plan to that of the given subscription ID. This returns a `LongviewSubscription` object for the updated Longview Pro plan, or an empty set `{}` if the updated plan is Longview Free.  You must have `\"longview_subscription\": true` configured as a `global` [user grant](https://techdocs.akamai.com/linode-api/reference/get-user-grants) in order to run this operation.  You can send a request to the [List Longview subscriptions](https://techdocs.akamai.com/linode-api/reference/get-longview-subscriptions) operation to receive the details, including `id`'s, of each plan.   <<LB>>  ---   - __CLI__.      ```     linode-cli longview plan-update --longview_subscription longview-10     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     longview:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_longview_plan200_response import GetLongviewPlan200Response
from openapi_client.models.put_longview_plan_request import PutLongviewPlanRequest
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
    api_instance = openapi_client.LongviewApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    put_longview_plan_request = openapi_client.PutLongviewPlanRequest() # PutLongviewPlanRequest | Update your Longview subscription plan.

    try:
        # Update a Longview plan
        api_response = api_instance.put_longview_plan(api_version, put_longview_plan_request)
        print("The response of LongviewApi->put_longview_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LongviewApi->put_longview_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **put_longview_plan_request** | [**PutLongviewPlanRequest**](PutLongviewPlanRequest.md)| Update your Longview subscription plan. | 

### Return type

[**GetLongviewPlan200Response**](GetLongviewPlan200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Longview plan details for this account. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

