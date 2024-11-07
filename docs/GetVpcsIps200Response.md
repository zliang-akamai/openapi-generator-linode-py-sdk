# GetVpcsIps200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | The current [page](https://techdocs.akamai.com/linode-api/reference/pagination). | [optional] [readonly] 
**pages** | **int** | The total number of [pages](https://techdocs.akamai.com/linode-api/reference/pagination). | [optional] [readonly] 
**results** | **int** | The total number of results. | [optional] [readonly] 
**data** | [**List[GetLinodeIps200ResponseIpv4VpcInner]**](GetLinodeIps200ResponseIpv4VpcInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_vpcs_ips200_response import GetVpcsIps200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetVpcsIps200Response from a JSON string
get_vpcs_ips200_response_instance = GetVpcsIps200Response.from_json(json)
# print the JSON string representation of the object
print(GetVpcsIps200Response.to_json())

# convert the object into a dict
get_vpcs_ips200_response_dict = get_vpcs_ips200_response_instance.to_dict()
# create an instance of GetVpcsIps200Response from a dict
get_vpcs_ips200_response_from_dict = GetVpcsIps200Response.from_dict(get_vpcs_ips200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


