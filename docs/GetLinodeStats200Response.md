# GetLinodeStats200Response

CPU, IO, IPv4, and IPv6 statistics. Graph data, if available, is in `[timestamp, reading]` array format. Timestamp is a UNIX timestamp in EST.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | **List[List[float]]** | Percentage of CPU used. | [optional] 
**io** | [**GetLinodeStats200ResponseIo**](GetLinodeStats200ResponseIo.md) |  | [optional] 
**netv4** | [**GetLinodeStats200ResponseNetv4**](GetLinodeStats200ResponseNetv4.md) |  | [optional] 
**netv6** | [**GetLinodeStats200ResponseNetv6**](GetLinodeStats200ResponseNetv6.md) |  | [optional] 
**title** | **str** | The title for this data set. | [optional] 

## Example

```python
from openapi_client.models.get_linode_stats200_response import GetLinodeStats200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetLinodeStats200Response from a JSON string
get_linode_stats200_response_instance = GetLinodeStats200Response.from_json(json)
# print the JSON string representation of the object
print(GetLinodeStats200Response.to_json())

# convert the object into a dict
get_linode_stats200_response_dict = get_linode_stats200_response_instance.to_dict()
# create an instance of GetLinodeStats200Response from a dict
get_linode_stats200_response_from_dict = GetLinodeStats200Response.from_dict(get_linode_stats200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


