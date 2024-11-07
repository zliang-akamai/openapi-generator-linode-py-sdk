# GetVpcs200ResponseAllOfDataInnerSubnetsInnerLinodesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of a Linode assigned to the VPC Subnet. | [optional] 
**interfaces** | [**List[GetVpcs200ResponseAllOfDataInnerSubnetsInnerLinodesInnerInterfacesInner]**](GetVpcs200ResponseAllOfDataInnerSubnetsInnerLinodesInnerInterfacesInner.md) | VPC purpose interfaces with the subnet&#39;s &#x60;subnet_id&#x60; assigned to the Linode. | [optional] 

## Example

```python
from openapi_client.models.get_vpcs200_response_all_of_data_inner_subnets_inner_linodes_inner import GetVpcs200ResponseAllOfDataInnerSubnetsInnerLinodesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetVpcs200ResponseAllOfDataInnerSubnetsInnerLinodesInner from a JSON string
get_vpcs200_response_all_of_data_inner_subnets_inner_linodes_inner_instance = GetVpcs200ResponseAllOfDataInnerSubnetsInnerLinodesInner.from_json(json)
# print the JSON string representation of the object
print(GetVpcs200ResponseAllOfDataInnerSubnetsInnerLinodesInner.to_json())

# convert the object into a dict
get_vpcs200_response_all_of_data_inner_subnets_inner_linodes_inner_dict = get_vpcs200_response_all_of_data_inner_subnets_inner_linodes_inner_instance.to_dict()
# create an instance of GetVpcs200ResponseAllOfDataInnerSubnetsInnerLinodesInner from a dict
get_vpcs200_response_all_of_data_inner_subnets_inner_linodes_inner_from_dict = GetVpcs200ResponseAllOfDataInnerSubnetsInnerLinodesInner.from_dict(get_vpcs200_response_all_of_data_inner_subnets_inner_linodes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


