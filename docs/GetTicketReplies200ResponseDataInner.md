# GetTicketReplies200ResponseDataInner

An object representing a reply to a Support Ticket.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | The date and time this Ticket reply was created. | [optional] [readonly] 
**created_by** | **str** | The User who submitted this reply. | [optional] [readonly] 
**description** | **str** | The body of this Support Ticket reply. | [optional] [readonly] 
**from_linode** | **bool** | If set to true, this reply came from a Linode employee. | [optional] [readonly] 
**gravatar_id** | **str** | The Gravatar ID of the User who created this reply. | [optional] [readonly] 
**id** | **int** | The unique ID of this Support Ticket reply. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_ticket_replies200_response_data_inner import GetTicketReplies200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTicketReplies200ResponseDataInner from a JSON string
get_ticket_replies200_response_data_inner_instance = GetTicketReplies200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetTicketReplies200ResponseDataInner.to_json())

# convert the object into a dict
get_ticket_replies200_response_data_inner_dict = get_ticket_replies200_response_data_inner_instance.to_dict()
# create an instance of GetTicketReplies200ResponseDataInner from a dict
get_ticket_replies200_response_data_inner_from_dict = GetTicketReplies200ResponseDataInner.from_dict(get_ticket_replies200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


