# GetDatabasesMysqlInstanceBackups200ResponseAllOfDataInner

A database backup object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | A time value given in a combined date and time format that represents when the database backup was created. | [optional] 
**id** | **int** | The ID of the database backup object. | [optional] 
**label** | **str** | The database backup&#39;s label, for display purposes only.  Must include only ASCII letters or numbers. | [optional] 
**type** | **str** | The type of database backup, determined by how the backup was created. | [optional] 

## Example

```python
from openapi_client.models.get_databases_mysql_instance_backups200_response_all_of_data_inner import GetDatabasesMysqlInstanceBackups200ResponseAllOfDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetDatabasesMysqlInstanceBackups200ResponseAllOfDataInner from a JSON string
get_databases_mysql_instance_backups200_response_all_of_data_inner_instance = GetDatabasesMysqlInstanceBackups200ResponseAllOfDataInner.from_json(json)
# print the JSON string representation of the object
print(GetDatabasesMysqlInstanceBackups200ResponseAllOfDataInner.to_json())

# convert the object into a dict
get_databases_mysql_instance_backups200_response_all_of_data_inner_dict = get_databases_mysql_instance_backups200_response_all_of_data_inner_instance.to_dict()
# create an instance of GetDatabasesMysqlInstanceBackups200ResponseAllOfDataInner from a dict
get_databases_mysql_instance_backups200_response_all_of_data_inner_from_dict = GetDatabasesMysqlInstanceBackups200ResponseAllOfDataInner.from_dict(get_databases_mysql_instance_backups200_response_all_of_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


