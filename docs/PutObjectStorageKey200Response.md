# PutObjectStorageKey200Response

An updated Object Storage key used to communicate with the Object Storage S3 API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | **str** | A unique string chosen by the API to identify this key. Used as a user name to identify this key when making requests to the S3 API. | [optional] [readonly] 
**id** | **int** | This Object Storage key&#39;s unique numeric identifier. | [optional] [readonly] 
**label** | **str** | The label given to this key. For display purposes only. | [optional] 
**limited** | **bool** | Whether this Object Storage key limits access to specific buckets and permissions. Returns &#x60;false&#x60; if this key grants full access.  &gt; 📘 &gt; &gt; The &#x60;bucket_access&#x60; array that contains limited Object Storage key settings doesn&#39;t appear in this response. Store this key&#39;s &#x60;id&#x60; from the response and run [Get an Object Storage key](https://techdocs.akamai.com/linode-api/reference/get-object-storage-key) to view these settings. | [optional] [readonly] 
**regions** | [**List[PutObjectStorageKey200ResponseRegionsInner]**](PutObjectStorageKey200ResponseRegionsInner.md) | The key can be used in these regions to create new buckets, but it can&#39;t be used to manage content in those buckets. See [Create an Object Storage key](https://techdocs.akamai.com/linode-api/reference/post-object-storage-keys) for more details. | [optional] 
**secret_key** | **str** | This Object Storage key&#39;s secret key. Used as a password to validate this key when making requests to the S3 API. This value is only revealed in a response after creating or modifying a key. | [optional] [readonly] 

## Example

```python
from openapi_client.models.put_object_storage_key200_response import PutObjectStorageKey200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PutObjectStorageKey200Response from a JSON string
put_object_storage_key200_response_instance = PutObjectStorageKey200Response.from_json(json)
# print the JSON string representation of the object
print(PutObjectStorageKey200Response.to_json())

# convert the object into a dict
put_object_storage_key200_response_dict = put_object_storage_key200_response_instance.to_dict()
# create an instance of PutObjectStorageKey200Response from a dict
put_object_storage_key200_response_from_dict = PutObjectStorageKey200Response.from_dict(put_object_storage_key200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


