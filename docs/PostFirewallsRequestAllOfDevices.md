# PostFirewallsRequestAllOfDevices

Devices to create for this Firewall. When a Device is created, the Firewall is assigned to its associated service. Currently, Devices can be created for Linode compute instances and NodeBalancers.  Additional devices can be assigned after Firewall creation by using the [Create a firewall device](https://techdocs.akamai.com/linode-api/reference/post-firewall-device) operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linodes** | **List[int]** | An array of Linode IDs. A Firewall Device is created for each ID. | [optional] 
**nodebalancers** | **List[int]** | An array containing a NodeBalancer ID. A Firewall Device is created for the ID.  - A NodeBalancer can have only one Firewall assigned to it. - Firewalls only apply to inbound TCP traffic to NodeBalancers. | [optional] 

## Example

```python
from openapi_client.models.post_firewalls_request_all_of_devices import PostFirewallsRequestAllOfDevices

# TODO update the JSON string below
json = "{}"
# create an instance of PostFirewallsRequestAllOfDevices from a JSON string
post_firewalls_request_all_of_devices_instance = PostFirewallsRequestAllOfDevices.from_json(json)
# print the JSON string representation of the object
print(PostFirewallsRequestAllOfDevices.to_json())

# convert the object into a dict
post_firewalls_request_all_of_devices_dict = post_firewalls_request_all_of_devices_instance.to_dict()
# create an instance of PostFirewallsRequestAllOfDevices from a dict
post_firewalls_request_all_of_devices_from_dict = PostFirewallsRequestAllOfDevices.from_dict(post_firewalls_request_all_of_devices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


