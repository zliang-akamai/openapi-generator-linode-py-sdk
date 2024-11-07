# GetLinodeTypes200ResponseDataInnerPrice

The default cost of provisioning this Linode Type. Prices are in US dollars, broken down into hourly and monthly charges.  Certain regions have different prices from the default. For region-specific prices, see `region_prices`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hourly** | **float** | Cost (in US dollars) per hour. | [optional] 
**monthly** | **float** | Cost per month, in US dollars. | [optional] 

## Example

```python
from openapi_client.models.get_linode_types200_response_data_inner_price import GetLinodeTypes200ResponseDataInnerPrice

# TODO update the JSON string below
json = "{}"
# create an instance of GetLinodeTypes200ResponseDataInnerPrice from a JSON string
get_linode_types200_response_data_inner_price_instance = GetLinodeTypes200ResponseDataInnerPrice.from_json(json)
# print the JSON string representation of the object
print(GetLinodeTypes200ResponseDataInnerPrice.to_json())

# convert the object into a dict
get_linode_types200_response_data_inner_price_dict = get_linode_types200_response_data_inner_price_instance.to_dict()
# create an instance of GetLinodeTypes200ResponseDataInnerPrice from a dict
get_linode_types200_response_data_inner_price_from_dict = GetLinodeTypes200ResponseDataInnerPrice.from_dict(get_linode_types200_response_data_inner_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


