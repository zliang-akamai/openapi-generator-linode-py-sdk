# PostProfilePhoneNumberVerifyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**otp_code** | **str** | The one-time code received via SMS message after running the [Send a phone number verification code](https://techdocs.akamai.com/linode-api/reference/post-profile-phone-number) operation. | 

## Example

```python
from openapi_client.models.post_profile_phone_number_verify_request import PostProfilePhoneNumberVerifyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostProfilePhoneNumberVerifyRequest from a JSON string
post_profile_phone_number_verify_request_instance = PostProfilePhoneNumberVerifyRequest.from_json(json)
# print the JSON string representation of the object
print(PostProfilePhoneNumberVerifyRequest.to_json())

# convert the object into a dict
post_profile_phone_number_verify_request_dict = post_profile_phone_number_verify_request_instance.to_dict()
# create an instance of PostProfilePhoneNumberVerifyRequest from a dict
post_profile_phone_number_verify_request_from_dict = PostProfilePhoneNumberVerifyRequest.from_dict(post_profile_phone_number_verify_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


