# GetNotifications200ResponseDataInnerEntity

Detailed information about the notification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique ID of the notification&#39;s entity, based on the entity type. Returns &#x60;null&#x60; for an &#x60;account&#x60; or &#x60;promotion&#x60; entity. | [optional] 
**label** | **str** | The current label for this notification&#39;s entity.  Returns &#x60;null&#x60; for the following entity types:  - &#x60;entity_transfer&#x60; - &#x60;promotion&#x60; - &#x60;region&#x60; | [optional] 
**type** | **str** | The type of entity this is related to. | [optional] 
**url** | **str** | The URL where you can access the notification&#39;s object. The URL is relative to the domain where you retrieved the notification. This value is &#x60;null&#x60; for the &#x60;promotion&#x60; entity type. | [optional] 

## Example

```python
from openapi_client.models.get_notifications200_response_data_inner_entity import GetNotifications200ResponseDataInnerEntity

# TODO update the JSON string below
json = "{}"
# create an instance of GetNotifications200ResponseDataInnerEntity from a JSON string
get_notifications200_response_data_inner_entity_instance = GetNotifications200ResponseDataInnerEntity.from_json(json)
# print the JSON string representation of the object
print(GetNotifications200ResponseDataInnerEntity.to_json())

# convert the object into a dict
get_notifications200_response_data_inner_entity_dict = get_notifications200_response_data_inner_entity_instance.to_dict()
# create an instance of GetNotifications200ResponseDataInnerEntity from a dict
get_notifications200_response_data_inner_entity_from_dict = GetNotifications200ResponseDataInnerEntity.from_dict(get_notifications200_response_data_inner_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


