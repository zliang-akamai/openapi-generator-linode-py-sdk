# GetUserGrants200ResponseGlobal

A structure containing the Account-level grants a User has.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_access** | **str** | The level of access this User has to Account-level actions, like billing information. A restricted User will never be able to manage users.  __Parent and child accounts__  In a [parent and child account](https://www.linode.com/docs/guides/parent-child-accounts/) environment, this grant can be added to a child account user, to give the user &#x60;read-write&#x60; access. This gives the child user unrestricted access to expected management operations, such as creating other child users. However, child users don&#39;t have write access to billing operations. The API issues a specific error message if a write operation is attempted by a child user. | [optional] 
**add_databases** | **bool** | If true, this User may add Managed Databases. | [optional] 
**add_domains** | **bool** | If true, this User may add Domains. | [optional] 
**add_firewalls** | **bool** | If true, this User may add Firewalls. | [optional] 
**add_images** | **bool** | If true, this User may add Images. | [optional] 
**add_linodes** | **bool** | If true, this User may create Linodes. | [optional] 
**add_loadbalancers** | **bool** | If true, this User may add Cloud Load Balancers. | [optional] 
**add_longview** | **bool** | If true, this User may create Longview clients and view the current plan. | [optional] 
**add_nodebalancers** | **bool** | If true, this User may add NodeBalancers. | [optional] 
**add_placement_groups** | **bool** | If true, this User may add Placement Groups. | [optional] 
**add_stackscripts** | **bool** | If true, this User may add StackScripts. | [optional] 
**add_volumes** | **bool** | If true, this User may add Volumes. | [optional] 
**add_vpcs** | **bool** | If true, this User may add VPCs. | [optional] 
**cancel_account** | **bool** | If true, this User may cancel the entire Account. | [optional] 
**child_account_access** | **bool** | In a [parent and child account](https://www.linode.com/docs/guides/parent-child-accounts/) environment, this gives a parent account access to endpoints that can be used to manage child accounts. Unrestricted parent account users have access to this grant, while restricted parent users don&#39;t. An unrestricted parent user can set this to &#x60;true&#x60; to add this grant to a restricted parent user. Displayed as &#x60;null&#x60; for all non-parent accounts. | [optional] 
**longview_subscription** | **bool** | If true, this User may manage the Account&#39;s Longview subscription. | [optional] 

## Example

```python
from openapi_client.models.get_user_grants200_response_global import GetUserGrants200ResponseGlobal

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserGrants200ResponseGlobal from a JSON string
get_user_grants200_response_global_instance = GetUserGrants200ResponseGlobal.from_json(json)
# print the JSON string representation of the object
print(GetUserGrants200ResponseGlobal.to_json())

# convert the object into a dict
get_user_grants200_response_global_dict = get_user_grants200_response_global_instance.to_dict()
# create an instance of GetUserGrants200ResponseGlobal from a dict
get_user_grants200_response_global_from_dict = GetUserGrants200ResponseGlobal.from_dict(get_user_grants200_response_global_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


