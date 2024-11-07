# GetObjectStorageTransfer200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**used** | **int** | The amount of outbound data transfer used by your account&#39;s Object Storage buckets, in bytes, for the current month&#39;s billing cycle. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_object_storage_transfer200_response import GetObjectStorageTransfer200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetObjectStorageTransfer200Response from a JSON string
get_object_storage_transfer200_response_instance = GetObjectStorageTransfer200Response.from_json(json)
# print the JSON string representation of the object
print(GetObjectStorageTransfer200Response.to_json())

# convert the object into a dict
get_object_storage_transfer200_response_dict = get_object_storage_transfer200_response_instance.to_dict()
# create an instance of GetObjectStorageTransfer200Response from a dict
get_object_storage_transfer200_response_from_dict = GetObjectStorageTransfer200Response.from_dict(get_object_storage_transfer200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


