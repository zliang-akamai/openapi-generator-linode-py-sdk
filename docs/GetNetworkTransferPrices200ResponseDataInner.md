# GetNetworkTransferPrices200ResponseDataInner

Returns collection of network transfer prices, including any region-specific rates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID representing the network transfer price. | [optional] [readonly] 
**label** | **str** | The network transfer price label is for display purposes only. | [optional] [readonly] 
**price** | [**GetNetworkTransferPrices200ResponseDataInnerPrice**](GetNetworkTransferPrices200ResponseDataInnerPrice.md) |  | [optional] 
**region_prices** | [**List[GetNetworkTransferPrices200ResponseDataInnerRegionPricesInner]**](GetNetworkTransferPrices200ResponseDataInnerRegionPricesInner.md) |  | [optional] 
**transfer** | **int** | The monthly outbound transfer amount, in MB. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_network_transfer_prices200_response_data_inner import GetNetworkTransferPrices200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetNetworkTransferPrices200ResponseDataInner from a JSON string
get_network_transfer_prices200_response_data_inner_instance = GetNetworkTransferPrices200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetNetworkTransferPrices200ResponseDataInner.to_json())

# convert the object into a dict
get_network_transfer_prices200_response_data_inner_dict = get_network_transfer_prices200_response_data_inner_instance.to_dict()
# create an instance of GetNetworkTransferPrices200ResponseDataInner from a dict
get_network_transfer_prices200_response_data_inner_from_dict = GetNetworkTransferPrices200ResponseDataInner.from_dict(get_network_transfer_prices200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


