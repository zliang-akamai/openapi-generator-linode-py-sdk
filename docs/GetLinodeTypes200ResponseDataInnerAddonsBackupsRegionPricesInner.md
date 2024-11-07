# GetLinodeTypes200ResponseDataInnerAddonsBackupsRegionPricesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hourly** | **float** | Cost (in US dollars) per hour to add Backups service in this Region. | [optional] 
**id** | **str** | The Region ID for these prices. | [optional] 
**monthly** | **float** | Cost (in US dollars) per month to add Backups service in this Region. | [optional] 

## Example

```python
from openapi_client.models.get_linode_types200_response_data_inner_addons_backups_region_prices_inner import GetLinodeTypes200ResponseDataInnerAddonsBackupsRegionPricesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLinodeTypes200ResponseDataInnerAddonsBackupsRegionPricesInner from a JSON string
get_linode_types200_response_data_inner_addons_backups_region_prices_inner_instance = GetLinodeTypes200ResponseDataInnerAddonsBackupsRegionPricesInner.from_json(json)
# print the JSON string representation of the object
print(GetLinodeTypes200ResponseDataInnerAddonsBackupsRegionPricesInner.to_json())

# convert the object into a dict
get_linode_types200_response_data_inner_addons_backups_region_prices_inner_dict = get_linode_types200_response_data_inner_addons_backups_region_prices_inner_instance.to_dict()
# create an instance of GetLinodeTypes200ResponseDataInnerAddonsBackupsRegionPricesInner from a dict
get_linode_types200_response_data_inner_addons_backups_region_prices_inner_from_dict = GetLinodeTypes200ResponseDataInnerAddonsBackupsRegionPricesInner.from_dict(get_linode_types200_response_data_inner_addons_backups_region_prices_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


