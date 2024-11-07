# PostAssignIpsRequest

Request object for IP Addresses Assign (POST /networking/ips/assign).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignments** | [**List[PostAssignIpsRequestAssignmentsInner]**](PostAssignIpsRequestAssignmentsInner.md) | The list of assignments to make. You must have read_write access to all IPs being assigned and all Linodes being assigned to in order for the assignments to succeed. | 
**region** | **str** | The ID of the Region in which these assignments are to take place. All IPs and Linodes must exist in this Region. | 

## Example

```python
from openapi_client.models.post_assign_ips_request import PostAssignIpsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostAssignIpsRequest from a JSON string
post_assign_ips_request_instance = PostAssignIpsRequest.from_json(json)
# print the JSON string representation of the object
print(PostAssignIpsRequest.to_json())

# convert the object into a dict
post_assign_ips_request_dict = post_assign_ips_request_instance.to_dict()
# create an instance of PostAssignIpsRequest from a dict
post_assign_ips_request_from_dict = PostAssignIpsRequest.from_dict(post_assign_ips_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


