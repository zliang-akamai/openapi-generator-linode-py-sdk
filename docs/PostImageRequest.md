# PostImageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_init** | **bool** | Whether this image supports [cloud-init](https://www.linode.com/docs/guides/write-files-with-cloud-init/). | [optional] 
**description** | **str** | A detailed description of this image. | [optional] 
**disk_id** | **int** | The ID of the target Linode disk for this image. | 
**label** | **str** | The short title for this image. If not provided, the disk&#39;s current label is used. | [optional] 
**tags** | **List[str]** | Tags used for organizational purposes. A tag can be from 3 to 100 characters long, and an image can have a maximum of 500 total tags. | [optional] 

## Example

```python
from openapi_client.models.post_image_request import PostImageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostImageRequest from a JSON string
post_image_request_instance = PostImageRequest.from_json(json)
# print the JSON string representation of the object
print(PostImageRequest.to_json())

# convert the object into a dict
post_image_request_dict = post_image_request_instance.to_dict()
# create an instance of PostImageRequest from a dict
post_image_request_from_dict = PostImageRequest.from_dict(post_image_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


