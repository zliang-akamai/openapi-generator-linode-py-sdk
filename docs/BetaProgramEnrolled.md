# BetaProgramEnrolled

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
from openapi_client.models.beta_program_enrolled import BetaProgramEnrolled

# TODO update the JSON string below
json = "{}"
# create an instance of BetaProgramEnrolled from a JSON string
beta_program_enrolled_instance = BetaProgramEnrolled.from_json(json)
# print the JSON string representation of the object
print(BetaProgramEnrolled.to_json())

# convert the object into a dict
beta_program_enrolled_dict = beta_program_enrolled_instance.to_dict()
# create an instance of BetaProgramEnrolled from a dict
beta_program_enrolled_from_dict = BetaProgramEnrolled.from_dict(beta_program_enrolled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


