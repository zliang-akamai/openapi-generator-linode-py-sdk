# GetObjectStorageKeys200ResponseDataInnerBucketAccessInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_name** | **str** | The name of the bucket the key can access in the &#x60;region&#x60;. | [optional] 
**cluster** | **str** | Identifies the legacy cluster where this key can be used. The key grants access to each specified &#x60;bucket_name&#x60;, based on the &#x60;permissions&#x60; set. To support backward compatibility, the API generates this value, based on the &#x60;region&#x60; set for a new key. See [Create an Object Storage key](https://techdocs.akamai.com/linode-api/reference/post-object-storage-keys) for more information. | [optional] 
**permissions** | **str** | The level of access the key grants to the &#x60;bucket_name&#x60;. Keys with &#x60;read_write&#x60; access can manage content in the &#x60;bucket_name&#x60;, while &#x60;read_only&#x60; can be used to view content. See [Create an Object Storage key(ref:post-object-storage-keys) for more details. | [optional] 
**region** | **str** | The region where the Object Store &#x60;bucket_name&#x60; resides. | [optional] 

## Example

```python
from openapi_client.models.get_object_storage_keys200_response_data_inner_bucket_access_inner import GetObjectStorageKeys200ResponseDataInnerBucketAccessInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetObjectStorageKeys200ResponseDataInnerBucketAccessInner from a JSON string
get_object_storage_keys200_response_data_inner_bucket_access_inner_instance = GetObjectStorageKeys200ResponseDataInnerBucketAccessInner.from_json(json)
# print the JSON string representation of the object
print(GetObjectStorageKeys200ResponseDataInnerBucketAccessInner.to_json())

# convert the object into a dict
get_object_storage_keys200_response_data_inner_bucket_access_inner_dict = get_object_storage_keys200_response_data_inner_bucket_access_inner_instance.to_dict()
# create an instance of GetObjectStorageKeys200ResponseDataInnerBucketAccessInner from a dict
get_object_storage_keys200_response_data_inner_bucket_access_inner_from_dict = GetObjectStorageKeys200ResponseDataInnerBucketAccessInner.from_dict(get_object_storage_keys200_response_data_inner_bucket_access_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


