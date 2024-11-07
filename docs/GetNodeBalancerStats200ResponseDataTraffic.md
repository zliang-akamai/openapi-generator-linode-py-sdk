# GetNodeBalancerStats200ResponseDataTraffic

Traffic statistics for this NodeBalancer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_in** | **List[float]** | An array of key/value pairs representing unix timestamp and reading for inbound traffic. | [optional] 
**out** | **List[float]** | An array of key/value pairs representing unix timestamp and reading for outbound traffic. | [optional] 

## Example

```python
from openapi_client.models.get_node_balancer_stats200_response_data_traffic import GetNodeBalancerStats200ResponseDataTraffic

# TODO update the JSON string below
json = "{}"
# create an instance of GetNodeBalancerStats200ResponseDataTraffic from a JSON string
get_node_balancer_stats200_response_data_traffic_instance = GetNodeBalancerStats200ResponseDataTraffic.from_json(json)
# print the JSON string representation of the object
print(GetNodeBalancerStats200ResponseDataTraffic.to_json())

# convert the object into a dict
get_node_balancer_stats200_response_data_traffic_dict = get_node_balancer_stats200_response_data_traffic_instance.to_dict()
# create an instance of GetNodeBalancerStats200ResponseDataTraffic from a dict
get_node_balancer_stats200_response_data_traffic_from_dict = GetNodeBalancerStats200ResponseDataTraffic.from_dict(get_node_balancer_stats200_response_data_traffic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


