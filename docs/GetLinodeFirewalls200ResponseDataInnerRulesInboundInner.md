# GetLinodeFirewalls200ResponseDataInnerRulesInboundInner

One of a Firewall's inbound or outbound access rules. The `ports` property can be used to allow traffic on a comma-separated list of different ports.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Controls whether traffic is accepted or dropped by this rule. Overrides the Firewall&#39;s &#x60;inbound_policy&#x60; if this is an inbound rule, or the &#x60;outbound_policy&#x60; if this is an outbound rule. | [optional] 
**addresses** | [**GetLinodeFirewalls200ResponseDataInnerRulesInboundInnerAddresses**](GetLinodeFirewalls200ResponseDataInnerRulesInboundInnerAddresses.md) |  | [optional] 
**description** | **str** | Used to describe this rule. For display purposes only. | [optional] 
**label** | **str** | Used to identify this rule. For display purposes only. | [optional] 
**ports** | **str** | A string representing the port or ports affected by this rule:  - The string may be a single port, a range of ports, or a comma-separated list of single ports and port ranges. A space is permitted following each comma. - A range of ports is inclusive of the start and end values for the range. The end value of the range must be greater than the start value. - Ports must be within 1 and 65535, and may not contain any leading zeroes. For example, port &#x60;080&#x60; is not allowed. - The ports string can have up to 15 _pieces_, where a single port is treated as one piece, and a port range is treated as two pieces. For example, the string \&quot;22-24, 80, 443\&quot; has four pieces. - If no ports are configured, all ports are affected. - Only allowed for the TCP and UDP protocols. Ports are not allowed for the ICMP and IPENCAP protocols. | [optional] 
**protocol** | **str** | The type of network traffic affected by this rule. | [optional] 

## Example

```python
from openapi_client.models.get_linode_firewalls200_response_data_inner_rules_inbound_inner import GetLinodeFirewalls200ResponseDataInnerRulesInboundInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLinodeFirewalls200ResponseDataInnerRulesInboundInner from a JSON string
get_linode_firewalls200_response_data_inner_rules_inbound_inner_instance = GetLinodeFirewalls200ResponseDataInnerRulesInboundInner.from_json(json)
# print the JSON string representation of the object
print(GetLinodeFirewalls200ResponseDataInnerRulesInboundInner.to_json())

# convert the object into a dict
get_linode_firewalls200_response_data_inner_rules_inbound_inner_dict = get_linode_firewalls200_response_data_inner_rules_inbound_inner_instance.to_dict()
# create an instance of GetLinodeFirewalls200ResponseDataInnerRulesInboundInner from a dict
get_linode_firewalls200_response_data_inner_rules_inbound_inner_from_dict = GetLinodeFirewalls200ResponseDataInnerRulesInboundInner.from_dict(get_linode_firewalls200_response_data_inner_rules_inbound_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


