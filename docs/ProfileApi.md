# openapi_client.ProfileApi

All URIs are relative to *https://api.linode.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_personal_access_token**](ProfileApi.md#delete_personal_access_token) | **DELETE** /{apiVersion}/profile/tokens/{tokenId} | Revoke a personal access token
[**delete_profile_app**](ProfileApi.md#delete_profile_app) | **DELETE** /{apiVersion}/profile/apps/{appId} | Revoke app access
[**delete_profile_phone_number**](ProfileApi.md#delete_profile_phone_number) | **DELETE** /{apiVersion}/profile/phone-number | Delete a phone number
[**delete_ssh_key**](ProfileApi.md#delete_ssh_key) | **DELETE** /{apiVersion}/profile/sshkeys/{sshKeyId} | Delete an SSH key
[**delete_trusted_device**](ProfileApi.md#delete_trusted_device) | **DELETE** /{apiVersion}/profile/devices/{deviceId} | Revoke a trusted device
[**get_devices**](ProfileApi.md#get_devices) | **GET** /{apiVersion}/profile/devices | List trusted devices
[**get_personal_access_token**](ProfileApi.md#get_personal_access_token) | **GET** /{apiVersion}/profile/tokens/{tokenId} | Get a personal access token
[**get_personal_access_tokens**](ProfileApi.md#get_personal_access_tokens) | **GET** /{apiVersion}/profile/tokens | List personal access tokens
[**get_profile**](ProfileApi.md#get_profile) | **GET** /{apiVersion}/profile | Get a profile
[**get_profile_app**](ProfileApi.md#get_profile_app) | **GET** /{apiVersion}/profile/apps/{appId} | Get an authorized app
[**get_profile_apps**](ProfileApi.md#get_profile_apps) | **GET** /{apiVersion}/profile/apps | List authorized apps
[**get_profile_grants**](ProfileApi.md#get_profile_grants) | **GET** /{apiVersion}/profile/grants | List grants
[**get_profile_login**](ProfileApi.md#get_profile_login) | **GET** /{apiVersion}/profile/logins/{loginId} | Get a profile&#39;s login
[**get_profile_logins**](ProfileApi.md#get_profile_logins) | **GET** /{apiVersion}/profile/logins | List logins
[**get_security_questions**](ProfileApi.md#get_security_questions) | **GET** /{apiVersion}/profile/security-questions | List security questions
[**get_ssh_key**](ProfileApi.md#get_ssh_key) | **GET** /{apiVersion}/profile/sshkeys/{sshKeyId} | Get an SSH key
[**get_ssh_keys**](ProfileApi.md#get_ssh_keys) | **GET** /{apiVersion}/profile/sshkeys | List SSH keys
[**get_trusted_device**](ProfileApi.md#get_trusted_device) | **GET** /{apiVersion}/profile/devices/{deviceId} | Get a trusted device
[**get_user_preferences**](ProfileApi.md#get_user_preferences) | **GET** /{apiVersion}/profile/preferences | Get user preferences
[**post_add_ssh_key**](ProfileApi.md#post_add_ssh_key) | **POST** /{apiVersion}/profile/sshkeys | Add an SSH key
[**post_personal_access_token**](ProfileApi.md#post_personal_access_token) | **POST** /{apiVersion}/profile/tokens | Create a personal access token
[**post_profile_phone_number**](ProfileApi.md#post_profile_phone_number) | **POST** /{apiVersion}/profile/phone-number | Send a phone number verification code
[**post_profile_phone_number_verify**](ProfileApi.md#post_profile_phone_number_verify) | **POST** /{apiVersion}/profile/phone-number/verify | Verify a phone number
[**post_security_questions**](ProfileApi.md#post_security_questions) | **POST** /{apiVersion}/profile/security-questions | Answer security questions
[**post_tfa_confirm**](ProfileApi.md#post_tfa_confirm) | **POST** /{apiVersion}/profile/tfa-enable-confirm | Enable two factor authentication
[**post_tfa_disable**](ProfileApi.md#post_tfa_disable) | **POST** /{apiVersion}/profile/tfa-disable | Disable two factor authentication
[**post_tfa_enable**](ProfileApi.md#post_tfa_enable) | **POST** /{apiVersion}/profile/tfa-enable | Create a two factor secret
[**put_personal_access_token**](ProfileApi.md#put_personal_access_token) | **PUT** /{apiVersion}/profile/tokens/{tokenId} | Update a personal access token
[**put_profile**](ProfileApi.md#put_profile) | **PUT** /{apiVersion}/profile | Update a profile
[**put_ssh_key**](ProfileApi.md#put_ssh_key) | **PUT** /{apiVersion}/profile/sshkeys/{sshKeyId} | Update an SSH key
[**put_user_preferences**](ProfileApi.md#put_user_preferences) | **PUT** /{apiVersion}/profile/preferences | Update a user&#39;s preferences


# **delete_personal_access_token**
> object delete_personal_access_token(api_version, token_id)

Revoke a personal access token

Revokes a Personal Access Token. The token will be invalidated immediately, and requests using that token will fail with a 401. It is possible to revoke access to the token making the request to revoke a token, but keep in mind that doing so could lose you access to the api and require you to create a new token through some other means.   <<LB>>  ---   - __CLI__.      ```     linode-cli profile token-delete 123     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.ProfileApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    token_id = 56 # int | The ID of the token to access.

    try:
        # Revoke a personal access token
        api_response = api_instance.delete_personal_access_token(api_version, token_id)
        print("The response of ProfileApi->delete_personal_access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->delete_personal_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **token_id** | **int**| The ID of the token to access. | 

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
**200** | Token revoked successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_profile_app**
> object delete_profile_app(api_version, app_id)

Revoke app access

Expires this app token. This token may no longer be used to access your Account.   <<LB>>  ---   - __CLI__.      ```     linode-cli profile app-delete 123     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.ProfileApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    app_id = 56 # int | The authorized app ID to manage.

    try:
        # Revoke app access
        api_response = api_instance.delete_profile_app(api_version, app_id)
        print("The response of ProfileApi->delete_profile_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->delete_profile_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **app_id** | **int**| The authorized app ID to manage. | 

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
**200** | App&#39;s authorization has been revoked. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_profile_phone_number**
> object delete_profile_phone_number(api_version)

Delete a phone number

Delete the verified phone number for the User making this request.  Use this operation to opt out of SMS messages for the requesting User after a phone number has been verified with the [Verify a phone number](https://techdocs.akamai.com/linode-api/reference/post-profile-phone-number-verify) operation.   <<LB>>  ---   - __CLI__.      ```     linode-cli phone delete     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.ProfileApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)

    try:
        # Delete a phone number
        api_response = api_instance.delete_profile_phone_number(api_version)
        print("The response of ProfileApi->delete_profile_phone_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->delete_profile_phone_number: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]

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
**200** | Phone number deletion request successful. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ssh_key**
> object delete_ssh_key(api_version, ssh_key_id)

Delete an SSH key

Deletes an SSH Key you have access to.  __Note__. deleting an SSH Key will _not_ remove it from any Linode or Disk that was deployed with `authorized_keys`. In those cases, the keys must be manually deleted on the Linode or Disk. This operation will only delete the key's association from your Profile.   <<LB>>  ---   - __CLI__.      ```     linode-cli sshkeys delete 42     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.ProfileApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    ssh_key_id = 56 # int | The ID of the SSHKey.

    try:
        # Delete an SSH key
        api_response = api_instance.delete_ssh_key(api_version, ssh_key_id)
        print("The response of ProfileApi->delete_ssh_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->delete_ssh_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **ssh_key_id** | **int**| The ID of the SSHKey. | 

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
**200** | SSH Key deleted successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_trusted_device**
> object delete_trusted_device(api_version, device_id)

Revoke a trusted device

Revoke an active TrustedDevice for your User.  Once a TrustedDevice is revoked, this device will have to log in again before accessing your Linode account.   <<LB>>  ---   - __CLI__.      ```     linode-cli profile device-revoke 123     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.ProfileApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    device_id = 56 # int | The ID of the TrustedDevice.

    try:
        # Revoke a trusted device
        api_response = api_instance.delete_trusted_device(api_version, device_id)
        print("The response of ProfileApi->delete_trusted_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->delete_trusted_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **device_id** | **int**| The ID of the TrustedDevice. | 

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
**200** | Session revoked successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices**
> GetDevices200Response get_devices(api_version)

List trusted devices

Returns a paginated list of active TrustedDevices for your User. Browsers with an active Remember Me Session are logged into your account until the session expires or is revoked.   <<LB>>  ---   - __CLI__.      ```     linode-cli profile devices-list     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_devices200_response import GetDevices200Response
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
    api_instance = openapi_client.ProfileApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)

    try:
        # List trusted devices
        api_response = api_instance.get_devices(api_version)
        print("The response of ProfileApi->get_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->get_devices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]

### Return type

[**GetDevices200Response**](GetDevices200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a paginated list of TrustedDevice objects. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_personal_access_token**
> GetPersonalAccessTokens200ResponseDataInner get_personal_access_token(api_version, token_id)

Get a personal access token

Returns a single Personal Access Token.   <<LB>>  ---   - __CLI__.      ```     linode-cli profile token-view 123     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_personal_access_tokens200_response_data_inner import GetPersonalAccessTokens200ResponseDataInner
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
    api_instance = openapi_client.ProfileApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    token_id = 56 # int | The ID of the token to access.

    try:
        # Get a personal access token
        api_response = api_instance.get_personal_access_token(api_version, token_id)
        print("The response of ProfileApi->get_personal_access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->get_personal_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **token_id** | **int**| The ID of the token to access. | 

### Return type

[**GetPersonalAccessTokens200ResponseDataInner**](GetPersonalAccessTokens200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested token. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_personal_access_tokens**
> GetPersonalAccessTokens200Response get_personal_access_tokens(api_version)

List personal access tokens

Returns a paginated list of Personal Access Tokens currently active for your User.   <<LB>>  ---   - __CLI__.      ```     linode-cli profile tokens-list     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_personal_access_tokens200_response import GetPersonalAccessTokens200Response
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
    api_instance = openapi_client.ProfileApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)

    try:
        # List personal access tokens
        api_response = api_instance.get_personal_access_tokens(api_version)
        print("The response of ProfileApi->get_personal_access_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->get_personal_access_tokens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]

### Return type

[**GetPersonalAccessTokens200Response**](GetPersonalAccessTokens200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of active tokens. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile**
> GetProfile200Response get_profile(api_version)

Get a profile

Returns information about the current User. This can be used to see who is acting in applications where more than one token is managed. For example, in third-party OAuth applications.  This operation is always accessible, no matter what OAuth scopes the acting token has.   <<LB>>  ---   - __CLI__.      ```     linode-cli profile view     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_profile200_response import GetProfile200Response
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
    api_instance = openapi_client.ProfileApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)

    try:
        # Get a profile
        api_response = api_instance.get_profile(api_version)
        print("The response of ProfileApi->get_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->get_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]

### Return type

[**GetProfile200Response**](GetProfile200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Profile response. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile_app**
> GetProfileApps200ResponseDataInner get_profile_app(api_version, app_id)

Get an authorized app

Returns information about a single app you've authorized to access your Account.   <<LB>>  ---   - __CLI__.      ```     linode-cli profile app-view 1234     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_profile_apps200_response_data_inner import GetProfileApps200ResponseDataInner
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
    api_instance = openapi_client.ProfileApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    app_id = 56 # int | The authorized app ID to manage.

    try:
        # Get an authorized app
        api_response = api_instance.get_profile_app(api_version, app_id)
        print("The response of ProfileApi->get_profile_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->get_profile_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **app_id** | **int**| The authorized app ID to manage. | 

### Return type

[**GetProfileApps200ResponseDataInner**](GetProfileApps200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The app requested. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile_apps**
> GetProfileApps200Response get_profile_apps(api_version, page=page, page_size=page_size)

List authorized apps

This is a collection of OAuth apps that you've given access to your Account, and includes the level of access granted.   <<LB>>  ---   - __CLI__.      ```     linode-cli profile apps-list     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_profile_apps200_response import GetProfileApps200Response
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
    api_instance = openapi_client.ProfileApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    page = 1 # int | The page of a collection to return. (optional) (default to 1)
    page_size = 100 # int | The number of items to return per page. (optional) (default to 100)

    try:
        # List authorized apps
        api_response = api_instance.get_profile_apps(api_version, page=page, page_size=page_size)
        print("The response of ProfileApi->get_profile_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->get_profile_apps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **page** | **int**| The page of a collection to return. | [optional] [default to 1]
 **page_size** | **int**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetProfileApps200Response**](GetProfileApps200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of apps you&#39;ve authorized. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile_grants**
> GetUserGrants200Response get_profile_grants(api_version)

List grants

This returns a GrantsResponse describing what the acting User has been granted access to.  For unrestricted users, this will return a  204 and no body because unrestricted users have access to everything without grants.  This will not return information about entities you do not have access to.  This operation is useful when writing third-party OAuth applications to see what options you should present to the acting User.  For example, if they do not have `global.add_linodes`, you might not display a button to deploy a new Linode.  Any client may run this operation; no OAuth scopes are required.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_user_grants200_response import GetUserGrants200Response
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
    api_instance = openapi_client.ProfileApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)

    try:
        # List grants
        api_response = api_instance.get_profile_grants(api_version)
        print("The response of ProfileApi->get_profile_grants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->get_profile_grants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]

### Return type

[**GetUserGrants200Response**](GetUserGrants200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GrantsResponse. |  -  |
**204** | This is an unrestricted User, who has no grants. This User can access everything on the Account. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile_login**
> GetAccountLogins200ResponseDataInner get_profile_login(api_version, login_id)

Get a profile's login

Returns a login object displaying information about a successful account login from this user.   <<LB>>  ---   - __CLI__.      ```     linode-cli profile login-view 1234     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_account_logins200_response_data_inner import GetAccountLogins200ResponseDataInner
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
    api_instance = openapi_client.ProfileApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    login_id = 56 # int | The ID of the login object to access.

    try:
        # Get a profile's login
        api_response = api_instance.get_profile_login(api_version, login_id)
        print("The response of ProfileApi->get_profile_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->get_profile_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **login_id** | **int**| The ID of the login object to access. | 

### Return type

[**GetAccountLogins200ResponseDataInner**](GetAccountLogins200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested login object. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile_logins**
> GetAccountLogins200Response get_profile_logins(api_version)

List logins

Returns a collection of successful account logins from this user during the last 90 days.   <<LB>>  ---   - __CLI__.      ```     linode-cli profile logins-list     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_account_logins200_response import GetAccountLogins200Response
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
    api_instance = openapi_client.ProfileApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)

    try:
        # List logins
        api_response = api_instance.get_profile_logins(api_version)
        print("The response of ProfileApi->get_profile_logins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->get_profile_logins: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]

### Return type

[**GetAccountLogins200Response**](GetAccountLogins200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of successful account logins from this user during the last 90 days. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_security_questions**
> GetSecurityQuestions200Response get_security_questions(api_version)

List security questions

Returns a collection of security questions and their responses, if any, for your User Profile.   <<LB>>  ---   - __CLI__.      ```     linode-cli security-questions list     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_security_questions200_response import GetSecurityQuestions200Response
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
    api_instance = openapi_client.ProfileApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)

    try:
        # List security questions
        api_response = api_instance.get_security_questions(api_version)
        print("The response of ProfileApi->get_security_questions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->get_security_questions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]

### Return type

[**GetSecurityQuestions200Response**](GetSecurityQuestions200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of security questions. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ssh_key**
> GetSshKeys200ResponseDataInner get_ssh_key(api_version, ssh_key_id)

Get an SSH key

Returns a single SSH Key object identified by `id` that you have access to view.   <<LB>>  ---   - __CLI__.      ```     linode-cli sshkeys view 42     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_ssh_keys200_response_data_inner import GetSshKeys200ResponseDataInner
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
    api_instance = openapi_client.ProfileApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    ssh_key_id = 56 # int | The ID of the SSHKey.

    try:
        # Get an SSH key
        api_response = api_instance.get_ssh_key(api_version, ssh_key_id)
        print("The response of ProfileApi->get_ssh_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->get_ssh_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **ssh_key_id** | **int**| The ID of the SSHKey. | 

### Return type

[**GetSshKeys200ResponseDataInner**](GetSshKeys200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An SSH Key object. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ssh_keys**
> GetSshKeys200Response get_ssh_keys(api_version, page=page, page_size=page_size)

List SSH keys

Returns a collection of SSH Keys you've added to your Profile.   <<LB>>  ---   - __CLI__.      ```     linode-cli sshkeys list     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_ssh_keys200_response import GetSshKeys200Response
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
    api_instance = openapi_client.ProfileApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    page = 1 # int | The page of a collection to return. (optional) (default to 1)
    page_size = 100 # int | The number of items to return per page. (optional) (default to 100)

    try:
        # List SSH keys
        api_response = api_instance.get_ssh_keys(api_version, page=page, page_size=page_size)
        print("The response of ProfileApi->get_ssh_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->get_ssh_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **page** | **int**| The page of a collection to return. | [optional] [default to 1]
 **page_size** | **int**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetSshKeys200Response**](GetSshKeys200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a paginated list of SSH Key objects. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trusted_device**
> GetDevices200ResponseDataInner get_trusted_device(api_version, device_id)

Get a trusted device

Returns a single active TrustedDevice for your User.   <<LB>>  ---   - __CLI__.      ```     linode-cli profile device-view 123     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_devices200_response_data_inner import GetDevices200ResponseDataInner
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
    api_instance = openapi_client.ProfileApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    device_id = 56 # int | The ID of the TrustedDevice.

    try:
        # Get a trusted device
        api_response = api_instance.get_trusted_device(api_version, device_id)
        print("The response of ProfileApi->get_trusted_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->get_trusted_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **device_id** | **int**| The ID of the TrustedDevice. | 

### Return type

[**GetDevices200ResponseDataInner**](GetDevices200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested TrustedDevice object. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_preferences**
> object get_user_preferences(api_version)

Get user preferences

View a list of user preferences tied to the OAuth client that generated the token making the request. The user preferences endpoints allow consumers of the API to store arbitrary JSON data, such as a user's font size preference or preferred display name. User preferences are available for each OAuth client registered to your account, and as such an account can have multiple user preferences.   <<LB>>  ---   - __OAuth scopes__.      ```     account:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.ProfileApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)

    try:
        # Get user preferences
        api_response = api_instance.get_user_preferences(api_version)
        print("The response of ProfileApi->get_user_preferences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->get_user_preferences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]

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
**200** | Returns an object of user preferences. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_add_ssh_key**
> GetSshKeys200ResponseDataInner post_add_ssh_key(api_version, get_ssh_keys200_response_data_inner=get_ssh_keys200_response_data_inner)

Add an SSH key

Adds an SSH Key to your Account profile.   <<LB>>  ---   - __CLI__.      ```     linode-cli sshkeys create \\   --label \"My SSH Key\" \\   --ssh_key \"ssh-rsa AAAA_valid_public_ssh_key_123456785== user@their-computer\"     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_ssh_keys200_response_data_inner import GetSshKeys200ResponseDataInner
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
    api_instance = openapi_client.ProfileApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    get_ssh_keys200_response_data_inner = openapi_client.GetSshKeys200ResponseDataInner() # GetSshKeys200ResponseDataInner | Add SSH Key. (optional)

    try:
        # Add an SSH key
        api_response = api_instance.post_add_ssh_key(api_version, get_ssh_keys200_response_data_inner=get_ssh_keys200_response_data_inner)
        print("The response of ProfileApi->post_add_ssh_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->post_add_ssh_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **get_ssh_keys200_response_data_inner** | [**GetSshKeys200ResponseDataInner**](GetSshKeys200ResponseDataInner.md)| Add SSH Key. | [optional] 

### Return type

[**GetSshKeys200ResponseDataInner**](GetSshKeys200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SSH Key associated successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_personal_access_token**
> GetPersonalAccessTokens200ResponseDataInner post_personal_access_token(api_version, post_personal_access_token_request)

Create a personal access token

Creates a Personal Access Token for your User. The raw token will be returned in the response, but will never be returned again afterward so be sure to take note of it. You may create a token with _at most_ the scopes of your current token. The created token will be able to access your Account until the given expiry, or until it is revoked. __Parent and child accounts__ In a [parent and child account](https://www.linode.com/docs/guides/parent-child-accounts/) environment, the following apply:  - If you're using a child account parent user (proxy user), you can't create this form of token. The only token available to a proxy user is one that lets you run operations in a child account. These are created with the [Create a proxy user token](https://techdocs.akamai.com/linode-api/reference/post-child-account-token) operation.   <<LB>>  ---   - __CLI__.      ```     linode-cli profile token-create \\   --scopes '*' \\   --expiry '2018-01-01T13:46:32' \\   --label linode-cli     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_personal_access_tokens200_response_data_inner import GetPersonalAccessTokens200ResponseDataInner
from openapi_client.models.post_personal_access_token_request import PostPersonalAccessTokenRequest
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
    api_instance = openapi_client.ProfileApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    post_personal_access_token_request = openapi_client.PostPersonalAccessTokenRequest() # PostPersonalAccessTokenRequest | Information about the requested token.

    try:
        # Create a personal access token
        api_response = api_instance.post_personal_access_token(api_version, post_personal_access_token_request)
        print("The response of ProfileApi->post_personal_access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->post_personal_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **post_personal_access_token_request** | [**PostPersonalAccessTokenRequest**](PostPersonalAccessTokenRequest.md)| Information about the requested token. | 

### Return type

[**GetPersonalAccessTokens200ResponseDataInner**](GetPersonalAccessTokens200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Token created successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_profile_phone_number**
> object post_profile_phone_number(api_version, post_profile_phone_number_request=post_profile_phone_number_request)

Send a phone number verification code

Send a one-time verification code via SMS message to the submitted phone number. Providing your phone number helps ensure you can securely access your Account in case other ways to connect are lost. Your phone number is only used to verify your identity by sending an SMS message. Standard carrier messaging fees may apply.  - By accessing this operation you are opting in to receive SMS messages. You can opt out of SMS messages by running the [Delete a phone number](https://techdocs.akamai.com/linode-api/reference/delete-profile-phone-number) operation after your phone number is verified.  - Verification codes are valid for 10 minutes after they are sent.  - Subsequent requests made prior to code expiration result in sending the same code.  Once a verification code is received, verify your phone number with the [Verify a phone number](https://techdocs.akamai.com/linode-api/reference/post-profile-phone-number-verify) operation.   <<LB>>  ---   - __CLI__.      ```     linode-cli phone sms-code-send \\   --iso-code US \\   --phone-number 555-555-5555     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.post_profile_phone_number_request import PostProfilePhoneNumberRequest
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
    api_instance = openapi_client.ProfileApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    post_profile_phone_number_request = openapi_client.PostProfilePhoneNumberRequest() # PostProfilePhoneNumberRequest | Enter a phone number and country code for verification. (optional)

    try:
        # Send a phone number verification code
        api_response = api_instance.post_profile_phone_number(api_version, post_profile_phone_number_request=post_profile_phone_number_request)
        print("The response of ProfileApi->post_profile_phone_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->post_profile_phone_number: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **post_profile_phone_number_request** | [**PostProfilePhoneNumberRequest**](PostProfilePhoneNumberRequest.md)| Enter a phone number and country code for verification. | [optional] 

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
**200** | Phone number verification code request successful. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_profile_phone_number_verify**
> object post_profile_phone_number_verify(api_version, post_profile_phone_number_verify_request=post_profile_phone_number_verify_request)

Verify a phone number

Verify a phone number by confirming the one-time code received via SMS message after running the [Send a phone number verification code](https://techdocs.akamai.com/linode-api/reference/post-profile-phone-number) operation.  - Verification codes are valid for 10 minutes after they are sent.  - Only the same User that made the verification code request can use that code with this operation.  Once completed, the verified phone number is assigned to the User making the request. To change the verified phone number for a User, first run the [Delete a phone number](https://techdocs.akamai.com/linode-api/reference/delete-profile-phone-number) operation, then begin the verification process again with the [Send a phone number verification code](https://techdocs.akamai.com/linode-api/reference/post-profile-phone-number) operation.   <<LB>>  ---   - __CLI__.      ```     linode-cli phone verify \\   --otp_code 123456     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.post_profile_phone_number_verify_request import PostProfilePhoneNumberVerifyRequest
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
    api_instance = openapi_client.ProfileApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    post_profile_phone_number_verify_request = openapi_client.PostProfilePhoneNumberVerifyRequest() # PostProfilePhoneNumberVerifyRequest | Enter a phone verification code for confirmation. (optional)

    try:
        # Verify a phone number
        api_response = api_instance.post_profile_phone_number_verify(api_version, post_profile_phone_number_verify_request=post_profile_phone_number_verify_request)
        print("The response of ProfileApi->post_profile_phone_number_verify:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->post_profile_phone_number_verify: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **post_profile_phone_number_verify_request** | [**PostProfilePhoneNumberVerifyRequest**](PostProfilePhoneNumberVerifyRequest.md)| Enter a phone verification code for confirmation. | [optional] 

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
**200** | Phone number verification successful. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_security_questions**
> PostSecurityQuestionsRequest post_security_questions(api_version, post_security_questions_request=post_security_questions_request)

Answer security questions

Adds security question responses for your User.  Requires exactly three unique questions.  Previous responses are overwritten if answered or reset to `null` if unanswered.  __Note__. Security questions must be answered for your User prior to accessing the [Create a two factor secret](https://techdocs.akamai.com/linode-api/reference/post-tfa-enable) operation.   <<LB>>  ---   - __OAuth scopes__.      ```     account:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.post_security_questions_request import PostSecurityQuestionsRequest
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
    api_instance = openapi_client.ProfileApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    post_security_questions_request = openapi_client.PostSecurityQuestionsRequest() # PostSecurityQuestionsRequest | Answer Security Questions. (optional)

    try:
        # Answer security questions
        api_response = api_instance.post_security_questions(api_version, post_security_questions_request=post_security_questions_request)
        print("The response of ProfileApi->post_security_questions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->post_security_questions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **post_security_questions_request** | [**PostSecurityQuestionsRequest**](PostSecurityQuestionsRequest.md)| Answer Security Questions. | [optional] 

### Return type

[**PostSecurityQuestionsRequest**](PostSecurityQuestionsRequest.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Security Questions answered successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tfa_confirm**
> PostTfaConfirm200Response post_tfa_confirm(api_version, post_tfa_confirm_request)

Enable two factor authentication

Confirms that you can successfully generate Two Factor codes and enables TFA on your Account. Once this is complete, login attempts from untrusted computers will be required to provide a Two Factor code before they are successful.   <<LB>>  ---   - __CLI__.      ```     linode-cli profile tfa-confirm \\   --tfa_code 213456     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.post_tfa_confirm200_response import PostTfaConfirm200Response
from openapi_client.models.post_tfa_confirm_request import PostTfaConfirmRequest
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
    api_instance = openapi_client.ProfileApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    post_tfa_confirm_request = openapi_client.PostTfaConfirmRequest() # PostTfaConfirmRequest | The Two Factor code you generated with your Two Factor secret.

    try:
        # Enable two factor authentication
        api_response = api_instance.post_tfa_confirm(api_version, post_tfa_confirm_request)
        print("The response of ProfileApi->post_tfa_confirm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->post_tfa_confirm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **post_tfa_confirm_request** | [**PostTfaConfirmRequest**](PostTfaConfirmRequest.md)| The Two Factor code you generated with your Two Factor secret. | 

### Return type

[**PostTfaConfirm200Response**](PostTfaConfirm200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TFA enabled successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tfa_disable**
> object post_tfa_disable(api_version)

Disable two factor authentication

Disables Two Factor Authentication for your User. Once successful, login attempts from untrusted computers will only require a password before being successful. This is less secure, and is discouraged.   <<LB>>  ---   - __CLI__.      ```     linode-cli profile tfa-disable     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.ProfileApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)

    try:
        # Disable two factor authentication
        api_response = api_instance.post_tfa_disable(api_version)
        print("The response of ProfileApi->post_tfa_disable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->post_tfa_disable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]

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
**200** | TFA disabled. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tfa_enable**
> PostTfaEnable200Response post_tfa_enable(api_version)

Create a two factor secret

Generates a Two Factor secret for your User. To enable TFA for your User, enter the secret obtained from this operation with the [Enable two factor authentication](https://techdocs.akamai.com/linode-api/reference/post-tfa-confirm) operation. Once enabled, logins from untrusted computers are required to provide a TFA code before they are successful.  Run the [Answer security questions](https://techdocs.akamai.com/linode-api/reference/post-security-questions) operation.   <<LB>>  ---   - __CLI__.      ```     linode-cli profile tfa-enable     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.post_tfa_enable200_response import PostTfaEnable200Response
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
    api_instance = openapi_client.ProfileApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)

    try:
        # Create a two factor secret
        api_response = api_instance.post_tfa_enable(api_version)
        print("The response of ProfileApi->post_tfa_enable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->post_tfa_enable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]

### Return type

[**PostTfaEnable200Response**](PostTfaEnable200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Two Factor secret generated. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_personal_access_token**
> GetPersonalAccessTokens200ResponseDataInner put_personal_access_token(api_version, token_id, get_personal_access_tokens200_response_data_inner)

Update a personal access token

Updates a Personal Access Token.   <<LB>>  ---   - __CLI__.      ```     linode-cli profile token-update 123 \\   --label linode-cli     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_personal_access_tokens200_response_data_inner import GetPersonalAccessTokens200ResponseDataInner
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
    api_instance = openapi_client.ProfileApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    token_id = 56 # int | The ID of the token to access.
    get_personal_access_tokens200_response_data_inner = openapi_client.GetPersonalAccessTokens200ResponseDataInner() # GetPersonalAccessTokens200ResponseDataInner | The fields to update.

    try:
        # Update a personal access token
        api_response = api_instance.put_personal_access_token(api_version, token_id, get_personal_access_tokens200_response_data_inner)
        print("The response of ProfileApi->put_personal_access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->put_personal_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **token_id** | **int**| The ID of the token to access. | 
 **get_personal_access_tokens200_response_data_inner** | [**GetPersonalAccessTokens200ResponseDataInner**](GetPersonalAccessTokens200ResponseDataInner.md)| The fields to update. | 

### Return type

[**GetPersonalAccessTokens200ResponseDataInner**](GetPersonalAccessTokens200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Token updated successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_profile**
> GetProfile200Response put_profile(api_version, get_profile200_response)

Update a profile

Update information in your Profile.  This operation requires the `account:read_write` OAuth Scope.  __Parent and child accounts__  In a [parent and child account](https://www.linode.com/docs/guides/parent-child-accounts/) environment, the following apply:  - You can't edit the `email` for a child account parent user (proxy user). This value is fixed and set when you provision this environment.   <<LB>>  ---   - __CLI__.      ```     linode-cli profile update \\   --email example-user@gmail.com \\   --timezone US/Eastern \\   --email_notifications true \\   --list_auth_method keys_only \\   --two_factor_auth true \\   --restricted false     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_profile200_response import GetProfile200Response
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
    api_instance = openapi_client.ProfileApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    get_profile200_response = openapi_client.GetProfile200Response() # GetProfile200Response | The fields to update.

    try:
        # Update a profile
        api_response = api_instance.put_profile(api_version, get_profile200_response)
        print("The response of ProfileApi->put_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->put_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **get_profile200_response** | [**GetProfile200Response**](GetProfile200Response.md)| The fields to update. | 

### Return type

[**GetProfile200Response**](GetProfile200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Profile updated successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_ssh_key**
> GetSshKeys200ResponseDataInner put_ssh_key(api_version, ssh_key_id, put_ssh_key_request)

Update an SSH key

Updates an SSH Key that you have permission to `read_write`.  Only SSH key labels can be updated.   <<LB>>  ---   - __CLI__.      ```     linode-cli sshkeys update 42 \\   --label \"my laptop\"     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     account:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_ssh_keys200_response_data_inner import GetSshKeys200ResponseDataInner
from openapi_client.models.put_ssh_key_request import PutSshKeyRequest
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
    api_instance = openapi_client.ProfileApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    ssh_key_id = 56 # int | The ID of the SSHKey.
    put_ssh_key_request = openapi_client.PutSshKeyRequest() # PutSshKeyRequest | The fields to update.

    try:
        # Update an SSH key
        api_response = api_instance.put_ssh_key(api_version, ssh_key_id, put_ssh_key_request)
        print("The response of ProfileApi->put_ssh_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->put_ssh_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **ssh_key_id** | **int**| The ID of the SSHKey. | 
 **put_ssh_key_request** | [**PutSshKeyRequest**](PutSshKeyRequest.md)| The fields to update. | 

### Return type

[**GetSshKeys200ResponseDataInner**](GetSshKeys200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SSH Key updated successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_user_preferences**
> object put_user_preferences(api_version, body)

Update a user's preferences

Updates a user's preferences. These preferences are tied to the OAuth client that generated the token making the request. The user preferences endpoints allow consumers of the API to store arbitrary JSON data, such as a user's font size preference or preferred display name. An account may have multiple preferences. Preferences, and the pertaining request body, may contain any arbitrary JSON data that the user would like to store.   <<LB>>  ---   - __OAuth scopes__.      ```     account:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.ProfileApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    body = None # object | The user preferences to update or store.

    try:
        # Update a user's preferences
        api_response = api_instance.put_user_preferences(api_version, body)
        print("The response of ProfileApi->put_user_preferences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->put_user_preferences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **body** | **object**| The user preferences to update or store. | 

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
**200** | Returns an object of user preferences. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

