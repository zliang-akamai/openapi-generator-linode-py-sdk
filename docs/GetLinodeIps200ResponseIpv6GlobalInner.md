# GetLinodeIps200ResponseIpv6GlobalInner

An object representing an IPv6 range.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefix** | **int** | The prefix length of the address. The total number of addresses that can be assigned from this range is calculated as 2&lt;sup&gt;(128 - prefix length)&lt;/sup&gt;. | [optional] 
**range** | **str** | The IPv6 address of this range. | [optional] [readonly] 
**region** | **str** | The region for this range of IPv6 addresses. | [optional] [readonly] 
**route_target** | **str** | The IPv6 SLAAC address. | [optional] 

## Example

```python
from openapi_client.models.get_linode_ips200_response_ipv6_global_inner import GetLinodeIps200ResponseIpv6GlobalInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLinodeIps200ResponseIpv6GlobalInner from a JSON string
get_linode_ips200_response_ipv6_global_inner_instance = GetLinodeIps200ResponseIpv6GlobalInner.from_json(json)
# print the JSON string representation of the object
print(GetLinodeIps200ResponseIpv6GlobalInner.to_json())

# convert the object into a dict
get_linode_ips200_response_ipv6_global_inner_dict = get_linode_ips200_response_ipv6_global_inner_instance.to_dict()
# create an instance of GetLinodeIps200ResponseIpv6GlobalInner from a dict
get_linode_ips200_response_ipv6_global_inner_from_dict = GetLinodeIps200ResponseIpv6GlobalInner.from_dict(get_linode_ips200_response_ipv6_global_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


