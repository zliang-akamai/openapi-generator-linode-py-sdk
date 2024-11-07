# PutLongviewPlanRequest

Longview Plan object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**longview_subscription** | **str** | The subscription ID for a particular Longview plan. A value of &#x60;null&#x60; corresponds to Longview Free. You can send a request to the [List Longview subscriptions](https://techdocs.akamai.com/linode-api/reference/get-longview-subscriptions) operation to receive the details of each plan. | [optional] 

## Example

```python
from openapi_client.models.put_longview_plan_request import PutLongviewPlanRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutLongviewPlanRequest from a JSON string
put_longview_plan_request_instance = PutLongviewPlanRequest.from_json(json)
# print the JSON string representation of the object
print(PutLongviewPlanRequest.to_json())

# convert the object into a dict
put_longview_plan_request_dict = put_longview_plan_request_instance.to_dict()
# create an instance of PutLongviewPlanRequest from a dict
put_longview_plan_request_from_dict = PutLongviewPlanRequest.from_dict(put_longview_plan_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


