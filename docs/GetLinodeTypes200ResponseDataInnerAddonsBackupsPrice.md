# GetLinodeTypes200ResponseDataInnerAddonsBackupsPrice

The default cost of enabling Backups for this Linode Type. Prices are in US dollars, broken down into hourly and monthly charges.  Certain regions have different prices from the default. For region-specific prices, see `region_prices`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hourly** | **float** | The cost (in US dollars) per hour to add Backups service. | [optional] 
**monthly** | **float** | The cost (in US dollars) per month to add Backups service. | [optional] 

## Example

```python
from openapi_client.models.get_linode_types200_response_data_inner_addons_backups_price import GetLinodeTypes200ResponseDataInnerAddonsBackupsPrice

# TODO update the JSON string below
json = "{}"
# create an instance of GetLinodeTypes200ResponseDataInnerAddonsBackupsPrice from a JSON string
get_linode_types200_response_data_inner_addons_backups_price_instance = GetLinodeTypes200ResponseDataInnerAddonsBackupsPrice.from_json(json)
# print the JSON string representation of the object
print(GetLinodeTypes200ResponseDataInnerAddonsBackupsPrice.to_json())

# convert the object into a dict
get_linode_types200_response_data_inner_addons_backups_price_dict = get_linode_types200_response_data_inner_addons_backups_price_instance.to_dict()
# create an instance of GetLinodeTypes200ResponseDataInnerAddonsBackupsPrice from a dict
get_linode_types200_response_data_inner_addons_backups_price_from_dict = GetLinodeTypes200ResponseDataInnerAddonsBackupsPrice.from_dict(get_linode_types200_response_data_inner_addons_backups_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


