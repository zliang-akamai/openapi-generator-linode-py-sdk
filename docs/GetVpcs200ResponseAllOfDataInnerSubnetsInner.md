# GetVpcs200ResponseAllOfDataInnerSubnetsInner

An object describing a VPC Subnet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | The date-time of VPC Subnet creation. | [optional] [readonly] 
**id** | **int** | The unique ID of the VPC Subnet. | [optional] [readonly] 
**ipv4** | **str** | IPv4 range in CIDR canonical form.  - The range must belong to a private address space as defined in [RFC1918](https://datatracker.ietf.org/doc/html/rfc1918). - Allowed prefix lengths: 1-29. - The range must not overlap with 192.168.128.0/17. - The range must not overlap with other Subnets on the same VPC. | [optional] 
**label** | **str** | The VPC Subnet&#39;s label, for display purposes only.  - Must be unique among the VPC&#39;s Subnets. - Can only contain ASCII letters, numbers, and hyphens (&#x60;-&#x60;). You can&#39;t use two consecutive hyphens (&#x60;--&#x60;). | [optional] 
**linodes** | [**List[GetVpcs200ResponseAllOfDataInnerSubnetsInnerLinodesInner]**](GetVpcs200ResponseAllOfDataInnerSubnetsInnerLinodesInner.md) | An array of Linode IDs assigned to the VPC Subnet.  A Linode is assigned to a VPC Subnet if it has a Configuration Profile with a &#x60;vpc&#x60; purpose interface with the subnet&#39;s &#x60;subnet_id&#x60;. Even if the Configuration Profile is not active, meaning the Linode does not have access to the Subnet, the Linode still appears in this array. | [optional] [readonly] 
**updated** | **datetime** | The date-time of the most recent VPC Subnet update. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_vpcs200_response_all_of_data_inner_subnets_inner import GetVpcs200ResponseAllOfDataInnerSubnetsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetVpcs200ResponseAllOfDataInnerSubnetsInner from a JSON string
get_vpcs200_response_all_of_data_inner_subnets_inner_instance = GetVpcs200ResponseAllOfDataInnerSubnetsInner.from_json(json)
# print the JSON string representation of the object
print(GetVpcs200ResponseAllOfDataInnerSubnetsInner.to_json())

# convert the object into a dict
get_vpcs200_response_all_of_data_inner_subnets_inner_dict = get_vpcs200_response_all_of_data_inner_subnets_inner_instance.to_dict()
# create an instance of GetVpcs200ResponseAllOfDataInnerSubnetsInner from a dict
get_vpcs200_response_all_of_data_inner_subnets_inner_from_dict = GetVpcs200ResponseAllOfDataInnerSubnetsInner.from_dict(get_vpcs200_response_all_of_data_inner_subnets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


