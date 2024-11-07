# GetIps200ResponseAllOfDataInnerVpcNat11

IPv4 address configured as a 1:1 NAT for this Interface. Empty if no address is configured as a 1:1 NAT.  __Note__. Only allowed for `vpc` type Interfaces.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The IPv4 address that is configured as a 1:1 NAT for this VPC interface. | [optional] 
**subnet_id** | **int** | The &#x60;id&#x60; of the VPC Subnet for this Interface. | [optional] 
**vpc_id** | **int** | The &#x60;id&#x60; of the VPC configured for this Interface. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_ips200_response_all_of_data_inner_vpc_nat11 import GetIps200ResponseAllOfDataInnerVpcNat11

# TODO update the JSON string below
json = "{}"
# create an instance of GetIps200ResponseAllOfDataInnerVpcNat11 from a JSON string
get_ips200_response_all_of_data_inner_vpc_nat11_instance = GetIps200ResponseAllOfDataInnerVpcNat11.from_json(json)
# print the JSON string representation of the object
print(GetIps200ResponseAllOfDataInnerVpcNat11.to_json())

# convert the object into a dict
get_ips200_response_all_of_data_inner_vpc_nat11_dict = get_ips200_response_all_of_data_inner_vpc_nat11_instance.to_dict()
# create an instance of GetIps200ResponseAllOfDataInnerVpcNat11 from a dict
get_ips200_response_all_of_data_inner_vpc_nat11_from_dict = GetIps200ResponseAllOfDataInnerVpcNat11.from_dict(get_ips200_response_all_of_data_inner_vpc_nat11_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


