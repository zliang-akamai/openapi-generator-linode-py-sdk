# GetTickets200ResponseDataInnerEntity

The entity this Ticket was opened for.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique ID for this Ticket&#39;s entity. | [optional] [readonly] 
**label** | **str** | The current label of this entity. | [optional] [readonly] 
**type** | **str** | The type of entity this is related to. | [optional] [readonly] 
**url** | **str** | The URL where you can access the object this event is for. If a relative URL, it is relative to the domain you retrieved the entity from. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_tickets200_response_data_inner_entity import GetTickets200ResponseDataInnerEntity

# TODO update the JSON string below
json = "{}"
# create an instance of GetTickets200ResponseDataInnerEntity from a JSON string
get_tickets200_response_data_inner_entity_instance = GetTickets200ResponseDataInnerEntity.from_json(json)
# print the JSON string representation of the object
print(GetTickets200ResponseDataInnerEntity.to_json())

# convert the object into a dict
get_tickets200_response_data_inner_entity_dict = get_tickets200_response_data_inner_entity_instance.to_dict()
# create an instance of GetTickets200ResponseDataInnerEntity from a dict
get_tickets200_response_data_inner_entity_from_dict = GetTickets200ResponseDataInnerEntity.from_dict(get_tickets200_response_data_inner_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


