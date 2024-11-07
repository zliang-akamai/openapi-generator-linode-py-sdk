# NodeBalancerTransfer

Information about the amount of transfer this NodeBalancer has had so far this month.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_in** | **float** | The total outbound transfer, in MB, used for this NodeBalancer this month. | [optional] [readonly] 
**out** | **float** | The total inbound transfer, in MB, used for this NodeBalancer this month. | [optional] [readonly] 
**total** | **float** | The total transfer, in MB, used by this NodeBalancer this month. | [optional] [readonly] 

## Example

```python
from openapi_client.models.node_balancer_transfer import NodeBalancerTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of NodeBalancerTransfer from a JSON string
node_balancer_transfer_instance = NodeBalancerTransfer.from_json(json)
# print the JSON string representation of the object
print(NodeBalancerTransfer.to_json())

# convert the object into a dict
node_balancer_transfer_dict = node_balancer_transfer_instance.to_dict()
# create an instance of NodeBalancerTransfer from a dict
node_balancer_transfer_from_dict = NodeBalancerTransfer.from_dict(node_balancer_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


