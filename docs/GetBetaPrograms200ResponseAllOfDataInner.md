# GetBetaPrograms200ResponseAllOfDataInner

An object representing Beta Program information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Additional details regarding the Beta Program. | [optional] [readonly] 
**ended** | **datetime** | The date-time that the Beta Program ended.  &#x60;null&#x60; indicates that the Beta Program is ongoing. | [optional] [readonly] 
**greenlight_only** | **bool** | Whether the Beta Program requires [Green Light](https://www.linode.com/green-light/) participation for enrollment. | [optional] [readonly] 
**id** | **str** | The unique identifier of the Beta Program. | [optional] 
**label** | **str** | The name of the Beta Program. | [optional] [readonly] 
**more_info** | **str** | Additional source of information for the Beta Program. | [optional] [readonly] 
**started** | **datetime** | The start date-time of the Beta Program. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_beta_programs200_response_all_of_data_inner import GetBetaPrograms200ResponseAllOfDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetBetaPrograms200ResponseAllOfDataInner from a JSON string
get_beta_programs200_response_all_of_data_inner_instance = GetBetaPrograms200ResponseAllOfDataInner.from_json(json)
# print the JSON string representation of the object
print(GetBetaPrograms200ResponseAllOfDataInner.to_json())

# convert the object into a dict
get_beta_programs200_response_all_of_data_inner_dict = get_beta_programs200_response_all_of_data_inner_instance.to_dict()
# create an instance of GetBetaPrograms200ResponseAllOfDataInner from a dict
get_beta_programs200_response_all_of_data_inner_from_dict = GetBetaPrograms200ResponseAllOfDataInner.from_dict(get_beta_programs200_response_all_of_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


