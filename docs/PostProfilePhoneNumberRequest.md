# PostProfilePhoneNumberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iso_code** | **str** | The two-letter ISO 3166 country code associated with the phone number. | 
**phone_number** | **str** | A valid phone number. | 

## Example

```python
from openapi_client.models.post_profile_phone_number_request import PostProfilePhoneNumberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostProfilePhoneNumberRequest from a JSON string
post_profile_phone_number_request_instance = PostProfilePhoneNumberRequest.from_json(json)
# print the JSON string representation of the object
print(PostProfilePhoneNumberRequest.to_json())

# convert the object into a dict
post_profile_phone_number_request_dict = post_profile_phone_number_request_instance.to_dict()
# create an instance of PostProfilePhoneNumberRequest from a dict
post_profile_phone_number_request_from_dict = PostProfilePhoneNumberRequest.from_dict(post_profile_phone_number_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


