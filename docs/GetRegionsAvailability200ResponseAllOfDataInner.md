# GetRegionsAvailability200ResponseAllOfDataInner

Compute instance availability information by [Type](https://techdocs.akamai.com/linode-api/reference/get-linode-types) and [Region](https://techdocs.akamai.com/linode-api/reference/get-regions).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **bool** | Whether the compute instance type is available in the region. | [optional] 
**plan** | **str** | The compute instance [Type](https://techdocs.akamai.com/linode-api/reference/get-linode-types) ID. | [optional] 
**region** | **str** | The [Region](https://techdocs.akamai.com/linode-api/reference/get-regions) ID. | [optional] 

## Example

```python
from openapi_client.models.get_regions_availability200_response_all_of_data_inner import GetRegionsAvailability200ResponseAllOfDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetRegionsAvailability200ResponseAllOfDataInner from a JSON string
get_regions_availability200_response_all_of_data_inner_instance = GetRegionsAvailability200ResponseAllOfDataInner.from_json(json)
# print the JSON string representation of the object
print(GetRegionsAvailability200ResponseAllOfDataInner.to_json())

# convert the object into a dict
get_regions_availability200_response_all_of_data_inner_dict = get_regions_availability200_response_all_of_data_inner_instance.to_dict()
# create an instance of GetRegionsAvailability200ResponseAllOfDataInner from a dict
get_regions_availability200_response_all_of_data_inner_from_dict = GetRegionsAvailability200ResponseAllOfDataInner.from_dict(get_regions_availability200_response_all_of_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


