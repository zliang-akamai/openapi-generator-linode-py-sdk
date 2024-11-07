# GetLinodeIps200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv4** | [**GetLinodeIps200ResponseIpv4**](GetLinodeIps200ResponseIpv4.md) |  | [optional] 
**ipv6** | [**GetLinodeIps200ResponseIpv6**](GetLinodeIps200ResponseIpv6.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_linode_ips200_response import GetLinodeIps200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetLinodeIps200Response from a JSON string
get_linode_ips200_response_instance = GetLinodeIps200Response.from_json(json)
# print the JSON string representation of the object
print(GetLinodeIps200Response.to_json())

# convert the object into a dict
get_linode_ips200_response_dict = get_linode_ips200_response_instance.to_dict()
# create an instance of GetLinodeIps200Response from a dict
get_linode_ips200_response_from_dict = GetLinodeIps200Response.from_dict(get_linode_ips200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


