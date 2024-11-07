# GetLinodeStats200ResponseNetv6

IPv6 statistics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_in** | **List[List[float]]** | Input stats for IPv6, measured in bits/s (bits/second). | [optional] 
**out** | **List[List[float]]** | Output stats for IPv6, measured in bits/s (bits/second). | [optional] 
**private_in** | **List[List[float]]** | Private IPv6 input statistics, measured in bits/s (bits/second). | [optional] 
**private_out** | **List[List[float]]** | Private IPv6 output statistics, measured in bits/s (bits/second). | [optional] 

## Example

```python
from openapi_client.models.get_linode_stats200_response_netv6 import GetLinodeStats200ResponseNetv6

# TODO update the JSON string below
json = "{}"
# create an instance of GetLinodeStats200ResponseNetv6 from a JSON string
get_linode_stats200_response_netv6_instance = GetLinodeStats200ResponseNetv6.from_json(json)
# print the JSON string representation of the object
print(GetLinodeStats200ResponseNetv6.to_json())

# convert the object into a dict
get_linode_stats200_response_netv6_dict = get_linode_stats200_response_netv6_instance.to_dict()
# create an instance of GetLinodeStats200ResponseNetv6 from a dict
get_linode_stats200_response_netv6_from_dict = GetLinodeStats200ResponseNetv6.from_dict(get_linode_stats200_response_netv6_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


