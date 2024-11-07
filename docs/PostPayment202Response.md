# PostPayment202Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**warnings** | [**List[PostPayment202ResponseWarningsInner]**](PostPayment202ResponseWarningsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.post_payment202_response import PostPayment202Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostPayment202Response from a JSON string
post_payment202_response_instance = PostPayment202Response.from_json(json)
# print the JSON string representation of the object
print(PostPayment202Response.to_json())

# convert the object into a dict
post_payment202_response_dict = post_payment202_response_instance.to_dict()
# create an instance of PostPayment202Response from a dict
post_payment202_response_from_dict = PostPayment202Response.from_dict(post_payment202_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


