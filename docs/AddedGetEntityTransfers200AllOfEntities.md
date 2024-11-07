# AddedGetEntityTransfers200AllOfEntities

A collection of the entities to include in this transfer request, separated by type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linodes** | **List[int]** | An array containing the IDs of each of the Linodes included in this transfer. | [optional] 

## Example

```python
from openapi_client.models.added_get_entity_transfers200_all_of_entities import AddedGetEntityTransfers200AllOfEntities

# TODO update the JSON string below
json = "{}"
# create an instance of AddedGetEntityTransfers200AllOfEntities from a JSON string
added_get_entity_transfers200_all_of_entities_instance = AddedGetEntityTransfers200AllOfEntities.from_json(json)
# print the JSON string representation of the object
print(AddedGetEntityTransfers200AllOfEntities.to_json())

# convert the object into a dict
added_get_entity_transfers200_all_of_entities_dict = added_get_entity_transfers200_all_of_entities_instance.to_dict()
# create an instance of AddedGetEntityTransfers200AllOfEntities from a dict
added_get_entity_transfers200_all_of_entities_from_dict = AddedGetEntityTransfers200AllOfEntities.from_dict(added_get_entity_transfers200_all_of_entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


