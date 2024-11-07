# openapi_client.ObjectStorageApi

All URIs are relative to *https://api.linode.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_object_storage_bucket**](ObjectStorageApi.md#delete_object_storage_bucket) | **DELETE** /{apiVersion}/object-storage/buckets/{regionId}/{bucket} | Remove an Object Storage bucket
[**delete_object_storage_key**](ObjectStorageApi.md#delete_object_storage_key) | **DELETE** /{apiVersion}/object-storage/keys/{keyId} | Revoke an Object Storage key
[**delete_object_storage_ssl**](ObjectStorageApi.md#delete_object_storage_ssl) | **DELETE** /{apiVersion}/object-storage/buckets/{regionId}/{bucket}/ssl | Delete an Object Storage TLS/SSL certificate
[**get_object_storage_bucket**](ObjectStorageApi.md#get_object_storage_bucket) | **GET** /{apiVersion}/object-storage/buckets/{regionId}/{bucket} | Get an Object Storage bucket
[**get_object_storage_bucket_acl**](ObjectStorageApi.md#get_object_storage_bucket_acl) | **GET** /{apiVersion}/object-storage/buckets/{regionId}/{bucket}/object-acl | Get an Object Storage object ACL config
[**get_object_storage_bucket_content**](ObjectStorageApi.md#get_object_storage_bucket_content) | **GET** /{apiVersion}/object-storage/buckets/{regionId}/{bucket}/object-list | List Object Storage bucket contents
[**get_object_storage_bucketin_cluster**](ObjectStorageApi.md#get_object_storage_bucketin_cluster) | **GET** /{apiVersion}/object-storage/buckets/{regionId} | List Object Storage buckets per region
[**get_object_storage_buckets**](ObjectStorageApi.md#get_object_storage_buckets) | **GET** /{apiVersion}/object-storage/buckets | List Object Storage buckets
[**get_object_storage_cluster**](ObjectStorageApi.md#get_object_storage_cluster) | **GET** /{apiVersion}/object-storage/clusters/{clusterId} | Get a cluster
[**get_object_storage_clusters**](ObjectStorageApi.md#get_object_storage_clusters) | **GET** /{apiVersion}/object-storage/clusters | List clusters
[**get_object_storage_key**](ObjectStorageApi.md#get_object_storage_key) | **GET** /{apiVersion}/object-storage/keys/{keyId} | Get an Object Storage key
[**get_object_storage_keys**](ObjectStorageApi.md#get_object_storage_keys) | **GET** /{apiVersion}/object-storage/keys | List Object Storage keys
[**get_object_storage_ssl**](ObjectStorageApi.md#get_object_storage_ssl) | **GET** /{apiVersion}/object-storage/buckets/{regionId}/{bucket}/ssl | Get an Object Storage TLS/SSL certificate
[**get_object_storage_transfer**](ObjectStorageApi.md#get_object_storage_transfer) | **GET** /{apiVersion}/object-storage/transfer | Get Object Storage transfer data
[**get_object_storage_types**](ObjectStorageApi.md#get_object_storage_types) | **GET** /{apiVersion}/object-storage/types | List Object Storage types
[**post_cancel_object_storage**](ObjectStorageApi.md#post_cancel_object_storage) | **POST** /{apiVersion}/object-storage/cancel | Cancel Object Storage
[**post_object_storage_bucket**](ObjectStorageApi.md#post_object_storage_bucket) | **POST** /{apiVersion}/object-storage/buckets | Create an Object Storage bucket
[**post_object_storage_bucket_access**](ObjectStorageApi.md#post_object_storage_bucket_access) | **POST** /{apiVersion}/object-storage/buckets/{regionId}/{bucket}/access | Modify access to an Object Storage bucket
[**post_object_storage_keys**](ObjectStorageApi.md#post_object_storage_keys) | **POST** /{apiVersion}/object-storage/keys | Create an Object Storage key
[**post_object_storage_object_url**](ObjectStorageApi.md#post_object_storage_object_url) | **POST** /{apiVersion}/object-storage/buckets/{regionId}/{bucket}/object-url | Create a URL for an object
[**post_object_storage_ssl**](ObjectStorageApi.md#post_object_storage_ssl) | **POST** /{apiVersion}/object-storage/buckets/{regionId}/{bucket}/ssl | Upload an Object Storage TLS/SSL certificate
[**put_object_storage_bucket_acl**](ObjectStorageApi.md#put_object_storage_bucket_acl) | **PUT** /{apiVersion}/object-storage/buckets/{regionId}/{bucket}/object-acl | Update an object&#39;s ACL config
[**put_object_storage_key**](ObjectStorageApi.md#put_object_storage_key) | **PUT** /{apiVersion}/object-storage/keys/{keyId} | Update an Object Storage key
[**put_storage_bucket_access**](ObjectStorageApi.md#put_storage_bucket_access) | **PUT** /{apiVersion}/object-storage/buckets/{regionId}/{bucket}/access | Update access to an Object Storage bucket


# **delete_object_storage_bucket**
> object delete_object_storage_bucket(api_version, region_id, bucket)

Remove an Object Storage bucket

Removes a single bucket.  > 📘 > > - You need to remove all objects from a bucket before you can delete it. While you *can* delete a bucket using the [s3cmd command-line tool](https://www.linode.com/docs/products/storage/object-storage/guides/s3cmd/#delete-a-bucket), this operation fails if the bucket contains too many objects. The best way to empty large buckets is to use the [S3 API to configure lifecycle policies](https://docs.ceph.com/en/latest/radosgw/bucketpolicy/#). Set a policy to remove all objects, wait a day or more for the system to remove all objects, then delete the bucket. > > - The [S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#delete-bucket) equivalent operation offers more detail.   <<LB>>  ---   - __OAuth scopes__.      ```     object_storage:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.ObjectStorageApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    region_id = 'region_id_example' # str | Identifies a region where this bucket lives.  > 📘 > > You can use a `clusterId` in place of `regionId` in requests for buckets that you created using the legacy version of the API. Run [List clusters](https://techdocs.akamai.com/linode-api/reference/get-object-storage-clusters) to see each cluster `id`.
    bucket = 'bucket_example' # str | The bucket name.

    try:
        # Remove an Object Storage bucket
        api_response = api_instance.delete_object_storage_bucket(api_version, region_id, bucket)
        print("The response of ObjectStorageApi->delete_object_storage_bucket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStorageApi->delete_object_storage_bucket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **region_id** | **str**| Identifies a region where this bucket lives.  &gt; 📘 &gt; &gt; You can use a &#x60;clusterId&#x60; in place of &#x60;regionId&#x60; in requests for buckets that you created using the legacy version of the API. Run [List clusters](https://techdocs.akamai.com/linode-api/reference/get-object-storage-clusters) to see each cluster &#x60;id&#x60;. | 
 **bucket** | **str**| The bucket name. | 

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
**200** | Bucket deleted successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_object_storage_key**
> object delete_object_storage_key(api_version, key_id)

Revoke an Object Storage key

Revokes an Object Storage Key. This keypair will no longer be usable by third-party clients.  - A successful request triggers an `obj_access_key_delete` event.   <<LB>>  ---   - __CLI__.      ```     linode-cli object-storage keys-delete 12345     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     object_storage:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.ObjectStorageApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    key_id = 56 # int | The key to look up.

    try:
        # Revoke an Object Storage key
        api_response = api_instance.delete_object_storage_key(api_version, key_id)
        print("The response of ObjectStorageApi->delete_object_storage_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStorageApi->delete_object_storage_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **key_id** | **int**| The key to look up. | 

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
**200** | Deletion successful. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_object_storage_ssl**
> object delete_object_storage_ssl(api_version, region_id, bucket)

Delete an Object Storage TLS/SSL certificate

Deletes this Object Storage bucket's user uploaded TLS/SSL certificate and private key.   <<LB>>  ---   - __CLI__.      ```     linode-cli object-storage ssl-delete \\   us-east-1 example-bucket     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     object_storage:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.ObjectStorageApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    region_id = 'region_id_example' # str | Identifies a region where this bucket lives.  > 📘 > > You can use a `clusterId` in place of `regionId` in requests for buckets that you created using the legacy version of the API. Run [List clusters](https://techdocs.akamai.com/linode-api/reference/get-object-storage-clusters) to see each cluster `id`.
    bucket = 'bucket_example' # str | The bucket name.

    try:
        # Delete an Object Storage TLS/SSL certificate
        api_response = api_instance.delete_object_storage_ssl(api_version, region_id, bucket)
        print("The response of ObjectStorageApi->delete_object_storage_ssl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStorageApi->delete_object_storage_ssl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **region_id** | **str**| Identifies a region where this bucket lives.  &gt; 📘 &gt; &gt; You can use a &#x60;clusterId&#x60; in place of &#x60;regionId&#x60; in requests for buckets that you created using the legacy version of the API. Run [List clusters](https://techdocs.akamai.com/linode-api/reference/get-object-storage-clusters) to see each cluster &#x60;id&#x60;. | 
 **bucket** | **str**| The bucket name. | 

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
**200** | Deletes this Object Storage bucket&#39;s user uploaded TLS/SSL certificate and private key. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_storage_bucket**
> GetObjectStorageBuckets200ResponseDataInner get_object_storage_bucket(api_version, region_id, bucket)

Get an Object Storage bucket

Returns a single Object Storage bucket.  > 📘 > > The [S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#get-bucket) equivalent operation offers more detail.   <<LB>>  ---   - __OAuth scopes__.      ```     object_storage:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_object_storage_buckets200_response_data_inner import GetObjectStorageBuckets200ResponseDataInner
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
    api_instance = openapi_client.ObjectStorageApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    region_id = 'region_id_example' # str | Identifies a region where this bucket lives.  > 📘 > > You can use a `clusterId` in place of `regionId` in requests for buckets that you created using the legacy version of the API. Run [List clusters](https://techdocs.akamai.com/linode-api/reference/get-object-storage-clusters) to see each cluster `id`.
    bucket = 'bucket_example' # str | The bucket name.

    try:
        # Get an Object Storage bucket
        api_response = api_instance.get_object_storage_bucket(api_version, region_id, bucket)
        print("The response of ObjectStorageApi->get_object_storage_bucket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStorageApi->get_object_storage_bucket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **region_id** | **str**| Identifies a region where this bucket lives.  &gt; 📘 &gt; &gt; You can use a &#x60;clusterId&#x60; in place of &#x60;regionId&#x60; in requests for buckets that you created using the legacy version of the API. Run [List clusters](https://techdocs.akamai.com/linode-api/reference/get-object-storage-clusters) to see each cluster &#x60;id&#x60;. | 
 **bucket** | **str**| The bucket name. | 

### Return type

[**GetObjectStorageBuckets200ResponseDataInner**](GetObjectStorageBuckets200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested bucket. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_storage_bucket_acl**
> GetObjectStorageBucketAcl200Response get_object_storage_bucket_acl(api_version, region_id, bucket, name)

Get an Object Storage object ACL config

View an Object's configured Access Control List (ACL) in this Object Storage bucket. ACLs define who can access your buckets and objects and specify the level of access granted to those users.  > 📘 > > The [S3 API](https://docs.ceph.com/en/latest/radosgw/s3/objectops/#get-object-acl) equivalent operation offers more detail.   <<LB>>  ---   - __OAuth scopes__.      ```     object_storage:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_object_storage_bucket_acl200_response import GetObjectStorageBucketAcl200Response
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
    api_instance = openapi_client.ObjectStorageApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    region_id = 'region_id_example' # str | Identifies a region where this bucket lives.  > 📘 > > You can use a `clusterId` in place of `regionId` in requests for buckets that you created using the legacy version of the API. Run [List clusters](https://techdocs.akamai.com/linode-api/reference/get-object-storage-clusters) to see each cluster `id`.
    bucket = 'bucket_example' # str | The bucket name.
    name = 'name_example' # str | The `name` of the object for which to retrieve its Access Control List (ACL). Run the [List Object Storage bucket contents](https://techdocs.akamai.com/linode-api/reference/get-object-storage-bucket-content) operation to access all object names in a bucket.

    try:
        # Get an Object Storage object ACL config
        api_response = api_instance.get_object_storage_bucket_acl(api_version, region_id, bucket, name)
        print("The response of ObjectStorageApi->get_object_storage_bucket_acl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStorageApi->get_object_storage_bucket_acl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **region_id** | **str**| Identifies a region where this bucket lives.  &gt; 📘 &gt; &gt; You can use a &#x60;clusterId&#x60; in place of &#x60;regionId&#x60; in requests for buckets that you created using the legacy version of the API. Run [List clusters](https://techdocs.akamai.com/linode-api/reference/get-object-storage-clusters) to see each cluster &#x60;id&#x60;. | 
 **bucket** | **str**| The bucket name. | 
 **name** | **str**| The &#x60;name&#x60; of the object for which to retrieve its Access Control List (ACL). Run the [List Object Storage bucket contents](https://techdocs.akamai.com/linode-api/reference/get-object-storage-bucket-content) operation to access all object names in a bucket. | 

### Return type

[**GetObjectStorageBucketAcl200Response**](GetObjectStorageBucketAcl200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Object&#39;s canned ACL and policy. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_storage_bucket_content**
> GetObjectStorageBucketContent200Response get_object_storage_bucket_content(api_version, region_id, bucket, marker=marker, delimiter=delimiter, prefix=prefix, page_size=page_size)

List Object Storage bucket contents

Returns the contents of a bucket. The contents are paginated using a `marker`, that's the name of the last object on the previous page.  Objects can also be filtered by `prefix` and `delimiter`. See [Filtering and sorting](https://techdocs.akamai.com/linode-api/reference/filtering-and-sorting) for more information.  > 📘 > > The [S3 API](https://docs.ceph.com/en/latest/radosgw/s3/objectops/#get-object) equivalent operation offers more detail.   <<LB>>  ---   - __OAuth scopes__.      ```     object_storage:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_object_storage_bucket_content200_response import GetObjectStorageBucketContent200Response
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
    api_instance = openapi_client.ObjectStorageApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    region_id = 'region_id_example' # str | Identifies a region where this bucket lives.  > 📘 > > You can use a `clusterId` in place of `regionId` in requests for buckets that you created using the legacy version of the API. Run [List clusters](https://techdocs.akamai.com/linode-api/reference/get-object-storage-clusters) to see each cluster `id`.
    bucket = 'bucket_example' # str | The bucket name.
    marker = 'marker_example' # str | The \"marker\" for this request, which can be used to paginate through large buckets. Its value should be the value of the `next_marker` property returned with the last page. Listing bucket contents _does not_ support arbitrary page access. See the `next_marker` property in the responses section for more details. (optional)
    delimiter = 'delimiter_example' # str | The delimiter for object names; if given, object names will be returned up to the first occurrence of this character. This is most commonly used with the `/` character to allow bucket transversal in a manner similar to a filesystem, however any delimiter may be used. Use in conjunction with `prefix` to see object names past the first occurrence of the delimiter. (optional)
    prefix = 'prefix_example' # str | Filters objects returned to only those whose name start with the given prefix. Commonly used in conjunction with `delimiter` to allow transversal of bucket contents in a manner similar to a filesystem. (optional)
    page_size = 100 # int | The number of items to return per page. (optional) (default to 100)

    try:
        # List Object Storage bucket contents
        api_response = api_instance.get_object_storage_bucket_content(api_version, region_id, bucket, marker=marker, delimiter=delimiter, prefix=prefix, page_size=page_size)
        print("The response of ObjectStorageApi->get_object_storage_bucket_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStorageApi->get_object_storage_bucket_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **region_id** | **str**| Identifies a region where this bucket lives.  &gt; 📘 &gt; &gt; You can use a &#x60;clusterId&#x60; in place of &#x60;regionId&#x60; in requests for buckets that you created using the legacy version of the API. Run [List clusters](https://techdocs.akamai.com/linode-api/reference/get-object-storage-clusters) to see each cluster &#x60;id&#x60;. | 
 **bucket** | **str**| The bucket name. | 
 **marker** | **str**| The \&quot;marker\&quot; for this request, which can be used to paginate through large buckets. Its value should be the value of the &#x60;next_marker&#x60; property returned with the last page. Listing bucket contents _does not_ support arbitrary page access. See the &#x60;next_marker&#x60; property in the responses section for more details. | [optional] 
 **delimiter** | **str**| The delimiter for object names; if given, object names will be returned up to the first occurrence of this character. This is most commonly used with the &#x60;/&#x60; character to allow bucket transversal in a manner similar to a filesystem, however any delimiter may be used. Use in conjunction with &#x60;prefix&#x60; to see object names past the first occurrence of the delimiter. | [optional] 
 **prefix** | **str**| Filters objects returned to only those whose name start with the given prefix. Commonly used in conjunction with &#x60;delimiter&#x60; to allow transversal of bucket contents in a manner similar to a filesystem. | [optional] 
 **page_size** | **int**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetObjectStorageBucketContent200Response**](GetObjectStorageBucketContent200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | One page of the requested bucket&#39;s contents. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_storage_bucketin_cluster**
> GetObjectStorageBuckets200Response get_object_storage_bucketin_cluster(api_version, region_id)

List Object Storage buckets per region

Returns a list of buckets on your account, in the specified region.  > 📘 > > The [S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#get-bucket) equivalent operation offers more detail.   <<LB>>  ---   - __OAuth scopes__.      ```     object_storage:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_object_storage_buckets200_response import GetObjectStorageBuckets200Response
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
    api_instance = openapi_client.ObjectStorageApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    region_id = 'region_id_example' # str | Identifies a region where this bucket lives.  > 📘 > > You can use a `clusterId` in place of `regionId` in requests for buckets that you created using the legacy version of the API. Run [List clusters](https://techdocs.akamai.com/linode-api/reference/get-object-storage-clusters) to see each cluster `id`.

    try:
        # List Object Storage buckets per region
        api_response = api_instance.get_object_storage_bucketin_cluster(api_version, region_id)
        print("The response of ObjectStorageApi->get_object_storage_bucketin_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStorageApi->get_object_storage_bucketin_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **region_id** | **str**| Identifies a region where this bucket lives.  &gt; 📘 &gt; &gt; You can use a &#x60;clusterId&#x60; in place of &#x60;regionId&#x60; in requests for buckets that you created using the legacy version of the API. Run [List clusters](https://techdocs.akamai.com/linode-api/reference/get-object-storage-clusters) to see each cluster &#x60;id&#x60;. | 

### Return type

[**GetObjectStorageBuckets200Response**](GetObjectStorageBuckets200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of buckets on your account in this region. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_storage_buckets**
> GetObjectStorageBuckets200Response get_object_storage_buckets(api_version)

List Object Storage buckets

Returns a paginated list of all Object Storage buckets available in your account.  > 📘 > > The [S3 API](https://docs.ceph.com/en/latest/radosgw/s3/serviceops/#list-buckets) equivalent operation offers more detail.   <<LB>>  ---   - __OAuth scopes__.      ```     object_storage:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_object_storage_buckets200_response import GetObjectStorageBuckets200Response
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
    api_instance = openapi_client.ObjectStorageApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)

    try:
        # List Object Storage buckets
        api_response = api_instance.get_object_storage_buckets(api_version)
        print("The response of ObjectStorageApi->get_object_storage_buckets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStorageApi->get_object_storage_buckets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]

### Return type

[**GetObjectStorageBuckets200Response**](GetObjectStorageBuckets200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of buckets you own. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_storage_cluster**
> GetObjectStorageClusters200ResponseDataInner get_object_storage_cluster(api_version, cluster_id)

Get a cluster

__Deprecated__ Returns a single Object Storage cluster.  > 📘 > > This displays deprecated `clusterId` values that represent regions used with older versions of the API. It's maintained for backward compatibility. Run [Get a region](https://techdocs.akamai.com/linode-api/reference/get-region), instead.   <<LB>>  ---   - __CLI__.      ```     linode-cli object-storage clusters-view us-east-1     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)

### Example


```python
import openapi_client
from openapi_client.models.get_object_storage_clusters200_response_data_inner import GetObjectStorageClusters200ResponseDataInner
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
    api_instance = openapi_client.ObjectStorageApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    cluster_id = 'us-east-1' # str | Identifies a cluster where this bucket lives. For backward compatibility with Object Storage in this API.  > 📘 > > You can use the applicable `regionId`, for example `us-west`, in place of the `clusterId`, for example, `us-west-1`. Run [List regions](https://techdocs.akamai.com/linode-api/reference/get-regions) to see all regions.

    try:
        # Get a cluster
        api_response = api_instance.get_object_storage_cluster(api_version, cluster_id)
        print("The response of ObjectStorageApi->get_object_storage_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStorageApi->get_object_storage_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **cluster_id** | **str**| Identifies a cluster where this bucket lives. For backward compatibility with Object Storage in this API.  &gt; 📘 &gt; &gt; You can use the applicable &#x60;regionId&#x60;, for example &#x60;us-west&#x60;, in place of the &#x60;clusterId&#x60;, for example, &#x60;us-west-1&#x60;. Run [List regions](https://techdocs.akamai.com/linode-api/reference/get-regions) to see all regions. | 

### Return type

[**GetObjectStorageClusters200ResponseDataInner**](GetObjectStorageClusters200ResponseDataInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Cluster. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_storage_clusters**
> GetObjectStorageClusters200Response get_object_storage_clusters(api_version)

List clusters

Returns a paginated list of available Object Storage legacy clusters.  > 📘 > > This displays deprecated `clusterId` values that represent regions used with older versions of the API. It's maintained for backward compatibility. Run [Get a region](https://techdocs.akamai.com/linode-api/reference/get-region), instead.   <<LB>>  ---   - __CLI__.      ```     linode-cli object-storage clusters-list     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)

### Example


```python
import openapi_client
from openapi_client.models.get_object_storage_clusters200_response import GetObjectStorageClusters200Response
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
    api_instance = openapi_client.ObjectStorageApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)

    try:
        # List clusters
        api_response = api_instance.get_object_storage_clusters(api_version)
        print("The response of ObjectStorageApi->get_object_storage_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStorageApi->get_object_storage_clusters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]

### Return type

[**GetObjectStorageClusters200Response**](GetObjectStorageClusters200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of available clusters. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_storage_key**
> GetObjectStorageKeys200ResponseDataInner get_object_storage_key(api_version, key_id)

Get an Object Storage key

Returns a single Object Storage key provisioned for your account.   <<LB>>  ---   - __CLI__.      ```     linode-cli object-storage keys-view \\   --keyId 12345     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     object_storage:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_object_storage_keys200_response_data_inner import GetObjectStorageKeys200ResponseDataInner
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
    api_instance = openapi_client.ObjectStorageApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    key_id = 56 # int | The key to look up.

    try:
        # Get an Object Storage key
        api_response = api_instance.get_object_storage_key(api_version, key_id)
        print("The response of ObjectStorageApi->get_object_storage_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStorageApi->get_object_storage_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **key_id** | **int**| The key to look up. | 

### Return type

[**GetObjectStorageKeys200ResponseDataInner**](GetObjectStorageKeys200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The keypair. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_storage_keys**
> GetObjectStorageKeys200Response get_object_storage_keys(api_version)

List Object Storage keys

Returns a paginated list of Object Storage keys for authenticating to the Object Storage S3 API.   <<LB>>  ---   - __CLI__.      ```     linode-cli object-storage keys-list     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     object_storage:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_object_storage_keys200_response import GetObjectStorageKeys200Response
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
    api_instance = openapi_client.ObjectStorageApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)

    try:
        # List Object Storage keys
        api_response = api_instance.get_object_storage_keys(api_version)
        print("The response of ObjectStorageApi->get_object_storage_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStorageApi->get_object_storage_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]

### Return type

[**GetObjectStorageKeys200Response**](GetObjectStorageKeys200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of Object Storage Keys. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_storage_ssl**
> GetObjectStorageSsl200Response get_object_storage_ssl(api_version, region_id, bucket)

Get an Object Storage TLS/SSL certificate

Returns a boolean value indicating if this bucket has a corresponding TLS/SSL certificate that was uploaded by an Account user.   <<LB>>  ---   - __CLI__.      ```     linode-cli object-storage ssl-view \\   us-east-1 example-bucket     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     object_storage:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_object_storage_ssl200_response import GetObjectStorageSsl200Response
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
    api_instance = openapi_client.ObjectStorageApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    region_id = 'region_id_example' # str | Identifies a region where this bucket lives.  > 📘 > > You can use a `clusterId` in place of `regionId` in requests for buckets that you created using the legacy version of the API. Run [List clusters](https://techdocs.akamai.com/linode-api/reference/get-object-storage-clusters) to see each cluster `id`.
    bucket = 'bucket_example' # str | The bucket name.

    try:
        # Get an Object Storage TLS/SSL certificate
        api_response = api_instance.get_object_storage_ssl(api_version, region_id, bucket)
        print("The response of ObjectStorageApi->get_object_storage_ssl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStorageApi->get_object_storage_ssl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **region_id** | **str**| Identifies a region where this bucket lives.  &gt; 📘 &gt; &gt; You can use a &#x60;clusterId&#x60; in place of &#x60;regionId&#x60; in requests for buckets that you created using the legacy version of the API. Run [List clusters](https://techdocs.akamai.com/linode-api/reference/get-object-storage-clusters) to see each cluster &#x60;id&#x60;. | 
 **bucket** | **str**| The bucket name. | 

### Return type

[**GetObjectStorageSsl200Response**](GetObjectStorageSsl200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a boolean value indicating if this bucket has a corresponding TLS/SSL certificate that was uploaded by an Account user. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_storage_transfer**
> GetObjectStorageTransfer200Response get_object_storage_transfer(api_version)

Get Object Storage transfer data

The amount of outbound data transfer used by your account's Object Storage buckets. Object Storage adds 1 terabyte of outbound data transfer to your data transfer pool. See the [Object Storage Overview](https://www.linode.com/docs/products/storage/object-storage/#pricing) guide for details on Object Storage transfer quotas.   <<LB>>  ---   - __OAuth scopes__.      ```     object_storage:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_object_storage_transfer200_response import GetObjectStorageTransfer200Response
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
    api_instance = openapi_client.ObjectStorageApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)

    try:
        # Get Object Storage transfer data
        api_response = api_instance.get_object_storage_transfer(api_version)
        print("The response of ObjectStorageApi->get_object_storage_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStorageApi->get_object_storage_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]

### Return type

[**GetObjectStorageTransfer200Response**](GetObjectStorageTransfer200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the amount of outbound data transfer used by your account&#39;s Object Storage buckets. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_storage_types**
> GetObjectStorageTypes200Response get_object_storage_types(api_version)

List Object Storage types

Returns Object Storage types and prices, including any region-specific rates.   <<LB>>  ---   - __CLI__.      ```     linode-cli object-storage types     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)

### Example


```python
import openapi_client
from openapi_client.models.get_object_storage_types200_response import GetObjectStorageTypes200Response
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
    api_instance = openapi_client.ObjectStorageApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)

    try:
        # List Object Storage types
        api_response = api_instance.get_object_storage_types(api_version)
        print("The response of ObjectStorageApi->get_object_storage_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStorageApi->get_object_storage_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]

### Return type

[**GetObjectStorageTypes200Response**](GetObjectStorageTypes200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of Object Storage types. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cancel_object_storage**
> object post_cancel_object_storage(api_version)

Cancel Object Storage

Cancel Object Storage on an Account.  __Warning__. This removes all buckets and their contents from your Account. This data is irretrievable once removed.   <<LB>>  ---   - __CLI__.      ```     linode-cli object-storage cancel     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     object_storage:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.ObjectStorageApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)

    try:
        # Cancel Object Storage
        api_response = api_instance.post_cancel_object_storage(api_version)
        print("The response of ObjectStorageApi->post_cancel_object_storage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStorageApi->post_cancel_object_storage: %s\n" % e)
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
**200** | Object Storage cancellation successful. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_object_storage_bucket**
> GetObjectStorageBuckets200ResponseDataInner post_object_storage_bucket(api_version, post_object_storage_bucket_request=post_object_storage_bucket_request)

Create an Object Storage bucket

Creates an Object Storage bucket in the specified data center ([region](https://techdocs.akamai.com/linode-api/reference/get-regions)). If the bucket already exists on your account, this operation returns a 200 response with that bucket as if the API just created it.  > 📘 > > - Accounts with negative balances can't access this operation. > > - The [S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#put-bucket) equivalent operation offers more detail. > > - The API still supports the `clusterId` equivalent (`us-west-1`) when setting a `region` for a new bucket, but you should use the `regionId` (`us-west`), instead.   <<LB>>  ---   - __OAuth scopes__.      ```     object_storage:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_object_storage_buckets200_response_data_inner import GetObjectStorageBuckets200ResponseDataInner
from openapi_client.models.post_object_storage_bucket_request import PostObjectStorageBucketRequest
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
    api_instance = openapi_client.ObjectStorageApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    post_object_storage_bucket_request = openapi_client.PostObjectStorageBucketRequest() # PostObjectStorageBucketRequest | Information about the bucket you want to create. (optional)

    try:
        # Create an Object Storage bucket
        api_response = api_instance.post_object_storage_bucket(api_version, post_object_storage_bucket_request=post_object_storage_bucket_request)
        print("The response of ObjectStorageApi->post_object_storage_bucket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStorageApi->post_object_storage_bucket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **post_object_storage_bucket_request** | [**PostObjectStorageBucketRequest**](PostObjectStorageBucketRequest.md)| Information about the bucket you want to create. | [optional] 

### Return type

[**GetObjectStorageBuckets200ResponseDataInner**](GetObjectStorageBuckets200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The bucket created successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_object_storage_bucket_access**
> object post_object_storage_bucket_access(api_version, region_id, bucket, put_storage_bucket_access_request=put_storage_bucket_access_request)

Modify access to an Object Storage bucket

Apply basic Cross-origin Resource Sharing (CORS) and Access Control Level (ACL) settings. You can configure CORS for all origins and set canned ACL settings.  > 📘 > > For more fine-grained control of both systems, use the [S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#put-bucket-acl).   <<LB>>  ---   - __OAuth scopes__.      ```     object_storage:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.put_storage_bucket_access_request import PutStorageBucketAccessRequest
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
    api_instance = openapi_client.ObjectStorageApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    region_id = 'region_id_example' # str | Identifies a region where this bucket lives.  > 📘 > > You can use a `clusterId` in place of `regionId` in requests for buckets that you created using the legacy version of the API. Run [List clusters](https://techdocs.akamai.com/linode-api/reference/get-object-storage-clusters) to see each cluster `id`.
    bucket = 'bucket_example' # str | The bucket name.
    put_storage_bucket_access_request = openapi_client.PutStorageBucketAccessRequest() # PutStorageBucketAccessRequest | The changes to make to the bucket's access controls. (optional)

    try:
        # Modify access to an Object Storage bucket
        api_response = api_instance.post_object_storage_bucket_access(api_version, region_id, bucket, put_storage_bucket_access_request=put_storage_bucket_access_request)
        print("The response of ObjectStorageApi->post_object_storage_bucket_access:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStorageApi->post_object_storage_bucket_access: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **region_id** | **str**| Identifies a region where this bucket lives.  &gt; 📘 &gt; &gt; You can use a &#x60;clusterId&#x60; in place of &#x60;regionId&#x60; in requests for buckets that you created using the legacy version of the API. Run [List clusters](https://techdocs.akamai.com/linode-api/reference/get-object-storage-clusters) to see each cluster &#x60;id&#x60;. | 
 **bucket** | **str**| The bucket name. | 
 **put_storage_bucket_access_request** | [**PutStorageBucketAccessRequest**](PutStorageBucketAccessRequest.md)| The changes to make to the bucket&#39;s access controls. | [optional] 

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
**200** | Access controls updated. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_object_storage_keys**
> GetObjectStorageKeys200ResponseDataInner post_object_storage_keys(api_version, post_object_storage_keys_request=post_object_storage_keys_request)

Create an Object Storage key

Provisions a new Object Storage key for authenticating to the Object Storage S3 API. A successful request triggers an `obj_access_key_create` [event](https://techdocs.akamai.com/linode-api/reference/get-events).  > 📘 > > Accounts with negative balances can't access this operation.  **The `regions` and `region` parameters**  When creating an Object Storage key, specify one or more data centers ([regions](https://techdocs.akamai.com/linode-api/reference/get-regions)) where you want to create and manage Object Storage buckets.  - **The `regions` array**. Populate it with `regionId` values. The resulting Object Storage key grants access to list and create new buckets in these regions. This *doesn't* give access to manage content in these buckets. To address this, you can:    - Use the `bucket_access` array instead to grant management access, per bucket.    - Use [bucket policies](https://www.linode.com/docs/products/storage/object-storage/guides/bucket-policies/) to change the access for this key.  - **The `bucket_access` array**. This optional array lets you set up limited keys. Include individual objects naming a `regionId`, the target `bucket_name`, and the `permissions` for the Object Storage key. Use the resulting key to manage content in the `bucket_name`, based on the permission level set. You can also use the key to create new buckets in the named region. However, the key doesn't have access to manage content in the newly created bucket. You can grant it this access using [bucket policies](https://www.linode.com/docs/products/storage/object-storage/guides/bucket-policies/).  - **Combine the two to apply varying levels of access in the key**. For example, set `regions` to `us-west` to give the key bucket list and create access in that region. Then, set up the `bucket_access` array to give access to a specific `bucket_name` in the `us-east` region. The key has access to manage content in that `bucket_name` and list and create buckets in the `us-east` region, too. If you include the same region in both, the settings applied in the `bucket_access` array take precedence. For example, assume you include `us-east` in the `regions` array, expecting to only give bucket list and creation access to that region. If you also set `us-east` as a `region` in the `bucket_access` array, the Object Storage key gives access to manage content in the specified `bucket_name`, and lets you list and create buckets in that region.  **The `cluster` parameter (legacy)**  For backward compatibility, include the `cluster` parameter to create an Object Storage key. Use the `clusterId` equivalent (us-west-1) instead of the `regionId` (us-west). Leave the `regions` array out. If including the `bucket_access` array to limit access, omit `region` from each object. Use the resulting key in clusters in all supported regions.  > 📘 > > While the API supports this method, you should use the `regions` parameters, instead.  - **Unlimited access**. Omit the `bucket_access` array. The Object Storage key has unlimited cluster access to all buckets, with all permissions.  - **Limited access**. Include the `bucket_access` array. Set the target `bucket_name` and the level of `permissions` for access to that bucket. Use the resulting key to manage content in the named bucket. A limited Object Storage key can [list all buckets](https://techdocs.akamai.com/linode-api/reference/get-object-storage-buckets) and [create a new bucket](https://techdocs.akamai.com/linode-api/reference/post-object-storage-bucket). However, you can't use the key to perform any actions on a bucket, unless the key has access to it. You can use [bucket policies](https://www.linode.com/docs/products/storage/object-storage/guides/bucket-policies/) to modify a key's access.   <<LB>>  ---   - __CLI__.      ```     linode-cli object-storage keys-create \\   --label \"my-object-storage-key\" \\   --bucket_access '[{\"region\": \"ap-south\", \"bucket_name\": \"bucket-example-1\", \"permissions\": \"read_write\" }]'     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     object_storage:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_object_storage_keys200_response_data_inner import GetObjectStorageKeys200ResponseDataInner
from openapi_client.models.post_object_storage_keys_request import PostObjectStorageKeysRequest
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
    api_instance = openapi_client.ObjectStorageApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    post_object_storage_keys_request = openapi_client.PostObjectStorageKeysRequest() # PostObjectStorageKeysRequest | The settings necessary to create a new key. (optional)

    try:
        # Create an Object Storage key
        api_response = api_instance.post_object_storage_keys(api_version, post_object_storage_keys_request=post_object_storage_keys_request)
        print("The response of ObjectStorageApi->post_object_storage_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStorageApi->post_object_storage_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **post_object_storage_keys_request** | [**PostObjectStorageKeysRequest**](PostObjectStorageKeysRequest.md)| The settings necessary to create a new key. | [optional] 

### Return type

[**GetObjectStorageKeys200ResponseDataInner**](GetObjectStorageKeys200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The new Object Storage key. *This is the only time* the secret key is returned. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_object_storage_object_url**
> PostObjectStorageObjectUrl200Response post_object_storage_object_url(api_version, region_id, bucket, post_object_storage_object_url_request=post_object_storage_object_url_request)

Create a URL for an object

Creates a pre-signed URL to access a single object in a bucket. Use it to share, create, or delete objects by using the appropriate HTTP method in your request body's `method` parameter.  > 📘 > > The [S3 API](https://docs.ceph.com/en/latest/radosgw/s3/) equivalent operation offers more detail.   <<LB>>  ---   - __OAuth scopes__.      ```     object_storage:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.post_object_storage_object_url200_response import PostObjectStorageObjectUrl200Response
from openapi_client.models.post_object_storage_object_url_request import PostObjectStorageObjectUrlRequest
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
    api_instance = openapi_client.ObjectStorageApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    region_id = 'region_id_example' # str | Identifies a region where this bucket lives.  > 📘 > > You can use a `clusterId` in place of `regionId` in requests for buckets that you created using the legacy version of the API. Run [List clusters](https://techdocs.akamai.com/linode-api/reference/get-object-storage-clusters) to see each cluster `id`.
    bucket = 'bucket_example' # str | The bucket name.
    post_object_storage_object_url_request = openapi_client.PostObjectStorageObjectUrlRequest() # PostObjectStorageObjectUrlRequest | Information about the request to sign. (optional)

    try:
        # Create a URL for an object
        api_response = api_instance.post_object_storage_object_url(api_version, region_id, bucket, post_object_storage_object_url_request=post_object_storage_object_url_request)
        print("The response of ObjectStorageApi->post_object_storage_object_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStorageApi->post_object_storage_object_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **region_id** | **str**| Identifies a region where this bucket lives.  &gt; 📘 &gt; &gt; You can use a &#x60;clusterId&#x60; in place of &#x60;regionId&#x60; in requests for buckets that you created using the legacy version of the API. Run [List clusters](https://techdocs.akamai.com/linode-api/reference/get-object-storage-clusters) to see each cluster &#x60;id&#x60;. | 
 **bucket** | **str**| The bucket name. | 
 **post_object_storage_object_url_request** | [**PostObjectStorageObjectUrlRequest**](PostObjectStorageObjectUrlRequest.md)| Information about the request to sign. | [optional] 

### Return type

[**PostObjectStorageObjectUrl200Response**](PostObjectStorageObjectUrl200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The URL with which to access your object. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_object_storage_ssl**
> GetObjectStorageSsl200Response post_object_storage_ssl(api_version, region_id, bucket, post_object_storage_ssl_request=post_object_storage_ssl_request)

Upload an Object Storage TLS/SSL certificate

Upload a TLS/SSL certificate and private key to be served when you visit your Object Storage bucket via HTTPS. Your TLS/SSL certificate and private key are stored encrypted at rest.  To replace an expired certificate, [delete your current certificates](https://techdocs.akamai.com/linode-api/reference/delete-object-storage-ssl) and upload a new one.   <<LB>>  ---   - __CLI__.      ```     linode-cli object-storage ssl-upload \\   us-east-1 example-bucket \\   --certificate \"-----BEGIN CERTIFICATE-----                  CERTIFICATE_INFORMATION                  -----END CERTIFICATE-----\" \\   --private_key \"-----BEGIN PRIVATE KEY-----                  PRIVATE_KEY_INFORMATION                  -----END PRIVATE KEY-----\"     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     object_storage:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_object_storage_ssl200_response import GetObjectStorageSsl200Response
from openapi_client.models.post_object_storage_ssl_request import PostObjectStorageSslRequest
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
    api_instance = openapi_client.ObjectStorageApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    region_id = 'region_id_example' # str | Identifies a region where this bucket lives.  > 📘 > > You can use a `clusterId` in place of `regionId` in requests for buckets that you created using the legacy version of the API. Run [List clusters](https://techdocs.akamai.com/linode-api/reference/get-object-storage-clusters) to see each cluster `id`.
    bucket = 'bucket_example' # str | The bucket name.
    post_object_storage_ssl_request = openapi_client.PostObjectStorageSslRequest() # PostObjectStorageSslRequest | Upload this TLS/SSL certificate with its corresponding secret key. (optional)

    try:
        # Upload an Object Storage TLS/SSL certificate
        api_response = api_instance.post_object_storage_ssl(api_version, region_id, bucket, post_object_storage_ssl_request=post_object_storage_ssl_request)
        print("The response of ObjectStorageApi->post_object_storage_ssl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStorageApi->post_object_storage_ssl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **region_id** | **str**| Identifies a region where this bucket lives.  &gt; 📘 &gt; &gt; You can use a &#x60;clusterId&#x60; in place of &#x60;regionId&#x60; in requests for buckets that you created using the legacy version of the API. Run [List clusters](https://techdocs.akamai.com/linode-api/reference/get-object-storage-clusters) to see each cluster &#x60;id&#x60;. | 
 **bucket** | **str**| The bucket name. | 
 **post_object_storage_ssl_request** | [**PostObjectStorageSslRequest**](PostObjectStorageSslRequest.md)| Upload this TLS/SSL certificate with its corresponding secret key. | [optional] 

### Return type

[**GetObjectStorageSsl200Response**](GetObjectStorageSsl200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response indicates whether this bucket has a corresponding TLS/SSL certificate that was uploaded by a user. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_object_storage_bucket_acl**
> GetObjectStorageBucketAcl200Response put_object_storage_bucket_acl(api_version, region_id, bucket, put_object_storage_bucket_acl_request=put_object_storage_bucket_acl_request)

Update an object's ACL config

Update an object's configured access control level (ACL) in this Object Storage bucket. ACLs define who can access your buckets and objects and specify the level of access granted to those users.  > 📘 > > The [S3 API](https://docs.ceph.com/en/latest/radosgw/s3/objectops/#set-object-acl) equivalent operation offers more detail.   <<LB>>  ---   - __OAuth scopes__.      ```     object_storage:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_object_storage_bucket_acl200_response import GetObjectStorageBucketAcl200Response
from openapi_client.models.put_object_storage_bucket_acl_request import PutObjectStorageBucketAclRequest
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
    api_instance = openapi_client.ObjectStorageApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    region_id = 'region_id_example' # str | Identifies a region where this bucket lives.  > 📘 > > You can use a `clusterId` in place of `regionId` in requests for buckets that you created using the legacy version of the API. Run [List clusters](https://techdocs.akamai.com/linode-api/reference/get-object-storage-clusters) to see each cluster `id`.
    bucket = 'bucket_example' # str | The bucket name.
    put_object_storage_bucket_acl_request = openapi_client.PutObjectStorageBucketAclRequest() # PutObjectStorageBucketAclRequest | The changes to make to this Object's access controls. (optional)

    try:
        # Update an object's ACL config
        api_response = api_instance.put_object_storage_bucket_acl(api_version, region_id, bucket, put_object_storage_bucket_acl_request=put_object_storage_bucket_acl_request)
        print("The response of ObjectStorageApi->put_object_storage_bucket_acl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStorageApi->put_object_storage_bucket_acl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **region_id** | **str**| Identifies a region where this bucket lives.  &gt; 📘 &gt; &gt; You can use a &#x60;clusterId&#x60; in place of &#x60;regionId&#x60; in requests for buckets that you created using the legacy version of the API. Run [List clusters](https://techdocs.akamai.com/linode-api/reference/get-object-storage-clusters) to see each cluster &#x60;id&#x60;. | 
 **bucket** | **str**| The bucket name. | 
 **put_object_storage_bucket_acl_request** | [**PutObjectStorageBucketAclRequest**](PutObjectStorageBucketAclRequest.md)| The changes to make to this Object&#39;s access controls. | [optional] 

### Return type

[**GetObjectStorageBucketAcl200Response**](GetObjectStorageBucketAcl200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Object&#39;s canned ACL and policy. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_object_storage_key**
> PutObjectStorageKey200Response put_object_storage_key(api_version, key_id, put_object_storage_key_request=put_object_storage_key_request)

Update an Object Storage key

Updates an Object Storage key on your account. A successful request triggers an `obj_access_key_update` [event](https://techdocs.akamai.com/linode-api/reference/get-events).   <<LB>>  ---   - __CLI__.      ```     linode-cli object-storage keys-update \\   --keyId 12345   --label \"my-object-storage-key\"     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     object_storage:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.put_object_storage_key200_response import PutObjectStorageKey200Response
from openapi_client.models.put_object_storage_key_request import PutObjectStorageKeyRequest
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
    api_instance = openapi_client.ObjectStorageApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    key_id = 56 # int | The key to look up.
    put_object_storage_key_request = openapi_client.PutObjectStorageKeyRequest() # PutObjectStorageKeyRequest | The fields to update. (optional)

    try:
        # Update an Object Storage key
        api_response = api_instance.put_object_storage_key(api_version, key_id, put_object_storage_key_request=put_object_storage_key_request)
        print("The response of ObjectStorageApi->put_object_storage_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStorageApi->put_object_storage_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **key_id** | **int**| The key to look up. | 
 **put_object_storage_key_request** | [**PutObjectStorageKeyRequest**](PutObjectStorageKeyRequest.md)| The fields to update. | [optional] 

### Return type

[**PutObjectStorageKey200Response**](PutObjectStorageKey200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update Successful. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_storage_bucket_access**
> object put_storage_bucket_access(api_version, region_id, bucket, put_storage_bucket_access_request=put_storage_bucket_access_request)

Update access to an Object Storage bucket

Update basic Cross-origin Resource Sharing (CORS) and Access Control Level (ACL) settings. You can configure CORS for all origins and set canned ACL settings.  > 📘 > > For more fine-grained control of both systems, use the [S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#put-bucket-acl).   <<LB>>  ---   - __OAuth scopes__.      ```     object_storage:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.put_storage_bucket_access_request import PutStorageBucketAccessRequest
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
    api_instance = openapi_client.ObjectStorageApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    region_id = 'region_id_example' # str | Identifies a region where this bucket lives.  > 📘 > > You can use a `clusterId` in place of `regionId` in requests for buckets that you created using the legacy version of the API. Run [List clusters](https://techdocs.akamai.com/linode-api/reference/get-object-storage-clusters) to see each cluster `id`.
    bucket = 'bucket_example' # str | The bucket name.
    put_storage_bucket_access_request = openapi_client.PutStorageBucketAccessRequest() # PutStorageBucketAccessRequest | The changes to make to the bucket's access controls. (optional)

    try:
        # Update access to an Object Storage bucket
        api_response = api_instance.put_storage_bucket_access(api_version, region_id, bucket, put_storage_bucket_access_request=put_storage_bucket_access_request)
        print("The response of ObjectStorageApi->put_storage_bucket_access:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStorageApi->put_storage_bucket_access: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **region_id** | **str**| Identifies a region where this bucket lives.  &gt; 📘 &gt; &gt; You can use a &#x60;clusterId&#x60; in place of &#x60;regionId&#x60; in requests for buckets that you created using the legacy version of the API. Run [List clusters](https://techdocs.akamai.com/linode-api/reference/get-object-storage-clusters) to see each cluster &#x60;id&#x60;. | 
 **bucket** | **str**| The bucket name. | 
 **put_storage_bucket_access_request** | [**PutStorageBucketAccessRequest**](PutStorageBucketAccessRequest.md)| The changes to make to the bucket&#39;s access controls. | [optional] 

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
**200** | Access controls updated. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

