# GetProfile200ResponseReferrals

Information about your status in our referral program.  This information becomes accessible after this Profile's Account has established at least $25.00 USD of total payments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Your referral code.  If others use this when signing up for Linode, you will receive account credit. | [optional] [readonly] 
**completed** | **int** | The number of completed signups with your referral code. | [optional] [readonly] 
**credit** | **int** | The amount of account credit in US Dollars issued to you through the referral program. | [optional] [readonly] 
**pending** | **int** | The number of pending signups with your referral code.  You will not receive credit for these signups until they are completed. | [optional] [readonly] 
**total** | **int** | The number of users who have signed up with your referral code. | [optional] [readonly] 
**url** | **str** | Your referral url, used to direct others to sign up for Linode with your referral code. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_profile200_response_referrals import GetProfile200ResponseReferrals

# TODO update the JSON string below
json = "{}"
# create an instance of GetProfile200ResponseReferrals from a JSON string
get_profile200_response_referrals_instance = GetProfile200ResponseReferrals.from_json(json)
# print the JSON string representation of the object
print(GetProfile200ResponseReferrals.to_json())

# convert the object into a dict
get_profile200_response_referrals_dict = get_profile200_response_referrals_instance.to_dict()
# create an instance of GetProfile200ResponseReferrals from a dict
get_profile200_response_referrals_from_dict = GetProfile200ResponseReferrals.from_dict(get_profile200_response_referrals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


