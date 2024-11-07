# GetIpv6Pools200ResponseDataInner

An object representing an IPv6 pool.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefix** | **int** | The prefix length of the address. The total number of addresses that can be assigned from this range is calculated as 2&lt;sup&gt;(128 - prefix length)&lt;/sup&gt;. | [optional] 
**range** | **str** | The IPv6 range of addresses in this pool. | [optional] [readonly] 
**region** | **str** | The region for this pool of IPv6 addresses. | [optional] [readonly] 
**route_target** | **str** | The last address in this block of IPv6 addresses. | [optional] 

## Example

```python
from openapi_client.models.get_ipv6_pools200_response_data_inner import GetIpv6Pools200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetIpv6Pools200ResponseDataInner from a JSON string
get_ipv6_pools200_response_data_inner_instance = GetIpv6Pools200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetIpv6Pools200ResponseDataInner.to_json())

# convert the object into a dict
get_ipv6_pools200_response_data_inner_dict = get_ipv6_pools200_response_data_inner_instance.to_dict()
# create an instance of GetIpv6Pools200ResponseDataInner from a dict
get_ipv6_pools200_response_data_inner_from_dict = GetIpv6Pools200ResponseDataInner.from_dict(get_ipv6_pools200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


