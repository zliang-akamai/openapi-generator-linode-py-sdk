# GetDatabasesTypes200ResponseAllOfDataInnerEnginesMysqlInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | [**GetDatabasesTypes200ResponseAllOfDataInnerEnginesMysqlInnerPrice**](GetDatabasesTypes200ResponseAllOfDataInnerEnginesMysqlInnerPrice.md) |  | [optional] 
**quantity** | **int** | The number of nodes for the Managed Database cluster for this subscription tier. | [optional] 

## Example

```python
from openapi_client.models.get_databases_types200_response_all_of_data_inner_engines_mysql_inner import GetDatabasesTypes200ResponseAllOfDataInnerEnginesMysqlInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetDatabasesTypes200ResponseAllOfDataInnerEnginesMysqlInner from a JSON string
get_databases_types200_response_all_of_data_inner_engines_mysql_inner_instance = GetDatabasesTypes200ResponseAllOfDataInnerEnginesMysqlInner.from_json(json)
# print the JSON string representation of the object
print(GetDatabasesTypes200ResponseAllOfDataInnerEnginesMysqlInner.to_json())

# convert the object into a dict
get_databases_types200_response_all_of_data_inner_engines_mysql_inner_dict = get_databases_types200_response_all_of_data_inner_engines_mysql_inner_instance.to_dict()
# create an instance of GetDatabasesTypes200ResponseAllOfDataInnerEnginesMysqlInner from a dict
get_databases_types200_response_all_of_data_inner_engines_mysql_inner_from_dict = GetDatabasesTypes200ResponseAllOfDataInnerEnginesMysqlInner.from_dict(get_databases_types200_response_all_of_data_inner_engines_mysql_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


