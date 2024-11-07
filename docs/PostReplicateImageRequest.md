# PostReplicateImageRequest

List of regions where the image should be replicated to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**regions** | **List[str]** | The unique identifier for each compute &#x60;region&#x60;. See [Regions and images](https://techdocs.akamai.com/cloud-computing/docs/images#regions-and-images) for full details on support for &#x60;regions&#x60;. | [optional] 

## Example

```python
from openapi_client.models.post_replicate_image_request import PostReplicateImageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostReplicateImageRequest from a JSON string
post_replicate_image_request_instance = PostReplicateImageRequest.from_json(json)
# print the JSON string representation of the object
print(PostReplicateImageRequest.to_json())

# convert the object into a dict
post_replicate_image_request_dict = post_replicate_image_request_instance.to_dict()
# create an instance of PostReplicateImageRequest from a dict
post_replicate_image_request_from_dict = PostReplicateImageRequest.from_dict(post_replicate_image_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


