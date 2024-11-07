# GetLkeTypes200ResponseDataInnerRegionPricesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hourly** | **float** | Cost per hour for this region, in US dollars. | [optional] 
**id** | **str** | The Region ID for these prices. | [optional] 
**monthly** | **float** | Cost per month for this region, in US dollars. | [optional] 

## Example

```python
from openapi_client.models.get_lke_types200_response_data_inner_region_prices_inner import GetLkeTypes200ResponseDataInnerRegionPricesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLkeTypes200ResponseDataInnerRegionPricesInner from a JSON string
get_lke_types200_response_data_inner_region_prices_inner_instance = GetLkeTypes200ResponseDataInnerRegionPricesInner.from_json(json)
# print the JSON string representation of the object
print(GetLkeTypes200ResponseDataInnerRegionPricesInner.to_json())

# convert the object into a dict
get_lke_types200_response_data_inner_region_prices_inner_dict = get_lke_types200_response_data_inner_region_prices_inner_instance.to_dict()
# create an instance of GetLkeTypes200ResponseDataInnerRegionPricesInner from a dict
get_lke_types200_response_data_inner_region_prices_inner_from_dict = GetLkeTypes200ResponseDataInnerRegionPricesInner.from_dict(get_lke_types200_response_data_inner_region_prices_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


