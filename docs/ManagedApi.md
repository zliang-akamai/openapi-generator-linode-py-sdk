# openapi_client.ManagedApi

All URIs are relative to *https://api.linode.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_managed_contact**](ManagedApi.md#delete_managed_contact) | **DELETE** /{apiVersion}/managed/contacts/{contactId} | Delete a managed contact
[**delete_managed_service**](ManagedApi.md#delete_managed_service) | **DELETE** /{apiVersion}/managed/services/{serviceId} | Delete a managed service
[**get_managed_contact**](ManagedApi.md#get_managed_contact) | **GET** /{apiVersion}/managed/contacts/{contactId} | Get a managed contact
[**get_managed_contacts**](ManagedApi.md#get_managed_contacts) | **GET** /{apiVersion}/managed/contacts | List managed contacts
[**get_managed_credential**](ManagedApi.md#get_managed_credential) | **GET** /{apiVersion}/managed/credentials/{credentialId} | Get a managed credential
[**get_managed_credentials**](ManagedApi.md#get_managed_credentials) | **GET** /{apiVersion}/managed/credentials | List managed credentials
[**get_managed_issue**](ManagedApi.md#get_managed_issue) | **GET** /{apiVersion}/managed/issues/{issueId} | Get a managed issue
[**get_managed_issues**](ManagedApi.md#get_managed_issues) | **GET** /{apiVersion}/managed/issues | List managed issues
[**get_managed_linode_setting**](ManagedApi.md#get_managed_linode_setting) | **GET** /{apiVersion}/managed/linode-settings/{linodeId} | Get a Linode&#39;s managed settings
[**get_managed_linode_settings**](ManagedApi.md#get_managed_linode_settings) | **GET** /{apiVersion}/managed/linode-settings | List managed Linode settings
[**get_managed_service**](ManagedApi.md#get_managed_service) | **GET** /{apiVersion}/managed/services/{serviceId} | Get a managed service
[**get_managed_services**](ManagedApi.md#get_managed_services) | **GET** /{apiVersion}/managed/services | List managed services
[**get_managed_ssh_key**](ManagedApi.md#get_managed_ssh_key) | **GET** /{apiVersion}/managed/credentials/sshkey | Get a managed SSH key
[**get_managed_stats**](ManagedApi.md#get_managed_stats) | **GET** /{apiVersion}/managed/stats | List managed stats
[**post_disable_managed_service**](ManagedApi.md#post_disable_managed_service) | **POST** /{apiVersion}/managed/services/{serviceId}/disable | Disable a managed service
[**post_enable_managed_service**](ManagedApi.md#post_enable_managed_service) | **POST** /{apiVersion}/managed/services/{serviceId}/enable | Enable a managed service
[**post_managed_contact**](ManagedApi.md#post_managed_contact) | **POST** /{apiVersion}/managed/contacts | Create a managed contact
[**post_managed_credential**](ManagedApi.md#post_managed_credential) | **POST** /{apiVersion}/managed/credentials | Create a managed credential
[**post_managed_credential_revoke**](ManagedApi.md#post_managed_credential_revoke) | **POST** /{apiVersion}/managed/credentials/{credentialId}/revoke | Delete a managed credential
[**post_managed_credential_username_password**](ManagedApi.md#post_managed_credential_username_password) | **POST** /{apiVersion}/managed/credentials/{credentialId}/update | Update a managed credential&#39;s username and password
[**post_managed_service**](ManagedApi.md#post_managed_service) | **POST** /{apiVersion}/managed/services | Create a managed service
[**put_managed_contact**](ManagedApi.md#put_managed_contact) | **PUT** /{apiVersion}/managed/contacts/{contactId} | Update a managed contact
[**put_managed_credential**](ManagedApi.md#put_managed_credential) | **PUT** /{apiVersion}/managed/credentials/{credentialId} | Update a managed credential
[**put_managed_linode_setting**](ManagedApi.md#put_managed_linode_setting) | **PUT** /{apiVersion}/managed/linode-settings/{linodeId} | Update a Linode&#39;s managed settings
[**put_managed_service**](ManagedApi.md#put_managed_service) | **PUT** /{apiVersion}/managed/services/{serviceId} | Update a managed service


# **delete_managed_contact**
> object delete_managed_contact(api_version, contact_id)

Delete a managed contact

Deletes a Managed Contact.  This operation can only be accessed by the unrestricted users of an account.   <<LB>>  ---   - __CLI__.      ```     linode-cli managed contact-delete 567     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.ManagedApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    contact_id = 56 # int | The ID of the contact to access.

    try:
        # Delete a managed contact
        api_response = api_instance.delete_managed_contact(api_version, contact_id)
        print("The response of ManagedApi->delete_managed_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedApi->delete_managed_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **contact_id** | **int**| The ID of the contact to access. | 

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
**200** | Contact deleted successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_managed_service**
> object delete_managed_service(api_version, service_id)

Delete a managed service

Deletes a Managed Service.  This service will no longer be monitored by Linode Managed.  This operation can only be accessed by the unrestricted users of an account.   <<LB>>  ---   - __CLI__.      ```     linode-cli managed service-delete 9994     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.ManagedApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    service_id = 56 # int | The ID of the Managed Service to access.

    try:
        # Delete a managed service
        api_response = api_instance.delete_managed_service(api_version, service_id)
        print("The response of ManagedApi->delete_managed_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedApi->delete_managed_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **service_id** | **int**| The ID of the Managed Service to access. | 

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
**200** | Service deleted successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_managed_contact**
> GetManagedContacts200ResponseDataInner get_managed_contact(api_version, contact_id)

Get a managed contact

Returns a single Managed Contact.  This operation can only be accessed by the unrestricted users of an account.   <<LB>>  ---   - __CLI__.      ```     linode-cli managed contact-view 567     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_managed_contacts200_response_data_inner import GetManagedContacts200ResponseDataInner
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
    api_instance = openapi_client.ManagedApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    contact_id = 56 # int | The ID of the contact to access.

    try:
        # Get a managed contact
        api_response = api_instance.get_managed_contact(api_version, contact_id)
        print("The response of ManagedApi->get_managed_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedApi->get_managed_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **contact_id** | **int**| The ID of the contact to access. | 

### Return type

[**GetManagedContacts200ResponseDataInner**](GetManagedContacts200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Managed Contact. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_managed_contacts**
> GetManagedContacts200Response get_managed_contacts(api_version, page=page, page_size=page_size)

List managed contacts

Returns a paginated list of Managed Contacts on your Account.  This operation can only be accessed by the unrestricted users of an account.   <<LB>>  ---   - __CLI__.      ```     linode-cli managed contacts-list     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_managed_contacts200_response import GetManagedContacts200Response
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
    api_instance = openapi_client.ManagedApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    page = 1 # int | The page of a collection to return. (optional) (default to 1)
    page_size = 100 # int | The number of items to return per page. (optional) (default to 100)

    try:
        # List managed contacts
        api_response = api_instance.get_managed_contacts(api_version, page=page, page_size=page_size)
        print("The response of ManagedApi->get_managed_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedApi->get_managed_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **page** | **int**| The page of a collection to return. | [optional] [default to 1]
 **page_size** | **int**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetManagedContacts200Response**](GetManagedContacts200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of ManagedContacts. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_managed_credential**
> GetManagedCredentials200ResponseDataInner get_managed_credential(api_version, credential_id)

Get a managed credential

Returns a single Managed Credential.  This operation can only be accessed by the unrestricted users of an account.   <<LB>>  ---   - __CLI__.      ```     linode-cli managed credential-view 9991     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_managed_credentials200_response_data_inner import GetManagedCredentials200ResponseDataInner
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
    api_instance = openapi_client.ManagedApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    credential_id = 56 # int | The ID of the Credential to access.

    try:
        # Get a managed credential
        api_response = api_instance.get_managed_credential(api_version, credential_id)
        print("The response of ManagedApi->get_managed_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedApi->get_managed_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **credential_id** | **int**| The ID of the Credential to access. | 

### Return type

[**GetManagedCredentials200ResponseDataInner**](GetManagedCredentials200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Managed Credential. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_managed_credentials**
> GetManagedCredentials200Response get_managed_credentials(api_version, page=page, page_size=page_size)

List managed credentials

Returns a paginated list of Managed Credentials on your Account.  This operation can only be accessed by the unrestricted users of an account.   <<LB>>  ---   - __CLI__.      ```     linode-cli managed credentials-list     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_managed_credentials200_response import GetManagedCredentials200Response
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
    api_instance = openapi_client.ManagedApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    page = 1 # int | The page of a collection to return. (optional) (default to 1)
    page_size = 100 # int | The number of items to return per page. (optional) (default to 100)

    try:
        # List managed credentials
        api_response = api_instance.get_managed_credentials(api_version, page=page, page_size=page_size)
        print("The response of ManagedApi->get_managed_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedApi->get_managed_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **page** | **int**| The page of a collection to return. | [optional] [default to 1]
 **page_size** | **int**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetManagedCredentials200Response**](GetManagedCredentials200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of ManagedCredentials. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_managed_issue**
> GetManagedIssues200ResponseDataInner get_managed_issue(api_version, issue_id)

Get a managed issue

Returns a single Issue that is impacting or did impact one of your Managed Services.  This operation can only be accessed by the unrestricted users of an account.   <<LB>>  ---   - __CLI__.      ```     linode-cli managed issue-view 823     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_managed_issues200_response_data_inner import GetManagedIssues200ResponseDataInner
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
    api_instance = openapi_client.ManagedApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    issue_id = 56 # int | The Issue to look up.

    try:
        # Get a managed issue
        api_response = api_instance.get_managed_issue(api_version, issue_id)
        print("The response of ManagedApi->get_managed_issue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedApi->get_managed_issue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **issue_id** | **int**| The Issue to look up. | 

### Return type

[**GetManagedIssues200ResponseDataInner**](GetManagedIssues200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested issue. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_managed_issues**
> GetManagedIssues200Response get_managed_issues(api_version, page=page, page_size=page_size)

List managed issues

Returns a paginated list of recent and ongoing issues detected on your Managed Services.  This operation can only be accessed by the unrestricted users of an account.   <<LB>>  ---   - __CLI__.      ```     linode-cli managed issues-list     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_managed_issues200_response import GetManagedIssues200Response
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
    api_instance = openapi_client.ManagedApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    page = 1 # int | The page of a collection to return. (optional) (default to 1)
    page_size = 100 # int | The number of items to return per page. (optional) (default to 100)

    try:
        # List managed issues
        api_response = api_instance.get_managed_issues(api_version, page=page, page_size=page_size)
        print("The response of ManagedApi->get_managed_issues:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedApi->get_managed_issues: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **page** | **int**| The page of a collection to return. | [optional] [default to 1]
 **page_size** | **int**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetManagedIssues200Response**](GetManagedIssues200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of open or ongoing Managed Issues. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_managed_linode_setting**
> GetManagedLinodeSettings200ResponseDataInner get_managed_linode_setting(api_version, linode_id)

Get a Linode's managed settings

Returns a single Linode's Managed settings.  This operation can only be accessed by the unrestricted users of an account.   <<LB>>  ---   - __CLI__.      ```     linode-cli managed linode-setting-view 123     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_managed_linode_settings200_response_data_inner import GetManagedLinodeSettings200ResponseDataInner
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
    api_instance = openapi_client.ManagedApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    linode_id = 56 # int | The Linode ID whose settings we are accessing.

    try:
        # Get a Linode's managed settings
        api_response = api_instance.get_managed_linode_setting(api_version, linode_id)
        print("The response of ManagedApi->get_managed_linode_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedApi->get_managed_linode_setting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **linode_id** | **int**| The Linode ID whose settings we are accessing. | 

### Return type

[**GetManagedLinodeSettings200ResponseDataInner**](GetManagedLinodeSettings200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Linode&#39;s Managed settings. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_managed_linode_settings**
> GetManagedLinodeSettings200Response get_managed_linode_settings(api_version, page=page, page_size=page_size)

List managed Linode settings

Returns a paginated list of Managed Settings for your Linodes. There will be one entry per Linode on your Account.  This operation can only be accessed by the unrestricted users of an account.   <<LB>>  ---   - __CLI__.      ```     linode-cli managed linode-settings-list     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_managed_linode_settings200_response import GetManagedLinodeSettings200Response
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
    api_instance = openapi_client.ManagedApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    page = 1 # int | The page of a collection to return. (optional) (default to 1)
    page_size = 100 # int | The number of items to return per page. (optional) (default to 100)

    try:
        # List managed Linode settings
        api_response = api_instance.get_managed_linode_settings(api_version, page=page, page_size=page_size)
        print("The response of ManagedApi->get_managed_linode_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedApi->get_managed_linode_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **page** | **int**| The page of a collection to return. | [optional] [default to 1]
 **page_size** | **int**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetManagedLinodeSettings200Response**](GetManagedLinodeSettings200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of Managed settings for your Linodes. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_managed_service**
> GetManagedServices200ResponseDataInner get_managed_service(api_version, service_id)

Get a managed service

Returns information about a single Managed Service on your Account.  This operation can only be accessed by the unrestricted users of an account.   <<LB>>  ---   - __CLI__.      ```     linode-cli managed service-view 9994     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_managed_services200_response_data_inner import GetManagedServices200ResponseDataInner
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
    api_instance = openapi_client.ManagedApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    service_id = 56 # int | The ID of the Managed Service to access.

    try:
        # Get a managed service
        api_response = api_instance.get_managed_service(api_version, service_id)
        print("The response of ManagedApi->get_managed_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedApi->get_managed_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **service_id** | **int**| The ID of the Managed Service to access. | 

### Return type

[**GetManagedServices200ResponseDataInner**](GetManagedServices200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Managed Service. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_managed_services**
> GetManagedServices200Response get_managed_services(api_version)

List managed services

Returns a paginated list of Managed Services on your Account. These are the services Linode Managed is monitoring and will report and attempt to resolve issues with.  This operation can only be accessed by the unrestricted users of an account.   <<LB>>  ---   - __CLI__.      ```     linode-cli managed services-list     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_managed_services200_response import GetManagedServices200Response
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
    api_instance = openapi_client.ManagedApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)

    try:
        # List managed services
        api_response = api_instance.get_managed_services(api_version)
        print("The response of ManagedApi->get_managed_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedApi->get_managed_services: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]

### Return type

[**GetManagedServices200Response**](GetManagedServices200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of Managed Services. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_managed_ssh_key**
> GetManagedSshKey200Response get_managed_ssh_key(api_version)

Get a managed SSH key

Returns the unique SSH public key assigned to your Linode account's Managed service. If you [add this public key](https://www.linode.com/docs/products/services/managed/get-started/#adding-the-public-key) to a Linode on your account, Linode special forces will be able to log in to the Linode with this key when attempting to resolve issues.  This operation can only be accessed by the unrestricted users of an account.   <<LB>>  ---   - __CLI__.      ```     linode-cli managed credential-sshkey-view     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_managed_ssh_key200_response import GetManagedSshKey200Response
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
    api_instance = openapi_client.ManagedApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)

    try:
        # Get a managed SSH key
        api_response = api_instance.get_managed_ssh_key(api_version)
        print("The response of ManagedApi->get_managed_ssh_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedApi->get_managed_ssh_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]

### Return type

[**GetManagedSshKey200Response**](GetManagedSshKey200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Managed SSH public key. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_managed_stats**
> GetManagedStats200Response get_managed_stats(api_version)

List managed stats

Returns a list of Managed Stats on your Account in the form of x and y data points. You can use these data points to plot your own graph visualizations. These stats reflect the last 24 hours of combined usage across all managed Linodes on your account giving you a high-level snapshot of data for the following:  - cpu - disk - swap - network in - network out  This operation can only be accessed by the unrestricted users of an account.   <<LB>>  ---   - __CLI__.      ```     linode-cli managed stats-list     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_managed_stats200_response import GetManagedStats200Response
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
    api_instance = openapi_client.ManagedApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)

    try:
        # List managed stats
        api_response = api_instance.get_managed_stats(api_version)
        print("The response of ManagedApi->get_managed_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedApi->get_managed_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]

### Return type

[**GetManagedStats200Response**](GetManagedStats200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Managed Stats from the last 24 hours. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_disable_managed_service**
> GetManagedServices200ResponseDataInner post_disable_managed_service(api_version, service_id)

Disable a managed service

Temporarily disables monitoring of a Managed Service.  This operation can only be accessed by the unrestricted users of an account.   <<LB>>  ---   - __CLI__.      ```     linode-cli managed service-disable 9994     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_managed_services200_response_data_inner import GetManagedServices200ResponseDataInner
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
    api_instance = openapi_client.ManagedApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    service_id = 56 # int | The ID of the Managed Service to disable.

    try:
        # Disable a managed service
        api_response = api_instance.post_disable_managed_service(api_version, service_id)
        print("The response of ManagedApi->post_disable_managed_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedApi->post_disable_managed_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **service_id** | **int**| The ID of the Managed Service to disable. | 

### Return type

[**GetManagedServices200ResponseDataInner**](GetManagedServices200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Service disabled. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_enable_managed_service**
> GetManagedServices200ResponseDataInner post_enable_managed_service(api_version, service_id)

Enable a managed service

Enables monitoring of a Managed Service.  This operation can only be accessed by the unrestricted users of an account.   <<LB>>  ---   - __CLI__.      ```     linode-cli managed service-enable 9994     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_managed_services200_response_data_inner import GetManagedServices200ResponseDataInner
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
    api_instance = openapi_client.ManagedApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    service_id = 56 # int | The ID of the Managed Service to enable.

    try:
        # Enable a managed service
        api_response = api_instance.post_enable_managed_service(api_version, service_id)
        print("The response of ManagedApi->post_enable_managed_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedApi->post_enable_managed_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **service_id** | **int**| The ID of the Managed Service to enable. | 

### Return type

[**GetManagedServices200ResponseDataInner**](GetManagedServices200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Service enabled. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_managed_contact**
> GetManagedContacts200ResponseDataInner post_managed_contact(api_version, get_managed_contacts200_response_data_inner=get_managed_contacts200_response_data_inner)

Create a managed contact

Creates a Managed Contact.  A Managed Contact is someone Linode special forces can contact in the course of attempting to resolve an issue with a Managed Service.  This operation can only be accessed by the unrestricted users of an account.   <<LB>>  ---   - __CLI__.      ```     linode-cli managed contact-create \\   --name \"John Doe\" \\   --email \"john.doe@example.org\" \\   --phone.primary \"123-456-7890\"     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_managed_contacts200_response_data_inner import GetManagedContacts200ResponseDataInner
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
    api_instance = openapi_client.ManagedApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    get_managed_contacts200_response_data_inner = openapi_client.GetManagedContacts200ResponseDataInner() # GetManagedContacts200ResponseDataInner | Information about the contact to create. (optional)

    try:
        # Create a managed contact
        api_response = api_instance.post_managed_contact(api_version, get_managed_contacts200_response_data_inner=get_managed_contacts200_response_data_inner)
        print("The response of ManagedApi->post_managed_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedApi->post_managed_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **get_managed_contacts200_response_data_inner** | [**GetManagedContacts200ResponseDataInner**](GetManagedContacts200ResponseDataInner.md)| Information about the contact to create. | [optional] 

### Return type

[**GetManagedContacts200ResponseDataInner**](GetManagedContacts200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contact created. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_managed_credential**
> GetManagedCredentials200ResponseDataInner post_managed_credential(api_version, post_managed_credential_request=post_managed_credential_request)

Create a managed credential

Creates a Managed Credential. A Managed Credential is stored securely to allow Linode special forces to access your Managed Services and resolve issues.  This operation can only be accessed by the unrestricted users of an account.   <<LB>>  ---   - __CLI__.      ```     linode-cli managed credential-create \\   --label prod-password-1 \\   --username johndoe \\   --password s3cur3P@ssw0rd     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_managed_credentials200_response_data_inner import GetManagedCredentials200ResponseDataInner
from openapi_client.models.post_managed_credential_request import PostManagedCredentialRequest
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
    api_instance = openapi_client.ManagedApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    post_managed_credential_request = openapi_client.PostManagedCredentialRequest() # PostManagedCredentialRequest | Information about the Credential to create. (optional)

    try:
        # Create a managed credential
        api_response = api_instance.post_managed_credential(api_version, post_managed_credential_request=post_managed_credential_request)
        print("The response of ManagedApi->post_managed_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedApi->post_managed_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **post_managed_credential_request** | [**PostManagedCredentialRequest**](PostManagedCredentialRequest.md)| Information about the Credential to create. | [optional] 

### Return type

[**GetManagedCredentials200ResponseDataInner**](GetManagedCredentials200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Credential created. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_managed_credential_revoke**
> object post_managed_credential_revoke(api_version, credential_id)

Delete a managed credential

Deletes a Managed Credential.  Linode special forces will no longer have access to this Credential when attempting to resolve issues.  This operation can only be accessed by the unrestricted users of an account.   <<LB>>  ---   - __CLI__.      ```     linode-cli managed credential-revoke 9991     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.ManagedApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    credential_id = 56 # int | The ID of the Credential to access.

    try:
        # Delete a managed credential
        api_response = api_instance.post_managed_credential_revoke(api_version, credential_id)
        print("The response of ManagedApi->post_managed_credential_revoke:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedApi->post_managed_credential_revoke: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **credential_id** | **int**| The ID of the Credential to access. | 

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
**200** | Credential deleted successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_managed_credential_username_password**
> object post_managed_credential_username_password(api_version, credential_id, post_managed_credential_username_password_request=post_managed_credential_username_password_request)

Update a managed credential's username and password

Updates the username and password for a Managed Credential.  This operation can only be accessed by the unrestricted users of an account.   <<LB>>  ---   - __CLI__.      ```     linode-cli managed credential-update-username-password 9991 \\   --username johndoe \\   --password s3cur3P@ssw0rd     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.post_managed_credential_username_password_request import PostManagedCredentialUsernamePasswordRequest
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
    api_instance = openapi_client.ManagedApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    credential_id = 56 # int | The ID of the Credential to update.
    post_managed_credential_username_password_request = openapi_client.PostManagedCredentialUsernamePasswordRequest() # PostManagedCredentialUsernamePasswordRequest | The new username and password to assign to the Managed Credential. (optional)

    try:
        # Update a managed credential's username and password
        api_response = api_instance.post_managed_credential_username_password(api_version, credential_id, post_managed_credential_username_password_request=post_managed_credential_username_password_request)
        print("The response of ManagedApi->post_managed_credential_username_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedApi->post_managed_credential_username_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **credential_id** | **int**| The ID of the Credential to update. | 
 **post_managed_credential_username_password_request** | [**PostManagedCredentialUsernamePasswordRequest**](PostManagedCredentialUsernamePasswordRequest.md)| The new username and password to assign to the Managed Credential. | [optional] 

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
**200** | Credential username and password updated. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_managed_service**
> GetManagedServices200ResponseDataInner post_managed_service(api_version, post_managed_service_request=post_managed_service_request)

Create a managed service

Creates a Managed Service. Linode Managed will begin monitoring this service and reporting and attempting to resolve any Issues.  This operation can only be accessed by the unrestricted users of an account.   <<LB>>  ---   - __CLI__.      ```     linode-cli managed service-create \\   --service_type url \\   --label prod-1 \\   --address \"https://example.org\" \\   --timeout 30 \\   --body \"it worked\" \\   --consultation_group on-call \\   --notes \"The service name is \\     my-cool-application\" \\   --credentials 9991     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_managed_services200_response_data_inner import GetManagedServices200ResponseDataInner
from openapi_client.models.post_managed_service_request import PostManagedServiceRequest
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
    api_instance = openapi_client.ManagedApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    post_managed_service_request = openapi_client.PostManagedServiceRequest() # PostManagedServiceRequest | Information about the service to monitor. (optional)

    try:
        # Create a managed service
        api_response = api_instance.post_managed_service(api_version, post_managed_service_request=post_managed_service_request)
        print("The response of ManagedApi->post_managed_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedApi->post_managed_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **post_managed_service_request** | [**PostManagedServiceRequest**](PostManagedServiceRequest.md)| Information about the service to monitor. | [optional] 

### Return type

[**GetManagedServices200ResponseDataInner**](GetManagedServices200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Service created. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_managed_contact**
> GetManagedContacts200ResponseDataInner put_managed_contact(api_version, contact_id, get_managed_contacts200_response_data_inner)

Update a managed contact

Updates information about a Managed Contact. This operation can only be accessed by the unrestricted users of an account.   <<LB>>  ---   - __CLI__.      ```     linode-cli managed contact-update 567 \\   --name \"John Doe\" \\   --email \"john.doe@example.org\" \\   --phone.primary \"123-456-7890\"     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_managed_contacts200_response_data_inner import GetManagedContacts200ResponseDataInner
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
    api_instance = openapi_client.ManagedApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    contact_id = 56 # int | The ID of the contact to access.
    get_managed_contacts200_response_data_inner = openapi_client.GetManagedContacts200ResponseDataInner() # GetManagedContacts200ResponseDataInner | The fields to update.

    try:
        # Update a managed contact
        api_response = api_instance.put_managed_contact(api_version, contact_id, get_managed_contacts200_response_data_inner)
        print("The response of ManagedApi->put_managed_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedApi->put_managed_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **contact_id** | **int**| The ID of the contact to access. | 
 **get_managed_contacts200_response_data_inner** | [**GetManagedContacts200ResponseDataInner**](GetManagedContacts200ResponseDataInner.md)| The fields to update. | 

### Return type

[**GetManagedContacts200ResponseDataInner**](GetManagedContacts200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contact updated successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_managed_credential**
> GetManagedCredentials200ResponseDataInner put_managed_credential(api_version, credential_id, get_managed_credentials200_response_data_inner)

Update a managed credential

Updates the label of a Managed Credential. This operation does not update the username and password for a Managed Credential. To do this, run the [Update a managed credential's username and password](https://techdocs.akamai.com/linode-api/reference/post-managed-credential-username-password)) operation instead. This operation can only be accessed by the unrestricted users of an account.   <<LB>>  ---   - __CLI__.      ```     linode-cli managed credential-update 9991 \\   --label prod-password-1     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_managed_credentials200_response_data_inner import GetManagedCredentials200ResponseDataInner
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
    api_instance = openapi_client.ManagedApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    credential_id = 56 # int | The ID of the Credential to access.
    get_managed_credentials200_response_data_inner = openapi_client.GetManagedCredentials200ResponseDataInner() # GetManagedCredentials200ResponseDataInner | The fields to update.

    try:
        # Update a managed credential
        api_response = api_instance.put_managed_credential(api_version, credential_id, get_managed_credentials200_response_data_inner)
        print("The response of ManagedApi->put_managed_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedApi->put_managed_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **credential_id** | **int**| The ID of the Credential to access. | 
 **get_managed_credentials200_response_data_inner** | [**GetManagedCredentials200ResponseDataInner**](GetManagedCredentials200ResponseDataInner.md)| The fields to update. | 

### Return type

[**GetManagedCredentials200ResponseDataInner**](GetManagedCredentials200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Credential updated successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_managed_linode_setting**
> GetManagedLinodeSettings200ResponseDataInner put_managed_linode_setting(api_version, linode_id, get_managed_linode_settings200_response_data_inner)

Update a Linode's managed settings

Updates a single Linode's Managed settings. This operation can only be accessed by the unrestricted users of an account.   <<LB>>  ---   - __CLI__.      ```     linode-cli managed linode-setting-update \\   7833234 \\   --ssh.access true \\   --ssh.user linode \\   --ssh.port 22 \\   --ssh.ip 203.0.113.1     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_managed_linode_settings200_response_data_inner import GetManagedLinodeSettings200ResponseDataInner
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
    api_instance = openapi_client.ManagedApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    linode_id = 56 # int | The Linode ID whose settings we are accessing.
    get_managed_linode_settings200_response_data_inner = openapi_client.GetManagedLinodeSettings200ResponseDataInner() # GetManagedLinodeSettings200ResponseDataInner | The settings to update.

    try:
        # Update a Linode's managed settings
        api_response = api_instance.put_managed_linode_setting(api_version, linode_id, get_managed_linode_settings200_response_data_inner)
        print("The response of ManagedApi->put_managed_linode_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedApi->put_managed_linode_setting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **linode_id** | **int**| The Linode ID whose settings we are accessing. | 
 **get_managed_linode_settings200_response_data_inner** | [**GetManagedLinodeSettings200ResponseDataInner**](GetManagedLinodeSettings200ResponseDataInner.md)| The settings to update. | 

### Return type

[**GetManagedLinodeSettings200ResponseDataInner**](GetManagedLinodeSettings200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Settings updated successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_managed_service**
> GetManagedServices200ResponseDataInner put_managed_service(api_version, service_id, get_managed_services200_response_data_inner)

Update a managed service

Updates information about a Managed Service.  This operation can only be accessed by the unrestricted users of an account.   <<LB>>  ---   - __CLI__.      ```     linode-cli managed service-update 9994 \\   --service_type url \\   --label prod-1 \\   --address \"https://example.org\" \\   --timeout 30 \\   --body \"it worked\" \\   --consultation_group on-call \\   --notes \"The service name is my-cool-application\" \\   --credentials 9991     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_managed_services200_response_data_inner import GetManagedServices200ResponseDataInner
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
    api_instance = openapi_client.ManagedApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    service_id = 56 # int | The ID of the Managed Service to access.
    get_managed_services200_response_data_inner = openapi_client.GetManagedServices200ResponseDataInner() # GetManagedServices200ResponseDataInner | The fields to update.

    try:
        # Update a managed service
        api_response = api_instance.put_managed_service(api_version, service_id, get_managed_services200_response_data_inner)
        print("The response of ManagedApi->put_managed_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedApi->put_managed_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **service_id** | **int**| The ID of the Managed Service to access. | 
 **get_managed_services200_response_data_inner** | [**GetManagedServices200ResponseDataInner**](GetManagedServices200ResponseDataInner.md)| The fields to update. | 

### Return type

[**GetManagedServices200ResponseDataInner**](GetManagedServices200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Service updated successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

