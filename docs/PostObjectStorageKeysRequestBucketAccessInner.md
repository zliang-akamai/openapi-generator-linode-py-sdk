# PostObjectStorageKeysRequestBucketAccessInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_name** | **str** | The &#x60;label&#x60; set for a bucket that this key grants access to. | [optional] 
**permissions** | **str** | The level of access the key grants to the specified &#x60;bucket_name&#x60;. Keys with &#x60;read_write&#x60; access can manage content in the &#x60;bucket_name&#x60;, while &#x60;read_only&#x60; can be used to view content. See [Create an Object Storage key]((ref:post-object-storage-keys) for more details. | [optional] 
**region** | **str** | The region where the &#x60;bucket_name&#x60; you want the key to access is located.  &gt; 📘 &gt; &gt; If you repeat the same &#x60;region&#x60; across objects, the response includes a single &#x60;s3_endpoint&#x60; for this region. Use it to access all &#x60;bucket_name&#x60; entries. | [optional] 

## Example

```python
from openapi_client.models.post_object_storage_keys_request_bucket_access_inner import PostObjectStorageKeysRequestBucketAccessInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostObjectStorageKeysRequestBucketAccessInner from a JSON string
post_object_storage_keys_request_bucket_access_inner_instance = PostObjectStorageKeysRequestBucketAccessInner.from_json(json)
# print the JSON string representation of the object
print(PostObjectStorageKeysRequestBucketAccessInner.to_json())

# convert the object into a dict
post_object_storage_keys_request_bucket_access_inner_dict = post_object_storage_keys_request_bucket_access_inner_instance.to_dict()
# create an instance of PostObjectStorageKeysRequestBucketAccessInner from a dict
post_object_storage_keys_request_bucket_access_inner_from_dict = PostObjectStorageKeysRequestBucketAccessInner.from_dict(post_object_storage_keys_request_bucket_access_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


