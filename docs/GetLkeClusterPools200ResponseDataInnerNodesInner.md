# GetLkeClusterPools200ResponseDataInnerNodesInner

Status information for a Node which is a member of a Kubernetes cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Node&#39;s ID. | [optional] 
**instance_id** | **str** | The Linode&#39;s ID. When no Linode is currently provisioned for this Node, this will be null. | [optional] 
**status** | **str** | The Node&#39;s status as it pertains to being a Kubernetes node. | [optional] 

## Example

```python
from openapi_client.models.get_lke_cluster_pools200_response_data_inner_nodes_inner import GetLkeClusterPools200ResponseDataInnerNodesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLkeClusterPools200ResponseDataInnerNodesInner from a JSON string
get_lke_cluster_pools200_response_data_inner_nodes_inner_instance = GetLkeClusterPools200ResponseDataInnerNodesInner.from_json(json)
# print the JSON string representation of the object
print(GetLkeClusterPools200ResponseDataInnerNodesInner.to_json())

# convert the object into a dict
get_lke_cluster_pools200_response_data_inner_nodes_inner_dict = get_lke_cluster_pools200_response_data_inner_nodes_inner_instance.to_dict()
# create an instance of GetLkeClusterPools200ResponseDataInnerNodesInner from a dict
get_lke_cluster_pools200_response_data_inner_nodes_inner_from_dict = GetLkeClusterPools200ResponseDataInnerNodesInner.from_dict(get_lke_cluster_pools200_response_data_inner_nodes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


