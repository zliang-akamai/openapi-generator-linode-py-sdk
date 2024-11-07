# StatsAvailableCpuInner

A stat data point.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x** | **int** | A stats graph data point. | [optional] [readonly] 
**y** | **int** | A stats graph data point. | [optional] [readonly] 

## Example

```python
from openapi_client.models.stats_available_cpu_inner import StatsAvailableCpuInner

# TODO update the JSON string below
json = "{}"
# create an instance of StatsAvailableCpuInner from a JSON string
stats_available_cpu_inner_instance = StatsAvailableCpuInner.from_json(json)
# print the JSON string representation of the object
print(StatsAvailableCpuInner.to_json())

# convert the object into a dict
stats_available_cpu_inner_dict = stats_available_cpu_inner_instance.to_dict()
# create an instance of StatsAvailableCpuInner from a dict
stats_available_cpu_inner_from_dict = StatsAvailableCpuInner.from_dict(stats_available_cpu_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


