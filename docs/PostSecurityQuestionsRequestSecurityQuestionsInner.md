# PostSecurityQuestionsRequestSecurityQuestionsInner

Single security question and response object for POST operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question_id** | **int** | The ID representing the security question. | [optional] 
**response** | **str** | The security question response. | [optional] 
**security_question** | **str** | The security question. | [optional] [readonly] 

## Example

```python
from openapi_client.models.post_security_questions_request_security_questions_inner import PostSecurityQuestionsRequestSecurityQuestionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostSecurityQuestionsRequestSecurityQuestionsInner from a JSON string
post_security_questions_request_security_questions_inner_instance = PostSecurityQuestionsRequestSecurityQuestionsInner.from_json(json)
# print the JSON string representation of the object
print(PostSecurityQuestionsRequestSecurityQuestionsInner.to_json())

# convert the object into a dict
post_security_questions_request_security_questions_inner_dict = post_security_questions_request_security_questions_inner_instance.to_dict()
# create an instance of PostSecurityQuestionsRequestSecurityQuestionsInner from a dict
post_security_questions_request_security_questions_inner_from_dict = PostSecurityQuestionsRequestSecurityQuestionsInner.from_dict(post_security_questions_request_security_questions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


