# Maintenance

Information about maintenance affecting an entity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**GetMaintenance200ResponseDataInnerEntity**](GetMaintenance200ResponseDataInnerEntity.md) |  | [optional] 
**reason** | **str** | The reason maintenance is being performed. | [optional] 
**status** | **str** | The maintenance status.  Maintenance progresses in the following sequence: pending, started, then completed. | [optional] 
**type** | **str** | The type of maintenance. | [optional] 
**when** | **datetime** | When the maintenance will begin.  [Filterable](https://techdocs.akamai.com/linode-api/reference/filtering-and-sorting) with the following parameters:  - A single value in date-time string format (&#x60;%Y-%m-%dT%H:%M:%S&#x60;), which returns only matches to that value.  - A dictionary containing pairs of inequality operator string keys (&#x60;+or&#x60;, &#x60;+gt&#x60;, &#x60;+gte&#x60;, &#x60;+lt&#x60;, &#x60;+lte&#x60;, or &#x60;+neq&#x60;) and single date-time string format values (&#x60;%Y-%m-%dT%H:%M:%S&#x60;). &#x60;+or&#x60; accepts an array of values that may consist of single date-time strings or dictionaries of inequality operator pairs. | [optional] 

## Example

```python
from openapi_client.models.maintenance import Maintenance

# TODO update the JSON string below
json = "{}"
# create an instance of Maintenance from a JSON string
maintenance_instance = Maintenance.from_json(json)
# print the JSON string representation of the object
print(Maintenance.to_json())

# convert the object into a dict
maintenance_dict = maintenance_instance.to_dict()
# create an instance of Maintenance from a dict
maintenance_from_dict = Maintenance.from_dict(maintenance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


