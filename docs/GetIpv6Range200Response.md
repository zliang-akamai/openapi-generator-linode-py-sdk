# GetIpv6Range200Response

An object representing an IPv6 range.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_bgp** | **bool** | Whether this IPv6 range is shared. | [optional] [readonly] 
**linodes** | **List[int]** | A list of Linodes targeted by this IPv6 range. Includes Linodes with IP sharing. | [optional] [readonly] 
**prefix** | **int** | The prefix length of the address. The total number of addresses that can be assigned from this range is calculated as 2&lt;sup&gt;(128 - prefix length)&lt;/sup&gt;. | [optional] 
**range** | **str** | The IPv6 address of this range. | [optional] [readonly] 
**region** | **str** | The region for this range of IPv6 addresses. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_ipv6_range200_response import GetIpv6Range200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetIpv6Range200Response from a JSON string
get_ipv6_range200_response_instance = GetIpv6Range200Response.from_json(json)
# print the JSON string representation of the object
print(GetIpv6Range200Response.to_json())

# convert the object into a dict
get_ipv6_range200_response_dict = get_ipv6_range200_response_instance.to_dict()
# create an instance of GetIpv6Range200Response from a dict
get_ipv6_range200_response_from_dict = GetIpv6Range200Response.from_dict(get_ipv6_range200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


