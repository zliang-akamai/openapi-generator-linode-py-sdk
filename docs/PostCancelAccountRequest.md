# PostCancelAccountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | **str** | Any reason for cancelling the account, and any other comments you might have about your Linode service. | [optional] 

## Example

```python
from openapi_client.models.post_cancel_account_request import PostCancelAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostCancelAccountRequest from a JSON string
post_cancel_account_request_instance = PostCancelAccountRequest.from_json(json)
# print the JSON string representation of the object
print(PostCancelAccountRequest.to_json())

# convert the object into a dict
post_cancel_account_request_dict = post_cancel_account_request_instance.to_dict()
# create an instance of PostCancelAccountRequest from a dict
post_cancel_account_request_from_dict = PostCancelAccountRequest.from_dict(post_cancel_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


