# GetLkeTypes200ResponseDataInnerPrice

The default cost of this Kubernetes type. Prices are in US dollars, broken down into hourly and monthly charges.  Certain regions have different prices from the default. For region-specific prices, see `region_prices`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hourly** | **float** | Cost (in US dollars) per hour. | [optional] 
**monthly** | **float** | Cost per month, in US dollars. | [optional] 

## Example

```python
from openapi_client.models.get_lke_types200_response_data_inner_price import GetLkeTypes200ResponseDataInnerPrice

# TODO update the JSON string below
json = "{}"
# create an instance of GetLkeTypes200ResponseDataInnerPrice from a JSON string
get_lke_types200_response_data_inner_price_instance = GetLkeTypes200ResponseDataInnerPrice.from_json(json)
# print the JSON string representation of the object
print(GetLkeTypes200ResponseDataInnerPrice.to_json())

# convert the object into a dict
get_lke_types200_response_data_inner_price_dict = get_lke_types200_response_data_inner_price_instance.to_dict()
# create an instance of GetLkeTypes200ResponseDataInnerPrice from a dict
get_lke_types200_response_data_inner_price_from_dict = GetLkeTypes200ResponseDataInnerPrice.from_dict(get_lke_types200_response_data_inner_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


