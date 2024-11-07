# GetObjectStorageBucketAcl200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acl** | **str** | The Access Control Level of the bucket, as a canned ACL string. For more fine-grained control of ACLs, use the S3 API directly. | [optional] 
**acl_xml** | **str** | The full XML of the object&#39;s ACL policy. | [optional] 

## Example

```python
from openapi_client.models.get_object_storage_bucket_acl200_response import GetObjectStorageBucketAcl200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetObjectStorageBucketAcl200Response from a JSON string
get_object_storage_bucket_acl200_response_instance = GetObjectStorageBucketAcl200Response.from_json(json)
# print the JSON string representation of the object
print(GetObjectStorageBucketAcl200Response.to_json())

# convert the object into a dict
get_object_storage_bucket_acl200_response_dict = get_object_storage_bucket_acl200_response_instance.to_dict()
# create an instance of GetObjectStorageBucketAcl200Response from a dict
get_object_storage_bucket_acl200_response_from_dict = GetObjectStorageBucketAcl200Response.from_dict(get_object_storage_bucket_acl200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


