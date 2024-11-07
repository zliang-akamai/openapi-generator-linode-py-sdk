# GetObjectStorageBuckets200ResponseDataInner

An Object Storage bucket. You should access this through the [S3 API](https://docs.ceph.com/en/latest/radosgw/s3/#api).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | **str** | The legacy &#x60;clusterId&#x60; equivalent for the &#x60;regionId&#x60; where this bucket lives. The API maintains this for backward compatibility.  &gt; 📘 &gt; &gt; - This value and the &#x60;regionId&#x60; are interchangeable when used in requests. Best practice is to use the &#x60;regionId&#x60;. &gt; &gt; - This value is empty for newer regions that don&#39;t have a legacy &#x60;clusterId&#x60;. | [optional] 
**created** | **datetime** | When this bucket was created. | [optional] 
**hostname** | **str** | The hostname where this bucket can be accessed. This hostname can be accessed through a browser if the bucket is made public. | [optional] 
**label** | **str** | The name of this bucket. | [optional] 
**objects** | **int** | The number of objects stored in this bucket. | [optional] 
**region** | **str** | The &#x60;id&#x60; of the [region](https://techdocs.akamai.com/linode-api/reference/get-regions) where this Object Storage bucket lives. | [optional] 
**size** | **int** | The size of the bucket in bytes. | [optional] 

## Example

```python
from openapi_client.models.get_object_storage_buckets200_response_data_inner import GetObjectStorageBuckets200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetObjectStorageBuckets200ResponseDataInner from a JSON string
get_object_storage_buckets200_response_data_inner_instance = GetObjectStorageBuckets200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetObjectStorageBuckets200ResponseDataInner.to_json())

# convert the object into a dict
get_object_storage_buckets200_response_data_inner_dict = get_object_storage_buckets200_response_data_inner_instance.to_dict()
# create an instance of GetObjectStorageBuckets200ResponseDataInner from a dict
get_object_storage_buckets200_response_data_inner_from_dict = GetObjectStorageBuckets200ResponseDataInner.from_dict(get_object_storage_buckets200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


