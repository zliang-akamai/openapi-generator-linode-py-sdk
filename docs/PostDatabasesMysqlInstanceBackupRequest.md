# PostDatabasesMysqlInstanceBackupRequest

Managed Database request object for snapshot backup.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The label for the Database snapshot backup.  - Can only contain ASCII letters, numbers, and underscores (&#x60;_&#x60;). - Must be unique among other backup labels for this Database. | 
**target** | **str** | The Database cluster target. If the Database is a high availability cluster, choosing &#x60;secondary&#x60; creates a snapshot backup of a replica node. | [optional] [default to 'primary']

## Example

```python
from openapi_client.models.post_databases_mysql_instance_backup_request import PostDatabasesMysqlInstanceBackupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostDatabasesMysqlInstanceBackupRequest from a JSON string
post_databases_mysql_instance_backup_request_instance = PostDatabasesMysqlInstanceBackupRequest.from_json(json)
# print the JSON string representation of the object
print(PostDatabasesMysqlInstanceBackupRequest.to_json())

# convert the object into a dict
post_databases_mysql_instance_backup_request_dict = post_databases_mysql_instance_backup_request_instance.to_dict()
# create an instance of PostDatabasesMysqlInstanceBackupRequest from a dict
post_databases_mysql_instance_backup_request_from_dict = PostDatabasesMysqlInstanceBackupRequest.from_dict(post_databases_mysql_instance_backup_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


