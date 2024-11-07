# PostTfaConfirm200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scratch** | **str** | A one-use code that can be used in place of your Two Factor code, in case you are unable to generate one.  Keep this in a safe place to avoid being locked out of your Account. | [optional] 

## Example

```python
from openapi_client.models.post_tfa_confirm200_response import PostTfaConfirm200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostTfaConfirm200Response from a JSON string
post_tfa_confirm200_response_instance = PostTfaConfirm200Response.from_json(json)
# print the JSON string representation of the object
print(PostTfaConfirm200Response.to_json())

# convert the object into a dict
post_tfa_confirm200_response_dict = post_tfa_confirm200_response_instance.to_dict()
# create an instance of PostTfaConfirm200Response from a dict
post_tfa_confirm200_response_from_dict = PostTfaConfirm200Response.from_dict(post_tfa_confirm200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


