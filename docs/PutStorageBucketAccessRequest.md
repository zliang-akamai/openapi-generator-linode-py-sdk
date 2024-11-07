# PutStorageBucketAccessRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acl** | **str** | The Access Control Level of the bucket, as a canned ACL string. For more fine-grained control of ACLs, use the S3 API directly. | [optional] 
**cors_enabled** | **bool** | If true, the bucket will be created with CORS enabled for all origins. For more fine-grained controls of CORS, use the S3 API directly. | [optional] 

## Example

```python
from openapi_client.models.put_storage_bucket_access_request import PutStorageBucketAccessRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutStorageBucketAccessRequest from a JSON string
put_storage_bucket_access_request_instance = PutStorageBucketAccessRequest.from_json(json)
# print the JSON string representation of the object
print(PutStorageBucketAccessRequest.to_json())

# convert the object into a dict
put_storage_bucket_access_request_dict = put_storage_bucket_access_request_instance.to_dict()
# create an instance of PutStorageBucketAccessRequest from a dict
put_storage_bucket_access_request_from_dict = PutStorageBucketAccessRequest.from_dict(put_storage_bucket_access_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


