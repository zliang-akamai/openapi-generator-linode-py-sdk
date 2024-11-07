# PostTfaConfirmRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tfa_code** | **str** | The Two Factor code you generated with your Two Factor secret. These codes are time-based, so be sure it is current. | [optional] 

## Example

```python
from openapi_client.models.post_tfa_confirm_request import PostTfaConfirmRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostTfaConfirmRequest from a JSON string
post_tfa_confirm_request_instance = PostTfaConfirmRequest.from_json(json)
# print the JSON string representation of the object
print(PostTfaConfirmRequest.to_json())

# convert the object into a dict
post_tfa_confirm_request_dict = post_tfa_confirm_request_instance.to_dict()
# create an instance of PostTfaConfirmRequest from a dict
post_tfa_confirm_request_from_dict = PostTfaConfirmRequest.from_dict(post_tfa_confirm_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


