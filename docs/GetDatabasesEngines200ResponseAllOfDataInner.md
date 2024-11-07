# GetDatabasesEngines200ResponseAllOfDataInner

Managed Database engine object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**engine** | **str** | The Managed Database engine type. | [optional] 
**id** | **str** | The Managed Database engine ID in engine/version format. | [optional] 
**total_disk_size_gb** | **int** | The total disk size of the database in GB. | [optional] 
**used_disk_size_gb** | **int** | The used space of the database in GB. | [optional] 
**version** | **str** | The Managed Database engine version. | [optional] 

## Example

```python
from openapi_client.models.get_databases_engines200_response_all_of_data_inner import GetDatabasesEngines200ResponseAllOfDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetDatabasesEngines200ResponseAllOfDataInner from a JSON string
get_databases_engines200_response_all_of_data_inner_instance = GetDatabasesEngines200ResponseAllOfDataInner.from_json(json)
# print the JSON string representation of the object
print(GetDatabasesEngines200ResponseAllOfDataInner.to_json())

# convert the object into a dict
get_databases_engines200_response_all_of_data_inner_dict = get_databases_engines200_response_all_of_data_inner_instance.to_dict()
# create an instance of GetDatabasesEngines200ResponseAllOfDataInner from a dict
get_databases_engines200_response_all_of_data_inner_from_dict = GetDatabasesEngines200ResponseAllOfDataInner.from_dict(get_databases_engines200_response_all_of_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


