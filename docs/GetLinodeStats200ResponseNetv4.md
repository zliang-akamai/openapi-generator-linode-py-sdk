# GetLinodeStats200ResponseNetv4

IPv4 statistics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_in** | **List[List[float]]** | Input stats for IPv4, measured in bits/s (bits/second). | [optional] 
**out** | **List[List[float]]** | Output stats for IPv4, measured in bits/s (bits/second). | [optional] 
**private_in** | **List[List[float]]** | Private IPv4 input statistics, measured in bits/s (bits/second). | [optional] 
**private_out** | **List[List[float]]** | Private IPv4 output statistics, measured in bits/s (bits/second). | [optional] 

## Example

```python
from openapi_client.models.get_linode_stats200_response_netv4 import GetLinodeStats200ResponseNetv4

# TODO update the JSON string below
json = "{}"
# create an instance of GetLinodeStats200ResponseNetv4 from a JSON string
get_linode_stats200_response_netv4_instance = GetLinodeStats200ResponseNetv4.from_json(json)
# print the JSON string representation of the object
print(GetLinodeStats200ResponseNetv4.to_json())

# convert the object into a dict
get_linode_stats200_response_netv4_dict = get_linode_stats200_response_netv4_instance.to_dict()
# create an instance of GetLinodeStats200ResponseNetv4 from a dict
get_linode_stats200_response_netv4_from_dict = GetLinodeStats200ResponseNetv4.from_dict(get_linode_stats200_response_netv4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


