# GetManagedIssues200ResponseDataInnerEntity

The ticket this Managed Issue opened.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | This ticket&#39;s ID. | [optional] [readonly] 
**label** | **str** | The summary for this Ticket. | [optional] [readonly] 
**type** | **str** | The type of entity this is. In this case, it is always a Ticket. | [optional] [readonly] 
**url** | **str** | The relative URL where you can access this Ticket. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_managed_issues200_response_data_inner_entity import GetManagedIssues200ResponseDataInnerEntity

# TODO update the JSON string below
json = "{}"
# create an instance of GetManagedIssues200ResponseDataInnerEntity from a JSON string
get_managed_issues200_response_data_inner_entity_instance = GetManagedIssues200ResponseDataInnerEntity.from_json(json)
# print the JSON string representation of the object
print(GetManagedIssues200ResponseDataInnerEntity.to_json())

# convert the object into a dict
get_managed_issues200_response_data_inner_entity_dict = get_managed_issues200_response_data_inner_entity_instance.to_dict()
# create an instance of GetManagedIssues200ResponseDataInnerEntity from a dict
get_managed_issues200_response_data_inner_entity_from_dict = GetManagedIssues200ResponseDataInnerEntity.from_dict(get_managed_issues200_response_data_inner_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


