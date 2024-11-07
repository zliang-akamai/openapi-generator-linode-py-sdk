# GetObjectStorageKeys200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GetObjectStorageKeys200ResponseDataInner]**](GetObjectStorageKeys200ResponseDataInner.md) |  | [optional] 
**page** | **int** | The current [page](https://techdocs.akamai.com/linode-api/reference/pagination). | [optional] [readonly] 
**pages** | **int** | The total number of [pages](https://techdocs.akamai.com/linode-api/reference/pagination). | [optional] [readonly] 
**results** | **int** | The total number of results. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_object_storage_keys200_response import GetObjectStorageKeys200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetObjectStorageKeys200Response from a JSON string
get_object_storage_keys200_response_instance = GetObjectStorageKeys200Response.from_json(json)
# print the JSON string representation of the object
print(GetObjectStorageKeys200Response.to_json())

# convert the object into a dict
get_object_storage_keys200_response_dict = get_object_storage_keys200_response_instance.to_dict()
# create an instance of GetObjectStorageKeys200Response from a dict
get_object_storage_keys200_response_from_dict = GetObjectStorageKeys200Response.from_dict(get_object_storage_keys200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


