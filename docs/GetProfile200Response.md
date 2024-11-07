# GetProfile200Response

A Profile represents your User in our system. This is where you can change information about your User. This information is available to any OAuth Client regardless of requested scopes, and can be used to populate User information in third-party applications.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_type** | **str** | This account&#39;s Cloud Manager authentication type. Authentication types are chosen through Cloud Manager and authorized when logging into your account. These authentication types are either the user&#39;s password (in conjunction with their username), or the name of their identity provider such as GitHub. For example, if a user:  - Has never used Third-Party Authentication, their authentication type will be &#x60;password&#x60;. - Is using Third-Party Authentication, their authentication type will be the name of their Identity Provider (eg. &#x60;github&#x60;). - Has used Third-Party Authentication and has since revoked it, their authentication type will be &#x60;password&#x60;.  __Note__. This functionality may not yet be available in Cloud Manager. See the [Cloud Manager Changelog](https://www.linode.com/docs/products/tools/cloud-manager/release-notes/) for the latest updates. | [optional] [readonly] 
**authorized_keys** | **List[str]** | The list of SSH Keys authorized to use Lish for your User. This value is ignored if &#x60;lish_auth_method&#x60; is &#x60;disabled&#x60;. | [optional] 
**email** | **str** | Your email address.  This address will be used for communication with Linode as necessary. | [optional] 
**email_notifications** | **bool** | If true, you will receive email notifications about account activity.  If false, you may still receive business-critical communications through email. | [optional] 
**ip_whitelist_enabled** | **bool** | If true, logins for your User will only be allowed from whitelisted IPs. This setting is currently deprecated, and cannot be enabled. If you disable this setting, you will not be able to re-enable it. | [optional] 
**lish_auth_method** | **str** | The authentication methods that are allowed when connecting to [the Linode Shell (Lish)](https://www.linode.com/docs/guides/lish/).  - &#x60;keys_only&#x60; is the most secure if you intend to use Lish. - &#x60;disabled&#x60; is recommended if you do not intend to use Lish at all. - If this account&#39;s Cloud Manager authentication type is set to a Third-Party Authentication method, &#x60;password_keys&#x60; cannot be used as your Lish authentication method. To view this account&#39;s Cloud Manager &#x60;authentication_type&#x60; field, send a request to the [Get a profile](https://techdocs.akamai.com/linode-api/reference/get-profile) operation. | [optional] 
**referrals** | [**GetProfile200ResponseReferrals**](GetProfile200ResponseReferrals.md) |  | [optional] 
**restricted** | **bool** | If true, your User has restrictions on what can be accessed on your Account. To get details on what entities/actions you can access/perform, run [List grants](https://techdocs.akamai.com/linode-api/reference/get-profile-grants). | [optional] 
**timezone** | **str** | The timezone you prefer to see times in. This is not used by the API directly. It is provided for the benefit of clients such as the Linode Cloud Manager and other clients built on the API. All times returned by the API are in UTC. | [optional] 
**two_factor_auth** | **bool** | If true, logins from untrusted computers will require Two Factor Authentication.  Run [Create a two factor secret](https://techdocs.akamai.com/linode-api/reference/post-tfa-enable) to enable Two Factor Authentication. | [optional] 
**uid** | **int** | Your unique ID in our system. This value will never change, and can safely be used to identify your User. | [optional] [readonly] 
**username** | **str** | Your username, used for logging in to our system. | [optional] [readonly] 
**verified_phone_number** | **str** | The phone number verified for this Profile with the [Verify a phone number](https://techdocs.akamai.com/linode-api/reference/post-profile-phone-number-verify) operation.  &#x60;null&#x60; if this Profile has no verified phone number. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_profile200_response import GetProfile200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetProfile200Response from a JSON string
get_profile200_response_instance = GetProfile200Response.from_json(json)
# print the JSON string representation of the object
print(GetProfile200Response.to_json())

# convert the object into a dict
get_profile200_response_dict = get_profile200_response_instance.to_dict()
# create an instance of GetProfile200Response from a dict
get_profile200_response_from_dict = GetProfile200Response.from_dict(get_profile200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


