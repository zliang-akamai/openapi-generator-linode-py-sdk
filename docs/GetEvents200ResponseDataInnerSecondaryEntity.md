# GetEvents200ResponseDataInnerSecondaryEntity

Detailed information about the Event's secondary entity, which provides additional information for events such as, but not limited to, `linode_boot`, `linode_reboot`, `linode_create`, and `linode_clone` Event actions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the object that is the secondary entity. | [optional] 
**label** | **str** | The label of this object. | [optional] 
**type** | **str** | The type of entity that is being referenced by the Event. | [optional] [readonly] 
**url** | **str** | The URL where you can access the object this Event is for. If a relative URL, it is relative to the domain you retrieved the Event from. | [optional] 

## Example

```python
from openapi_client.models.get_events200_response_data_inner_secondary_entity import GetEvents200ResponseDataInnerSecondaryEntity

# TODO update the JSON string below
json = "{}"
# create an instance of GetEvents200ResponseDataInnerSecondaryEntity from a JSON string
get_events200_response_data_inner_secondary_entity_instance = GetEvents200ResponseDataInnerSecondaryEntity.from_json(json)
# print the JSON string representation of the object
print(GetEvents200ResponseDataInnerSecondaryEntity.to_json())

# convert the object into a dict
get_events200_response_data_inner_secondary_entity_dict = get_events200_response_data_inner_secondary_entity_instance.to_dict()
# create an instance of GetEvents200ResponseDataInnerSecondaryEntity from a dict
get_events200_response_data_inner_secondary_entity_from_dict = GetEvents200ResponseDataInnerSecondaryEntity.from_dict(get_events200_response_data_inner_secondary_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


