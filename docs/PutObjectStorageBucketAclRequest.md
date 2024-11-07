# PutObjectStorageBucketAclRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acl** | **str** | The Access Control Level of the bucket, as a canned ACL string. For more fine-grained control of ACLs, use the S3 API directly. | 
**name** | **str** | The &#x60;name&#x60; of the object for which to update its Access Control List (ACL). Run the [List Object Storage bucket contents](https://techdocs.akamai.com/linode-api/reference/get-object-storage-bucket-content) operation to access all object names in a bucket. | 

## Example

```python
from openapi_client.models.put_object_storage_bucket_acl_request import PutObjectStorageBucketAclRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutObjectStorageBucketAclRequest from a JSON string
put_object_storage_bucket_acl_request_instance = PutObjectStorageBucketAclRequest.from_json(json)
# print the JSON string representation of the object
print(PutObjectStorageBucketAclRequest.to_json())

# convert the object into a dict
put_object_storage_bucket_acl_request_dict = put_object_storage_bucket_acl_request_instance.to_dict()
# create an instance of PutObjectStorageBucketAclRequest from a dict
put_object_storage_bucket_acl_request_from_dict = PutObjectStorageBucketAclRequest.from_dict(put_object_storage_bucket_acl_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


