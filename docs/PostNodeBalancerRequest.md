# PostNodeBalancerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_conn_throttle** | **int** | Throttle connections per second.  Set to 0 (zero) to disable throttling. | [optional] 
**configs** | [**List[PostNodeBalancerRequestConfigsInner]**](PostNodeBalancerRequestConfigsInner.md) | The port Configs to create for this NodeBalancer.  Each Config must have a unique port and at least one Node. | [optional] 
**firewall_id** | **int** | The ID of the Firewall to assign to the NodeBalancer.  - A NodeBalancer can have only one Firewall assigned to it. - Firewalls only apply to inbound TCP traffic to NodeBalancers. | [optional] 
**label** | **str** | This NodeBalancer&#39;s label. These must be unique on your Account. | [optional] 
**region** | **str** | The ID of the Region to create this NodeBalancer in. | 
**tags** | **List[str]** | An array of Tags applied to this object. Tags are for organizational purposes only. | [optional] 

## Example

```python
from openapi_client.models.post_node_balancer_request import PostNodeBalancerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostNodeBalancerRequest from a JSON string
post_node_balancer_request_instance = PostNodeBalancerRequest.from_json(json)
# print the JSON string representation of the object
print(PostNodeBalancerRequest.to_json())

# convert the object into a dict
post_node_balancer_request_dict = post_node_balancer_request_instance.to_dict()
# create an instance of PostNodeBalancerRequest from a dict
post_node_balancer_request_from_dict = PostNodeBalancerRequest.from_dict(post_node_balancer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


