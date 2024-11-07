# Volume1

A Block Storage Volume associated with your Account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | When this Volume was created. | [optional] [readonly] 
**encryption** | **str** | Displays if encryption is enabled on this volume. | [optional] [readonly] 
**filesystem_path** | **str** | The full filesystem path for the Volume based on the Volume&#39;s label. Path is /dev/disk/by-id/scsi-0Linode_Volume_ + Volume label. | [optional] [readonly] 
**hardware_type** | **str** | The storage type of this Volume. | [optional] [readonly] 
**id** | **int** | The unique ID of this Volume. | [optional] [readonly] 
**label** | **str** | The Volume&#39;s label is for display purposes only. | [optional] 
**linode_id** | **int** | If a Volume is attached to a specific Linode, the ID of that Linode will be displayed here. | [optional] 
**linode_label** | **str** | If a Volume is attached to a specific Linode, the label of that Linode will be displayed here. | [optional] [readonly] 
**region** | **str** | The unique ID of this Region. | [optional] [readonly] 
**size** | **int** | The Volume&#39;s size, in GiB. | [optional] 
**status** | **str** | The current status of the volume.  Can be one of:    - &#x60;creating&#x60;. The volume is being created and is not yet available for use.   - &#x60;active&#x60;. The volume is online and available for use.   - &#x60;resizing&#x60;. The volume is in the process of upgrading its current capacity.   - &#x60;key_rotating&#x60;. The volume is in the process of rotating encryption keys. Requests to resize, delete, or clone a volume fails during encryption key rotation. | [optional] [readonly] 
**tags** | **List[str]** | An array of Tags applied to this object.  Tags are for organizational purposes only. | [optional] 
**updated** | **datetime** | When this Volume was last updated. | [optional] [readonly] 

## Example

```python
from openapi_client.models.volume1 import Volume1

# TODO update the JSON string below
json = "{}"
# create an instance of Volume1 from a JSON string
volume1_instance = Volume1.from_json(json)
# print the JSON string representation of the object
print(Volume1.to_json())

# convert the object into a dict
volume1_dict = volume1_instance.to_dict()
# create an instance of Volume1 from a dict
volume1_from_dict = Volume1.from_dict(volume1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


