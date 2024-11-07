# PostResizeDiskRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **int** | The desired size, in MB, of the disk. | 

## Example

```python
from openapi_client.models.post_resize_disk_request import PostResizeDiskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostResizeDiskRequest from a JSON string
post_resize_disk_request_instance = PostResizeDiskRequest.from_json(json)
# print the JSON string representation of the object
print(PostResizeDiskRequest.to_json())

# convert the object into a dict
post_resize_disk_request_dict = post_resize_disk_request_instance.to_dict()
# create an instance of PostResizeDiskRequest from a dict
post_resize_disk_request_from_dict = PostResizeDiskRequest.from_dict(post_resize_disk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


