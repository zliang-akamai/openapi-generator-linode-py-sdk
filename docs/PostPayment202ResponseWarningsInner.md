# PostPayment202ResponseWarningsInner

An object for describing a single warning associated with a response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | **str** | Specific information related to the warning. | [optional] 
**title** | **str** | The general warning message. | [optional] 

## Example

```python
from openapi_client.models.post_payment202_response_warnings_inner import PostPayment202ResponseWarningsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostPayment202ResponseWarningsInner from a JSON string
post_payment202_response_warnings_inner_instance = PostPayment202ResponseWarningsInner.from_json(json)
# print the JSON string representation of the object
print(PostPayment202ResponseWarningsInner.to_json())

# convert the object into a dict
post_payment202_response_warnings_inner_dict = post_payment202_response_warnings_inner_instance.to_dict()
# create an instance of PostPayment202ResponseWarningsInner from a dict
post_payment202_response_warnings_inner_from_dict = PostPayment202ResponseWarningsInner.from_dict(post_payment202_response_warnings_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


