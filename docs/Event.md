# Event

A collection of Event objects. An Event is an action taken against an entity related to your Account. For example, booting a Linode would create an Event. The Events returned depends on your grants.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action that caused this Event. New actions may be added in the future. | [optional] [readonly] 
**created** | **datetime** | When this Event was created. | [optional] [readonly] 
**duration** | **float** | The total duration in seconds that it takes for the Event to complete. | [optional] [readonly] 
**entity** | [**GetEvents200ResponseDataInnerEntity**](GetEvents200ResponseDataInnerEntity.md) |  | [optional] 
**id** | **int** | The unique ID of this Event. | [optional] [readonly] 
**message** | **str** | Provides additional information about the event. Additional information may include, but is not limited to, a more detailed representation of events which can help diagnose non-obvious failures. | [optional] 
**percent_complete** | **int** | A percentage estimating the amount of time remaining for an Event. Returns &#x60;null&#x60; for notification events. | [optional] [readonly] 
**rate** | **str** | The rate of completion of the Event. Only some Events will return rate; for example, migration and resize Events. | [optional] [readonly] 
**read** | **bool** | If this Event has been read. | [optional] [readonly] 
**secondary_entity** | [**GetEvents200ResponseDataInnerSecondaryEntity**](GetEvents200ResponseDataInnerSecondaryEntity.md) |  | [optional] 
**seen** | **bool** | If this Event has been seen. | [optional] [readonly] 
**status** | **str** | The current status of this Event. | [optional] [readonly] 
**time_remaining** | **str** | The estimated time remaining until the completion of this Event. This value is only returned for some in-progress migration events. For all other in-progress events, the &#x60;percent_complete&#x60; attribute will indicate about how much more work is to be done. | [optional] [readonly] 
**username** | **str** | The username of the User who caused the Event. | [optional] [readonly] 

## Example

```python
from openapi_client.models.event import Event

# TODO update the JSON string below
json = "{}"
# create an instance of Event from a JSON string
event_instance = Event.from_json(json)
# print the JSON string representation of the object
print(Event.to_json())

# convert the object into a dict
event_dict = event_instance.to_dict()
# create an instance of Event from a dict
event_from_dict = Event.from_dict(event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


