# openapi_client.ImagesApi

All URIs are relative to *https://api.linode.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_image**](ImagesApi.md#delete_image) | **DELETE** /{apiVersion}/images/{imageId} | Delete an image
[**get_image**](ImagesApi.md#get_image) | **GET** /{apiVersion}/images/{imageId} | Get an image
[**get_images**](ImagesApi.md#get_images) | **GET** /{apiVersion}/images | List images
[**post_image**](ImagesApi.md#post_image) | **POST** /{apiVersion}/images | Create an image
[**post_replicate_image**](ImagesApi.md#post_replicate_image) | **POST** /{apiVersion}/images/{imageId}/regions | Replicate an image
[**post_upload_image**](ImagesApi.md#post_upload_image) | **POST** /{apiVersion}/images/upload | Upload an image
[**put_image**](ImagesApi.md#put_image) | **PUT** /{apiVersion}/images/{imageId} | Update an image


# **delete_image**
> object delete_image(api_version, image_id)

Delete an image

Deletes a private image you have permission to `read_write`.  > 🚧 > > - You can't undo this delete action. > > - When you delete an image, all [replicated instances](https://techdocs.akamai.com/linode-api/reference/post-replicate-image) of that image are also deleted.   <<LB>>  ---   - __CLI__.      ```     linode-cli images delete 12345     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     images:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
    api_instance = openapi_client.ImagesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    image_id = 'linode/debian11' # str | The unique identifier assigned to the image after creation.

    try:
        # Delete an image
        api_response = api_instance.delete_image(api_version, image_id)
        print("The response of ImagesApi->delete_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->delete_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **image_id** | **str**| The unique identifier assigned to the image after creation. | 

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

# **get_image**
> GetImages200ResponseDataInner get_image(api_version, image_id)

Get an image

Get information about a single image. An image can be one of two types:  - **Public image**. The `id` for these images begins with `linode/`. These images are generally available to all users. To limit the response to public images, don't include [authentication](https://techdocs.akamai.com/linode-api/reference/get-started#authentication) when calling this operation.  - **Private image**. The `id` for these images begins with `private/`. These images are account-specific and only accessible to users with appropriate [grants](https://techdocs.akamai.com/linode-api/reference/get-user-grants). To view private images, you need to include authentication when calling this operation. The response will also include public images.   <<LB>>  ---   - __CLI__.      ```     linode-cli images view linode/debian9     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     images:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_images200_response_data_inner import GetImages200ResponseDataInner
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
    api_instance = openapi_client.ImagesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    image_id = 'linode/debian11' # str | The unique identifier assigned to the image after creation.

    try:
        # Get an image
        api_response = api_instance.get_image(api_version, image_id)
        print("The response of ImagesApi->get_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->get_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **image_id** | **str**| The unique identifier assigned to the image after creation. | 

### Return type

[**GetImages200ResponseDataInner**](GetImages200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single image object. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_images**
> GetImages200Response get_images(api_version, page=page, page_size=page_size)

List images

Returns a paginated list of images. An image can be one of two types:  - **Public image**. The `id` for these images begins with `linode/`. These images are generally available to all users. To limit the response to public images, don't include [authentication](https://techdocs.akamai.com/linode-api/reference/get-started#authentication) when calling this operation.  - **Private image**. The `id` for these images begins with `private/`. These images are account-specific and only accessible to users with appropriate [grants](https://techdocs.akamai.com/linode-api/reference/get-user-grants). To view private images, you need to include authentication when calling this operation. The response includes both private and public images.   <<LB>>  ---   - __CLI__.      ```     linode-cli images list     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     images:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_images200_response import GetImages200Response
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
    api_instance = openapi_client.ImagesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    page = 1 # int | The page of a collection to return. (optional) (default to 1)
    page_size = 100 # int | The number of items to return per page. (optional) (default to 100)

    try:
        # List images
        api_response = api_instance.get_images(api_version, page=page, page_size=page_size)
        print("The response of ImagesApi->get_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->get_images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **page** | **int**| The page of a collection to return. | [optional] [default to 1]
 **page_size** | **int**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetImages200Response**](GetImages200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of images. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_image**
> GetImages200ResponseDataInner post_image(api_version, post_image_request=post_image_request)

Create an image

Captures a private, gold-master image from a Linode disk.  > 📘 > > - Captured images are stored using our Object Storage service. The `region` where the target image exists determines where the [resulting image is stored](https://techdocs.akamai.com/cloud-computing/docs/images#regions-and-captured-custom-images). > > - If you create an image from an encrypted disk, the API doesn't encrypt the image. When you rebuild a compute instance from that image, the resulting disk will be automatically encrypted.   <<LB>>  ---   - __CLI__.      ```     linode-cli images create \\   --label this_is_a_label \\   --description \"A longer description \\     of the image\" \\   --disk_id 123     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     images:read_write linodes:read_only     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_images200_response_data_inner import GetImages200ResponseDataInner
from openapi_client.models.post_image_request import PostImageRequest
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
    api_instance = openapi_client.ImagesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    post_image_request = openapi_client.PostImageRequest() # PostImageRequest |  (optional)

    try:
        # Create an image
        api_response = api_instance.post_image(api_version, post_image_request=post_image_request)
        print("The response of ImagesApi->post_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->post_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **post_image_request** | [**PostImageRequest**](PostImageRequest.md)|  | [optional] 

### Return type

[**GetImages200ResponseDataInner**](GetImages200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New private image created successfully. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_replicate_image**
> GetImages200ResponseDataInner post_replicate_image(api_version, image_id, post_replicate_image_request)

Replicate an image

__Limited availability__ Target an existing image and replicate it to another compute region.  - This operation is in Limited Availability. Talk to your account team about access to it.  - This is only available in a `region` that supports Object Storage, which stores the replicated image. Run the [List regions](https://techdocs.akamai.com/linode-api/reference/get-regions) operation to review a region's `capabilities`.  - To replicate an image, it needs to have a `status` of `available`. Run the [List images](https://techdocs.akamai.com/linode-api/reference/get-images) operation to view an image's `status`.  - To also keep the target image in its original compute region, you need to include that `region` in the request's data. If you leave it out, the API removes the image from that region. Run the [Get an image](https://techdocs.akamai.com/linode-api/reference/get-image) operation to see the `regions` where an image currently exists.  - You can't include an empty array to delete all images. You need to provide at least one compute `region` where the image is `available`. Use the [Delete an image](https://techdocs.akamai.com/linode-api/reference/delete-image) operation.   <<LB>>  ---   - __CLI__.      ```     linode-cli images replicate private/12345 \\   --regions \"us-mia\" \\   --regions \"us-east\"     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     images:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_images200_response_data_inner import GetImages200ResponseDataInner
from openapi_client.models.post_replicate_image_request import PostReplicateImageRequest
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
    api_instance = openapi_client.ImagesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    image_id = 'linode/debian11' # str | The unique identifier assigned to the image after creation.
    post_replicate_image_request = openapi_client.PostReplicateImageRequest() # PostReplicateImageRequest | 

    try:
        # Replicate an image
        api_response = api_instance.post_replicate_image(api_version, image_id, post_replicate_image_request)
        print("The response of ImagesApi->post_replicate_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->post_replicate_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **image_id** | **str**| The unique identifier assigned to the image after creation. | 
 **post_replicate_image_request** | [**PostReplicateImageRequest**](PostReplicateImageRequest.md)|  | 

### Return type

[**GetImages200ResponseDataInner**](GetImages200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Replication details for the image. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_upload_image**
> PostUploadImage200Response post_upload_image(api_version, post_upload_image_request=post_upload_image_request)

Upload an image

Creates a new private image container and returns a URL as the `upload_to` object in the response. Use this URL to upload your own disk image to the container.  1. Ensure the disk image is raw disk image (`.img`) format.  2. Compress the disk image using gzip (`.gz`) format. Compressed, the file can be up to 5 GB and decompressed it can be up to 6 GB.  3. Upload the file in a separate PUT request that includes the `Content-type: application/octet-stream` header:    ```   curl -v \\     -H \"Content-Type: application/octet-stream\" \\     --upload-file example.img.gz \\     $UPLOAD_URL \\     --progress-bar \\     --output /dev/null   ```  > 📘 > > - You need to upload image data within 24 hours of creation or the API cancels the upload and deletes the image container. > > - Only core regions that support our [Object Storage](https://techdocs.akamai.com/cloud-computing/reference/how-to-choose-a-data-center#product-availability) service can store an uploaded image. > > - If you create an image from an encrypted disk, the API doesn't encrypt the image. When you rebuild a compute instance from that image, the resulting disk will be automatically encrypted. > > - You can create a new image and upload image data using a single process through [Cloud Manager](https://www.linode.com/docs/products/tools/images/guides/upload-an-image/#uploading-an-image-file-through-the-cloud-manager) or the [Linode CLI](https://www.linode.com/docs/products/tools/images/guides/upload-an-image/#uploading-an-image-file-through-the-linode-cli).   <<LB>>  ---   - __CLI__.      ```     # Run the operation to just get the upload_to URL linode-cli images upload \\   --description \"Optional details about the Image\" \\   --label \"Example Image\" \\   --region us-east  # Upload the image file in a single step linode-cli image-upload \\   --description \"Optional details about the Image\" \\   --label \"Example Image\" \\   --region us-east \\   /path/to/image-file.img.gz     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     images:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.post_upload_image200_response import PostUploadImage200Response
from openapi_client.models.post_upload_image_request import PostUploadImageRequest
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
    api_instance = openapi_client.ImagesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    post_upload_image_request = openapi_client.PostUploadImageRequest() # PostUploadImageRequest | The uploaded image details. (optional)

    try:
        # Upload an image
        api_response = api_instance.post_upload_image(api_version, post_upload_image_request=post_upload_image_request)
        print("The response of ImagesApi->post_upload_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->post_upload_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **post_upload_image_request** | [**PostUploadImageRequest**](PostUploadImageRequest.md)| The uploaded image details. | [optional] 

### Return type

[**PostUploadImage200Response**](PostUploadImage200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image Upload object including the upload URL and image object. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_image**
> GetImages200ResponseDataInner put_image(api_version, image_id, get_images200_response_data_inner)

Update an image

Updates a private image that you have permission to `read_write`.  > 📘 > > You can't update the `regions` with this operation. Use the [Replicate an image](https://techdocs.akamai.com/linode-api/reference/post-replicate-image) operation to modify the existing regions for your image.   <<LB>>  ---   - __CLI__.      ```     linode-cli images update private/12345 \\   --label \"My gold-master image\" \\   --description \"The detailed description \\     of my image.\"     ```      [Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)  - __OAuth scopes__.      ```     images:read_write     ```      [Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.get_images200_response_data_inner import GetImages200ResponseDataInner
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
    api_instance = openapi_client.ImagesApi(api_client)
    api_version = v4 # str | __Enum__ Call either the `v4` URL, or `v4beta` for operations still in Beta. (default to v4)
    image_id = 'linode/debian11' # str | The unique identifier assigned to the image after creation.
    get_images200_response_data_inner = openapi_client.GetImages200ResponseDataInner() # GetImages200ResponseDataInner | 

    try:
        # Update an image
        api_response = api_instance.put_image(api_version, image_id, get_images200_response_data_inner)
        print("The response of ImagesApi->put_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->put_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| __Enum__ Call either the &#x60;v4&#x60; URL, or &#x60;v4beta&#x60; for operations still in Beta. | [default to v4]
 **image_id** | **str**| The unique identifier assigned to the image after creation. | 
 **get_images200_response_data_inner** | [**GetImages200ResponseDataInner**](GetImages200ResponseDataInner.md)|  | 

### Return type

[**GetImages200ResponseDataInner**](GetImages200ResponseDataInner.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated image. |  -  |
**0** | See [Errors](https://techdocs.akamai.com/linode-api/reference/errors) for the range of possible error response codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

