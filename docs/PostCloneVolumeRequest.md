# PostCloneVolumeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The Volume&#39;s label is for display purposes only. | 

## Example

```python
from openapi_client.models.post_clone_volume_request import PostCloneVolumeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostCloneVolumeRequest from a JSON string
post_clone_volume_request_instance = PostCloneVolumeRequest.from_json(json)
# print the JSON string representation of the object
print(PostCloneVolumeRequest.to_json())

# convert the object into a dict
post_clone_volume_request_dict = post_clone_volume_request_instance.to_dict()
# create an instance of PostCloneVolumeRequest from a dict
post_clone_volume_request_from_dict = PostCloneVolumeRequest.from_dict(post_clone_volume_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


