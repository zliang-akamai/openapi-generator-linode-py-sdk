# PostRestoreBackupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linode_id** | **int** | The ID of the Linode to restore a Backup to. | 
**overwrite** | **bool** | If True, deletes all Disks and Configs on the target Linode before restoring.  If False, and the Disk image size is larger than the available space on the Linode, an error message indicating insufficient space is returned. | [optional] 

## Example

```python
from openapi_client.models.post_restore_backup_request import PostRestoreBackupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostRestoreBackupRequest from a JSON string
post_restore_backup_request_instance = PostRestoreBackupRequest.from_json(json)
# print the JSON string representation of the object
print(PostRestoreBackupRequest.to_json())

# convert the object into a dict
post_restore_backup_request_dict = post_restore_backup_request_instance.to_dict()
# create an instance of PostRestoreBackupRequest from a dict
post_restore_backup_request_from_dict = PostRestoreBackupRequest.from_dict(post_restore_backup_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


