# GetLinodeIps200ResponseIpv4PublicInner

An IP address that exists in Linode's system, either IPv4 or IPv6.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The IP address. | [optional] [readonly] 
**gateway** | **str** | The default gateway for this address. | [optional] [readonly] 
**linode_id** | **int** | The ID of the Linode this address currently belongs to. For IPv4 addresses, this is by default the Linode that this address was assigned to on creation, and these addresses my be moved using the [Assign IPv4s to Linodes](https://techdocs.akamai.com/linode-api/reference/post-assign-ipv4s) operation. For SLAAC and link-local addresses, this value may not be changed. | [optional] [readonly] 
**prefix** | **int** | The number of bits set in the subnet mask. | [optional] [readonly] 
**public** | **bool** | Whether this is a public or private IP address. | [optional] [readonly] 
**rdns** | **str** | The reverse DNS assigned to this address. For public IPv4 addresses, this will be set to a default value provided by Linode if not explicitly set. | [optional] 
**region** | **str** | The Region this IP address resides in. | [optional] [readonly] 
**subnet_mask** | **str** | The mask that separates host bits from network bits for this address. | [optional] [readonly] 
**type** | **str** | The type of address this is. | [optional] [readonly] 
**vpc_nat_1_1** | [**GetLinodeIps200ResponseIpv4PublicInnerVpcNat11**](GetLinodeIps200ResponseIpv4PublicInnerVpcNat11.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_linode_ips200_response_ipv4_public_inner import GetLinodeIps200ResponseIpv4PublicInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLinodeIps200ResponseIpv4PublicInner from a JSON string
get_linode_ips200_response_ipv4_public_inner_instance = GetLinodeIps200ResponseIpv4PublicInner.from_json(json)
# print the JSON string representation of the object
print(GetLinodeIps200ResponseIpv4PublicInner.to_json())

# convert the object into a dict
get_linode_ips200_response_ipv4_public_inner_dict = get_linode_ips200_response_ipv4_public_inner_instance.to_dict()
# create an instance of GetLinodeIps200ResponseIpv4PublicInner from a dict
get_linode_ips200_response_ipv4_public_inner_from_dict = GetLinodeIps200ResponseIpv4PublicInner.from_dict(get_linode_ips200_response_ipv4_public_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


