# PostLkeClusterPoolsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoscaler** | [**PostLkeClusterRequestNodePoolsInnerAutoscaler**](PostLkeClusterRequestNodePoolsInnerAutoscaler.md) |  | [optional] 
**count** | **int** | The number of nodes in the Node Pool. | 
**disks** | [**List[PostLkeClusterRequestNodePoolsInnerDisksInner]**](PostLkeClusterRequestNodePoolsInnerDisksInner.md) | This node pool&#39;s custom disk layout. Each item in this array will create a new disk partition for each node in this node pool.  &gt; 📘 &gt; &gt; Omit this field, except for special use cases. The disks specified here are partitions in _addition_ to the primary partition and reduce the size of the primary partition. This can lead to stability problems for the node.    - The custom disk layout is applied to each node in this node pool.    - The maximum number of custom disk partitions that can be configured is 7.    - Once the requested disk partitions are allocated, the remaining disk space is allocated to the node&#39;s boot disk.    - A node pool&#39;s custom disk layout is immutable over the lifetime of the node pool. | [optional] 
**labels** | **List[object]** | Key-value pairs added as labels to nodes in the node pool. Labels help classify your nodes and easily select subsets of objects. To learn more, review [Add Labels and Taints to your LKE node pools](https://www.linode.com/docs/products/compute/kubernetes/guides/deploy-and-manage-cluster-with-the-linode-api/#add-labels-and-taints-to-your-lke-node-pools).  Specifying an empty dictionary value will remove all previously set labels. | [optional] 
**tags** | **List[str]** | An array of tags applied to this object. Tags are for organizational purposes only. | [optional] 
**taints** | [**List[PostLkeClusterRequestNodePoolsInnerTaintsInner]**](PostLkeClusterRequestNodePoolsInnerTaintsInner.md) | Kubernetes taints to add to node pool nodes. Taints help control how pods are scheduled onto nodes, specifically allowing them to repel certain pods. To learn more, review [Add labels and taints to your LKE node pools](https://www.linode.com/docs/products/compute/kubernetes/guides/deploy-and-manage-cluster-with-the-linode-api/#add-labels-and-taints-to-your-lke-node-pools).  Specifying an empty array (&#x60;[]&#x60;) removes all previously set taints. | [optional] 
**type** | **str** | The Linode Type for all of the nodes in the Node Pool. | 

## Example

```python
from openapi_client.models.post_lke_cluster_pools_request import PostLkeClusterPoolsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostLkeClusterPoolsRequest from a JSON string
post_lke_cluster_pools_request_instance = PostLkeClusterPoolsRequest.from_json(json)
# print the JSON string representation of the object
print(PostLkeClusterPoolsRequest.to_json())

# convert the object into a dict
post_lke_cluster_pools_request_dict = post_lke_cluster_pools_request_instance.to_dict()
# create an instance of PostLkeClusterPoolsRequest from a dict
post_lke_cluster_pools_request_from_dict = PostLkeClusterPoolsRequest.from_dict(post_lke_cluster_pools_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


