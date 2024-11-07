# PostCancelAccount200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**survey_link** | **str** | A link to Linode&#39;s exit survey. | [optional] 

## Example

```python
from openapi_client.models.post_cancel_account200_response import PostCancelAccount200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostCancelAccount200Response from a JSON string
post_cancel_account200_response_instance = PostCancelAccount200Response.from_json(json)
# print the JSON string representation of the object
print(PostCancelAccount200Response.to_json())

# convert the object into a dict
post_cancel_account200_response_dict = post_cancel_account200_response_instance.to_dict()
# create an instance of PostCancelAccount200Response from a dict
post_cancel_account200_response_from_dict = PostCancelAccount200Response.from_dict(post_cancel_account200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


