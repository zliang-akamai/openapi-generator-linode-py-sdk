# GetManagedLinodeSettings200ResponseDataInnerSsh

The SSH settings for this Linode.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | **bool** | If true, Linode special forces may access this Linode over ssh to respond to Issues. | [optional] [default to True]
**ip** | **str** | The IP Linode special forces should use to access this Linode when responding to an Issue.  By default, any of a Linode&#39;s IP addresses can be used for incident response access. | [optional] [default to 'any']
**port** | **int** | The port Linode special forces should use to access this Linode over ssh to respond to an Issue.  The default &#x60;null&#x60; value corresponds to port 22. | [optional] 
**user** | **str** | The specific user, if any, Linode&#39;s special forces should use when accessing this Linode to respond to an issue.  The default &#x60;null&#x60; value corresponds to the root user. | [optional] 

## Example

```python
from openapi_client.models.get_managed_linode_settings200_response_data_inner_ssh import GetManagedLinodeSettings200ResponseDataInnerSsh

# TODO update the JSON string below
json = "{}"
# create an instance of GetManagedLinodeSettings200ResponseDataInnerSsh from a JSON string
get_managed_linode_settings200_response_data_inner_ssh_instance = GetManagedLinodeSettings200ResponseDataInnerSsh.from_json(json)
# print the JSON string representation of the object
print(GetManagedLinodeSettings200ResponseDataInnerSsh.to_json())

# convert the object into a dict
get_managed_linode_settings200_response_data_inner_ssh_dict = get_managed_linode_settings200_response_data_inner_ssh_instance.to_dict()
# create an instance of GetManagedLinodeSettings200ResponseDataInnerSsh from a dict
get_managed_linode_settings200_response_data_inner_ssh_from_dict = GetManagedLinodeSettings200ResponseDataInnerSsh.from_dict(get_managed_linode_settings200_response_data_inner_ssh_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


