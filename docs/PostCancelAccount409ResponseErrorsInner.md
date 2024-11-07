# PostCancelAccount409ResponseErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | A string explaining that the account could not be canceled because there is an outstanding balance on the account that must be paid first. | [optional] 

## Example

```python
from openapi_client.models.post_cancel_account409_response_errors_inner import PostCancelAccount409ResponseErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostCancelAccount409ResponseErrorsInner from a JSON string
post_cancel_account409_response_errors_inner_instance = PostCancelAccount409ResponseErrorsInner.from_json(json)
# print the JSON string representation of the object
print(PostCancelAccount409ResponseErrorsInner.to_json())

# convert the object into a dict
post_cancel_account409_response_errors_inner_dict = post_cancel_account409_response_errors_inner_instance.to_dict()
# create an instance of PostCancelAccount409ResponseErrorsInner from a dict
post_cancel_account409_response_errors_inner_from_dict = PostCancelAccount409ResponseErrorsInner.from_dict(post_cancel_account409_response_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


