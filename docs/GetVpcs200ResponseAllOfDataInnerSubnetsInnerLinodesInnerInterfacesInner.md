# GetVpcs200ResponseAllOfDataInnerSubnetsInnerLinodesInnerInterfacesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Returns &#x60;true&#x60; if the Interface is in use, meaning that the Linode was powered on using the Configuration Profile to which the Interface belongs. Otherwise returns &#x60;false&#x60;. | [optional] 
**id** | **int** | ID of the interface. | [optional] 

## Example

```python
from openapi_client.models.get_vpcs200_response_all_of_data_inner_subnets_inner_linodes_inner_interfaces_inner import GetVpcs200ResponseAllOfDataInnerSubnetsInnerLinodesInnerInterfacesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetVpcs200ResponseAllOfDataInnerSubnetsInnerLinodesInnerInterfacesInner from a JSON string
get_vpcs200_response_all_of_data_inner_subnets_inner_linodes_inner_interfaces_inner_instance = GetVpcs200ResponseAllOfDataInnerSubnetsInnerLinodesInnerInterfacesInner.from_json(json)
# print the JSON string representation of the object
print(GetVpcs200ResponseAllOfDataInnerSubnetsInnerLinodesInnerInterfacesInner.to_json())

# convert the object into a dict
get_vpcs200_response_all_of_data_inner_subnets_inner_linodes_inner_interfaces_inner_dict = get_vpcs200_response_all_of_data_inner_subnets_inner_linodes_inner_interfaces_inner_instance.to_dict()
# create an instance of GetVpcs200ResponseAllOfDataInnerSubnetsInnerLinodesInnerInterfacesInner from a dict
get_vpcs200_response_all_of_data_inner_subnets_inner_linodes_inner_interfaces_inner_from_dict = GetVpcs200ResponseAllOfDataInnerSubnetsInnerLinodesInnerInterfacesInner.from_dict(get_vpcs200_response_all_of_data_inner_subnets_inner_linodes_inner_interfaces_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


