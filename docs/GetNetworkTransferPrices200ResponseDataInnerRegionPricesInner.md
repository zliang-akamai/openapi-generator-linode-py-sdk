# GetNetworkTransferPrices200ResponseDataInnerRegionPricesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hourly** | **float** | Cost per hour for this region, in US dollars. | [optional] 
**id** | **str** | The Region ID for these prices. | [optional] 
**monthly** | **float** | Cost per month for this region, in US dollars. | [optional] 

## Example

```python
from openapi_client.models.get_network_transfer_prices200_response_data_inner_region_prices_inner import GetNetworkTransferPrices200ResponseDataInnerRegionPricesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetNetworkTransferPrices200ResponseDataInnerRegionPricesInner from a JSON string
get_network_transfer_prices200_response_data_inner_region_prices_inner_instance = GetNetworkTransferPrices200ResponseDataInnerRegionPricesInner.from_json(json)
# print the JSON string representation of the object
print(GetNetworkTransferPrices200ResponseDataInnerRegionPricesInner.to_json())

# convert the object into a dict
get_network_transfer_prices200_response_data_inner_region_prices_inner_dict = get_network_transfer_prices200_response_data_inner_region_prices_inner_instance.to_dict()
# create an instance of GetNetworkTransferPrices200ResponseDataInnerRegionPricesInner from a dict
get_network_transfer_prices200_response_data_inner_region_prices_inner_from_dict = GetNetworkTransferPrices200ResponseDataInnerRegionPricesInner.from_dict(get_network_transfer_prices200_response_data_inner_region_prices_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


