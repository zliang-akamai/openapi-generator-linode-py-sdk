# PostSecurityQuestionsRequest

Security questions and responses object for POST operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**security_questions** | [**List[PostSecurityQuestionsRequestSecurityQuestionsInner]**](PostSecurityQuestionsRequestSecurityQuestionsInner.md) | Security questions and response objects. | [optional] 

## Example

```python
from openapi_client.models.post_security_questions_request import PostSecurityQuestionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSecurityQuestionsRequest from a JSON string
post_security_questions_request_instance = PostSecurityQuestionsRequest.from_json(json)
# print the JSON string representation of the object
print(PostSecurityQuestionsRequest.to_json())

# convert the object into a dict
post_security_questions_request_dict = post_security_questions_request_instance.to_dict()
# create an instance of PostSecurityQuestionsRequest from a dict
post_security_questions_request_from_dict = PostSecurityQuestionsRequest.from_dict(post_security_questions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


