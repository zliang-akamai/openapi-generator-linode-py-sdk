# Grant

Represents the level of access a restricted User has to a specific resource on the Account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the entity this grant applies to. | [optional] 
**label** | **str** | The current label of the entity this grant applies to, for display purposes. | [optional] [readonly] 
**permissions** | **str** | The level of access this User has to this entity.  If null, this User has no access. | [optional] 

## Example

```python
from openapi_client.models.grant import Grant

# TODO update the JSON string below
json = "{}"
# create an instance of Grant from a JSON string
grant_instance = Grant.from_json(json)
# print the JSON string representation of the object
print(Grant.to_json())

# convert the object into a dict
grant_dict = grant_instance.to_dict()
# create an instance of Grant from a dict
grant_from_dict = Grant.from_dict(grant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


