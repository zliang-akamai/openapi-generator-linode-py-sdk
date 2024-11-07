# PostAddLinodeDiskRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorized_keys** | **List[str]** | A list of public SSH keys that will be automatically appended to the root user&#39;s &#x60;~/.ssh/authorized_keys&#x60; file when deploying from an Image. | [optional] 
**authorized_users** | **List[str]** | A list of usernames. If the usernames have associated SSH keys, the keys will be appended to the root users &#x60;~/.ssh/authorized_keys&#x60; file automatically when deploying from an Image. | [optional] 
**filesystem** | **str** | The file system of the disk. This can be &#x60;raw&#x60;, which indicates no file system, just a raw binary stream, &#x60;swap&#x60; for a Linux swap area, &#x60;ext3&#x60; or &#x60;ext4&#x60; for the ext3 of ext4 journaling file systems for Linux, respectively, or &#x60;initrd&#x60; for uncompressed initrd, ext2 with a maximum size of 32 MB. | [optional] 
**image** | **str** | An Image ID to deploy the Linode Disk from.  Run the [List images](https://techdocs.akamai.com/linode-api/reference/get-images) operation with authentication to view all available Images. Official Linode Images start with &#x60;linode/&#x60;, while your Account&#39;s Images start with &#x60;private/&#x60;. Creating a disk from a Private Image requires &#x60;read_only&#x60; or &#x60;read_write&#x60; permissions for that Image. Run the [Update a user&#39;s grants](https://techdocs.akamai.com/linode-api/reference/put-user-grants) operation to adjust permissions for an Account Image. | [optional] 
**label** | **str** | The name of the disk. This is for display purposes only. | [optional] 
**root_pass** | **str** | This sets the root user&#39;s password on a newly created Linode Disk when deploying from an Image.  - __Required__ when creating a Linode Disk from an Image, including when using a StackScript.  - Must meet a password strength score requirement that is calculated internally by the API. If the strength requirement is not met, you will receive a &#x60;Password does not meet strength requirement&#x60; error. | [optional] 
**size** | **int** | The size of the Disk in MB.  Images require a minimum size. Run the [Get an image](https://techdocs.akamai.com/linode-api/reference/get-image) operation to view its size. | 
**stackscript_data** | **object** | This field is required only if the StackScript being deployed requires input data from the User for successful completion. See [User Defined Fields (UDFs)](https://www.linode.com/docs/products/tools/stackscripts/guides/write-a-custom-script/#declare-user-defined-fields-udfs) for more details.  This field is required to be valid JSON.  Total length cannot exceed 65,535 characters. | [optional] 
**stackscript_id** | **int** | A StackScript ID that will cause the referenced StackScript to be run during deployment of this Linode. A compatible &#x60;image&#x60; is required to use a StackScript. To get a list of available StackScript and their permitted Images, run [List StackScripts](https://techdocs.akamai.com/linode-api/reference/get-stack-scripts). This field cannot be used when deploying from a Backup or a Private Image. | [optional] 

## Example

```python
from openapi_client.models.post_add_linode_disk_request import PostAddLinodeDiskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostAddLinodeDiskRequest from a JSON string
post_add_linode_disk_request_instance = PostAddLinodeDiskRequest.from_json(json)
# print the JSON string representation of the object
print(PostAddLinodeDiskRequest.to_json())

# convert the object into a dict
post_add_linode_disk_request_dict = post_add_linode_disk_request_instance.to_dict()
# create an instance of PostAddLinodeDiskRequest from a dict
post_add_linode_disk_request_from_dict = PostAddLinodeDiskRequest.from_dict(post_add_linode_disk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


