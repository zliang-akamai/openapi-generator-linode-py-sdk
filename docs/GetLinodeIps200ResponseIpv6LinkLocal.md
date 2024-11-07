# GetLinodeIps200ResponseIpv6LinkLocal

A link-local IPv6 address that exists in Linode's system.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The IPv6 link-local address. | [optional] [readonly] 
**gateway** | **str** | The default gateway for this address. | [optional] [readonly] 
**linode_id** | **int** | The ID of the Linode this address currently belongs to. | [optional] [readonly] 
**prefix** | **int** | The network prefix. | [optional] [readonly] 
**public** | **bool** | Whether this is a public or private IP address. | [optional] [readonly] 
**rdns** | **str** | The reverse DNS assigned to this address. | [optional] 
**region** | **str** | The Region this address resides in. | [optional] [readonly] 
**subnet_mask** | **str** | The subnet mask. | [optional] [readonly] 
**type** | **str** | The type of address this is. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_linode_ips200_response_ipv6_link_local import GetLinodeIps200ResponseIpv6LinkLocal

# TODO update the JSON string below
json = "{}"
# create an instance of GetLinodeIps200ResponseIpv6LinkLocal from a JSON string
get_linode_ips200_response_ipv6_link_local_instance = GetLinodeIps200ResponseIpv6LinkLocal.from_json(json)
# print the JSON string representation of the object
print(GetLinodeIps200ResponseIpv6LinkLocal.to_json())

# convert the object into a dict
get_linode_ips200_response_ipv6_link_local_dict = get_linode_ips200_response_ipv6_link_local_instance.to_dict()
# create an instance of GetLinodeIps200ResponseIpv6LinkLocal from a dict
get_linode_ips200_response_ipv6_link_local_from_dict = GetLinodeIps200ResponseIpv6LinkLocal.from_dict(get_linode_ips200_response_ipv6_link_local_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

