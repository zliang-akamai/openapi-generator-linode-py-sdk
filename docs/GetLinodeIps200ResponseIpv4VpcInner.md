# GetLinodeIps200ResponseIpv4VpcInner

A VPC IP address that exists in Linode's system, specific to the response for the [List VPC IP addresses](https://techdocs.akamai.com/linode-api/reference/get-vpcs-ips) operation. Returned as an empty set for Linodes that are not part of a VPC.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Returns &#x60;true&#x60; if the VPC interface is in use, meaning that the Linode was powered on using the &#x60;config_id&#x60; to which the interface belongs. Otherwise returns &#x60;false&#x60;. | [optional] [readonly] 
**address** | **str** | An IPv4 address configured for this VPC interface. These follow the [RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918) private address format. Displayed as &#x60;null&#x60; if an &#x60;address_range&#x60;. | [optional] [readonly] 
**address_range** | **str** | A range of IPv4 addresses configured for this VPC interface. Displayed as &#x60;null&#x60; if a single &#x60;address&#x60;. | [optional] [readonly] 
**config_id** | **int** | The globally general entity identifier for the Linode configuration profile where the VPC is included. | [optional] [readonly] 
**gateway** | **str** | The default gateway for the VPC subnet that the IP or IP range belongs to. | [optional] [readonly] 
**interface_id** | **int** | The globally general API entity identifier for the Linode interface. | [optional] [readonly] 
**linode_id** | **int** | The identifier for the Linode the VPC interface currently belongs to. | [optional] [readonly] 
**nat_1_1** | **str** | The public IP address used for NAT 1:1 with the VPC. This is empty if NAT 1:1 isn&#39;t used. | [optional] [readonly] 
**prefix** | **int** | The number of bits set in the &#x60;subnet_mask&#x60;. | [optional] [readonly] 
**region** | **str** | The region of the VPC. | [optional] [readonly] 
**subnet_id** | **int** | The &#x60;id&#x60; of the VPC Subnet for this interface. | [optional] 
**subnet_mask** | **str** | The mask that separates host bits from network bits for the &#x60;address&#x60; or &#x60;address_range&#x60;. | [optional] [readonly] 
**vpc_id** | **int** | The unique globally general API entity identifier for the VPC. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_linode_ips200_response_ipv4_vpc_inner import GetLinodeIps200ResponseIpv4VpcInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLinodeIps200ResponseIpv4VpcInner from a JSON string
get_linode_ips200_response_ipv4_vpc_inner_instance = GetLinodeIps200ResponseIpv4VpcInner.from_json(json)
# print the JSON string representation of the object
print(GetLinodeIps200ResponseIpv4VpcInner.to_json())

# convert the object into a dict
get_linode_ips200_response_ipv4_vpc_inner_dict = get_linode_ips200_response_ipv4_vpc_inner_instance.to_dict()
# create an instance of GetLinodeIps200ResponseIpv4VpcInner from a dict
get_linode_ips200_response_ipv4_vpc_inner_from_dict = GetLinodeIps200ResponseIpv4VpcInner.from_dict(get_linode_ips200_response_ipv4_vpc_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


