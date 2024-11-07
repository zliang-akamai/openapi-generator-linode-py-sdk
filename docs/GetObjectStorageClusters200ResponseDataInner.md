# GetObjectStorageClusters200ResponseDataInner

An Object Storage Cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The base URL for this cluster, used for connecting with third-party clients. | [optional] 
**id** | **str** | The unique ID for this cluster. | [optional] 
**region** | **str** | The region where this cluster is located. | [optional] 
**static_site_domain** | **str** | The base URL for this cluster used when hosting static sites. | [optional] 
**status** | **str** | This cluster&#39;s status. | [optional] 

## Example

```python
from openapi_client.models.get_object_storage_clusters200_response_data_inner import GetObjectStorageClusters200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetObjectStorageClusters200ResponseDataInner from a JSON string
get_object_storage_clusters200_response_data_inner_instance = GetObjectStorageClusters200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetObjectStorageClusters200ResponseDataInner.to_json())

# convert the object into a dict
get_object_storage_clusters200_response_data_inner_dict = get_object_storage_clusters200_response_data_inner_instance.to_dict()
# create an instance of GetObjectStorageClusters200ResponseDataInner from a dict
get_object_storage_clusters200_response_data_inner_from_dict = GetObjectStorageClusters200ResponseDataInner.from_dict(get_object_storage_clusters200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


