# GetUsers200ResponseDataInnerAllOfLastLogin

Information for the most recent login attempt for this User.  `null` if no login attempts have been made since creation of this User.  Run the [List user logins](https://techdocs.akamai.com/linode-api/reference/get-account-logins) operation for additional login information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login_datetime** | **datetime** | The date and time of this User&#39;s most recent login attempt. | [optional] [readonly] 
**status** | **str** | The result of the most recent login attempt for this User. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_users200_response_data_inner_all_of_last_login import GetUsers200ResponseDataInnerAllOfLastLogin

# TODO update the JSON string below
json = "{}"
# create an instance of GetUsers200ResponseDataInnerAllOfLastLogin from a JSON string
get_users200_response_data_inner_all_of_last_login_instance = GetUsers200ResponseDataInnerAllOfLastLogin.from_json(json)
# print the JSON string representation of the object
print(GetUsers200ResponseDataInnerAllOfLastLogin.to_json())

# convert the object into a dict
get_users200_response_data_inner_all_of_last_login_dict = get_users200_response_data_inner_all_of_last_login_instance.to_dict()
# create an instance of GetUsers200ResponseDataInnerAllOfLastLogin from a dict
get_users200_response_data_inner_all_of_last_login_from_dict = GetUsers200ResponseDataInnerAllOfLastLogin.from_dict(get_users200_response_data_inner_all_of_last_login_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


