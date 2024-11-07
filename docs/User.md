# User

A User on your Account. Unrestricted users can log in and access information about your Account, while restricted users may only access entities or perform actions they've been granted access to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The email address for the User. Linode sends emails to this address for account management communications. May be used for other communications as configured. | [optional] 
**last_login** | [**GetUsers200ResponseDataInnerAllOfLastLogin**](GetUsers200ResponseDataInnerAllOfLastLogin.md) |  | [optional] 
**password_created** | **datetime** | The date and time when this User&#39;s current password was created.  User passwords are first created during the Account sign-up process, and updated using the [Reset Password](https://login.linode.com/forgot/password) webpage.  &#x60;null&#x60; if this User has not created a password yet. | [optional] [readonly] 
**restricted** | **bool** | If true, the User must be granted access to perform actions or access entities on this Account. Run [List a user&#39;s grants](https://techdocs.akamai.com/linode-api/reference/get-user-grants) for details on how to configure grants for a restricted User. | [optional] 
**ssh_keys** | **List[str]** | A list of SSH Key labels added by this User.  Users can add keys with the [Add an SSH key](https://techdocs.akamai.com/linode-api/reference/post-add-ssh-key) operation.  These keys are deployed when this User is included in the &#x60;authorized_users&#x60; field of the following requests:  - [Create a Linode](https://techdocs.akamai.com/linode-api/reference/post-linode-instance) - [Rebuild a Linode](https://techdocs.akamai.com/linode-api/reference/post-rebuild-linode-instance) - [Create a disk](https://techdocs.akamai.com/linode-api/reference/post-add-linode-disk) | [optional] [readonly] 
**tfa_enabled** | **bool** | A boolean value indicating if the User has Two Factor Authentication (TFA) enabled. Run the [Create a two factor secret](https://techdocs.akamai.com/linode-api/reference/post-tfa-enable) operation to enable TFA. | [optional] [readonly] 
**username** | **str** | The User&#39;s username. This is used for logging in, and may also be displayed alongside actions the User performs (for example, in Events or public StackScripts). | [optional] 
**verified_phone_number** | **str** | The phone number verified for this User Profile with the [Verify a phone number](https://techdocs.akamai.com/linode-api/reference/post-profile-phone-number-verify) operation.  &#x60;null&#x60; if this User Profile has no verified phone number. | [optional] [readonly] 

## Example

```python
from openapi_client.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


