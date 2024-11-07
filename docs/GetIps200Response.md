# GetIps200Response

The response data for the [List IP addresses](https://techdocs.akamai.com/linode-api/reference/get-ips) operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | The current [page](https://techdocs.akamai.com/linode-api/reference/pagination). | [optional] [readonly] 
**pages** | **int** | The total number of [pages](https://techdocs.akamai.com/linode-api/reference/pagination). | [optional] [readonly] 
**results** | **int** | The total number of results. | [optional] [readonly] 
**data** | [**List[GetIps200ResponseAllOfDataInner]**](GetIps200ResponseAllOfDataInner.md) | IP addresses that exist in Linode&#39;s system, either IPv4 or IPv6, specific to the response for the [List IP addresses](https://techdocs.akamai.com/linode-api/reference/get-ips) operation. | [optional] 

## Example

```python
from openapi_client.models.get_ips200_response import GetIps200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetIps200Response from a JSON string
get_ips200_response_instance = GetIps200Response.from_json(json)
# print the JSON string representation of the object
print(GetIps200Response.to_json())

# convert the object into a dict
get_ips200_response_dict = get_ips200_response_instance.to_dict()
# create an instance of GetIps200Response from a dict
get_ips200_response_from_dict = GetIps200Response.from_dict(get_ips200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


