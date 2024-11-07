# GetDatabasesTypes200ResponseAllOfDataInner

Managed Database plan type object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_class** | **str** | The compute class category. | [optional] 
**deprecated** | **bool** | Whether this Database plan type has been deprecated and is no longer available. | [optional] 
**disk** | **int** | The amount of disk space set aside for Databases of this plan type. The value is represented in megabytes. | [optional] 
**engines** | [**GetDatabasesTypes200ResponseAllOfDataInnerEngines**](GetDatabasesTypes200ResponseAllOfDataInnerEngines.md) |  | [optional] 
**id** | **str** | The ID representing the Managed Database node plan type. | [optional] [readonly] 
**label** | **str** | A human-readable string that describes each plan type. For display purposes only. | [optional] [readonly] 
**memory** | **int** | The amount of RAM allocated to Database created of this plan type. The value is represented in megabytes. | [optional] 
**vcpus** | **int** | The number of CPUs allocated to databases of this plan type. | [optional] 

## Example

```python
from openapi_client.models.get_databases_types200_response_all_of_data_inner import GetDatabasesTypes200ResponseAllOfDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetDatabasesTypes200ResponseAllOfDataInner from a JSON string
get_databases_types200_response_all_of_data_inner_instance = GetDatabasesTypes200ResponseAllOfDataInner.from_json(json)
# print the JSON string representation of the object
print(GetDatabasesTypes200ResponseAllOfDataInner.to_json())

# convert the object into a dict
get_databases_types200_response_all_of_data_inner_dict = get_databases_types200_response_all_of_data_inner_instance.to_dict()
# create an instance of GetDatabasesTypes200ResponseAllOfDataInner from a dict
get_databases_types200_response_all_of_data_inner_from_dict = GetDatabasesTypes200ResponseAllOfDataInner.from_dict(get_databases_types200_response_all_of_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


