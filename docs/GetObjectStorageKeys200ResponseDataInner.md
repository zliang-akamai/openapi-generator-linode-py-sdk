# GetObjectStorageKeys200ResponseDataInner

A key used to communicate with the Object Storage S3 API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | **str** | A unique string chosen by the API to identify this key. Used as a user name to identify this key when making requests to the S3 API. | [optional] [readonly] 
**bucket_access** | [**List[GetObjectStorageKeys200ResponseDataInnerBucketAccessInner]**](GetObjectStorageKeys200ResponseDataInnerBucketAccessInner.md) | Settings that limit access to specific buckets, each with a specific permission level. | [optional] 
**id** | **int** | This Object Storage key&#39;s unique ID. | [optional] [readonly] 
**label** | **str** | The label given to this key. For display purposes only. | [optional] 
**limited** | **bool** | Whether this Object Storage key limits access to specific buckets and permissions. Returns &#x60;false&#x60; if this key grants full access. Specific limitations are set in &#x60;bucket_access&#x60;. | [optional] [readonly] 
**regions** | [**List[GetObjectStorageKeys200ResponseDataInnerRegionsInner]**](GetObjectStorageKeys200ResponseDataInnerRegionsInner.md) | The key can be used in these regions to create new buckets but it can&#39;t be used to manage content in those buckets. See [Create an Object Storage key](https://techdocs.akamai.com/linode-api/reference/post-object-storage-keys) for more details. | [optional] 
**secret_key** | **str** | This Object Storage key&#39;s secret key. Used as a password to validate this key when making requests to the S3 API. This value is only revealed in a response after creating or modifying a key. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_object_storage_keys200_response_data_inner import GetObjectStorageKeys200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetObjectStorageKeys200ResponseDataInner from a JSON string
get_object_storage_keys200_response_data_inner_instance = GetObjectStorageKeys200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetObjectStorageKeys200ResponseDataInner.to_json())

# convert the object into a dict
get_object_storage_keys200_response_data_inner_dict = get_object_storage_keys200_response_data_inner_instance.to_dict()
# create an instance of GetObjectStorageKeys200ResponseDataInner from a dict
get_object_storage_keys200_response_data_inner_from_dict = GetObjectStorageKeys200ResponseDataInner.from_dict(get_object_storage_keys200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


