# GetMaintenance200ResponseDataInnerEntity

The entity being affected by maintenance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | The id of the entity being affected by maintenance. | [optional] 
**label** | **str** | The label of the entity being affected by maintenance. | [optional] 
**type** | **str** | The type of entity. | [optional] 
**url** | **str** | The API endpoint prefix to use in combination with the entity id to find specific information about the entity. | [optional] 

## Example

```python
from openapi_client.models.get_maintenance200_response_data_inner_entity import GetMaintenance200ResponseDataInnerEntity

# TODO update the JSON string below
json = "{}"
# create an instance of GetMaintenance200ResponseDataInnerEntity from a JSON string
get_maintenance200_response_data_inner_entity_instance = GetMaintenance200ResponseDataInnerEntity.from_json(json)
# print the JSON string representation of the object
print(GetMaintenance200ResponseDataInnerEntity.to_json())

# convert the object into a dict
get_maintenance200_response_data_inner_entity_dict = get_maintenance200_response_data_inner_entity_instance.to_dict()
# create an instance of GetMaintenance200ResponseDataInnerEntity from a dict
get_maintenance200_response_data_inner_entity_from_dict = GetMaintenance200ResponseDataInnerEntity.from_dict(get_maintenance200_response_data_inner_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


