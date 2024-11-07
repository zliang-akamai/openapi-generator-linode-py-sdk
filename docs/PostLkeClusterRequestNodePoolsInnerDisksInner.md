# PostLkeClusterRequestNodePoolsInnerDisksInner

The values to assign to each partition in this Node Pool's custom disk layout.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **int** | The size of this custom disk partition in MB. The size of this disk partition can&#39;t exceed the capacity of the node&#39;s plan type. | [optional] 
**type** | **str** | This custom disk partition&#39;s filesystem type. | [optional] 

## Example

```python
from openapi_client.models.post_lke_cluster_request_node_pools_inner_disks_inner import PostLkeClusterRequestNodePoolsInnerDisksInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostLkeClusterRequestNodePoolsInnerDisksInner from a JSON string
post_lke_cluster_request_node_pools_inner_disks_inner_instance = PostLkeClusterRequestNodePoolsInnerDisksInner.from_json(json)
# print the JSON string representation of the object
print(PostLkeClusterRequestNodePoolsInnerDisksInner.to_json())

# convert the object into a dict
post_lke_cluster_request_node_pools_inner_disks_inner_dict = post_lke_cluster_request_node_pools_inner_disks_inner_instance.to_dict()
# create an instance of PostLkeClusterRequestNodePoolsInnerDisksInner from a dict
post_lke_cluster_request_node_pools_inner_disks_inner_from_dict = PostLkeClusterRequestNodePoolsInnerDisksInner.from_dict(post_lke_cluster_request_node_pools_inner_disks_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


