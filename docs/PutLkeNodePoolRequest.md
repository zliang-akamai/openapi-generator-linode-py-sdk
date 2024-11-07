# PutLkeNodePoolRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoscaler** | [**PostLkeClusterRequestNodePoolsInnerAutoscaler**](PostLkeClusterRequestNodePoolsInnerAutoscaler.md) |  | [optional] 
**count** | **int** | The number of nodes in the Node Pool. | [optional] 
**labels** | **List[object]** | Key-value pairs added as labels to nodes in the node pool. Labels help classify your nodes and easily select subsets of objects. To learn more, review [Add Labels and Taints to your LKE node pools](https://www.linode.com/docs/products/compute/kubernetes/guides/deploy-and-manage-cluster-with-the-linode-api/#add-labels-and-taints-to-your-lke-node-pools).  Specifying an empty dictionary value will remove all previously set labels. | [optional] 
**taints** | [**List[PostLkeClusterRequestNodePoolsInnerTaintsInner]**](PostLkeClusterRequestNodePoolsInnerTaintsInner.md) | Kubernetes taints to add to node pool nodes. Taints help control how pods are scheduled onto nodes, specifically allowing them to repel certain pods. To learn more, review [Add labels and taints to your LKE node pools](https://www.linode.com/docs/products/compute/kubernetes/guides/deploy-and-manage-cluster-with-the-linode-api/#add-labels-and-taints-to-your-lke-node-pools).  Specifying an empty array (&#x60;[]&#x60;) removes all previously set taints. | [optional] 

## Example

```python
from openapi_client.models.put_lke_node_pool_request import PutLkeNodePoolRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutLkeNodePoolRequest from a JSON string
put_lke_node_pool_request_instance = PutLkeNodePoolRequest.from_json(json)
# print the JSON string representation of the object
print(PutLkeNodePoolRequest.to_json())

# convert the object into a dict
put_lke_node_pool_request_dict = put_lke_node_pool_request_instance.to_dict()
# create an instance of PutLkeNodePoolRequest from a dict
put_lke_node_pool_request_from_dict = PutLkeNodePoolRequest.from_dict(put_lke_node_pool_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


