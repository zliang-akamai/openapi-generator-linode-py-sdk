# GetNotifications200ResponseDataInner

An important, often time-sensitive item related to your account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | A full description of this notification, in markdown format. Not all notifications include a &#x60;body&#x60;. | [optional] [readonly] 
**entity** | [**GetNotifications200ResponseDataInnerEntity**](GetNotifications200ResponseDataInnerEntity.md) |  | [optional] 
**label** | **str** | A short description of this notification. | [optional] [readonly] 
**message** | **str** | A human-readable description of the notification. | [optional] [readonly] 
**severity** | **str** | The severity of this notification. This field determines how prominently the notification is displayed and the color of the display text. | [optional] [readonly] 
**type** | **str** | The type of notification. | [optional] [readonly] 
**until** | **datetime** | If this notification has a duration, this is when the event or action will complete. For example, if there&#39;s scheduled maintenance for one of our systems, &#x60;until&#x60; represents the end of the maintenance window. | [optional] [readonly] 
**when** | **datetime** | If this notification is for an event in the future, this specifies when the action occurs. For example, if a compute instance needs to migrate in response to a security advisory, this field sets the approximate time the compute instance will be taken offline for migration. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_notifications200_response_data_inner import GetNotifications200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetNotifications200ResponseDataInner from a JSON string
get_notifications200_response_data_inner_instance = GetNotifications200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetNotifications200ResponseDataInner.to_json())

# convert the object into a dict
get_notifications200_response_data_inner_dict = get_notifications200_response_data_inner_instance.to_dict()
# create an instance of GetNotifications200ResponseDataInner from a dict
get_notifications200_response_data_inner_from_dict = GetNotifications200ResponseDataInner.from_dict(get_notifications200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


