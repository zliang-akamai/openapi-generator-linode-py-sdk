# GetLinodeTypes200ResponseDataInnerAddonsBackups

Information about the optional Backup service offered for Linodes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | [**GetLinodeTypes200ResponseDataInnerAddonsBackupsPrice**](GetLinodeTypes200ResponseDataInnerAddonsBackupsPrice.md) |  | [optional] 
**region_prices** | [**List[GetLinodeTypes200ResponseDataInnerAddonsBackupsRegionPricesInner]**](GetLinodeTypes200ResponseDataInnerAddonsBackupsRegionPricesInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_linode_types200_response_data_inner_addons_backups import GetLinodeTypes200ResponseDataInnerAddonsBackups

# TODO update the JSON string below
json = "{}"
# create an instance of GetLinodeTypes200ResponseDataInnerAddonsBackups from a JSON string
get_linode_types200_response_data_inner_addons_backups_instance = GetLinodeTypes200ResponseDataInnerAddonsBackups.from_json(json)
# print the JSON string representation of the object
print(GetLinodeTypes200ResponseDataInnerAddonsBackups.to_json())

# convert the object into a dict
get_linode_types200_response_data_inner_addons_backups_dict = get_linode_types200_response_data_inner_addons_backups_instance.to_dict()
# create an instance of GetLinodeTypes200ResponseDataInnerAddonsBackups from a dict
get_linode_types200_response_data_inner_addons_backups_from_dict = GetLinodeTypes200ResponseDataInnerAddonsBackups.from_dict(get_linode_types200_response_data_inner_addons_backups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


