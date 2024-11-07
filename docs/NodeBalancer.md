# NodeBalancer

Linode's load balancing solution.  Can handle multiple ports, SSL termination, and any number of backends.  NodeBalancer ports are configured with NodeBalancer Configs, and each config is given one or more NodeBalancer Node that accepts traffic.  The traffic should be routed to the  NodeBalancer's ip address, the NodeBalancer will handle routing individual requests to backends.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_conn_throttle** | **int** | Throttle connections per second.  Set to 0 (zero) to disable throttling. | [optional] 
**created** | **datetime** | When this NodeBalancer was created. | [optional] [readonly] 
**hostname** | **str** | This NodeBalancer&#39;s hostname, beginning with its IP address and ending with _.ip.linodeusercontent.com_. | [optional] [readonly] 
**id** | **int** | This NodeBalancer&#39;s unique ID. | [optional] [readonly] 
**ipv4** | **str** | This NodeBalancer&#39;s public IPv4 address. | [optional] [readonly] 
**ipv6** | **str** | This NodeBalancer&#39;s public IPv6 address. | [optional] [readonly] 
**label** | **str** | This NodeBalancer&#39;s label. These must be unique on your Account. | [optional] 
**region** | **str** | The Region where this NodeBalancer is located. NodeBalancers only support backends in the same Region. | [optional] [readonly] 
**tags** | **List[str]** | An array of Tags applied to this object.  Tags are for organizational purposes only. | [optional] 
**transfer** | [**NodeBalancerTransfer**](NodeBalancerTransfer.md) |  | [optional] 
**updated** | **datetime** | When this NodeBalancer was last updated. | [optional] [readonly] 

## Example

```python
from openapi_client.models.node_balancer import NodeBalancer

# TODO update the JSON string below
json = "{}"
# create an instance of NodeBalancer from a JSON string
node_balancer_instance = NodeBalancer.from_json(json)
# print the JSON string representation of the object
print(NodeBalancer.to_json())

# convert the object into a dict
node_balancer_dict = node_balancer_instance.to_dict()
# create an instance of NodeBalancer from a dict
node_balancer_from_dict = NodeBalancer.from_dict(node_balancer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


