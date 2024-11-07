# GetEvents200ResponseDataInnerEntity

Detailed information about the Event's entity, including ID, type, label, and URL used to access it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique ID for an Event&#39;s entity.  Some Event entities do not have IDs associated with them, so they will not be returned when filtering by ID. These Events include:    - &#x60;account&#x60;   - &#x60;profile&#x60;  Entities for some Events are assigned the ID of the Linode they correspond to. When filtering by ID for these Events, use the corresponding Linode&#39;s ID. These Events include:    - &#x60;disks&#x60;   - &#x60;backups&#x60;  Tag Events use a tag&#39;s name for the entity ID field. When filtering by ID for tag Events, supply the name of the tag. | [optional] 
**label** | **str** | The current label of this object. The label may reflect changes that occur with this Event. | [optional] 
**type** | **str** | The type of entity that is being referenced by the Event. | [optional] [readonly] 
**url** | **str** | The URL where you can access the object this Event is for. If a relative URL, it is relative to the domain you retrieved the Event from. | [optional] 

## Example

```python
from openapi_client.models.get_events200_response_data_inner_entity import GetEvents200ResponseDataInnerEntity

# TODO update the JSON string below
json = "{}"
# create an instance of GetEvents200ResponseDataInnerEntity from a JSON string
get_events200_response_data_inner_entity_instance = GetEvents200ResponseDataInnerEntity.from_json(json)
# print the JSON string representation of the object
print(GetEvents200ResponseDataInnerEntity.to_json())

# convert the object into a dict
get_events200_response_data_inner_entity_dict = get_events200_response_data_inner_entity_instance.to_dict()
# create an instance of GetEvents200ResponseDataInnerEntity from a dict
get_events200_response_data_inner_entity_from_dict = GetEvents200ResponseDataInnerEntity.from_dict(get_events200_response_data_inner_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


