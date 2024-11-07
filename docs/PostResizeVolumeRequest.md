# PostResizeVolumeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **int** | The Volume&#39;s size, in GiB. | 

## Example

```python
from openapi_client.models.post_resize_volume_request import PostResizeVolumeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostResizeVolumeRequest from a JSON string
post_resize_volume_request_instance = PostResizeVolumeRequest.from_json(json)
# print the JSON string representation of the object
print(PostResizeVolumeRequest.to_json())

# convert the object into a dict
post_resize_volume_request_dict = post_resize_volume_request_instance.to_dict()
# create an instance of PostResizeVolumeRequest from a dict
post_resize_volume_request_from_dict = PostResizeVolumeRequest.from_dict(post_resize_volume_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


