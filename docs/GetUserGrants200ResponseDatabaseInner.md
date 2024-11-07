# GetUserGrants200ResponseDatabaseInner

Represents the level of access a restricted User has to a specific resource on the Account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the entity this grant applies to. | [optional] 
**label** | **str** | The current label of the entity this grant applies to, for display purposes. | [optional] [readonly] 
**permissions** | **str** | The level of access this User has to this entity.  If null, this User has no access. | [optional] 

## Example

```python
from openapi_client.models.get_user_grants200_response_database_inner import GetUserGrants200ResponseDatabaseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserGrants200ResponseDatabaseInner from a JSON string
get_user_grants200_response_database_inner_instance = GetUserGrants200ResponseDatabaseInner.from_json(json)
# print the JSON string representation of the object
print(GetUserGrants200ResponseDatabaseInner.to_json())

# convert the object into a dict
get_user_grants200_response_database_inner_dict = get_user_grants200_response_database_inner_instance.to_dict()
# create an instance of GetUserGrants200ResponseDatabaseInner from a dict
get_user_grants200_response_database_inner_from_dict = GetUserGrants200ResponseDatabaseInner.from_dict(get_user_grants200_response_database_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


