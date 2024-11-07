# GetObjectStorageBucketContent200ResponseDataInner

An Object in Object Storage, or a \"prefix\" that contains one or more objects when a `delimiter` is used.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**etag** | **str** | An MD-5 hash of the object. &#x60;null&#x60; if this object represents a prefix. | [optional] 
**last_modified** | **datetime** | The date and time this object was last modified. &#x60;null&#x60; if this object represents a prefix. | [optional] 
**name** | **str** | The name of this object or prefix. | [optional] 
**owner** | **str** | The owner of this object, as a UUID. &#x60;null&#x60; if this object represents a prefix. | [optional] 
**size** | **int** | The size of this object, in bytes. &#x60;null&#x60; if this object represents a prefix. | [optional] 

## Example

```python
from openapi_client.models.get_object_storage_bucket_content200_response_data_inner import GetObjectStorageBucketContent200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetObjectStorageBucketContent200ResponseDataInner from a JSON string
get_object_storage_bucket_content200_response_data_inner_instance = GetObjectStorageBucketContent200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetObjectStorageBucketContent200ResponseDataInner.to_json())

# convert the object into a dict
get_object_storage_bucket_content200_response_data_inner_dict = get_object_storage_bucket_content200_response_data_inner_instance.to_dict()
# create an instance of GetObjectStorageBucketContent200ResponseDataInner from a dict
get_object_storage_bucket_content200_response_data_inner_from_dict = GetObjectStorageBucketContent200ResponseDataInner.from_dict(get_object_storage_bucket_content200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


