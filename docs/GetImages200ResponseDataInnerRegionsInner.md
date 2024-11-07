# GetImages200ResponseDataInnerRegionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region** | **str** | The unique identifier for the core compute region where this image is stored. | [optional] 
**status** | **str** | The status of the image in this &#x60;region&#x60;. Possible values are &#x60;available&#x60;, &#x60;creating&#x60;, &#x60;pending&#x60;, &#x60;pending deletion&#x60;, &#x60;pending replication&#x60;, or &#x60;replicating&#x60;. | [optional] 

## Example

```python
from openapi_client.models.get_images200_response_data_inner_regions_inner import GetImages200ResponseDataInnerRegionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetImages200ResponseDataInnerRegionsInner from a JSON string
get_images200_response_data_inner_regions_inner_instance = GetImages200ResponseDataInnerRegionsInner.from_json(json)
# print the JSON string representation of the object
print(GetImages200ResponseDataInnerRegionsInner.to_json())

# convert the object into a dict
get_images200_response_data_inner_regions_inner_dict = get_images200_response_data_inner_regions_inner_instance.to_dict()
# create an instance of GetImages200ResponseDataInnerRegionsInner from a dict
get_images200_response_data_inner_regions_inner_from_dict = GetImages200ResponseDataInnerRegionsInner.from_dict(get_images200_response_data_inner_regions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


