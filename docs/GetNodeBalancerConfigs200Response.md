# GetNodeBalancerConfigs200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GetNodeBalancerConfigs200ResponseDataInner]**](GetNodeBalancerConfigs200ResponseDataInner.md) |  | [optional] 
**page** | **int** | The current [page](https://techdocs.akamai.com/linode-api/reference/pagination). | [optional] [readonly] 
**pages** | **int** | The total number of [pages](https://techdocs.akamai.com/linode-api/reference/pagination). | [optional] [readonly] 
**results** | **int** | The total number of results. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_node_balancer_configs200_response import GetNodeBalancerConfigs200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetNodeBalancerConfigs200Response from a JSON string
get_node_balancer_configs200_response_instance = GetNodeBalancerConfigs200Response.from_json(json)
# print the JSON string representation of the object
print(GetNodeBalancerConfigs200Response.to_json())

# convert the object into a dict
get_node_balancer_configs200_response_dict = get_node_balancer_configs200_response_instance.to_dict()
# create an instance of GetNodeBalancerConfigs200Response from a dict
get_node_balancer_configs200_response_from_dict = GetNodeBalancerConfigs200Response.from_dict(get_node_balancer_configs200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


