# AddedPostCancelAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | **str** | Any reason for cancelling the account, and any other comments you might have about your Linode service. | [optional] 

## Example

```python
from openapi_client.models.added_post_cancel_account import AddedPostCancelAccount

# TODO update the JSON string below
json = "{}"
# create an instance of AddedPostCancelAccount from a JSON string
added_post_cancel_account_instance = AddedPostCancelAccount.from_json(json)
# print the JSON string representation of the object
print(AddedPostCancelAccount.to_json())

# convert the object into a dict
added_post_cancel_account_dict = added_post_cancel_account_instance.to_dict()
# create an instance of AddedPostCancelAccount from a dict
added_post_cancel_account_from_dict = AddedPostCancelAccount.from_dict(added_post_cancel_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


