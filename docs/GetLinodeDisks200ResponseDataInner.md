# GetLinodeDisks200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | When this Disk was created. | [optional] [readonly] 
**disk_encryption** | **str** | Displays if encryption is enabled on this disk. This setting is based on the &#x60;disk_encryption&#x60; setting of the Linode. | [optional] [readonly] [default to 'enabled']
**filesystem** | **str** | The file system of the disk. This can be &#x60;raw&#x60;, which indicates no file system, just a raw binary stream, &#x60;swap&#x60; for a Linux swap area, &#x60;ext3&#x60; or &#x60;ext4&#x60; for the ext3 of ext4 journaling file systems for Linux, respectively, or &#x60;initrd&#x60; for uncompressed initrd, ext2 with a maximum size of 32 MB. | [optional] 
**id** | **int** | This disk&#39;s ID. You need this value to run other operations that interact with the disk. | [optional] [readonly] 
**label** | **str** | The name of the disk. This is for display purposes only. | [optional] 
**size** | **int** | The size of the disk in MB. | [optional] 
**status** | **str** | The current state of the disk. | [optional] [readonly] 
**updated** | **datetime** | When this disk was last updated. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_linode_disks200_response_data_inner import GetLinodeDisks200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLinodeDisks200ResponseDataInner from a JSON string
get_linode_disks200_response_data_inner_instance = GetLinodeDisks200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetLinodeDisks200ResponseDataInner.to_json())

# convert the object into a dict
get_linode_disks200_response_data_inner_dict = get_linode_disks200_response_data_inner_instance.to_dict()
# create an instance of GetLinodeDisks200ResponseDataInner from a dict
get_linode_disks200_response_data_inner_from_dict = GetLinodeDisks200ResponseDataInner.from_dict(get_linode_disks200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


