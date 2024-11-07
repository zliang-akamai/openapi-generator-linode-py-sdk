# GetNodeBalancerStats200ResponseData

The data returned about this NodeBalancers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connections** | **List[float]** | An array of key/value pairs representing unix timestamp and reading for connections to this NodeBalancer. | [optional] 
**traffic** | [**GetNodeBalancerStats200ResponseDataTraffic**](GetNodeBalancerStats200ResponseDataTraffic.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_node_balancer_stats200_response_data import GetNodeBalancerStats200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetNodeBalancerStats200ResponseData from a JSON string
get_node_balancer_stats200_response_data_instance = GetNodeBalancerStats200ResponseData.from_json(json)
# print the JSON string representation of the object
print(GetNodeBalancerStats200ResponseData.to_json())

# convert the object into a dict
get_node_balancer_stats200_response_data_dict = get_node_balancer_stats200_response_data_instance.to_dict()
# create an instance of GetNodeBalancerStats200ResponseData from a dict
get_node_balancer_stats200_response_data_from_dict = GetNodeBalancerStats200ResponseData.from_dict(get_node_balancer_stats200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


