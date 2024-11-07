# PostLkeClusterRequestNodePoolsInnerAutoscaler

When enabled, the number of nodes automatically scales within the defined minimum and maximum values. When making a request, `max` and `min` require each other.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether automatic scaling is enabled for this node pool. Defaults to &#x60;false&#x60;. | [optional] 
**max** | **int** | The maximum number of nodes to automatically scale to. Defaults to the value provided by the &#x60;count&#x60; field. | [optional] 
**min** | **int** | The minimum number of nodes to automatically scale to. Defaults to the node pool&#39;s &#x60;count&#x60;. | [optional] 

## Example

```python
from openapi_client.models.post_lke_cluster_request_node_pools_inner_autoscaler import PostLkeClusterRequestNodePoolsInnerAutoscaler

# TODO update the JSON string below
json = "{}"
# create an instance of PostLkeClusterRequestNodePoolsInnerAutoscaler from a JSON string
post_lke_cluster_request_node_pools_inner_autoscaler_instance = PostLkeClusterRequestNodePoolsInnerAutoscaler.from_json(json)
# print the JSON string representation of the object
print(PostLkeClusterRequestNodePoolsInnerAutoscaler.to_json())

# convert the object into a dict
post_lke_cluster_request_node_pools_inner_autoscaler_dict = post_lke_cluster_request_node_pools_inner_autoscaler_instance.to_dict()
# create an instance of PostLkeClusterRequestNodePoolsInnerAutoscaler from a dict
post_lke_cluster_request_node_pools_inner_autoscaler_from_dict = PostLkeClusterRequestNodePoolsInnerAutoscaler.from_dict(post_lke_cluster_request_node_pools_inner_autoscaler_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


