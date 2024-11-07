# GetDatabasesInstances200ResponseAllOfDataInnerUpdates

Configuration settings for automated patch update maintenance for the Managed Database.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_of_week** | **int** | The day to perform maintenance. 1&#x3D;Monday, 2&#x3D;Tuesday, etc. | [optional] 
**duration** | **int** | The maximum maintenance window time in hours. | [optional] 
**frequency** | **str** | Whether maintenance occurs on a weekly or monthly basis. | [optional] [default to 'weekly']
**hour_of_day** | **int** | The hour to begin maintenance based in UTC time. | [optional] 
**week_of_month** | **int** | The week of the month to perform &#x60;monthly&#x60; frequency updates. Defaults to &#x60;null&#x60;.  - Required for &#x60;monthly&#x60; frequency updates.  - Must be &#x60;null&#x60; for &#x60;weekly&#x60; frequency updates. | [optional] 

## Example

```python
from openapi_client.models.get_databases_instances200_response_all_of_data_inner_updates import GetDatabasesInstances200ResponseAllOfDataInnerUpdates

# TODO update the JSON string below
json = "{}"
# create an instance of GetDatabasesInstances200ResponseAllOfDataInnerUpdates from a JSON string
get_databases_instances200_response_all_of_data_inner_updates_instance = GetDatabasesInstances200ResponseAllOfDataInnerUpdates.from_json(json)
# print the JSON string representation of the object
print(GetDatabasesInstances200ResponseAllOfDataInnerUpdates.to_json())

# convert the object into a dict
get_databases_instances200_response_all_of_data_inner_updates_dict = get_databases_instances200_response_all_of_data_inner_updates_instance.to_dict()
# create an instance of GetDatabasesInstances200ResponseAllOfDataInnerUpdates from a dict
get_databases_instances200_response_all_of_data_inner_updates_from_dict = GetDatabasesInstances200ResponseAllOfDataInnerUpdates.from_dict(get_databases_instances200_response_all_of_data_inner_updates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


