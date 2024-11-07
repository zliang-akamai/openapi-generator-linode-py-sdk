# openapi_client.DatabasesApi

All URIs are relative to *https://api.linode.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_database_mysql_instance_backup**](DatabasesApi.md#delete_database_mysql_instance_backup) | **DELETE** /{apiVersion}/databases/mysql/instances/{instanceId}/backups/{backupId} | Delete a managed MySQL database backup
[**delete_database_postgre_sql_instance_backup**](DatabasesApi.md#delete_database_postgre_sql_instance_backup) | **DELETE** /{apiVersion}/databases/postgresql/instances/{instanceId}/backups/{backupId} | Delete a managed PostgreSQL database backup
[**delete_databases_mysql_instance**](DatabasesApi.md#delete_databases_mysql_instance) | **DELETE** /{apiVersion}/databases/mysql/instances/{instanceId} | Delete a managed MySQL database
[**delete_databases_postgre_sql_instance**](DatabasesApi.md#delete_databases_postgre_sql_instance) | **DELETE** /{apiVersion}/databases/postgresql/instances/{instanceId} | Delete a managed PostgreSQL database
[**get_databases_engine**](DatabasesApi.md#get_databases_engine) | **GET** /{apiVersion}/databases/engines/{engineId} | Get a managed database engine
[**get_databases_engines**](DatabasesApi.md#get_databases_engines) | **GET** /{apiVersion}/databases/engines | List managed database engines
[**get_databases_instances**](DatabasesApi.md#get_databases_instances) | **GET** /{apiVersion}/databases/instances | List managed databases
[**get_databases_mysql_instance**](DatabasesApi.md#get_databases_mysql_instance) | **GET** /{apiVersion}/databases/mysql/instances/{instanceId} | Get a managed MySQL database
[**get_databases_mysql_instance_backup**](DatabasesApi.md#get_databases_mysql_instance_backup) | **GET** /{apiVersion}/databases/mysql/instances/{instanceId}/backups/{backupId} | Get a managed MySQL database backup
[**get_databases_mysql_instance_backups**](DatabasesApi.md#get_databases_mysql_instance_backups) | **GET** /{apiVersion}/databases/mysql/instances/{instanceId}/backups | List managed MySQL database backups
[**get_databases_mysql_instance_credentials**](DatabasesApi.md#get_databases_mysql_instance_credentials) | **GET** /{apiVersion}/databases/mysql/instances/{instanceId}/credentials | Get managed MySQL database credentials
[**get_databases_mysql_instance_ssl**](DatabasesApi.md#get_databases_mysql_instance_ssl) | **GET** /{apiVersion}/databases/mysql/instances/{instanceId}/ssl | Get a managed MySQL database SSL certificate
[**get_databases_mysql_instances**](DatabasesApi.md#get_databases_mysql_instances) | **GET** /{apiVersion}/databases/mysql/instances | List managed MySQL databases
[**get_databases_postgre_sql_instance**](DatabasesApi.md#get_databases_postgre_sql_instance) | **GET** /{apiVersion}/databases/postgresql/instances/{instanceId} | Get a managed PostgreSQL database
[**get_databases_postgre_sql_instance_backups**](DatabasesApi.md#get_databases_postgre_sql_instance_backups) | **GET** /{apiVersion}/databases/postgresql/instances/{instanceId}/backups | List managed PostgreSQL database backups
[**get_databases_postgre_sql_instance_credentials**](DatabasesApi.md#get_databases_postgre_sql_instance_credentials) | **GET** /{apiVersion}/databases/postgresql/instances/{instanceId}/credentials | Get managed PostgreSQL database credentials
[**get_databases_postgre_sql_instances**](DatabasesApi.md#get_databases_postgre_sql_instances) | **GET** /{apiVersion}/databases/postgresql/instances | List managed PostgreSQL databases
[**get_databases_postgresql_instance_backup**](DatabasesApi.md#get_databases_postgresql_instance_backup) | **GET** /{apiVersion}/databases/postgresql/instances/{instanceId}/backups/{backupId} | Get a managed PostgreSQL database backup
[**get_databases_postgresql_instance_ssl**](DatabasesApi.md#get_databases_postgresql_instance_ssl) | **GET** /{apiVersion}/databases/postgresql/instances/{instanceId}/ssl | Get a managed PostgreSQL database SSL certificate
[**get_databases_type**](DatabasesApi.md#get_databases_type) | **GET** /{apiVersion}/databases/types/{typeId} | Get a managed database type
[**get_databases_types**](DatabasesApi.md#get_databases_types) | **GET** /{apiVersion}/databases/types | List managed database types
[**post_databases_mysql_instance_backup**](DatabasesApi.md#post_databases_mysql_instance_backup) | **POST** /{apiVersion}/databases/mysql/instances/{instanceId}/backups | Create a managed MySQL database backup snapshot
[**post_databases_mysql_instance_backup_restore**](DatabasesApi.md#post_databases_mysql_instance_backup_restore) | **POST** /{apiVersion}/databases/mysql/instances/{instanceId}/backups/{backupId}/restore | Restore a managed MySQL database backup
[**post_databases_mysql_instance_credentials_reset**](DatabasesApi.md#post_databases_mysql_instance_credentials_reset) | **POST** /{apiVersion}/databases/mysql/instances/{instanceId}/credentials/reset | Reset managed MySQL database credentials
[**post_databases_mysql_instance_patch**](DatabasesApi.md#post_databases_mysql_instance_patch) | **POST** /{apiVersion}/databases/mysql/instances/{instanceId}/patch | Patch a managed MySQL database
[**post_databases_mysql_instances**](DatabasesApi.md#post_databases_mysql_instances) | **POST** /{apiVersion}/databases/mysql/instances | Create a managed MySQL database
[**post_databases_postgre_sql_instance_backup**](DatabasesApi.md#post_databases_postgre_sql_instance_backup) | **POST** /{apiVersion}/databases/postgresql/instances/{instanceId}/backups | Create a managed PostgreSQL database backup snapshot
[**post_databases_postgre_sql_instance_backup_restore**](DatabasesApi.md#post_databases_postgre_sql_instance_backup_restore) | **POST** /{apiVersion}/databases/postgresql/instances/{instanceId}/backups/{backupId}/restore | Restore a managed PostgreSQL database backup
[**post_databases_postgre_sql_instance_credentials_reset**](DatabasesApi.md#post_databases_postgre_sql_instance_credentials_reset) | **POST** /{apiVersion}/databases/postgresql/instances/{instanceId}/credentials/reset | Reset managed PostgreSQL database credentials
[**post_databases_postgre_sql_instance_patch**](DatabasesApi.md#post_databases_postgre_sql_instance_patch) | **POST** /{apiVersion}/databases/postgresql/instances/{instanceId}/patch | Patch a managed PostgreSQL database
[**post_databases_postgre_sql_instances**](DatabasesApi.md#post_databases_postgre_sql_instances) | **POST** /{apiVersion}/databases/postgresql/instances | Create a managed PostgreSQL database
[**put_databases_mysql_instance**](DatabasesApi.md#put_databases_mysql_instance) | **PUT** /{apiVersion}/databases/mysql/instances/{instanceId} | Update a managed MySQL database
[**put_databases_postgre_sql_instance**](DatabasesApi.md#put_databases_postgre_sql_instance) | **PUT** /{apiVersion}/databases/postgresql/instances/{instanceId} | Update a managed PostgreSQL database


# **delete_database_mysql_instance_backup**
> object delete_database_mysql_instance_backup(api_version, instance_id, backup_id)

Delete a managed MySQL database backup

__This operation is currently only available for customers who already have an active Managed Database.__  Delete a single backup for an accessible Managed MySQL Database.  Requires `read_write` access to the Database.  The Database must not be provisioning to perform this operation.   <<LB>>  ---   - __CLI__.      ```     linode-cli databases mysql-backup-delete 123 456     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     databases:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.DatabasesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    instance_id = 56 # int | The ID of the Managed PostgreSQL Database.
    backup_id = 56 # int | The ID of the Managed MySQL Database backup.

    try:
        # Delete a managed MySQL database backup
        api_response = api_instance.delete_database_mysql_instance_backup(api_version, instance_id, backup_id)
        print("The response of DatabasesApi->delete_database_mysql_instance_backup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->delete_database_mysql_instance_backup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **instance_id** | **int**| The ID of the Managed PostgreSQL Database. | 
 **backup_id** | **int**| The ID of the Managed MySQL Database backup. | 

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
**200** | Request to delete Database backup successful. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_database_postgre_sql_instance_backup**
> object delete_database_postgre_sql_instance_backup(api_version, instance_id, backup_id)

Delete a managed PostgreSQL database backup

__This operation is currently only available for customers who already have an active Managed Database.__  Delete a single backup for an accessible Managed PostgreSQL Database.  Requires `read_write` access to the Database.  The Database must not be provisioning to perform this operation.   <<LB>>  ---   - __CLI__.      ```     linode-cli databases postgresql-backup-delete 123 456     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     databases:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.DatabasesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    instance_id = 56 # int | The ID of the Managed PostgreSQL Database.
    backup_id = 56 # int | The ID of the Managed PostgreSQL Database backup.

    try:
        # Delete a managed PostgreSQL database backup
        api_response = api_instance.delete_database_postgre_sql_instance_backup(api_version, instance_id, backup_id)
        print("The response of DatabasesApi->delete_database_postgre_sql_instance_backup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->delete_database_postgre_sql_instance_backup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **instance_id** | **int**| The ID of the Managed PostgreSQL Database. | 
 **backup_id** | **int**| The ID of the Managed PostgreSQL Database backup. | 

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
**200** | Request to delete Database backup successful. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_databases_mysql_instance**
> object delete_databases_mysql_instance(api_version, instance_id)

Delete a managed MySQL database

__This operation is currently only available for customers who already have an active Managed Database.__  Remove a Managed MySQL Database from your Account.  Requires `read_write` access to the Database.  The Database must have an `active`, `failed`, or `degraded` status to perform this operation.  Only unrestricted Users can access this operation, and have access regardless of the acting token's OAuth scopes.   <<LB>>  ---   - __CLI__.      ```     linode-cli databases mysql-delete 123     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     databases:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.DatabasesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    instance_id = 56 # int | The ID of the Managed PostgreSQL Database.

    try:
        # Delete a managed MySQL database
        api_response = api_instance.delete_databases_mysql_instance(api_version, instance_id)
        print("The response of DatabasesApi->delete_databases_mysql_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->delete_databases_mysql_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **instance_id** | **int**| The ID of the Managed PostgreSQL Database. | 

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
**200** | Managed MySQL Database successfully deleted. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_databases_postgre_sql_instance**
> object delete_databases_postgre_sql_instance(api_version, instance_id)

Delete a managed PostgreSQL database

__This operation is currently only available for customers who already have an active Managed Database.__  Remove a Managed PostgreSQL Database from your Account.  Requires `read_write` access to the Database.  The Database must have an `active`, `failed`, or `degraded` status to perform this operation.  Only unrestricted Users can access this operation, and have access regardless of the acting token's OAuth scopes.   <<LB>>  ---   - __CLI__.      ```     linode-cli databases postgresql-delete 123     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     databases:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.DatabasesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    instance_id = 56 # int | The ID of the Managed PostgreSQL Database.

    try:
        # Delete a managed PostgreSQL database
        api_response = api_instance.delete_databases_postgre_sql_instance(api_version, instance_id)
        print("The response of DatabasesApi->delete_databases_postgre_sql_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->delete_databases_postgre_sql_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **instance_id** | **int**| The ID of the Managed PostgreSQL Database. | 

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
**200** | Managed PostgreSQL Database successfully deleted. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_databases_engine**
> GetDatabasesEngines200ResponseAllOfDataInner get_databases_engine(api_version, engine_id, page=page, page_size=page_size)

Get a managed database engine

__This operation is currently only available for customers who already have an active Managed Database.__  Display information for a single Managed Database engine type and version.   <<LB>>  ---   - __CLI__.      ```     linode-cli databases engine-view     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)

### Example


```python
import openapi_client
from openapi_client.models.get_databases_engines200_response_all_of_data_inner import GetDatabasesEngines200ResponseAllOfDataInner
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
    api_instance = openapi_client.DatabasesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    engine_id = 'engine_id_example' # str | The ID of the Managed Database engine.
    page = 1 # int | The page of a collection to return. (optional) (default to 1)
    page_size = 100 # int | The number of items to return per page. (optional) (default to 100)

    try:
        # Get a managed database engine
        api_response = api_instance.get_databases_engine(api_version, engine_id, page=page, page_size=page_size)
        print("The response of DatabasesApi->get_databases_engine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_databases_engine: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **engine_id** | **str**| The ID of the Managed Database engine. | 
 **page** | **int**| The page of a collection to return. | [optional] [default to 1]
 **page_size** | **int**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetDatabasesEngines200ResponseAllOfDataInner**](GetDatabasesEngines200ResponseAllOfDataInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns information for a single Managed Database engine type and version. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_databases_engines**
> GetDatabasesEngines200Response get_databases_engines(api_version, page=page, page_size=page_size)

List managed database engines

__This operation is currently only available for customers who already have an active Managed Database.__  Display all available Managed Database engine types and versions. Engine IDs are used when creating new Managed Databases.   <<LB>>  ---   - __CLI__.      ```     linode-cli databases engines     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)

### Example


```python
import openapi_client
from openapi_client.models.get_databases_engines200_response import GetDatabasesEngines200Response
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
    api_instance = openapi_client.DatabasesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    page = 1 # int | The page of a collection to return. (optional) (default to 1)
    page_size = 100 # int | The number of items to return per page. (optional) (default to 100)

    try:
        # List managed database engines
        api_response = api_instance.get_databases_engines(api_version, page=page, page_size=page_size)
        print("The response of DatabasesApi->get_databases_engines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_databases_engines: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **page** | **int**| The page of a collection to return. | [optional] [default to 1]
 **page_size** | **int**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetDatabasesEngines200Response**](GetDatabasesEngines200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a paginated list of all available Managed Database engines and versions. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_databases_instances**
> GetDatabasesInstances200Response get_databases_instances(api_version, page=page, page_size=page_size)

List managed databases

__This operation is currently only available for customers who already have an active Managed Database.__  Display all Managed Databases that are accessible by your User, regardless of engine type.  For more detailed information on a particular Database instance, make a request to its `instance_uri`.   <<LB>>  ---   - __CLI__.      ```     linode-cli databases list     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     databases:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_databases_instances200_response import GetDatabasesInstances200Response
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
    api_instance = openapi_client.DatabasesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    page = 1 # int | The page of a collection to return. (optional) (default to 1)
    page_size = 100 # int | The number of items to return per page. (optional) (default to 100)

    try:
        # List managed databases
        api_response = api_instance.get_databases_instances(api_version, page=page, page_size=page_size)
        print("The response of DatabasesApi->get_databases_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_databases_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **page** | **int**| The page of a collection to return. | [optional] [default to 1]
 **page_size** | **int**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetDatabasesInstances200Response**](GetDatabasesInstances200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a paginated list of all accessible Managed Databases on your Account. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_databases_mysql_instance**
> GetDatabasesMysqlInstances200ResponseAllOfDataInner get_databases_mysql_instance(api_version, instance_id)

Get a managed MySQL database

__This operation is currently only available for customers who already have an active Managed Database.__  Display information for a single, accessible Managed MySQL Database.   <<LB>>  ---   - __CLI__.      ```     linode-cli databases mysql-view 123     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     databases:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_databases_mysql_instances200_response_all_of_data_inner import GetDatabasesMysqlInstances200ResponseAllOfDataInner
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
    api_instance = openapi_client.DatabasesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    instance_id = 56 # int | The ID of the Managed PostgreSQL Database.

    try:
        # Get a managed MySQL database
        api_response = api_instance.get_databases_mysql_instance(api_version, instance_id)
        print("The response of DatabasesApi->get_databases_mysql_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_databases_mysql_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **instance_id** | **int**| The ID of the Managed PostgreSQL Database. | 

### Return type

[**GetDatabasesMysqlInstances200ResponseAllOfDataInner**](GetDatabasesMysqlInstances200ResponseAllOfDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns information for a single Managed MySQL Database. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_databases_mysql_instance_backup**
> GetDatabasesMysqlInstanceBackups200ResponseAllOfDataInner get_databases_mysql_instance_backup(api_version, instance_id, backup_id)

Get a managed MySQL database backup

__This operation is currently only available for customers who already have an active Managed Database.__  Display information for a single backup for an accessible Managed MySQL Database.  The Database must not be provisioning to perform this operation.   <<LB>>  ---   - __CLI__.      ```     linode-cli databases mysql-backup-view 123 456     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     databases:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_databases_mysql_instance_backups200_response_all_of_data_inner import GetDatabasesMysqlInstanceBackups200ResponseAllOfDataInner
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
    api_instance = openapi_client.DatabasesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    instance_id = 56 # int | The ID of the Managed PostgreSQL Database.
    backup_id = 56 # int | The ID of the Managed MySQL Database backup.

    try:
        # Get a managed MySQL database backup
        api_response = api_instance.get_databases_mysql_instance_backup(api_version, instance_id, backup_id)
        print("The response of DatabasesApi->get_databases_mysql_instance_backup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_databases_mysql_instance_backup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **instance_id** | **int**| The ID of the Managed PostgreSQL Database. | 
 **backup_id** | **int**| The ID of the Managed MySQL Database backup. | 

### Return type

[**GetDatabasesMysqlInstanceBackups200ResponseAllOfDataInner**](GetDatabasesMysqlInstanceBackups200ResponseAllOfDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single backup for the Managed MySQL Database. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_databases_mysql_instance_backups**
> GetDatabasesMysqlInstanceBackups200Response get_databases_mysql_instance_backups(api_version, instance_id, page=page, page_size=page_size)

List managed MySQL database backups

__This operation is currently only available for customers who already have an active Managed Database.__  Display all backups for an accessible Managed MySQL Database.  The Database must not be provisioning to perform this operation.  Database `auto` type backups are created every 24 hours at 0:00 UTC. Each `auto` backup is retained for 7 days.  Database `snapshot` type backups are created by accessing the [Create a managed MySQL database backup snapshot](https://techdocs.akamai.com/linode-api/reference/post-databases-mysql-instance-backup) operation.   <<LB>>  ---   - __CLI__.      ```     linode-cli databases mysql-backups-list 123     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     databases:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_databases_mysql_instance_backups200_response import GetDatabasesMysqlInstanceBackups200Response
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
    api_instance = openapi_client.DatabasesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    instance_id = 56 # int | The ID of the Managed PostgreSQL Database.
    page = 1 # int | The page of a collection to return. (optional) (default to 1)
    page_size = 100 # int | The number of items to return per page. (optional) (default to 100)

    try:
        # List managed MySQL database backups
        api_response = api_instance.get_databases_mysql_instance_backups(api_version, instance_id, page=page, page_size=page_size)
        print("The response of DatabasesApi->get_databases_mysql_instance_backups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_databases_mysql_instance_backups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **instance_id** | **int**| The ID of the Managed PostgreSQL Database. | 
 **page** | **int**| The page of a collection to return. | [optional] [default to 1]
 **page_size** | **int**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetDatabasesMysqlInstanceBackups200Response**](GetDatabasesMysqlInstanceBackups200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a paginated list of backups for the Managed MySQL Database. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_databases_mysql_instance_credentials**
> GetDatabasesMysqlInstanceCredentials200Response get_databases_mysql_instance_credentials(api_version, instance_id)

Get managed MySQL database credentials

__This operation is currently only available for customers who already have an active Managed Database.__  Display the root username and password for an accessible Managed MySQL Database.  The Database must have an `active` status to perform this operation.   <<LB>>  ---   - __CLI__.      ```     linode-cli databases mysql-creds-view 123     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     databases:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_databases_mysql_instance_credentials200_response import GetDatabasesMysqlInstanceCredentials200Response
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
    api_instance = openapi_client.DatabasesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    instance_id = 56 # int | The ID of the Managed PostgreSQL Database.

    try:
        # Get managed MySQL database credentials
        api_response = api_instance.get_databases_mysql_instance_credentials(api_version, instance_id)
        print("The response of DatabasesApi->get_databases_mysql_instance_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_databases_mysql_instance_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **instance_id** | **int**| The ID of the Managed PostgreSQL Database. | 

### Return type

[**GetDatabasesMysqlInstanceCredentials200Response**](GetDatabasesMysqlInstanceCredentials200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Managed Database root username and password. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_databases_mysql_instance_ssl**
> GetDatabasesMysqlInstanceSsl200Response get_databases_mysql_instance_ssl(api_version, instance_id)

Get a managed MySQL database SSL certificate

__This operation is currently only available for customers who already have an active Managed Database.__  Display the SSL CA certificate for an accessible Managed MySQL Database.  The Database must have an `active` status to perform this operation.   <<LB>>  ---   - __CLI__.      ```     linode-cli databases mysql-ssl-cert 123     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     databases:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_databases_mysql_instance_ssl200_response import GetDatabasesMysqlInstanceSsl200Response
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
    api_instance = openapi_client.DatabasesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    instance_id = 56 # int | The ID of the Managed MySQL Database.

    try:
        # Get a managed MySQL database SSL certificate
        api_response = api_instance.get_databases_mysql_instance_ssl(api_version, instance_id)
        print("The response of DatabasesApi->get_databases_mysql_instance_ssl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_databases_mysql_instance_ssl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **instance_id** | **int**| The ID of the Managed MySQL Database. | 

### Return type

[**GetDatabasesMysqlInstanceSsl200Response**](GetDatabasesMysqlInstanceSsl200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the SSL CA certificate of a single Managed MySQL Database. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_databases_mysql_instances**
> GetDatabasesMysqlInstances200Response get_databases_mysql_instances(api_version, page=page, page_size=page_size)

List managed MySQL databases

__This operation is currently only available for customers who already have an active Managed Database.__  Display all accessible Managed MySQL Databases.   <<LB>>  ---   - __CLI__.      ```     linode-cli databases mysql-list     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     databases:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_databases_mysql_instances200_response import GetDatabasesMysqlInstances200Response
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
    api_instance = openapi_client.DatabasesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    page = 1 # int | The page of a collection to return. (optional) (default to 1)
    page_size = 100 # int | The number of items to return per page. (optional) (default to 100)

    try:
        # List managed MySQL databases
        api_response = api_instance.get_databases_mysql_instances(api_version, page=page, page_size=page_size)
        print("The response of DatabasesApi->get_databases_mysql_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_databases_mysql_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **page** | **int**| The page of a collection to return. | [optional] [default to 1]
 **page_size** | **int**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetDatabasesMysqlInstances200Response**](GetDatabasesMysqlInstances200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a paginated list of all accessible Managed MySQL Databases on your Account. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_databases_postgre_sql_instance**
> GetDatabasesPostgreSqlInstances200ResponseAllOfDataInner get_databases_postgre_sql_instance(api_version, instance_id)

Get a managed PostgreSQL database

__This operation is currently only available for customers who already have an active Managed Database.__  Display information for a single, accessible Managed PostgreSQL Database.   <<LB>>  ---   - __CLI__.      ```     linode-cli databases postgresql-view 123     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     databases:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_databases_postgre_sql_instances200_response_all_of_data_inner import GetDatabasesPostgreSqlInstances200ResponseAllOfDataInner
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
    api_instance = openapi_client.DatabasesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    instance_id = 56 # int | The ID of the Managed PostgreSQL Database.

    try:
        # Get a managed PostgreSQL database
        api_response = api_instance.get_databases_postgre_sql_instance(api_version, instance_id)
        print("The response of DatabasesApi->get_databases_postgre_sql_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_databases_postgre_sql_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **instance_id** | **int**| The ID of the Managed PostgreSQL Database. | 

### Return type

[**GetDatabasesPostgreSqlInstances200ResponseAllOfDataInner**](GetDatabasesPostgreSqlInstances200ResponseAllOfDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns information for a single Managed PostgreSQL Database. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_databases_postgre_sql_instance_backups**
> GetDatabasesMysqlInstanceBackups200Response get_databases_postgre_sql_instance_backups(api_version, instance_id, page=page, page_size=page_size)

List managed PostgreSQL database backups

__This operation is currently only available for customers who already have an active Managed Database.__  Display all backups for an accessible Managed PostgreSQL Database.  The Database must not be provisioning to perform this operation.  Database `auto` type backups are created every 24 hours at 0:00 UTC. Each `auto` backup is retained for 7 days.  Database `snapshot` type backups are created by accessing the [Create a managed PostgreSQL database backup snapshot](https://techdocs.akamai.com/linode-api/reference/post-databases-postgre-sql-instance-backup) operation.   <<LB>>  ---   - __CLI__.      ```     linode-cli databases postgresql-backups-list 123     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     databases:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_databases_mysql_instance_backups200_response import GetDatabasesMysqlInstanceBackups200Response
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
    api_instance = openapi_client.DatabasesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    instance_id = 56 # int | The ID of the Managed PostgreSQL Database.
    page = 1 # int | The page of a collection to return. (optional) (default to 1)
    page_size = 100 # int | The number of items to return per page. (optional) (default to 100)

    try:
        # List managed PostgreSQL database backups
        api_response = api_instance.get_databases_postgre_sql_instance_backups(api_version, instance_id, page=page, page_size=page_size)
        print("The response of DatabasesApi->get_databases_postgre_sql_instance_backups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_databases_postgre_sql_instance_backups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **instance_id** | **int**| The ID of the Managed PostgreSQL Database. | 
 **page** | **int**| The page of a collection to return. | [optional] [default to 1]
 **page_size** | **int**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetDatabasesMysqlInstanceBackups200Response**](GetDatabasesMysqlInstanceBackups200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a paginated list of backups for the Managed PostgreSQL Database. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_databases_postgre_sql_instance_credentials**
> GetDatabasesMysqlInstanceCredentials200Response get_databases_postgre_sql_instance_credentials(api_version, instance_id)

Get managed PostgreSQL database credentials

__This operation is currently only available for customers who already have an active Managed Database.__  Display the root username and password for an accessible Managed PostgreSQL Database.  The Database must have an `active` status to perform this operation.   <<LB>>  ---   - __CLI__.      ```     linode-cli databases postgresql-creds-view 123     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     databases:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_databases_mysql_instance_credentials200_response import GetDatabasesMysqlInstanceCredentials200Response
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
    api_instance = openapi_client.DatabasesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    instance_id = 56 # int | The ID of the Managed PostgreSQL Database.

    try:
        # Get managed PostgreSQL database credentials
        api_response = api_instance.get_databases_postgre_sql_instance_credentials(api_version, instance_id)
        print("The response of DatabasesApi->get_databases_postgre_sql_instance_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_databases_postgre_sql_instance_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **instance_id** | **int**| The ID of the Managed PostgreSQL Database. | 

### Return type

[**GetDatabasesMysqlInstanceCredentials200Response**](GetDatabasesMysqlInstanceCredentials200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Managed Database root username and password. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_databases_postgre_sql_instances**
> GetDatabasesPostgreSqlInstances200Response get_databases_postgre_sql_instances(api_version, page=page, page_size=page_size)

List managed PostgreSQL databases

__This operation is currently only available for customers who already have an active Managed Database.__  Display all accessible Managed PostgreSQL Databases.   <<LB>>  ---   - __CLI__.      ```     linode-cli databases postgresql-list     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     databases:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_databases_postgre_sql_instances200_response import GetDatabasesPostgreSqlInstances200Response
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
    api_instance = openapi_client.DatabasesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    page = 1 # int | The page of a collection to return. (optional) (default to 1)
    page_size = 100 # int | The number of items to return per page. (optional) (default to 100)

    try:
        # List managed PostgreSQL databases
        api_response = api_instance.get_databases_postgre_sql_instances(api_version, page=page, page_size=page_size)
        print("The response of DatabasesApi->get_databases_postgre_sql_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_databases_postgre_sql_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **page** | **int**| The page of a collection to return. | [optional] [default to 1]
 **page_size** | **int**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetDatabasesPostgreSqlInstances200Response**](GetDatabasesPostgreSqlInstances200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a paginated list of all accessible Managed PostgreSQL Databases on your Account. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_databases_postgresql_instance_backup**
> GetDatabasesMysqlInstanceBackups200ResponseAllOfDataInner get_databases_postgresql_instance_backup(api_version, instance_id, backup_id)

Get a managed PostgreSQL database backup

__This operation is currently only available for customers who already have an active Managed Database.__  Display information for a single backup for an accessible Managed PostgreSQL Database.  The Database must not be provisioning to perform this operation.   <<LB>>  ---   - __CLI__.      ```     linode-cli databases postgresql-backup-view 123 456     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     databases:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_databases_mysql_instance_backups200_response_all_of_data_inner import GetDatabasesMysqlInstanceBackups200ResponseAllOfDataInner
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
    api_instance = openapi_client.DatabasesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    instance_id = 56 # int | The ID of the Managed PostgreSQL Database.
    backup_id = 56 # int | The ID of the Managed PostgreSQL Database backup.

    try:
        # Get a managed PostgreSQL database backup
        api_response = api_instance.get_databases_postgresql_instance_backup(api_version, instance_id, backup_id)
        print("The response of DatabasesApi->get_databases_postgresql_instance_backup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_databases_postgresql_instance_backup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **instance_id** | **int**| The ID of the Managed PostgreSQL Database. | 
 **backup_id** | **int**| The ID of the Managed PostgreSQL Database backup. | 

### Return type

[**GetDatabasesMysqlInstanceBackups200ResponseAllOfDataInner**](GetDatabasesMysqlInstanceBackups200ResponseAllOfDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single backup for the Managed PostgreSQL Database. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_databases_postgresql_instance_ssl**
> GetDatabasesMysqlInstanceSsl200Response get_databases_postgresql_instance_ssl(api_version, instance_id)

Get a managed PostgreSQL database SSL certificate

__This operation is currently only available for customers who already have an active Managed Database.__  Display the SSL CA certificate for an accessible Managed PostgreSQL Database.  The Database must have an `active` status to perform this operation.   <<LB>>  ---   - __CLI__.      ```     linode-cli databases postgresql-ssl-cert 123     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     databases:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_databases_mysql_instance_ssl200_response import GetDatabasesMysqlInstanceSsl200Response
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
    api_instance = openapi_client.DatabasesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    instance_id = 56 # int | The ID of the Managed PostgreSQL Database.

    try:
        # Get a managed PostgreSQL database SSL certificate
        api_response = api_instance.get_databases_postgresql_instance_ssl(api_version, instance_id)
        print("The response of DatabasesApi->get_databases_postgresql_instance_ssl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_databases_postgresql_instance_ssl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **instance_id** | **int**| The ID of the Managed PostgreSQL Database. | 

### Return type

[**GetDatabasesMysqlInstanceSsl200Response**](GetDatabasesMysqlInstanceSsl200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the SSL CA certificate of a single Managed PostgreSQL Database. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_databases_type**
> GetDatabasesTypes200ResponseAllOfDataInner get_databases_type(api_version, type_id, page=page, page_size=page_size)

Get a managed database type

__This operation is currently only available for customers who already have an active Managed Database.__  Display the details of a single Managed Database type. The type and number of nodes determine the resources and price of a Managed Database instance.   <<LB>>  ---   - __CLI__.      ```     linode-cli databases type-view     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)

### Example


```python
import openapi_client
from openapi_client.models.get_databases_types200_response_all_of_data_inner import GetDatabasesTypes200ResponseAllOfDataInner
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
    api_instance = openapi_client.DatabasesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    type_id = 'type_id_example' # str | The ID of the Managed Database type.
    page = 1 # int | The page of a collection to return. (optional) (default to 1)
    page_size = 100 # int | The number of items to return per page. (optional) (default to 100)

    try:
        # Get a managed database type
        api_response = api_instance.get_databases_type(api_version, type_id, page=page, page_size=page_size)
        print("The response of DatabasesApi->get_databases_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_databases_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **type_id** | **str**| The ID of the Managed Database type. | 
 **page** | **int**| The page of a collection to return. | [optional] [default to 1]
 **page_size** | **int**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetDatabasesTypes200ResponseAllOfDataInner**](GetDatabasesTypes200ResponseAllOfDataInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single Managed Database type. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_databases_types**
> GetDatabasesTypes200Response get_databases_types(api_version, page=page, page_size=page_size)

List managed database types

__This operation is currently only available for customers who already have an active Managed Database.__  Display all Managed Database node types. The type and number of nodes determine the resources and price of a Managed Database instance.  Each Managed Database can have one node type. In the case of a high availability Database, all nodes are provisioned according to the chosen type.   <<LB>>  ---   - __CLI__.      ```     linode-cli databases types     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)

### Example


```python
import openapi_client
from openapi_client.models.get_databases_types200_response import GetDatabasesTypes200Response
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
    api_instance = openapi_client.DatabasesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    page = 1 # int | The page of a collection to return. (optional) (default to 1)
    page_size = 100 # int | The number of items to return per page. (optional) (default to 100)

    try:
        # List managed database types
        api_response = api_instance.get_databases_types(api_version, page=page, page_size=page_size)
        print("The response of DatabasesApi->get_databases_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_databases_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **page** | **int**| The page of a collection to return. | [optional] [default to 1]
 **page_size** | **int**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetDatabasesTypes200Response**](GetDatabasesTypes200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a paginated list of all Managed Database types. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_databases_mysql_instance_backup**
> object post_databases_mysql_instance_backup(api_version, instance_id, post_databases_mysql_instance_backup_request=post_databases_mysql_instance_backup_request)

Create a managed MySQL database backup snapshot

__This operation is currently only available for customers who already have an active Managed Database.__  Creates a snapshot backup of a Managed MySQL Database.  Requires `read_write` access to the Database.  Up to 3 snapshot backups for each Database can be stored at a time. If 3 snapshots have been created for a Database, one must be deleted before another can be made.  Backups generated by this operation have the type `snapshot`. Snapshot backups may take several minutes to complete, after which they will be accessible to view or restore.  The Database must have an `active` status to perform this operation. If another backup is in progress, it must complete before a new backup can be initiated.   <<LB>>  ---   - __CLI__.      ```     linode-cli databases mysql-backup-snapshot 123 \\   --label snapshot1 \\   --target primary     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     databases:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.post_databases_mysql_instance_backup_request import PostDatabasesMysqlInstanceBackupRequest
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
    api_instance = openapi_client.DatabasesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    instance_id = 56 # int | The ID of the Managed PostgreSQL Database.
    post_databases_mysql_instance_backup_request = openapi_client.PostDatabasesMysqlInstanceBackupRequest() # PostDatabasesMysqlInstanceBackupRequest | Information about the snapshot backup to create. (optional)

    try:
        # Create a managed MySQL database backup snapshot
        api_response = api_instance.post_databases_mysql_instance_backup(api_version, instance_id, post_databases_mysql_instance_backup_request=post_databases_mysql_instance_backup_request)
        print("The response of DatabasesApi->post_databases_mysql_instance_backup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->post_databases_mysql_instance_backup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **instance_id** | **int**| The ID of the Managed PostgreSQL Database. | 
 **post_databases_mysql_instance_backup_request** | [**PostDatabasesMysqlInstanceBackupRequest**](PostDatabasesMysqlInstanceBackupRequest.md)| Information about the snapshot backup to create. | [optional] 

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
**200** | Database snapshot backup request successful. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_databases_mysql_instance_backup_restore**
> object post_databases_mysql_instance_backup_restore(api_version, instance_id, backup_id)

Restore a managed MySQL database backup

__This operation is currently only available for customers who already have an active Managed Database.__  Restore a backup to a Managed MySQL Database on your Account.  Requires `read_write` access to the Database.  The Database must have an `active`, `degraded`, or `failed` status to perform this operation.  __Note__. Restoring from a backup will erase all existing data on the database instance and replace it with backup data.  __Note__. Currently, restoring a backup after resetting Managed Database credentials results in a failed cluster. Please contact Customer Support if this occurs.   <<LB>>  ---   - __CLI__.      ```     linode-cli databases mysql-backup-restore 123 456     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     databases:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.DatabasesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    instance_id = 56 # int | The ID of the Managed MySQL Database.
    backup_id = 56 # int | The ID of the Managed MySQL Database backup.

    try:
        # Restore a managed MySQL database backup
        api_response = api_instance.post_databases_mysql_instance_backup_restore(api_version, instance_id, backup_id)
        print("The response of DatabasesApi->post_databases_mysql_instance_backup_restore:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->post_databases_mysql_instance_backup_restore: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **instance_id** | **int**| The ID of the Managed MySQL Database. | 
 **backup_id** | **int**| The ID of the Managed MySQL Database backup. | 

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
**200** | Request to restore backup successful. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_databases_mysql_instance_credentials_reset**
> object post_databases_mysql_instance_credentials_reset(api_version, instance_id)

Reset managed MySQL database credentials

__This operation is currently only available for customers who already have an active Managed Database.__  Reset the root password for a Managed MySQL Database.  Requires `read_write` access to the Database.  A new root password is randomly generated and accessible with the [Get managed MySQL database credentials](https://techdocs.akamai.com/linode-api/reference/get-databases-mysql-instance-credentials) operation.  Only unrestricted Users can access this operation, and have access regardless of the acting token's OAuth scopes.  __Note__. It may take several seconds for credentials to reset.   <<LB>>  ---   - __CLI__.      ```     linode-cli databases mysql-creds-reset 123     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     databases:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.DatabasesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    instance_id = 56 # int | The ID of the Managed MySQL Database.

    try:
        # Reset managed MySQL database credentials
        api_response = api_instance.post_databases_mysql_instance_credentials_reset(api_version, instance_id)
        print("The response of DatabasesApi->post_databases_mysql_instance_credentials_reset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->post_databases_mysql_instance_credentials_reset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **instance_id** | **int**| The ID of the Managed MySQL Database. | 

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
**200** | Managed Database instance credentials successfully reset. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_databases_mysql_instance_patch**
> object post_databases_mysql_instance_patch(api_version, instance_id)

Patch a managed MySQL database

__This operation is currently only available for customers who already have an active Managed Database.__  Apply security patches and updates to the underlying operating system of the Managed MySQL Database. This function runs during regular maintenance windows, which are configurable with the [Update a managed MySQL database](https://techdocs.akamai.com/linode-api/reference/put-databases-mysql-instance) operation.  Requires `read_write` access to the Database.  The Database must have an `active` status to perform this operation.  __Note__  - If your database cluster is configured with a single node, you will experience downtime during this maintenance. Consider upgrading to a high availability plan to avoid any downtime due to maintenance.  - __The database software is not updated automatically.__ To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then [migrate your databases](https://www.linode.com/docs/products/databases/managed-databases/guides/migrate-mysql/) from the original Managed Database cluster to the new one.   <<LB>>  ---   - __CLI__.      ```     linode-cli databases mysql-patch 123     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     databases:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.DatabasesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    instance_id = 56 # int | The ID of the Managed PostgreSQL Database.

    try:
        # Patch a managed MySQL database
        api_response = api_instance.post_databases_mysql_instance_patch(api_version, instance_id)
        print("The response of DatabasesApi->post_databases_mysql_instance_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->post_databases_mysql_instance_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **instance_id** | **int**| The ID of the Managed PostgreSQL Database. | 

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
**200** | Managed Database instance patch request successful. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_databases_mysql_instances**
> GetDatabasesMysqlInstances200ResponseAllOfDataInner post_databases_mysql_instances(api_version, post_databases_mysql_instances_request)

Create a managed MySQL database

__This operation is currently only available for customers who already have an active Managed Database.__  Provision a Managed MySQL Database.  Restricted Users must have the `add_databases` grant to use this operation.  New instances can take approximately 15 to 30 minutes to provision.  The `allow_list` is used to control access to the Managed Database.  - IP addresses and ranges in this list can access the Managed Database. All other sources are blocked.  - If `0.0.0.0/0` is a value in this list, then all IP addresses can access the Managed Database.  - Entering an empty array (`[]`) blocks all connections (both public and private) to the Managed Database.  All Managed Databases include automatic, daily backups. Up to seven backups are automatically stored for each Managed Database, providing restore points for each day of the past week.  All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed MySQL Database during configurable maintenance windows.  - If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It's recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.  - __The database software is not updated automatically.__ To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then [migrate your databases](https://www.linode.com/docs/products/databases/managed-databases/guides/migrate-mysql/) from the original Managed Database cluster to the new one.  - To modify update the maintenance window for a Database, run the [Update a managed MySQL database](https://techdocs.akamai.com/linode-api/reference/put-databases-mysql-instance) operation.   <<LB>>  ---   - __CLI__.      ```     linode-cli databases mysql-create \\   --label example-db1 \\   --region us-east \\   --type g6-dedicated-2 \\   --cluster_size 3 \\   --engine mysql/8.0.26 \\   --encrypted false \\   --ssl_connection false \\   --replication_type semi_synch \\   --allow_list 203.0.113.1 \\   --allow_list 192.0.1.0/24     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     databases:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_databases_mysql_instances200_response_all_of_data_inner import GetDatabasesMysqlInstances200ResponseAllOfDataInner
from openapi_client.models.post_databases_mysql_instances_request import PostDatabasesMysqlInstancesRequest
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
    api_instance = openapi_client.DatabasesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    post_databases_mysql_instances_request = openapi_client.PostDatabasesMysqlInstancesRequest() # PostDatabasesMysqlInstancesRequest | Information about the Managed MySQL Database you are creating.

    try:
        # Create a managed MySQL database
        api_response = api_instance.post_databases_mysql_instances(api_version, post_databases_mysql_instances_request)
        print("The response of DatabasesApi->post_databases_mysql_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->post_databases_mysql_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **post_databases_mysql_instances_request** | [**PostDatabasesMysqlInstancesRequest**](PostDatabasesMysqlInstancesRequest.md)| Information about the Managed MySQL Database you are creating. | 

### Return type

[**GetDatabasesMysqlInstances200ResponseAllOfDataInner**](GetDatabasesMysqlInstances200ResponseAllOfDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A new Managed MySQL Database is provisioning. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_databases_postgre_sql_instance_backup**
> object post_databases_postgre_sql_instance_backup(api_version, instance_id, post_databases_mysql_instance_backup_request=post_databases_mysql_instance_backup_request)

Create a managed PostgreSQL database backup snapshot

__This operation is currently only available for customers who already have an active Managed Database.__  Creates a snapshot backup of a Managed PostgreSQL Database.  Requires `read_write` access to the Database.  Up to 3 snapshot backups for each Database can be stored at a time. If 3 snapshots have been created for a Database, one must be deleted before another can be made.  Backups generated by this operation have the type `snapshot`. Snapshot backups may take several minutes to complete, after which they will be accessible to view or restore.  The Database must have an `active` status to perform this operation. If another backup is in progress, it must complete before a new backup can be initiated.   <<LB>>  ---   - __CLI__.      ```     linode-cli databases postgresql-backup-snapshot 123 \\   --label snapshot1 \\   --target primary     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     databases:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.post_databases_mysql_instance_backup_request import PostDatabasesMysqlInstanceBackupRequest
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
    api_instance = openapi_client.DatabasesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    instance_id = 56 # int | The ID of the Managed PostgreSQL Database.
    post_databases_mysql_instance_backup_request = openapi_client.PostDatabasesMysqlInstanceBackupRequest() # PostDatabasesMysqlInstanceBackupRequest | Information about the snapshot backup to create. (optional)

    try:
        # Create a managed PostgreSQL database backup snapshot
        api_response = api_instance.post_databases_postgre_sql_instance_backup(api_version, instance_id, post_databases_mysql_instance_backup_request=post_databases_mysql_instance_backup_request)
        print("The response of DatabasesApi->post_databases_postgre_sql_instance_backup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->post_databases_postgre_sql_instance_backup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **instance_id** | **int**| The ID of the Managed PostgreSQL Database. | 
 **post_databases_mysql_instance_backup_request** | [**PostDatabasesMysqlInstanceBackupRequest**](PostDatabasesMysqlInstanceBackupRequest.md)| Information about the snapshot backup to create. | [optional] 

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
**200** | Database snapshot backup request successful. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_databases_postgre_sql_instance_backup_restore**
> object post_databases_postgre_sql_instance_backup_restore(api_version, instance_id, backup_id)

Restore a managed PostgreSQL database backup

__This operation is currently only available for customers who already have an active Managed Database.__  Restore a backup to a Managed PostgreSQL Database on your Account.  Requires `read_write` access to the Database.  The Database must have an `active`, `degraded`, or `failed` status to perform this operation.  __Note__. Restoring from a backup will erase all existing data on the database instance and replace it with backup data.  __Note__. Currently, restoring a backup after resetting Managed Database credentials results in a failed cluster. Please contact Customer Support if this occurs.   <<LB>>  ---   - __CLI__.      ```     linode-cli databases postgresql-backup-restore 123 456     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     databases:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.DatabasesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    instance_id = 56 # int | The ID of the Managed PostgreSQL Database.
    backup_id = 56 # int | The ID of the Managed PostgreSQL Database backup.

    try:
        # Restore a managed PostgreSQL database backup
        api_response = api_instance.post_databases_postgre_sql_instance_backup_restore(api_version, instance_id, backup_id)
        print("The response of DatabasesApi->post_databases_postgre_sql_instance_backup_restore:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->post_databases_postgre_sql_instance_backup_restore: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **instance_id** | **int**| The ID of the Managed PostgreSQL Database. | 
 **backup_id** | **int**| The ID of the Managed PostgreSQL Database backup. | 

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
**200** | Request to restore backup successful. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_databases_postgre_sql_instance_credentials_reset**
> object post_databases_postgre_sql_instance_credentials_reset(api_version, instance_id)

Reset managed PostgreSQL database credentials

__This operation is currently only available for customers who already have an active Managed Database.__  Reset the root password for a Managed PostgreSQL Database.  Requires `read_write` access to the Database.  A new root password is randomly generated and accessible with the [Get managed PostgreSQL database credentials](https://techdocs.akamai.com/linode-api/reference/get-databases-postgre-sql-instance-credentials) operation.  Only unrestricted Users can access this operation, and have access regardless of the acting token's OAuth scopes.  __Note__. It may take several seconds for credentials to reset.   <<LB>>  ---   - __CLI__.      ```     linode-cli databases postgresql-creds-reset 123     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     databases:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.DatabasesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    instance_id = 56 # int | The ID of the Managed PostgreSQL Database.

    try:
        # Reset managed PostgreSQL database credentials
        api_response = api_instance.post_databases_postgre_sql_instance_credentials_reset(api_version, instance_id)
        print("The response of DatabasesApi->post_databases_postgre_sql_instance_credentials_reset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->post_databases_postgre_sql_instance_credentials_reset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **instance_id** | **int**| The ID of the Managed PostgreSQL Database. | 

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
**200** | Managed Database instance credentials successfully reset. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_databases_postgre_sql_instance_patch**
> object post_databases_postgre_sql_instance_patch(api_version, instance_id)

Patch a managed PostgreSQL database

__This operation is currently only available for customers who already have an active Managed Database.__  Apply security patches and updates to the underlying operating system of the Managed PostgreSQL Database. This function runs during regular maintenance windows, which are configurable with the [Update a managed PostgreSQL database](https://techdocs.akamai.com/linode-api/reference/put-databases-postgre-sql-instance) operation.  Requires `read_write` access to the Database.  The Database must have an `active` status to perform this operation.  __Note__  - If your database cluster is configured with a single node, you will experience downtime during this maintenance. Consider upgrading to a high availability plan to avoid any downtime due to maintenance.  - __The database software is not updated automatically.__ To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one.   <<LB>>  ---   - __CLI__.      ```     linode-cli databases postgresql-patch 123     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     databases:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.DatabasesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    instance_id = 56 # int | The ID of the Managed PostgreSQL Database.

    try:
        # Patch a managed PostgreSQL database
        api_response = api_instance.post_databases_postgre_sql_instance_patch(api_version, instance_id)
        print("The response of DatabasesApi->post_databases_postgre_sql_instance_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->post_databases_postgre_sql_instance_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **instance_id** | **int**| The ID of the Managed PostgreSQL Database. | 

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
**200** | Managed Database instance patch request successful. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_databases_postgre_sql_instances**
> GetDatabasesPostgreSqlInstances200ResponseAllOfDataInner post_databases_postgre_sql_instances(api_version, post_databases_postgre_sql_instances_request)

Create a managed PostgreSQL database

__This operation is currently only available for customers who already have an active Managed Database.__  Provision a Managed PostgreSQL Database.  Restricted Users must have the `add_databases` grant to use this operation.  New instances can take approximately 15 to 30 minutes to provision.  The `allow_list` is used to control access to the Managed Database.  - IP addresses and ranges in this list can access the Managed Database. All other sources are blocked.  - If `0.0.0.0/0` is a value in this list, then all IP addresses can access the Managed Database.  - Entering an empty array (`[]`) blocks all connections (both public and private) to the Managed Database.  All Managed Databases include automatic, daily backups. Up to seven backups are automatically stored for each Managed Database, providing restore points for each day of the past week.  All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed PostgreSQL Database during configurable maintenance windows.  - If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It's recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.  - __The database software is not updated automatically.__ To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one.  - To modify update the maintenance window for a Database, run the [Update a managed PostgreSQL database](https://techdocs.akamai.com/linode-api/reference/put-databases-postgre-sql-instance) operation.   <<LB>>  ---   - __CLI__.      ```     linode-cli databases postgresql-create \\   --label example-db \\   --region us-east \\   --type g6-dedicated-2 \\   --cluster_size 3 \\   --engine postgresql/13.2 \\   --encrypted false \\   --ssl_connection false \\   --replication_type asynch \\   --replication_commit_type local \\   --allow_list 203.0.113.1 \\   --allow_list 192.0.1.0/24     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     databases:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_databases_postgre_sql_instances200_response_all_of_data_inner import GetDatabasesPostgreSqlInstances200ResponseAllOfDataInner
from openapi_client.models.post_databases_postgre_sql_instances_request import PostDatabasesPostgreSqlInstancesRequest
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
    api_instance = openapi_client.DatabasesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    post_databases_postgre_sql_instances_request = openapi_client.PostDatabasesPostgreSqlInstancesRequest() # PostDatabasesPostgreSqlInstancesRequest | Information about the Managed PostgreSQL Database you are creating.

    try:
        # Create a managed PostgreSQL database
        api_response = api_instance.post_databases_postgre_sql_instances(api_version, post_databases_postgre_sql_instances_request)
        print("The response of DatabasesApi->post_databases_postgre_sql_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->post_databases_postgre_sql_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **post_databases_postgre_sql_instances_request** | [**PostDatabasesPostgreSqlInstancesRequest**](PostDatabasesPostgreSqlInstancesRequest.md)| Information about the Managed PostgreSQL Database you are creating. | 

### Return type

[**GetDatabasesPostgreSqlInstances200ResponseAllOfDataInner**](GetDatabasesPostgreSqlInstances200ResponseAllOfDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A new Managed PostgreSQL Database is provisioning. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_databases_mysql_instance**
> GetDatabasesMysqlInstances200ResponseAllOfDataInner put_databases_mysql_instance(api_version, instance_id, put_databases_mysql_instance_request)

Update a managed MySQL database

__This operation is currently only available for customers who already have an active Managed Database.__  Update a Managed MySQL Database.  Requires `read_write` access to the Database.  The Database must have an `active` status to perform this operation.  Updating addresses in the `allow_list` overwrites any existing addresses.  - IP addresses and ranges in this list can access the Managed Database. All other sources are blocked.  - If `0.0.0.0/0` is a value in this list, then all IP addresses can access the Managed Database.  - Entering an empty array (`[]`) blocks all connections (both public and private) to the Managed Database.  - __Note__. Updates to the `allow_list` may take a short period of time to complete, making this operation inappropriate for rapid successive updates to this property.  All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed MySQL Database. The maintenance window for these updates is configured with the Managed Database's `updates` property.  - If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It's recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.  - __The database software is not updated automatically.__ To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then [migrate your databases](https://www.linode.com/docs/products/databases/managed-databases/guides/migrate-mysql/) from the original Managed Database cluster to the new one.   <<LB>>  ---   - __CLI__.      ```     linode-cli databases mysql-update 123 \\   --label example-db \\   --allow_list 203.0.113.1 \\   --allow_list 192.0.1.0/24 \\   --type g6-standard-1 \\   --updates.frequency monthly \\   --updates.duration 3 \\   --updates.hour_of_day 12 \\   --updates.day_of_week 4 \\   --updates.week_of_month 3     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     databases:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_databases_mysql_instances200_response_all_of_data_inner import GetDatabasesMysqlInstances200ResponseAllOfDataInner
from openapi_client.models.put_databases_mysql_instance_request import PutDatabasesMysqlInstanceRequest
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
    api_instance = openapi_client.DatabasesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    instance_id = 56 # int | The ID of the Managed PostgreSQL Database.
    put_databases_mysql_instance_request = openapi_client.PutDatabasesMysqlInstanceRequest() # PutDatabasesMysqlInstanceRequest | Updated information for the Managed MySQL Database.

    try:
        # Update a managed MySQL database
        api_response = api_instance.put_databases_mysql_instance(api_version, instance_id, put_databases_mysql_instance_request)
        print("The response of DatabasesApi->put_databases_mysql_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->put_databases_mysql_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **instance_id** | **int**| The ID of the Managed PostgreSQL Database. | 
 **put_databases_mysql_instance_request** | [**PutDatabasesMysqlInstanceRequest**](PutDatabasesMysqlInstanceRequest.md)| Updated information for the Managed MySQL Database. | 

### Return type

[**GetDatabasesMysqlInstances200ResponseAllOfDataInner**](GetDatabasesMysqlInstances200ResponseAllOfDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Managed Database updated successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_databases_postgre_sql_instance**
> GetDatabasesPostgreSqlInstances200ResponseAllOfDataInner put_databases_postgre_sql_instance(api_version, instance_id, put_databases_postgre_sql_instance_request)

Update a managed PostgreSQL database

__This operation is currently only available for customers who already have an active Managed Database.__  Update a Managed PostgreSQL Database.  Requires `read_write` access to the Database.  The Database must have an `active` status to perform this operation.  Updating addresses in the `allow_list` overwrites any existing addresses.  - IP addresses and ranges in this list can access the Managed Database. All other sources are blocked.  - If `0.0.0.0/0` is a value in this list, then all IP addresses can access the Managed Database.  - Entering an empty array (`[]`) blocks all connections (both public and private) to the Managed Database.  - __Note__. Updates to the `allow_list` may take a short period of time to complete, making this operation inappropriate for rapid successive updates to this property.  All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed PostgreSQL Database. The maintenance window for these updates is configured with the Managed Database's `updates` property.  - If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It's recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.  - __The database software is not updated automatically.__ To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one.   <<LB>>  ---   - __CLI__.      ```     linode-cli databases postgresql-update 123 \\   --label example-db \\   --allow_list 203.0.113.1 \\   --allow_list 192.0.1.0/24 \\   --type g6-standard-1 \\   --updates.frequency monthly \\   --updates.duration 3 \\   --updates.hour_of_day 12 \\   --updates.day_of_week 4 \\   --updates.week_of_month 3     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     databases:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_databases_postgre_sql_instances200_response_all_of_data_inner import GetDatabasesPostgreSqlInstances200ResponseAllOfDataInner
from openapi_client.models.put_databases_postgre_sql_instance_request import PutDatabasesPostgreSqlInstanceRequest
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
    api_instance = openapi_client.DatabasesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    instance_id = 56 # int | The ID of the Managed PostgreSQL Database.
    put_databases_postgre_sql_instance_request = openapi_client.PutDatabasesPostgreSqlInstanceRequest() # PutDatabasesPostgreSqlInstanceRequest | Updated information for the Managed PostgreSQL Database.

    try:
        # Update a managed PostgreSQL database
        api_response = api_instance.put_databases_postgre_sql_instance(api_version, instance_id, put_databases_postgre_sql_instance_request)
        print("The response of DatabasesApi->put_databases_postgre_sql_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->put_databases_postgre_sql_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **instance_id** | **int**| The ID of the Managed PostgreSQL Database. | 
 **put_databases_postgre_sql_instance_request** | [**PutDatabasesPostgreSqlInstanceRequest**](PutDatabasesPostgreSqlInstanceRequest.md)| Updated information for the Managed PostgreSQL Database. | 

### Return type

[**GetDatabasesPostgreSqlInstances200ResponseAllOfDataInner**](GetDatabasesPostgreSqlInstances200ResponseAllOfDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Managed Database updated successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

