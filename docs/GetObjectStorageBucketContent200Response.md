# GetObjectStorageBucketContent200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GetObjectStorageBucketContent200ResponseDataInner]**](GetObjectStorageBucketContent200ResponseDataInner.md) |  | [optional] 
**is_truncated** | **bool** | Designates if there is another page of bucket objects. | [optional] 
**next_marker** | **str** | Returns the value you should pass to the &#x60;marker&#x60; query parameter to get the next page of objects. If there is no next page, &#x60;null&#x60; will be returned. | [optional] 

## Example

```python
from openapi_client.models.get_object_storage_bucket_content200_response import GetObjectStorageBucketContent200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetObjectStorageBucketContent200Response from a JSON string
get_object_storage_bucket_content200_response_instance = GetObjectStorageBucketContent200Response.from_json(json)
# print the JSON string representation of the object
print(GetObjectStorageBucketContent200Response.to_json())

# convert the object into a dict
get_object_storage_bucket_content200_response_dict = get_object_storage_bucket_content200_response_instance.to_dict()
# create an instance of GetObjectStorageBucketContent200Response from a dict
get_object_storage_bucket_content200_response_from_dict = GetObjectStorageBucketContent200Response.from_dict(get_object_storage_bucket_content200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


