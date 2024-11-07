# GetDatabasesMysqlInstanceSsl200Response

Managed Database SSL object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_certificate** | **str** | The base64-encoded SSL CA certificate for the Managed Database instance. | [optional] 

## Example

```python
from openapi_client.models.get_databases_mysql_instance_ssl200_response import GetDatabasesMysqlInstanceSsl200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDatabasesMysqlInstanceSsl200Response from a JSON string
get_databases_mysql_instance_ssl200_response_instance = GetDatabasesMysqlInstanceSsl200Response.from_json(json)
# print the JSON string representation of the object
print(GetDatabasesMysqlInstanceSsl200Response.to_json())

# convert the object into a dict
get_databases_mysql_instance_ssl200_response_dict = get_databases_mysql_instance_ssl200_response_instance.to_dict()
# create an instance of GetDatabasesMysqlInstanceSsl200Response from a dict
get_databases_mysql_instance_ssl200_response_from_dict = GetDatabasesMysqlInstanceSsl200Response.from_dict(get_databases_mysql_instance_ssl200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


