# Entities

A collection of the entities to include in this transfer request, separated by type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linodes** | **List[int]** | An array containing the IDs of each of the Linodes included in this transfer. | [optional] 

## Example

```python
from openapi_client.models.entities import Entities

# TODO update the JSON string below
json = "{}"
# create an instance of Entities from a JSON string
entities_instance = Entities.from_json(json)
# print the JSON string representation of the object
print(Entities.to_json())

# convert the object into a dict
entities_dict = entities_instance.to_dict()
# create an instance of Entities from a dict
entities_from_dict = Entities.from_dict(entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


