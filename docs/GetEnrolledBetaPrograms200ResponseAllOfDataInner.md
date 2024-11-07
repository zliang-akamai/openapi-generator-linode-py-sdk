# GetEnrolledBetaPrograms200ResponseAllOfDataInner

An object representing an enrolled Beta Program for the Account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Additional details regarding the Beta Program. | [optional] [readonly] 
**ended** | **datetime** | The date-time that the Beta Program ended.  &#x60;null&#x60; indicates that the Beta Program is ongoing. | [optional] [readonly] 
**enrolled** | **datetime** | The date-time of Account enrollment to the Beta Program. | [optional] [readonly] 
**id** | **str** | The unique identifier of the Beta Program. | [optional] 
**label** | **str** | The name of the Beta Program. | [optional] [readonly] 
**started** | **datetime** | The start date-time of the Beta Program. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_enrolled_beta_programs200_response_all_of_data_inner import GetEnrolledBetaPrograms200ResponseAllOfDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetEnrolledBetaPrograms200ResponseAllOfDataInner from a JSON string
get_enrolled_beta_programs200_response_all_of_data_inner_instance = GetEnrolledBetaPrograms200ResponseAllOfDataInner.from_json(json)
# print the JSON string representation of the object
print(GetEnrolledBetaPrograms200ResponseAllOfDataInner.to_json())

# convert the object into a dict
get_enrolled_beta_programs200_response_all_of_data_inner_dict = get_enrolled_beta_programs200_response_all_of_data_inner_instance.to_dict()
# create an instance of GetEnrolledBetaPrograms200ResponseAllOfDataInner from a dict
get_enrolled_beta_programs200_response_all_of_data_inner_from_dict = GetEnrolledBetaPrograms200ResponseAllOfDataInner.from_dict(get_enrolled_beta_programs200_response_all_of_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


