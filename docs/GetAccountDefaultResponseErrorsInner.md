# GetAccountDefaultResponseErrorsInner

An object for describing a single error that occurred during the processing of a request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | The field in the request that caused this error. This may be a path, separated by periods in the case of nested fields. In some cases this may come back as &#x60;null&#x60; if the error is not specific to any single element of the request. | [optional] 
**reason** | **str** | What happened to cause this error. In most cases, this can be fixed immediately by changing the data you sent in the request, but in some cases you will be instructed to [Open a support ticket](https://techdocs.akamai.com/linode-api/reference/post-ticket) or perform some other action before you can complete the request successfully. | [optional] 

## Example

```python
from openapi_client.models.get_account_default_response_errors_inner import GetAccountDefaultResponseErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountDefaultResponseErrorsInner from a JSON string
get_account_default_response_errors_inner_instance = GetAccountDefaultResponseErrorsInner.from_json(json)
# print the JSON string representation of the object
print(GetAccountDefaultResponseErrorsInner.to_json())

# convert the object into a dict
get_account_default_response_errors_inner_dict = get_account_default_response_errors_inner_instance.to_dict()
# create an instance of GetAccountDefaultResponseErrorsInner from a dict
get_account_default_response_errors_inner_from_dict = GetAccountDefaultResponseErrorsInner.from_dict(get_account_default_response_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


