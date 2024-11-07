# GetLinodeIps200ResponseIpv6

Information about this Linode's IPv6 addresses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_global** | [**List[GetLinodeIps200ResponseIpv6GlobalInner]**](GetLinodeIps200ResponseIpv6GlobalInner.md) | A list of IPv6 range objects assigned to this Linode. | [optional] 
**link_local** | [**GetLinodeIps200ResponseIpv6LinkLocal**](GetLinodeIps200ResponseIpv6LinkLocal.md) |  | [optional] 
**slaac** | [**GetLinodeIps200ResponseIpv6Slaac**](GetLinodeIps200ResponseIpv6Slaac.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_linode_ips200_response_ipv6 import GetLinodeIps200ResponseIpv6

# TODO update the JSON string below
json = "{}"
# create an instance of GetLinodeIps200ResponseIpv6 from a JSON string
get_linode_ips200_response_ipv6_instance = GetLinodeIps200ResponseIpv6.from_json(json)
# print the JSON string representation of the object
print(GetLinodeIps200ResponseIpv6.to_json())

# convert the object into a dict
get_linode_ips200_response_ipv6_dict = get_linode_ips200_response_ipv6_instance.to_dict()
# create an instance of GetLinodeIps200ResponseIpv6 from a dict
get_linode_ips200_response_ipv6_from_dict = GetLinodeIps200ResponseIpv6.from_dict(get_linode_ips200_response_ipv6_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


