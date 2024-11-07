# UserType

The type of user on an account. Mostly applies to the use of the parent and child accounts for Akamai partners functionality.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_type** | **str** | If the user belongs to a [parent or child account](https://www.linode.com/docs/guides/parent-child-accounts/) relationship, this defines the user type in the respective account. Possible values include:  - &#x60;parent&#x60;. This is a user in an Akamai partner account. Akamai partners have a contractural relationship with their end customers, to sell Akamai services. This user can either have full access (a parent account admin user) or limited access. Limited users don&#39;t have access to manage child accounts, but they can be granted this access by an admin user.  - &#x60;child&#x60;. This is an Akamai partner&#39;s end customer user, in a child account. A child user can have either full or limited access. Full access lets the user manage other child users and the proxy user in a child account.  - &#x60;proxy&#x60;. This is a user on a child account that gives parent account users access to that child account. A parent account user with the &#x60;child_account_access&#x60; grant can [Create a proxy user token](https://techdocs.akamai.com/linode-api/reference/post-child-account-token) from the parent account. The parent user can use this token to run API operations from the child account, as if they were a child user.  - &#x60;default&#x60;. This applies to all regular, non-parent-child account users. | [optional] [readonly] 

## Example

```python
from openapi_client.models.user_type import UserType

# TODO update the JSON string below
json = "{}"
# create an instance of UserType from a JSON string
user_type_instance = UserType.from_json(json)
# print the JSON string representation of the object
print(UserType.to_json())

# convert the object into a dict
user_type_dict = user_type_instance.to_dict()
# create an instance of UserType from a dict
user_type_from_dict = UserType.from_dict(user_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


