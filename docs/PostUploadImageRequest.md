# PostUploadImageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_init** | **bool** | Whether the uploaded Image supports cloud-init. | [optional] 
**description** | **str** | Description for the uploaded image. | [optional] 
**label** | **str** | Label for the uploaded image. | 
**region** | **str** | The region to upload to. Once uploaded, the image can be used in any region. | 
**tags** | **List[str]** | Tags you can use to organize images. A tag can be from 3 to 100 characters long, and an image can have a maximum of 500 total tags. | [optional] 

## Example

```python
from openapi_client.models.post_upload_image_request import PostUploadImageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostUploadImageRequest from a JSON string
post_upload_image_request_instance = PostUploadImageRequest.from_json(json)
# print the JSON string representation of the object
print(PostUploadImageRequest.to_json())

# convert the object into a dict
post_upload_image_request_dict = post_upload_image_request_instance.to_dict()
# create an instance of PostUploadImageRequest from a dict
post_upload_image_request_from_dict = PostUploadImageRequest.from_dict(post_upload_image_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


