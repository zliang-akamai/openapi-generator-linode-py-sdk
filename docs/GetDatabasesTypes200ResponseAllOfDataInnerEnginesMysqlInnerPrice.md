# GetDatabasesTypes200ResponseAllOfDataInnerEnginesMysqlInnerPrice

Cost in US dollars, broken down into hourly and monthly charges.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hourly** | **float** | Cost (in US dollars) per hour for this subscription tier. | [optional] 
**monthly** | **float** | Maximum cost (in US dollars) per month for this subscription tier. | [optional] 

## Example

```python
from openapi_client.models.get_databases_types200_response_all_of_data_inner_engines_mysql_inner_price import GetDatabasesTypes200ResponseAllOfDataInnerEnginesMysqlInnerPrice

# TODO update the JSON string below
json = "{}"
# create an instance of GetDatabasesTypes200ResponseAllOfDataInnerEnginesMysqlInnerPrice from a JSON string
get_databases_types200_response_all_of_data_inner_engines_mysql_inner_price_instance = GetDatabasesTypes200ResponseAllOfDataInnerEnginesMysqlInnerPrice.from_json(json)
# print the JSON string representation of the object
print(GetDatabasesTypes200ResponseAllOfDataInnerEnginesMysqlInnerPrice.to_json())

# convert the object into a dict
get_databases_types200_response_all_of_data_inner_engines_mysql_inner_price_dict = get_databases_types200_response_all_of_data_inner_engines_mysql_inner_price_instance.to_dict()
# create an instance of GetDatabasesTypes200ResponseAllOfDataInnerEnginesMysqlInnerPrice from a dict
get_databases_types200_response_all_of_data_inner_engines_mysql_inner_price_from_dict = GetDatabasesTypes200ResponseAllOfDataInnerEnginesMysqlInnerPrice.from_dict(get_databases_types200_response_all_of_data_inner_engines_mysql_inner_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


