# PostTicketReplyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The content of your reply. | 

## Example

```python
from openapi_client.models.post_ticket_reply_request import PostTicketReplyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostTicketReplyRequest from a JSON string
post_ticket_reply_request_instance = PostTicketReplyRequest.from_json(json)
# print the JSON string representation of the object
print(PostTicketReplyRequest.to_json())

# convert the object into a dict
post_ticket_reply_request_dict = post_ticket_reply_request_instance.to_dict()
# create an instance of PostTicketReplyRequest from a dict
post_ticket_reply_request_from_dict = PostTicketReplyRequest.from_dict(post_ticket_reply_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


