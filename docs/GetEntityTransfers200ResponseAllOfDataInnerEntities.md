# GetEntityTransfers200ResponseAllOfDataInnerEntities

A collection of the entities to include in this transfer request, separated by type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linodes** | **List[int]** | An array containing the IDs of each of the Linodes included in this transfer. | [optional] 

## Example

```python
from openapi_client.models.get_entity_transfers200_response_all_of_data_inner_entities import GetEntityTransfers200ResponseAllOfDataInnerEntities

# TODO update the JSON string below
json = "{}"
# create an instance of GetEntityTransfers200ResponseAllOfDataInnerEntities from a JSON string
get_entity_transfers200_response_all_of_data_inner_entities_instance = GetEntityTransfers200ResponseAllOfDataInnerEntities.from_json(json)
# print the JSON string representation of the object
print(GetEntityTransfers200ResponseAllOfDataInnerEntities.to_json())

# convert the object into a dict
get_entity_transfers200_response_all_of_data_inner_entities_dict = get_entity_transfers200_response_all_of_data_inner_entities_instance.to_dict()
# create an instance of GetEntityTransfers200ResponseAllOfDataInnerEntities from a dict
get_entity_transfers200_response_all_of_data_inner_entities_from_dict = GetEntityTransfers200ResponseAllOfDataInnerEntities.from_dict(get_entity_transfers200_response_all_of_data_inner_entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


