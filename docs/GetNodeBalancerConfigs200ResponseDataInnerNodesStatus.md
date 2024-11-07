# GetNodeBalancerConfigs200ResponseDataInnerNodesStatus

A structure containing information about the health of the backends for this port.  This information is updated periodically as checks are performed against backends.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**down** | **int** | The number of backends considered to be \&quot;DOWN\&quot; and unhealthy.  These are not in rotation, and not serving requests. | [optional] [readonly] 
**up** | **int** | The number of backends considered to be \&quot;UP\&quot; and healthy, and that are serving requests. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_node_balancer_configs200_response_data_inner_nodes_status import GetNodeBalancerConfigs200ResponseDataInnerNodesStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GetNodeBalancerConfigs200ResponseDataInnerNodesStatus from a JSON string
get_node_balancer_configs200_response_data_inner_nodes_status_instance = GetNodeBalancerConfigs200ResponseDataInnerNodesStatus.from_json(json)
# print the JSON string representation of the object
print(GetNodeBalancerConfigs200ResponseDataInnerNodesStatus.to_json())

# convert the object into a dict
get_node_balancer_configs200_response_data_inner_nodes_status_dict = get_node_balancer_configs200_response_data_inner_nodes_status_instance.to_dict()
# create an instance of GetNodeBalancerConfigs200ResponseDataInnerNodesStatus from a dict
get_node_balancer_configs200_response_data_inner_nodes_status_from_dict = GetNodeBalancerConfigs200ResponseDataInnerNodesStatus.from_dict(get_node_balancer_configs200_response_data_inner_nodes_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


