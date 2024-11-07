# GetDatabasesTypes200ResponseAllOfDataInnerEngines


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mysql** | [**List[GetDatabasesTypes200ResponseAllOfDataInnerEnginesMysqlInner]**](GetDatabasesTypes200ResponseAllOfDataInnerEnginesMysqlInner.md) | Pricing details for MySQL Managed Databases. | [optional] 
**postgresql** | [**List[GetDatabasesTypes200ResponseAllOfDataInnerEnginesMysqlInner]**](GetDatabasesTypes200ResponseAllOfDataInnerEnginesMysqlInner.md) | Pricing details for PostgreSQL Managed Databases. | [optional] 

## Example

```python
from openapi_client.models.get_databases_types200_response_all_of_data_inner_engines import GetDatabasesTypes200ResponseAllOfDataInnerEngines

# TODO update the JSON string below
json = "{}"
# create an instance of GetDatabasesTypes200ResponseAllOfDataInnerEngines from a JSON string
get_databases_types200_response_all_of_data_inner_engines_instance = GetDatabasesTypes200ResponseAllOfDataInnerEngines.from_json(json)
# print the JSON string representation of the object
print(GetDatabasesTypes200ResponseAllOfDataInnerEngines.to_json())

# convert the object into a dict
get_databases_types200_response_all_of_data_inner_engines_dict = get_databases_types200_response_all_of_data_inner_engines_instance.to_dict()
# create an instance of GetDatabasesTypes200ResponseAllOfDataInnerEngines from a dict
get_databases_types200_response_all_of_data_inner_engines_from_dict = GetDatabasesTypes200ResponseAllOfDataInnerEngines.from_dict(get_databases_types200_response_all_of_data_inner_engines_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


