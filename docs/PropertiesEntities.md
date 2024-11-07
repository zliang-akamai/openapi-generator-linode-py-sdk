# PropertiesEntities

A collection of the services to include in this transfer request, separated by type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linodes** | **List[int]** | An array containing the IDs of each of the Linodes included in this transfer. | [optional] 

## Example

```python
from openapi_client.models.properties_entities import PropertiesEntities

# TODO update the JSON string below
json = "{}"
# create an instance of PropertiesEntities from a JSON string
properties_entities_instance = PropertiesEntities.from_json(json)
# print the JSON string representation of the object
print(PropertiesEntities.to_json())

# convert the object into a dict
properties_entities_dict = properties_entities_instance.to_dict()
# create an instance of PropertiesEntities from a dict
properties_entities_from_dict = PropertiesEntities.from_dict(properties_entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


