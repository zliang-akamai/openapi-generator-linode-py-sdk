# PostLinodeConfigInterfacesRequest

Linode Configuration Interfaces Order request object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** | An ordered array of existing Configuration Profile Interface &#x60;id&#x60;s.  - All current Interface &#x60;id&#x60;s must be present in the array. - If the Configuration Profile contains Interfaces and is active on the Linode, the Linode must first be shut down prior to running this operation. - Reordering takes effect after rebooting the Linode with this Configuration Profile.  The position in the array determines which of the Linode&#39;s network Interfaces is configured:  - First [0]:  eth0 - Second [1]: eth1 - Third [2]:  eth2 | 

## Example

```python
from openapi_client.models.post_linode_config_interfaces_request import PostLinodeConfigInterfacesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostLinodeConfigInterfacesRequest from a JSON string
post_linode_config_interfaces_request_instance = PostLinodeConfigInterfacesRequest.from_json(json)
# print the JSON string representation of the object
print(PostLinodeConfigInterfacesRequest.to_json())

# convert the object into a dict
post_linode_config_interfaces_request_dict = post_linode_config_interfaces_request_instance.to_dict()
# create an instance of PostLinodeConfigInterfacesRequest from a dict
post_linode_config_interfaces_request_from_dict = PostLinodeConfigInterfacesRequest.from_dict(post_linode_config_interfaces_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


