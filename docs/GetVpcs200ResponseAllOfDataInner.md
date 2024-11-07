# GetVpcs200ResponseAllOfDataInner

An object describing a VPC belonging to the Account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | The date-time of VPC creation. | [optional] [readonly] 
**description** | **str** | A written description to help distinguish the VPC. | [optional] [default to '']
**id** | **int** | The unique ID of the VPC. | [optional] [readonly] 
**label** | **str** | The VPC&#39;s label, for display purposes only.  - Needs to be unique among the Account&#39;s VPCs. - Can only contain ASCII letters, numbers, and hyphens (&#x60;-&#x60;). You can&#39;t use two consecutive hyphens (&#x60;--&#x60;). | [optional] 
**region** | **str** | The Region for the VPC. | [optional] 
**subnets** | [**List[GetVpcs200ResponseAllOfDataInnerSubnetsInner]**](GetVpcs200ResponseAllOfDataInnerSubnetsInner.md) | A list of subnets associated with the VPC. | [optional] 
**updated** | **datetime** | The date-time of the most recent VPC update. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_vpcs200_response_all_of_data_inner import GetVpcs200ResponseAllOfDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetVpcs200ResponseAllOfDataInner from a JSON string
get_vpcs200_response_all_of_data_inner_instance = GetVpcs200ResponseAllOfDataInner.from_json(json)
# print the JSON string representation of the object
print(GetVpcs200ResponseAllOfDataInner.to_json())

# convert the object into a dict
get_vpcs200_response_all_of_data_inner_dict = get_vpcs200_response_all_of_data_inner_instance.to_dict()
# create an instance of GetVpcs200ResponseAllOfDataInner from a dict
get_vpcs200_response_all_of_data_inner_from_dict = GetVpcs200ResponseAllOfDataInner.from_dict(get_vpcs200_response_all_of_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


