# GetLinodeIps200ResponseIpv4

Information about this Linode's IPv4 addresses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**private** | [**List[GetLinodeIps200ResponseIpv4PrivateInner]**](GetLinodeIps200ResponseIpv4PrivateInner.md) | A list of private IP Address objects belonging to this Linode. | [optional] [readonly] 
**public** | [**List[GetLinodeIps200ResponseIpv4PublicInner]**](GetLinodeIps200ResponseIpv4PublicInner.md) | A list of public IP Address objects belonging to this Linode. | [optional] [readonly] 
**reserved** | [**List[GetLinodeIps200ResponseIpv4PublicInner]**](GetLinodeIps200ResponseIpv4PublicInner.md) | A list of reserved IP Address objects belonging to this Linode. | [optional] [readonly] 
**shared** | [**List[GetLinodeIps200ResponseIpv4PublicInner]**](GetLinodeIps200ResponseIpv4PublicInner.md) | A list of shared IP Address objects assigned to this Linode. | [optional] [readonly] 
**vpc** | [**List[GetLinodeIps200ResponseIpv4VpcInner]**](GetLinodeIps200ResponseIpv4VpcInner.md) | A list of Virtual Private Cloud (VPC)-specific addresses or ranges for the Linode. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_linode_ips200_response_ipv4 import GetLinodeIps200ResponseIpv4

# TODO update the JSON string below
json = "{}"
# create an instance of GetLinodeIps200ResponseIpv4 from a JSON string
get_linode_ips200_response_ipv4_instance = GetLinodeIps200ResponseIpv4.from_json(json)
# print the JSON string representation of the object
print(GetLinodeIps200ResponseIpv4.to_json())

# convert the object into a dict
get_linode_ips200_response_ipv4_dict = get_linode_ips200_response_ipv4_instance.to_dict()
# create an instance of GetLinodeIps200ResponseIpv4 from a dict
get_linode_ips200_response_ipv4_from_dict = GetLinodeIps200ResponseIpv4.from_dict(get_linode_ips200_response_ipv4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


