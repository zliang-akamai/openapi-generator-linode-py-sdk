# GetSecurityQuestions200Response

Security questions and responses object for GET operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**security_questions** | [**List[GetSecurityQuestions200ResponseSecurityQuestionsInner]**](GetSecurityQuestions200ResponseSecurityQuestionsInner.md) | Security questions and response objects. | [optional] 

## Example

```python
from openapi_client.models.get_security_questions200_response import GetSecurityQuestions200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSecurityQuestions200Response from a JSON string
get_security_questions200_response_instance = GetSecurityQuestions200Response.from_json(json)
# print the JSON string representation of the object
print(GetSecurityQuestions200Response.to_json())

# convert the object into a dict
get_security_questions200_response_dict = get_security_questions200_response_instance.to_dict()
# create an instance of GetSecurityQuestions200Response from a dict
get_security_questions200_response_from_dict = GetSecurityQuestions200Response.from_dict(get_security_questions200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


