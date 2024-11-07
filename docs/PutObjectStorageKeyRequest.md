# PutObjectStorageKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The label for the Object Storage key. Used for display purposes. Omit this to leave the &#x60;label&#x60; unchanged. | [optional] 
**regions** | **List[str]** | Replace the current list of &#x60;regions&#x60; set in a specific key. Include an existing region to maintain it or leave it out to remove it. If you include new &#x60;regions&#x60; in the key, they can&#39;t be used to manage content in buckets in that specific region. You can grant these keys this access using [bucket policies](https://www.linode.com/docs/products/storage/object-storage/guides/bucket-policies/). Omit this to leave the existing list unchanged.  &gt; 🚧 &gt; &gt; You can&#39;t remove a &#x60;region&#x60; from a limited key&#39;s original &#x60;bucket_access&#x60; list. If you include the &#x60;regions&#x60; array in this operation, you need to include all existing &#x60;region&#x60; entries from the &#x60;bucket_access&#x60; array. Otherwise, the operation fails with an error. Run [Get an Object Storage key](https://techdocs.akamai.com/linode-api/reference/get-object-storage-key) to review current &#x60;region&#x60; entries in a limited key. | [optional] 

## Example

```python
from openapi_client.models.put_object_storage_key_request import PutObjectStorageKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutObjectStorageKeyRequest from a JSON string
put_object_storage_key_request_instance = PutObjectStorageKeyRequest.from_json(json)
# print the JSON string representation of the object
print(PutObjectStorageKeyRequest.to_json())

# convert the object into a dict
put_object_storage_key_request_dict = put_object_storage_key_request_instance.to_dict()
# create an instance of PutObjectStorageKeyRequest from a dict
put_object_storage_key_request_from_dict = PutObjectStorageKeyRequest.from_dict(put_object_storage_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


