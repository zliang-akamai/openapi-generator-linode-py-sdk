# GetLinodeIps200ResponseIpv4PublicInnerVpcNat11

IPv4 address configured as a 1:1 NAT for this Interface. If no address is configured as a 1:1 NAT, `null` is returned.  __Note__. Only allowed for `vpc` type Interfaces.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The IPv4 address that is configured as a 1:1 NAT for this VPC interface. | [optional] 
**subnet_id** | **int** | The &#x60;id&#x60; of the VPC Subnet for this Interface. | [optional] 
**vpc_id** | **int** | The &#x60;id&#x60; of the VPC configured for this Interface. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_linode_ips200_response_ipv4_public_inner_vpc_nat11 import GetLinodeIps200ResponseIpv4PublicInnerVpcNat11

# TODO update the JSON string below
json = "{}"
# create an instance of GetLinodeIps200ResponseIpv4PublicInnerVpcNat11 from a JSON string
get_linode_ips200_response_ipv4_public_inner_vpc_nat11_instance = GetLinodeIps200ResponseIpv4PublicInnerVpcNat11.from_json(json)
# print the JSON string representation of the object
print(GetLinodeIps200ResponseIpv4PublicInnerVpcNat11.to_json())

# convert the object into a dict
get_linode_ips200_response_ipv4_public_inner_vpc_nat11_dict = get_linode_ips200_response_ipv4_public_inner_vpc_nat11_instance.to_dict()
# create an instance of GetLinodeIps200ResponseIpv4PublicInnerVpcNat11 from a dict
get_linode_ips200_response_ipv4_public_inner_vpc_nat11_from_dict = GetLinodeIps200ResponseIpv4PublicInnerVpcNat11.from_dict(get_linode_ips200_response_ipv4_public_inner_vpc_nat11_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


