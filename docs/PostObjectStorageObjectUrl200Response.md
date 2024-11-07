# PostObjectStorageObjectUrl200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The signed URL to perform the request at. | [optional] 

## Example

```python
from openapi_client.models.post_object_storage_object_url200_response import PostObjectStorageObjectUrl200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostObjectStorageObjectUrl200Response from a JSON string
post_object_storage_object_url200_response_instance = PostObjectStorageObjectUrl200Response.from_json(json)
# print the JSON string representation of the object
print(PostObjectStorageObjectUrl200Response.to_json())

# convert the object into a dict
post_object_storage_object_url200_response_dict = post_object_storage_object_url200_response_instance.to_dict()
# create an instance of PostObjectStorageObjectUrl200Response from a dict
post_object_storage_object_url200_response_from_dict = PostObjectStorageObjectUrl200Response.from_dict(post_object_storage_object_url200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


