# GetLinodeTransferByYearMonth200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytes_in** | **int** | The amount of inbound public network traffic received by this Linode, in bytes, for a specific year/month. | [optional] [readonly] 
**bytes_out** | **int** | The amount of outbound public network traffic sent by this Linode, in bytes, for a specific year/month. | [optional] [readonly] 
**bytes_total** | **int** | The total amount of public network traffic sent and received by this Linode, in bytes, for a specific year/month. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_linode_transfer_by_year_month200_response import GetLinodeTransferByYearMonth200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetLinodeTransferByYearMonth200Response from a JSON string
get_linode_transfer_by_year_month200_response_instance = GetLinodeTransferByYearMonth200Response.from_json(json)
# print the JSON string representation of the object
print(GetLinodeTransferByYearMonth200Response.to_json())

# convert the object into a dict
get_linode_transfer_by_year_month200_response_dict = get_linode_transfer_by_year_month200_response_instance.to_dict()
# create an instance of GetLinodeTransferByYearMonth200Response from a dict
get_linode_transfer_by_year_month200_response_from_dict = GetLinodeTransferByYearMonth200Response.from_dict(get_linode_transfer_by_year_month200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


