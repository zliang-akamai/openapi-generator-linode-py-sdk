# PostObjectStorageBucketRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acl** | **str** | The Access Control Level of the bucket using a canned ACL string. For more fine-grained control of ACLs, use the S3 API directly. | [optional] [default to 'private']
**cors_enabled** | **bool** | If set to &#x60;false&#x60;, CORS is disabled for all origins in the bucket. For more fine-grained controls of CORS, use the S3 API directly. | [optional] [default to True]
**label** | **str** | The name for this bucket.  * A bucket name can contain from 3 to 63 alphanumeric characters, dashes (&#x60;-&#x60;), or dots (&#x60;.&#x60;). * A bucket name can&#39;t end in a dash and you can&#39;t use two consecutive dashes. * A bucket name can&#39;t start or end in a dot, and you can&#39;t use two consecutive dots. As a best practice, only use dots if a certificate you&#39;re using with your bucket requires it. (For example, if you&#39;re using a custom TLS certificate.) * A bucket name needs to be unique in the &#x60;region&#x60; where you&#39;re creating the bucket. The API only reserves labels for the &#x60;region&#x60; where active buckets are created and stored. If you want to reserve this bucket&#39;s label in another &#x60;region&#x60;, create a new bucket with the same label in the new &#x60;region&#x60;. | 
**region** | **str** | The &#x60;id&#x60; assigned to the data center ([region](https://techdocs.akamai.com/linode-api/reference/get-regions)) where this Object Storage bucket should be created.  &gt; 📘 &gt; &gt; This supports legacy &#x60;clusterId&#x60; values that represented a specific region. For example, &#x60;us-east-1&#x60; is the legacy reference for the &#x60;us-east&#x60; region. | [optional] 

## Example

```python
from openapi_client.models.post_object_storage_bucket_request import PostObjectStorageBucketRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostObjectStorageBucketRequest from a JSON string
post_object_storage_bucket_request_instance = PostObjectStorageBucketRequest.from_json(json)
# print the JSON string representation of the object
print(PostObjectStorageBucketRequest.to_json())

# convert the object into a dict
post_object_storage_bucket_request_dict = post_object_storage_bucket_request_instance.to_dict()
# create an instance of PostObjectStorageBucketRequest from a dict
post_object_storage_bucket_request_from_dict = PostObjectStorageBucketRequest.from_dict(post_object_storage_bucket_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


