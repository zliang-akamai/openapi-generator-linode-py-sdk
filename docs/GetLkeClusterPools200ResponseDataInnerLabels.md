# GetLkeClusterPools200ResponseDataInnerLabels

Key-value pairs added as labels to nodes in the node pool. Labels help classify your nodes and to easily select subsets of objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The Kubernetes label key. | [optional] 
**value** | **str** | The Kubernetes label value. | [optional] 

## Example

```python
from openapi_client.models.get_lke_cluster_pools200_response_data_inner_labels import GetLkeClusterPools200ResponseDataInnerLabels

# TODO update the JSON string below
json = "{}"
# create an instance of GetLkeClusterPools200ResponseDataInnerLabels from a JSON string
get_lke_cluster_pools200_response_data_inner_labels_instance = GetLkeClusterPools200ResponseDataInnerLabels.from_json(json)
# print the JSON string representation of the object
print(GetLkeClusterPools200ResponseDataInnerLabels.to_json())

# convert the object into a dict
get_lke_cluster_pools200_response_data_inner_labels_dict = get_lke_cluster_pools200_response_data_inner_labels_instance.to_dict()
# create an instance of GetLkeClusterPools200ResponseDataInnerLabels from a dict
get_lke_cluster_pools200_response_data_inner_labels_from_dict = GetLkeClusterPools200ResponseDataInnerLabels.from_dict(get_lke_cluster_pools200_response_data_inner_labels_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


