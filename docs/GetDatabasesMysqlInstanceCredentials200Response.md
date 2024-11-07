# GetDatabasesMysqlInstanceCredentials200Response

Managed Database object for database credentials.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | The randomly generated root password for the Managed Database instance. | [optional] [readonly] 
**username** | **str** | The root username for the Managed Database instance. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_databases_mysql_instance_credentials200_response import GetDatabasesMysqlInstanceCredentials200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDatabasesMysqlInstanceCredentials200Response from a JSON string
get_databases_mysql_instance_credentials200_response_instance = GetDatabasesMysqlInstanceCredentials200Response.from_json(json)
# print the JSON string representation of the object
print(GetDatabasesMysqlInstanceCredentials200Response.to_json())

# convert the object into a dict
get_databases_mysql_instance_credentials200_response_dict = get_databases_mysql_instance_credentials200_response_instance.to_dict()
# create an instance of GetDatabasesMysqlInstanceCredentials200Response from a dict
get_databases_mysql_instance_credentials200_response_from_dict = GetDatabasesMysqlInstanceCredentials200Response.from_dict(get_databases_mysql_instance_credentials200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


