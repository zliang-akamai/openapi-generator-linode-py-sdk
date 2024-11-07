# GrantsResponse

A structure representing all grants a restricted User has on the Account. Not available for unrestricted users, as they have access to everything without grants. If retrieved from the `/profile/grants` endpoint, entities to which a User has no access will be omitted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database** | [**List[GetUserGrants200ResponseDatabaseInner]**](GetUserGrants200ResponseDatabaseInner.md) | The grants this User has for each Database that is owned by this Account. | [optional] 
**domain** | [**List[GetUserGrants200ResponseDatabaseInner]**](GetUserGrants200ResponseDatabaseInner.md) | The grants this User has for each Domain that is owned by this Account. | [optional] 
**firewall** | [**List[GetUserGrants200ResponseDatabaseInner]**](GetUserGrants200ResponseDatabaseInner.md) | The grants this User has for each Firewall that is owned by this Account. | [optional] 
**var_global** | [**GetUserGrants200ResponseGlobal**](GetUserGrants200ResponseGlobal.md) |  | [optional] 
**image** | [**List[GetUserGrants200ResponseDatabaseInner]**](GetUserGrants200ResponseDatabaseInner.md) | The grants this User has for each Image that is owned by this Account. | [optional] 
**linode** | [**List[GetUserGrants200ResponseDatabaseInner]**](GetUserGrants200ResponseDatabaseInner.md) | The grants this User has for each Linode that is owned by this Account. | [optional] 
**longview** | [**List[GetUserGrants200ResponseDatabaseInner]**](GetUserGrants200ResponseDatabaseInner.md) | The grants this User has for each Longview Client that is owned by this Account. | [optional] 
**nodebalancer** | [**List[GetUserGrants200ResponseDatabaseInner]**](GetUserGrants200ResponseDatabaseInner.md) | The grants this User has for each NodeBalancer that is owned by this Account. | [optional] 
**placement_group** | [**List[GetUserGrants200ResponseDatabaseInner]**](GetUserGrants200ResponseDatabaseInner.md) | The grants this User has for each Placement Group that is owned by this Account. | [optional] 
**stackscript** | [**List[GetUserGrants200ResponseDatabaseInner]**](GetUserGrants200ResponseDatabaseInner.md) | The grants this User has for each StackScript that is owned by this Account. | [optional] 
**volume** | [**List[GetUserGrants200ResponseDatabaseInner]**](GetUserGrants200ResponseDatabaseInner.md) | The grants this User has for each Block Storage Volume that is owned by this Account. | [optional] 
**vpc** | [**List[GetUserGrants200ResponseDatabaseInner]**](GetUserGrants200ResponseDatabaseInner.md) | The grants this User has for each VPC that is owned by this Account. | [optional] 

## Example

```python
from openapi_client.models.grants_response import GrantsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GrantsResponse from a JSON string
grants_response_instance = GrantsResponse.from_json(json)
# print the JSON string representation of the object
print(GrantsResponse.to_json())

# convert the object into a dict
grants_response_dict = grants_response_instance.to_dict()
# create an instance of GrantsResponse from a dict
grants_response_from_dict = GrantsResponse.from_dict(grants_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

