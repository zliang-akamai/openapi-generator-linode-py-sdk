# PutLinodeConfigInterfaceRequest

Linode Configuration Interface Update request object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_ranges** | **List[str]** | An array of IPv4 CIDR VPC Subnet ranges that are routed to this Interface.  - Array items are only allowed for &#x60;vpc&#x60; type Interfaces. - This must be empty for non-&#x60;vpc&#x60; type Interfaces.  For requests:  - Addresses in submitted ranges must not already be actively assigned. - Submitting values replaces any existing values. - Submitting an empty array removes any existing values. - Omitting this property results in no change to existing values. | [optional] 
**ipv4** | [**PostLinodeInstanceRequestAllOfInterfacesInnerIpv4**](PostLinodeInstanceRequestAllOfInterfacesInnerIpv4.md) |  | [optional] 
**primary** | **bool** | The primary Interface is configured as the default route to the Linode.  Each Configuration Profile can have up to one &#x60;\&quot;primary\&quot;: true&#x60; Interface at a time.  Must be &#x60;false&#x60; for &#x60;vlan&#x60; type Interfaces.  If no Interface is configured as the primary, the first non-&#x60;vlan&#x60; type Interface in the &#x60;interfaces&#x60; array is automatically treated as the primary Interface. | [optional] 

## Example

```python
from openapi_client.models.put_linode_config_interface_request import PutLinodeConfigInterfaceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutLinodeConfigInterfaceRequest from a JSON string
put_linode_config_interface_request_instance = PutLinodeConfigInterfaceRequest.from_json(json)
# print the JSON string representation of the object
print(PutLinodeConfigInterfaceRequest.to_json())

# convert the object into a dict
put_linode_config_interface_request_dict = put_linode_config_interface_request_instance.to_dict()
# create an instance of PutLinodeConfigInterfaceRequest from a dict
put_linode_config_interface_request_from_dict = PutLinodeConfigInterfaceRequest.from_dict(put_linode_config_interface_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


