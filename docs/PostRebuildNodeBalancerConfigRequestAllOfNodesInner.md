# PostRebuildNodeBalancerConfigRequestAllOfNodesInner

NodeBalancer Node request object including ID.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The private IP Address where this backend can be reached. This _must_ be a private IP address. | [optional] 
**id** | **int** | The unique ID of the Node to update. | [optional] 
**label** | **str** | The label for this node.  This is for display purposes only. | [optional] 
**mode** | **str** | The mode this NodeBalancer should use when sending traffic to this backend.  - If set to &#x60;accept&#x60; this backend is accepting traffic. - If set to &#x60;reject&#x60; this backend will not receive traffic. - If set to &#x60;drain&#x60; this backend will not receive _new_ traffic, but connections already pinned to it will continue to be routed to it. - If set to &#x60;backup&#x60;, this backend will only receive traffic if all &#x60;accept&#x60; nodes are down. | [optional] 
**weight** | **int** | Used when picking a backend to serve a request and is not pinned to a single backend yet.  Nodes with a higher weight will receive more traffic. | [optional] 

## Example

```python
from openapi_client.models.post_rebuild_node_balancer_config_request_all_of_nodes_inner import PostRebuildNodeBalancerConfigRequestAllOfNodesInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostRebuildNodeBalancerConfigRequestAllOfNodesInner from a JSON string
post_rebuild_node_balancer_config_request_all_of_nodes_inner_instance = PostRebuildNodeBalancerConfigRequestAllOfNodesInner.from_json(json)
# print the JSON string representation of the object
print(PostRebuildNodeBalancerConfigRequestAllOfNodesInner.to_json())

# convert the object into a dict
post_rebuild_node_balancer_config_request_all_of_nodes_inner_dict = post_rebuild_node_balancer_config_request_all_of_nodes_inner_instance.to_dict()
# create an instance of PostRebuildNodeBalancerConfigRequestAllOfNodesInner from a dict
post_rebuild_node_balancer_config_request_all_of_nodes_inner_from_dict = PostRebuildNodeBalancerConfigRequestAllOfNodesInner.from_dict(post_rebuild_node_balancer_config_request_all_of_nodes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


