# GetNodeBalancerStats200Response

Stats for this NodeBalancer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GetNodeBalancerStats200ResponseData**](GetNodeBalancerStats200ResponseData.md) |  | [optional] 
**title** | **str** | The title for the statistics generated in this response. | [optional] 

## Example

```python
from openapi_client.models.get_node_balancer_stats200_response import GetNodeBalancerStats200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetNodeBalancerStats200Response from a JSON string
get_node_balancer_stats200_response_instance = GetNodeBalancerStats200Response.from_json(json)
# print the JSON string representation of the object
print(GetNodeBalancerStats200Response.to_json())

# convert the object into a dict
get_node_balancer_stats200_response_dict = get_node_balancer_stats200_response_instance.to_dict()
# create an instance of GetNodeBalancerStats200Response from a dict
get_node_balancer_stats200_response_from_dict = GetNodeBalancerStats200Response.from_dict(get_node_balancer_stats200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


