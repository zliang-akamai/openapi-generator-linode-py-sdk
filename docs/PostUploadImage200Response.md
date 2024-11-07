# PostUploadImage200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | [**GetImages200ResponseDataInner**](GetImages200ResponseDataInner.md) |  | [optional] 
**upload_to** | **str** | The URL to upload the Image to. | [optional] 

## Example

```python
from openapi_client.models.post_upload_image200_response import PostUploadImage200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostUploadImage200Response from a JSON string
post_upload_image200_response_instance = PostUploadImage200Response.from_json(json)
# print the JSON string representation of the object
print(PostUploadImage200Response.to_json())

# convert the object into a dict
post_upload_image200_response_dict = post_upload_image200_response_instance.to_dict()
# create an instance of PostUploadImage200Response from a dict
post_upload_image200_response_from_dict = PostUploadImage200Response.from_dict(post_upload_image200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


