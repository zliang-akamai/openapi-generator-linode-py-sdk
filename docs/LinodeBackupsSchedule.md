# LinodeBackupsSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | **str** | The day of the week that your Linode&#39;s weekly backup is taken. If not set manually, a day will be chosen for you. Backups are taken every day, but backups taken on this day are preferred when selecting backups to retain for a longer period.  If not set manually, then when backups are initially enabled, this may come back as &#x60;Scheduling&#x60; until the &#x60;day&#x60; is automatically selected. | [optional] 
**window** | **str** | When your backups will be taken, in UTC. A backups window is a two-hour span of time in which the backup may occur.  For example, &#x60;W10&#x60; indicates that your backups should be taken between 10:00 and 12:00. If you don&#39;t choose a backup window, the API automatically assigns one.  If not set manually, when backups are initially enabled this may come back as &#x60;Scheduling&#x60; until the &#x60;window&#x60; is automatically selected. | [optional] 

## Example

```python
from openapi_client.models.linode_backups_schedule import LinodeBackupsSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of LinodeBackupsSchedule from a JSON string
linode_backups_schedule_instance = LinodeBackupsSchedule.from_json(json)
# print the JSON string representation of the object
print(LinodeBackupsSchedule.to_json())

# convert the object into a dict
linode_backups_schedule_dict = linode_backups_schedule_instance.to_dict()
# create an instance of LinodeBackupsSchedule from a dict
linode_backups_schedule_from_dict = LinodeBackupsSchedule.from_dict(linode_backups_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


