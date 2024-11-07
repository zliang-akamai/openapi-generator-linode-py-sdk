# PostCancelAccount409Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[PostCancelAccount409ResponseErrorsInner]**](PostCancelAccount409ResponseErrorsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.post_cancel_account409_response import PostCancelAccount409Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostCancelAccount409Response from a JSON string
post_cancel_account409_response_instance = PostCancelAccount409Response.from_json(json)
# print the JSON string representation of the object
print(PostCancelAccount409Response.to_json())

# convert the object into a dict
post_cancel_account409_response_dict = post_cancel_account409_response_instance.to_dict()
# create an instance of PostCancelAccount409Response from a dict
post_cancel_account409_response_from_dict = PostCancelAccount409Response.from_dict(post_cancel_account409_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


