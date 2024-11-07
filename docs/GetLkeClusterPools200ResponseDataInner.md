# GetLkeClusterPools200ResponseDataInner

The set of Node Pools which are members of the Kubernetes cluster. Node Pools consist of a Linode type, the number of Linodes to deploy of that type, and additional status information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoscaler** | [**GetLkeClusterPools200ResponseDataInnerAutoscaler**](GetLkeClusterPools200ResponseDataInnerAutoscaler.md) |  | [optional] 
**count** | **int** | The number of nodes in the Node Pool. | [optional] 
**disk_encryption** | **str** | For new LKE node pools, &#x60;disk_encryption&#x60; is automatically &#x60;enabled&#x60; where disk encryption is supported. It can&#39;t be &#x60;disabled&#x60;. For existing LKE node pools, this derives from the Linode&#39;s &#x60;disk_encryption&#x60; setting. If a Linode&#39;s node pool is not encrypted and you want an encrypted node pool, delete the node pool and create a new node pool. | [optional] 
**disks** | [**List[PostLkeClusterRequestNodePoolsInnerDisksInner]**](PostLkeClusterRequestNodePoolsInnerDisksInner.md) | This Node Pool&#39;s custom disk layout. | [optional] 
**id** | **int** | This Node Pool&#39;s unique ID. | [optional] 
**labels** | [**GetLkeClusterPools200ResponseDataInnerLabels**](GetLkeClusterPools200ResponseDataInnerLabels.md) |  | [optional] 
**nodes** | [**List[GetLkeClusterPools200ResponseDataInnerNodesInner]**](GetLkeClusterPools200ResponseDataInnerNodesInner.md) | Status information for the Nodes which are members of this Node Pool. If a Linode has not been provisioned for a given Node slot, the instance_id will be returned as null. | [optional] 
**tags** | **List[str]** | An array of tags applied to this object. Tags are for organizational purposes only. | [optional] 
**taints** | [**List[GetLkeClusterPools200ResponseDataInnerTaintsInner]**](GetLkeClusterPools200ResponseDataInnerTaintsInner.md) | Kubernetes taints added to nodes in the node pool. Taints help control how pods are scheduled onto nodes, specifically allowing them to repel certain pods. | [optional] 
**type** | **str** | The Linode Type for all of the nodes in the Node Pool. | [optional] 

## Example

```python
from openapi_client.models.get_lke_cluster_pools200_response_data_inner import GetLkeClusterPools200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLkeClusterPools200ResponseDataInner from a JSON string
get_lke_cluster_pools200_response_data_inner_instance = GetLkeClusterPools200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetLkeClusterPools200ResponseDataInner.to_json())

# convert the object into a dict
get_lke_cluster_pools200_response_data_inner_dict = get_lke_cluster_pools200_response_data_inner_instance.to_dict()
# create an instance of GetLkeClusterPools200ResponseDataInner from a dict
get_lke_cluster_pools200_response_data_inner_from_dict = GetLkeClusterPools200ResponseDataInner.from_dict(get_lke_cluster_pools200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


