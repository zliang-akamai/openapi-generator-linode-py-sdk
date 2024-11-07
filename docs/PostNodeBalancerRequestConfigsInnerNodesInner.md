# PostNodeBalancerRequestConfigsInnerNodesInner

A NodeBalancerNode represents a single backend serving requests for a single port of a NodeBalancer.  Nodes are specific to NodeBalancer Configs, and serve traffic over their private IP.  If the same Linode is serving traffic for more than one port on the same NodeBalancer, one NodeBalancer Node is required for each config (port) it should serve requests on.  For example, if you have four backends, and each should response to both HTTP and HTTPS requests, you will need two NodeBalancerConfigs (port 80 and port 443) and four backends each - one for each of the Linodes serving requests for that port.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The private IP Address where this backend can be reached. This _must_ be a private IP address. | [optional] 
**config_id** | **int** | The NodeBalancer Config ID that this Node belongs to. | [optional] [readonly] 
**id** | **int** | This node&#39;s unique ID. | [optional] [readonly] 
**label** | **str** | The label for this node.  This is for display purposes only. | [optional] 
**mode** | **str** | The mode this NodeBalancer should use when sending traffic to this backend.  - If set to &#x60;accept&#x60; this backend is accepting traffic. - If set to &#x60;reject&#x60; this backend will not receive traffic. - If set to &#x60;drain&#x60; this backend will not receive _new_ traffic, but connections already pinned to it will continue to be routed to it. - If set to &#x60;backup&#x60;, this backend will only receive traffic if all &#x60;accept&#x60; nodes are down. | [optional] 
**nodebalancer_id** | **int** | The NodeBalancer ID that this Node belongs to. | [optional] [readonly] 
**status** | **str** | The current status of this node, based on the configured checks of its NodeBalancer Config. | [optional] [readonly] 
**weight** | **int** | Used when picking a backend to serve a request and is not pinned to a single backend yet.  Nodes with a higher weight will receive more traffic. | [optional] 

## Example

```python
from openapi_client.models.post_node_balancer_request_configs_inner_nodes_inner import PostNodeBalancerRequestConfigsInnerNodesInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostNodeBalancerRequestConfigsInnerNodesInner from a JSON string
post_node_balancer_request_configs_inner_nodes_inner_instance = PostNodeBalancerRequestConfigsInnerNodesInner.from_json(json)
# print the JSON string representation of the object
print(PostNodeBalancerRequestConfigsInnerNodesInner.to_json())

# convert the object into a dict
post_node_balancer_request_configs_inner_nodes_inner_dict = post_node_balancer_request_configs_inner_nodes_inner_instance.to_dict()
# create an instance of PostNodeBalancerRequestConfigsInnerNodesInner from a dict
post_node_balancer_request_configs_inner_nodes_inner_from_dict = PostNodeBalancerRequestConfigsInnerNodesInner.from_dict(post_node_balancer_request_configs_inner_nodes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


