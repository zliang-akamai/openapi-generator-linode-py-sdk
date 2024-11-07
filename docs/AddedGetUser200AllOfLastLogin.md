# AddedGetUser200AllOfLastLogin

Information for the most recent login attempt for this User.  `null` if no login attempts have been made since creation of this User.  Run the [List user logins](https://techdocs.akamai.com/linode-api/reference/get-account-logins) operation for additional login information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login_datetime** | **datetime** | The date and time of this User&#39;s most recent login attempt. | [optional] [readonly] 
**status** | **str** | The result of the most recent login attempt for this User. | [optional] [readonly] 

## Example

```python
from openapi_client.models.added_get_user200_all_of_last_login import AddedGetUser200AllOfLastLogin

# TODO update the JSON string below
json = "{}"
# create an instance of AddedGetUser200AllOfLastLogin from a JSON string
added_get_user200_all_of_last_login_instance = AddedGetUser200AllOfLastLogin.from_json(json)
# print the JSON string representation of the object
print(AddedGetUser200AllOfLastLogin.to_json())

# convert the object into a dict
added_get_user200_all_of_last_login_dict = added_get_user200_all_of_last_login_instance.to_dict()
# create an instance of AddedGetUser200AllOfLastLogin from a dict
added_get_user200_all_of_last_login_from_dict = AddedGetUser200AllOfLastLogin.from_dict(added_get_user200_all_of_last_login_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


