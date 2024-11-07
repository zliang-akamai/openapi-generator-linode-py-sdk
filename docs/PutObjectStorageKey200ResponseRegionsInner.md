# PutObjectStorageKey200ResponseRegionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifies each region where you can use the Object Storage key. | [optional] 
**s3_endpoint** | **str** | The S3-compatible hostname you can use to access your Object Storage buckets in this region. | [optional] 

## Example

```python
from openapi_client.models.put_object_storage_key200_response_regions_inner import PutObjectStorageKey200ResponseRegionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PutObjectStorageKey200ResponseRegionsInner from a JSON string
put_object_storage_key200_response_regions_inner_instance = PutObjectStorageKey200ResponseRegionsInner.from_json(json)
# print the JSON string representation of the object
print(PutObjectStorageKey200ResponseRegionsInner.to_json())

# convert the object into a dict
put_object_storage_key200_response_regions_inner_dict = put_object_storage_key200_response_regions_inner_instance.to_dict()
# create an instance of PutObjectStorageKey200ResponseRegionsInner from a dict
put_object_storage_key200_response_regions_inner_from_dict = PutObjectStorageKey200ResponseRegionsInner.from_dict(put_object_storage_key200_response_regions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


