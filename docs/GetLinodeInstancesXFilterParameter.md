# GetLinodeInstancesXFilterParameter

Specifies the `X-Filter` header JSON object's filtering and sort criteria.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | **List[object]** | All conditions need to be true. | [optional] 
**contains** | **str** | The provided string needs to be in the value. | [optional] 
**gt** | **float** | The value needs to be greater than the provided number. | [optional] 
**gte** | **float** | The value needs to be greater than or equal to the provided number. | [optional] 
**lt** | **float** | The value needs to be less than the provided number. | [optional] 
**lte** | **float** | The value needs to be less than or equal to the provided number. | [optional] 
**neq** | **str** | The provided string is left out of the results. | [optional] 
**var_or** | **List[object]** | At least one condition needs to be true. | [optional] 
**order** | **str** | Sort in ascending (&#x60;asc&#x60;) or descending (&#x60;desc&#x60;) order. This defaults to &#x60;asc&#x60;. Requires &#x60;+order_by&#x60;. | [optional] [default to 'asc']
**order_by** | **str** | Order results based on the provided attribute. The attribute needs to be filterable. | [optional] 

## Example

```python
from openapi_client.models.get_linode_instances_x_filter_parameter import GetLinodeInstancesXFilterParameter

# TODO update the JSON string below
json = "{}"
# create an instance of GetLinodeInstancesXFilterParameter from a JSON string
get_linode_instances_x_filter_parameter_instance = GetLinodeInstancesXFilterParameter.from_json(json)
# print the JSON string representation of the object
print(GetLinodeInstancesXFilterParameter.to_json())

# convert the object into a dict
get_linode_instances_x_filter_parameter_dict = get_linode_instances_x_filter_parameter_instance.to_dict()
# create an instance of GetLinodeInstancesXFilterParameter from a dict
get_linode_instances_x_filter_parameter_from_dict = GetLinodeInstancesXFilterParameter.from_dict(get_linode_instances_x_filter_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


