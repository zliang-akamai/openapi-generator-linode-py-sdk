# PostVolumeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_id** | **int** | When creating a Volume attached to a Linode, the ID of the Linode Config to include the new Volume in. This Config must belong to the Linode referenced by &#x60;linode_id&#x60;. Must _not_ be provided if &#x60;linode_id&#x60; is not sent. If a &#x60;linode_id&#x60; is sent without a &#x60;config_id&#x60;, the volume will be attached:    - to the Linode&#39;s only config if it only has one config.   - to the Linode&#39;s last used config, if possible.  If no config can be selected for attachment, an error will be returned. | [optional] 
**encryption** | **str** | Enables encryption on the volume. Full disk encryption ensures the data stored on a block storage volume drive is secure. It protects against unauthorized access by keeping the data encrypted if the volume drive is removed from the data center, decommissioned, or disposed of.  The platform automatically manages the encryption and decryption process for you. You can use an encrypted volume the same way as you use a non-encrypted volume.  You can enable or disable disk encryption only when creating new block storage volumes. After a volume is created, the encryption setting can&#39;t be changed. | [optional] [default to 'disabled']
**label** | **str** | The Volume&#39;s label, which is also used in the &#x60;filesystem_path&#x60; of the resulting volume. | 
**linode_id** | **int** | The Linode this volume should be attached to upon creation. If not given, the volume will be created without an attachment. | [optional] 
**region** | **str** | The Region to deploy this Volume in. This is only required if a linode_id is not given. | [optional] 
**size** | **int** | The initial size of this volume, in GB.  Be aware that volumes may only be resized up after creation. | [optional] [default to 20]
**tags** | **List[str]** | An array of Tags applied to this object.  Tags are for organizational purposes only. | [optional] 

## Example

```python
from openapi_client.models.post_volume_request import PostVolumeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostVolumeRequest from a JSON string
post_volume_request_instance = PostVolumeRequest.from_json(json)
# print the JSON string representation of the object
print(PostVolumeRequest.to_json())

# convert the object into a dict
post_volume_request_dict = post_volume_request_instance.to_dict()
# create an instance of PostVolumeRequest from a dict
post_volume_request_from_dict = PostVolumeRequest.from_dict(post_volume_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


