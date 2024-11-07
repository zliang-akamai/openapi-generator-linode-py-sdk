# GetTickets200ResponseDataInner

A Support Ticket opened on your Account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | **List[str]** | A list of filenames representing attached files associated with this Ticket. | [optional] [readonly] 
**closable** | **bool** | Whether the Support Ticket may be closed. | [optional] 
**closed** | **datetime** | The date and time this Ticket was closed. | [optional] [readonly] 
**description** | **str** | The full details of the issue or question. | [optional] [readonly] 
**entity** | [**GetTickets200ResponseDataInnerEntity**](GetTickets200ResponseDataInnerEntity.md) |  | [optional] 
**gravatar_id** | **str** | The Gravatar ID of the User who opened this Ticket. | [optional] [readonly] 
**id** | **int** | The ID of the Support Ticket. | [optional] [readonly] 
**opened** | **datetime** | The date and time this Ticket was created. | [optional] [readonly] 
**opened_by** | **str** | The User who opened this Ticket. | [optional] [readonly] 
**status** | **str** | The current status of this Ticket. | [optional] [readonly] 
**summary** | **str** | The summary or title for this Ticket. | [optional] [readonly] 
**updated** | **datetime** | The date and time this Ticket was last updated. | [optional] [readonly] 
**updated_by** | **str** | The User who last updated this Ticket. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_tickets200_response_data_inner import GetTickets200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTickets200ResponseDataInner from a JSON string
get_tickets200_response_data_inner_instance = GetTickets200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetTickets200ResponseDataInner.to_json())

# convert the object into a dict
get_tickets200_response_data_inner_dict = get_tickets200_response_data_inner_instance.to_dict()
# create an instance of GetTickets200ResponseDataInner from a dict
get_tickets200_response_data_inner_from_dict = GetTickets200ResponseDataInner.from_dict(get_tickets200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


