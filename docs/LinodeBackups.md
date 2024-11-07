# LinodeBackups

Information about this Linode's backups status. For information about available backups, run [List backups](https://techdocs.akamai.com/linode-api/reference/get-backups).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **bool** | Whether Backups for this Linode are available for restoration.  Backups undergoing maintenance are not available for restoration. | [optional] [readonly] 
**enabled** | **bool** | If this Linode has the Backup service enabled. To enable backups, run [Enable backups](https://techdocs.akamai.com/linode-api/reference/post-enable-backups). | [optional] [readonly] 
**last_successful** | **datetime** | The last successful backup time. Displayed as &#x60;null&#x60; if there was no previous backup. | [optional] [readonly] 
**schedule** | [**LinodeBackupsSchedule**](LinodeBackupsSchedule.md) |  | [optional] 

## Example

```python
from openapi_client.models.linode_backups import LinodeBackups

# TODO update the JSON string below
json = "{}"
# create an instance of LinodeBackups from a JSON string
linode_backups_instance = LinodeBackups.from_json(json)
# print the JSON string representation of the object
print(LinodeBackups.to_json())

# convert the object into a dict
linode_backups_dict = linode_backups_instance.to_dict()
# create an instance of LinodeBackups from a dict
linode_backups_from_dict = LinodeBackups.from_dict(linode_backups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


