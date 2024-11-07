# GetSecurityQuestions200ResponseSecurityQuestionsInner

Single security question and response object for GET operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID representing the security question. | [optional] 
**question** | **str** | The security question. | [optional] [readonly] 
**response** | **str** | The security question response. | [optional] 

## Example

```python
from openapi_client.models.get_security_questions200_response_security_questions_inner import GetSecurityQuestions200ResponseSecurityQuestionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSecurityQuestions200ResponseSecurityQuestionsInner from a JSON string
get_security_questions200_response_security_questions_inner_instance = GetSecurityQuestions200ResponseSecurityQuestionsInner.from_json(json)
# print the JSON string representation of the object
print(GetSecurityQuestions200ResponseSecurityQuestionsInner.to_json())

# convert the object into a dict
get_security_questions200_response_security_questions_inner_dict = get_security_questions200_response_security_questions_inner_instance.to_dict()
# create an instance of GetSecurityQuestions200ResponseSecurityQuestionsInner from a dict
get_security_questions200_response_security_questions_inner_from_dict = GetSecurityQuestions200ResponseSecurityQuestionsInner.from_dict(get_security_questions200_response_security_questions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


