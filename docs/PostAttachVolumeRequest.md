# PostAttachVolumeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_id** | **int** | The ID of the Linode Config to include this Volume in. Must belong to the Linode referenced by &#x60;linode_id&#x60;. If not given, the last booted Config will be chosen. | [optional] 
**linode_id** | **int** | The ID of the Linode to attach the volume to. | 
**persist_across_boots** | **bool** | Defaults to true, if false is provided, the Volume will not be attached to the Linode Config. In this case more than 8 Volumes may be attached to a Linode if a Linode has 16GB of RAM or more. The number of volumes that can be attached is equal to the number of GB of RAM that the Linode has, up to a maximum of 64. &#x60;config_id&#x60; should not be passed if this is set to false and linode_id must be passed. The Linode must be running. | [optional] 

## Example

```python
from openapi_client.models.post_attach_volume_request import PostAttachVolumeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostAttachVolumeRequest from a JSON string
post_attach_volume_request_instance = PostAttachVolumeRequest.from_json(json)
# print the JSON string representation of the object
print(PostAttachVolumeRequest.to_json())

# convert the object into a dict
post_attach_volume_request_dict = post_attach_volume_request_instance.to_dict()
# create an instance of PostAttachVolumeRequest from a dict
post_attach_volume_request_from_dict = PostAttachVolumeRequest.from_dict(post_attach_volume_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


