# GetBackups200ResponseAutomaticInnerAllOfDisksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filesystem** | **str** | The file system of the disk. This can be &#x60;raw&#x60;, which indicates no file system, just a raw binary stream, &#x60;swap&#x60; for a Linux swap area, &#x60;ext3&#x60; or &#x60;ext4&#x60; for the ext3 of ext4 journaling file systems for Linux, respectively, or &#x60;initrd&#x60; for uncompressed initrd, ext2 with a maximum size of 32 MB. | [optional] 
**label** | **str** |  | [optional] 
**size** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.get_backups200_response_automatic_inner_all_of_disks_inner import GetBackups200ResponseAutomaticInnerAllOfDisksInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetBackups200ResponseAutomaticInnerAllOfDisksInner from a JSON string
get_backups200_response_automatic_inner_all_of_disks_inner_instance = GetBackups200ResponseAutomaticInnerAllOfDisksInner.from_json(json)
# print the JSON string representation of the object
print(GetBackups200ResponseAutomaticInnerAllOfDisksInner.to_json())

# convert the object into a dict
get_backups200_response_automatic_inner_all_of_disks_inner_dict = get_backups200_response_automatic_inner_all_of_disks_inner_instance.to_dict()
# create an instance of GetBackups200ResponseAutomaticInnerAllOfDisksInner from a dict
get_backups200_response_automatic_inner_all_of_disks_inner_from_dict = GetBackups200ResponseAutomaticInnerAllOfDisksInner.from_dict(get_backups200_response_automatic_inner_all_of_disks_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


