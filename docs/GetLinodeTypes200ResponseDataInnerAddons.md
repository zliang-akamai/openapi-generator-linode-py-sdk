# GetLinodeTypes200ResponseDataInnerAddons

A list of optional add-on services for Linodes and their associated costs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backups** | [**GetLinodeTypes200ResponseDataInnerAddonsBackups**](GetLinodeTypes200ResponseDataInnerAddonsBackups.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_linode_types200_response_data_inner_addons import GetLinodeTypes200ResponseDataInnerAddons

# TODO update the JSON string below
json = "{}"
# create an instance of GetLinodeTypes200ResponseDataInnerAddons from a JSON string
get_linode_types200_response_data_inner_addons_instance = GetLinodeTypes200ResponseDataInnerAddons.from_json(json)
# print the JSON string representation of the object
print(GetLinodeTypes200ResponseDataInnerAddons.to_json())

# convert the object into a dict
get_linode_types200_response_data_inner_addons_dict = get_linode_types200_response_data_inner_addons_instance.to_dict()
# create an instance of GetLinodeTypes200ResponseDataInnerAddons from a dict
get_linode_types200_response_data_inner_addons_from_dict = GetLinodeTypes200ResponseDataInnerAddons.from_dict(get_linode_types200_response_data_inner_addons_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


