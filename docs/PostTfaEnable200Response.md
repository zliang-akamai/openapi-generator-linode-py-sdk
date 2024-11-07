# PostTfaEnable200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry** | **datetime** | When this Two Factor secret expires. | [optional] 
**secret** | **str** | Your Two Factor secret. This is used to generate time-based two factor codes required for logging in. Doing this will be required to confirm TFA an actually enable it. | [optional] 

## Example

```python
from openapi_client.models.post_tfa_enable200_response import PostTfaEnable200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostTfaEnable200Response from a JSON string
post_tfa_enable200_response_instance = PostTfaEnable200Response.from_json(json)
# print the JSON string representation of the object
print(PostTfaEnable200Response.to_json())

# convert the object into a dict
post_tfa_enable200_response_dict = post_tfa_enable200_response_instance.to_dict()
# create an instance of PostTfaEnable200Response from a dict
post_tfa_enable200_response_from_dict = PostTfaEnable200Response.from_dict(post_tfa_enable200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


