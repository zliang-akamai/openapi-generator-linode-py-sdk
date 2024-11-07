# GetObjectStorageKeys200ResponseDataInnerRegionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifies each region where you can use the Object Storage key. | [optional] 
**s3_endpoint** | **str** | The S3-compatible hostname you can use to access the Object Storage buckets in this region. | [optional] 

## Example

```python
from openapi_client.models.get_object_storage_keys200_response_data_inner_regions_inner import GetObjectStorageKeys200ResponseDataInnerRegionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetObjectStorageKeys200ResponseDataInnerRegionsInner from a JSON string
get_object_storage_keys200_response_data_inner_regions_inner_instance = GetObjectStorageKeys200ResponseDataInnerRegionsInner.from_json(json)
# print the JSON string representation of the object
print(GetObjectStorageKeys200ResponseDataInnerRegionsInner.to_json())

# convert the object into a dict
get_object_storage_keys200_response_data_inner_regions_inner_dict = get_object_storage_keys200_response_data_inner_regions_inner_instance.to_dict()
# create an instance of GetObjectStorageKeys200ResponseDataInnerRegionsInner from a dict
get_object_storage_keys200_response_data_inner_regions_inner_from_dict = GetObjectStorageKeys200ResponseDataInnerRegionsInner.from_dict(get_object_storage_keys200_response_data_inner_regions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


