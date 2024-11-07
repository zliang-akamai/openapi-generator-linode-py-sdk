# PostNodeBalancerNodeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The private IP Address where this backend can be reached. This _must_ be a private IP address. | 
**config_id** | **int** | The NodeBalancer Config ID that this Node belongs to. | [optional] [readonly] 
**id** | **int** | This node&#39;s unique ID. | [optional] [readonly] 
**label** | **str** | The label for this node.  This is for display purposes only. | 
**mode** | **str** | The mode this NodeBalancer should use when sending traffic to this backend.  - If set to &#x60;accept&#x60; this backend is accepting traffic. - If set to &#x60;reject&#x60; this backend will not receive traffic. - If set to &#x60;drain&#x60; this backend will not receive _new_ traffic, but connections already pinned to it will continue to be routed to it. - If set to &#x60;backup&#x60;, this backend will only receive traffic if all &#x60;accept&#x60; nodes are down. | [optional] 
**nodebalancer_id** | **int** | The NodeBalancer ID that this Node belongs to. | [optional] [readonly] 
**status** | **str** | The current status of this node, based on the configured checks of its NodeBalancer Config. | [optional] [readonly] 
**weight** | **int** | Used when picking a backend to serve a request and is not pinned to a single backend yet.  Nodes with a higher weight will receive more traffic. | [optional] 

## Example

```python
from openapi_client.models.post_node_balancer_node_request import PostNodeBalancerNodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostNodeBalancerNodeRequest from a JSON string
post_node_balancer_node_request_instance = PostNodeBalancerNodeRequest.from_json(json)
# print the JSON string representation of the object
print(PostNodeBalancerNodeRequest.to_json())

# convert the object into a dict
post_node_balancer_node_request_dict = post_node_balancer_node_request_instance.to_dict()
# create an instance of PostNodeBalancerNodeRequest from a dict
post_node_balancer_node_request_from_dict = PostNodeBalancerNodeRequest.from_dict(post_node_balancer_node_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


