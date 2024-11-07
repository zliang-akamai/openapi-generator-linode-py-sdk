# PostObjectStorageKeysRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_access** | [**List[PostObjectStorageKeysRequestBucketAccessInner]**](PostObjectStorageKeysRequestBucketAccessInner.md) | Set up the key to limit access to specific buckets, each with a specific permission level. You can create a limited Object Storage key with access to no buckets. Include an empty &#x60;bucket_access&#x60; array in the request. | [optional] 
**label** | **str** | The label for the Object Storage key, for display purposes only. | [optional] 
**regions** | **List[str]** | You can use a key to create new buckets in regions set in this array. But it can&#39;t be used to manage content in those buckets. See [Create an Object Storage key](https://techdocs.akamai.com/linode-api/reference/post-object-storage-keys) for more details. | [optional] 

## Example

```python
from openapi_client.models.post_object_storage_keys_request import PostObjectStorageKeysRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostObjectStorageKeysRequest from a JSON string
post_object_storage_keys_request_instance = PostObjectStorageKeysRequest.from_json(json)
# print the JSON string representation of the object
print(PostObjectStorageKeysRequest.to_json())

# convert the object into a dict
post_object_storage_keys_request_dict = post_object_storage_keys_request_instance.to_dict()
# create an instance of PostObjectStorageKeysRequest from a dict
post_object_storage_keys_request_from_dict = PostObjectStorageKeysRequest.from_dict(post_object_storage_keys_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


