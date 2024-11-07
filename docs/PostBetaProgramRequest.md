# PostBetaProgramRequest

The Beta Program ID to enroll in for your Account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the Beta Program. | 

## Example

```python
from openapi_client.models.post_beta_program_request import PostBetaProgramRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostBetaProgramRequest from a JSON string
post_beta_program_request_instance = PostBetaProgramRequest.from_json(json)
# print the JSON string representation of the object
print(PostBetaProgramRequest.to_json())

# convert the object into a dict
post_beta_program_request_dict = post_beta_program_request_instance.to_dict()
# create an instance of PostBetaProgramRequest from a dict
post_beta_program_request_from_dict = PostBetaProgramRequest.from_dict(post_beta_program_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


