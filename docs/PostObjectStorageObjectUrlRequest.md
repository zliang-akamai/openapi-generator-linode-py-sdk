# PostObjectStorageObjectUrlRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** | The expected &#x60;Content-type&#x60; header of the request this signed URL will be valid for.  If provided, the &#x60;Content-type&#x60; header _must_ be sent with the request when this URL is used, and _must_ be the same as it was when the signed URL was created. Required for all methods _except_ &#x60;GET&#x60; or &#x60;DELETE&#x60;. | [optional] 
**expires_in** | **int** | How long this signed URL will be valid for, in seconds.  If omitted, the URL will be valid for 3600 seconds (1 hour). | [optional] [default to 3600]
**method** | **str** | The HTTP method allowed to be used with the pre-signed URL. | [default to 'GET']
**name** | **str** | The name of the object that will be accessed with the pre-signed URL. This object need not exist, and no error will be returned if it doesn&#39;t. This behavior is useful for generating pre-signed URLs to upload new objects to by setting the &#x60;method&#x60; to &#x60;PUT&#x60;. | 

## Example

```python
from openapi_client.models.post_object_storage_object_url_request import PostObjectStorageObjectUrlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostObjectStorageObjectUrlRequest from a JSON string
post_object_storage_object_url_request_instance = PostObjectStorageObjectUrlRequest.from_json(json)
# print the JSON string representation of the object
print(PostObjectStorageObjectUrlRequest.to_json())

# convert the object into a dict
post_object_storage_object_url_request_dict = post_object_storage_object_url_request_instance.to_dict()
# create an instance of PostObjectStorageObjectUrlRequest from a dict
post_object_storage_object_url_request_from_dict = PostObjectStorageObjectUrlRequest.from_dict(post_object_storage_object_url_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


