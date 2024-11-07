# openapi_client.LinodeStackScriptsApi

All URIs are relative to *https://api.linode.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_stack_script**](LinodeStackScriptsApi.md#delete_stack_script) | **DELETE** /{apiVersion}/linode/stackscripts/{stackscriptId} | Delete a StackScript
[**get_stack_script**](LinodeStackScriptsApi.md#get_stack_script) | **GET** /{apiVersion}/linode/stackscripts/{stackscriptId} | Get a StackScript
[**get_stack_scripts**](LinodeStackScriptsApi.md#get_stack_scripts) | **GET** /{apiVersion}/linode/stackscripts | List StackScripts
[**post_add_stack_script**](LinodeStackScriptsApi.md#post_add_stack_script) | **POST** /{apiVersion}/linode/stackscripts | Create a StackScript
[**put_stack_script**](LinodeStackScriptsApi.md#put_stack_script) | **PUT** /{apiVersion}/linode/stackscripts/{stackscriptId} | Update a StackScript


# **delete_stack_script**
> object delete_stack_script(api_version, stackscript_id)

Delete a StackScript

Deletes a private StackScript you have permission to `read_write`. You cannot delete a public StackScript.   <<LB>>  ---   - __CLI__.      ```     linode-cli stackscripts delete 10079     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     stackscripts:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.LinodeStackScriptsApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    stackscript_id = 'stackscript_id_example' # str | The ID of the StackScript to look up.

    try:
        # Delete a StackScript
        api_response = api_instance.delete_stack_script(api_version, stackscript_id)
        print("The response of LinodeStackScriptsApi->delete_stack_script:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinodeStackScriptsApi->delete_stack_script: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **stackscript_id** | **str**| The ID of the StackScript to look up. | 

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
**200** | StackScript was deleted. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stack_script**
> GetStackScripts200ResponseDataInner get_stack_script(api_version, stackscript_id)

Get a StackScript

Returns all of the information about a specified StackScript, including the contents of the script.   <<LB>>  ---   - __CLI__.      ```     linode-cli stackscripts view 10079     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     stackscripts:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_stack_scripts200_response_data_inner import GetStackScripts200ResponseDataInner
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
    api_instance = openapi_client.LinodeStackScriptsApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    stackscript_id = 'stackscript_id_example' # str | The ID of the StackScript to look up.

    try:
        # Get a StackScript
        api_response = api_instance.get_stack_script(api_version, stackscript_id)
        print("The response of LinodeStackScriptsApi->get_stack_script:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinodeStackScriptsApi->get_stack_script: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **stackscript_id** | **str**| The ID of the StackScript to look up. | 

### Return type

[**GetStackScripts200ResponseDataInner**](GetStackScripts200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single StackScript. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stack_scripts**
> GetStackScripts200Response get_stack_scripts(api_version, page=page, page_size=page_size)

List StackScripts

If the request is not authenticated, only public StackScripts are returned.  For more information on StackScripts, please read our [StackScripts documentation](https://www.linode.com/docs/products/tools/stackscripts/).   <<LB>>  ---   - __CLI__.      ```     linode-cli stackscripts list     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     stackscripts:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_stack_scripts200_response import GetStackScripts200Response
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
    api_instance = openapi_client.LinodeStackScriptsApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    page = 1 # int | The page of a collection to return. (optional) (default to 1)
    page_size = 100 # int | The number of items to return per page. (optional) (default to 100)

    try:
        # List StackScripts
        api_response = api_instance.get_stack_scripts(api_version, page=page, page_size=page_size)
        print("The response of LinodeStackScriptsApi->get_stack_scripts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinodeStackScriptsApi->get_stack_scripts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **page** | **int**| The page of a collection to return. | [optional] [default to 1]
 **page_size** | **int**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetStackScripts200Response**](GetStackScripts200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of StackScripts available to the User, including private StackScripts owned by the User if the request is authenticated. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_add_stack_script**
> GetStackScripts200ResponseDataInner post_add_stack_script(api_version, post_add_stack_script_request)

Create a StackScript

Creates a StackScript in your Account.   <<LB>>  ---   - __CLI__.      ```     linode-cli stackscripts create \\   --label a-stackscript \\   --description \"This StackScript install and configures MySQL\" \\   --images \"linode/debian9\" \\   --images \"linode/debian8\" \\   --is_public true \\   --rev_note \"Set up MySQL\" \\   --script '#!/bin/bash'     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     stackscripts:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_stack_scripts200_response_data_inner import GetStackScripts200ResponseDataInner
from openapi_client.models.post_add_stack_script_request import PostAddStackScriptRequest
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
    api_instance = openapi_client.LinodeStackScriptsApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    post_add_stack_script_request = openapi_client.PostAddStackScriptRequest() # PostAddStackScriptRequest | The properties to set for the new StackScript.

    try:
        # Create a StackScript
        api_response = api_instance.post_add_stack_script(api_version, post_add_stack_script_request)
        print("The response of LinodeStackScriptsApi->post_add_stack_script:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinodeStackScriptsApi->post_add_stack_script: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **post_add_stack_script_request** | [**PostAddStackScriptRequest**](PostAddStackScriptRequest.md)| The properties to set for the new StackScript. | 

### Return type

[**GetStackScripts200ResponseDataInner**](GetStackScripts200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | StackScript successfully created. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_stack_script**
> GetStackScripts200ResponseDataInner put_stack_script(api_version, stackscript_id, get_stack_scripts200_response_data_inner=get_stack_scripts200_response_data_inner)

Update a StackScript

Updates a StackScript.  __Once a StackScript is made public, it cannot be made private.__   <<LB>>  ---   - __CLI__.      ```     linode-cli stackscripts update 10079 \\   --label a-stackscript \\   --description \"This StackScript installs \\     and configures MySQL\" \\   --images \"linode/debian9\" \\   --images \"linode/debian8\" \\   --is_public true \\   --rev_note \"Set up MySQL\" \\   --script '#!/bin/bash'     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     stackscripts:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_stack_scripts200_response_data_inner import GetStackScripts200ResponseDataInner
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
    api_instance = openapi_client.LinodeStackScriptsApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    stackscript_id = 'stackscript_id_example' # str | The ID of the StackScript to look up.
    get_stack_scripts200_response_data_inner = openapi_client.GetStackScripts200ResponseDataInner() # GetStackScripts200ResponseDataInner | The fields to update. (optional)

    try:
        # Update a StackScript
        api_response = api_instance.put_stack_script(api_version, stackscript_id, get_stack_scripts200_response_data_inner=get_stack_scripts200_response_data_inner)
        print("The response of LinodeStackScriptsApi->put_stack_script:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinodeStackScriptsApi->put_stack_script: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **stackscript_id** | **str**| The ID of the StackScript to look up. | 
 **get_stack_scripts200_response_data_inner** | [**GetStackScripts200ResponseDataInner**](GetStackScripts200ResponseDataInner.md)| The fields to update. | [optional] 

### Return type

[**GetStackScripts200ResponseDataInner**](GetStackScripts200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | StackScript was successfully modified. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

