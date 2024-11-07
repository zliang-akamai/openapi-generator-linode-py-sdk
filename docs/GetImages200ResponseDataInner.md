# GetImages200ResponseDataInner

Image object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | **List[str]** | A list of the possible capabilities of this image.  - &#x60;cloud-init&#x60;. The image supports the cloud-init multi-distribution method with our [Metadata service](https://www.linode.com/docs/products/compute/compute-instances/guides/metadata/#troubleshoot-metadata-and-cloud-init). This only applies to public images.  - &#x60;distributed-sites&#x60;. Whether the image can be used in distributed compute regions. Compared to a core compute region, distributed compute regions offer limited functionality, but they&#39;re globally distributed. Your image can be geographically closer to you, potentially letting you deploy it quicker. See [Regions and images](https://techdocs.akamai.com/cloud-computing/docs/images#regions-and-images) for complete details. | [optional] [readonly] 
**created** | **datetime** | When this image was created. | [optional] [readonly] 
**created_by** | **str** | The name of the user who created this image, or &#x60;linode&#x60; for public images. | [optional] [readonly] 
**deprecated** | **bool** | Whether this image is deprecated. Only public images can be deprecated. | [optional] [readonly] 
**description** | **str** | A detailed description of this image. | [optional] 
**eol** | **datetime** | The date of the public image&#39;s planned removal from service. This is &#x60;null&#x60; for private images. | [optional] [readonly] 
**expiry** | **datetime** | Only images created automatically from a deleted compute instance (type&#x3D;automatic) expire. This is &#x60;null&#x60; for private images. | [optional] [readonly] 
**id** | **str** | The unique identifier for each image. | [optional] [readonly] 
**is_public** | **bool** | Revealed as &#x60;true&#x60; if the image is a public distribution image. Private, account-specific images are listed as &#x60;false&#x60;. | [optional] [readonly] 
**label** | **str** | A short description of the image. | [optional] 
**regions** | [**List[GetImages200ResponseDataInnerRegionsInner]**](GetImages200ResponseDataInnerRegionsInner.md) | Details on the regions where this image is stored. See [Regions and images](https://techdocs.akamai.com/cloud-computing/docs/images#regions-and-images) for full details on support for &#x60;regions&#x60;. | [optional] [readonly] 
**size** | **int** | The minimum size in MB this image needs to deploy. | [optional] [readonly] 
**status** | **str** | The current status of the image. Possible values are &#x60;available&#x60;, &#x60;creating&#x60;, and &#x60;pending_upload&#x60;.  &gt; 📘 &gt; &gt; The &#x60;+order_by&#x60; and &#x60;+order&#x60; operators are not available when [filtering](https://techdocs.akamai.com/linode-api/reference/filtering-and-sorting) on this key. | [optional] [readonly] 
**tags** | **List[str]** | Tags used for organizational purposes. A tag can be from 3 to 100 characters long, and an image can have a maximum of 500 total tags. | [optional] 
**total_size** | **int** | The total size in bytes of all instances of this image, in all &#x60;regions&#x60;.  &gt; 📘 &gt; &gt; This object is empty for existing images. It&#39;s intended for use with future functionality. | [optional] [readonly] 
**type** | **str** | How the image was created. Create a &#x60;manual&#x60; image at any time. An &#x60;automatic&#x60; image is created automatically from a deleted compute instance. | [optional] [readonly] 
**updated** | **datetime** | When this image was last updated. | [optional] [readonly] 
**vendor** | **str** | The upstream distribution vendor. This is &#x60;null&#x60; for private images. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_images200_response_data_inner import GetImages200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetImages200ResponseDataInner from a JSON string
get_images200_response_data_inner_instance = GetImages200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetImages200ResponseDataInner.to_json())

# convert the object into a dict
get_images200_response_data_inner_dict = get_images200_response_data_inner_instance.to_dict()
# create an instance of GetImages200ResponseDataInner from a dict
get_images200_response_data_inner_from_dict = GetImages200ResponseDataInner.from_dict(get_images200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


