# GetLinodeFirewalls200ResponseDataInnerRulesInboundInnerAddresses

The IPv4 and/or IPv6 addresses affected by this rule. A Rule can have up to 255 total addresses or networks listed across its IPv4 and IPv6 arrays. A network and a single IP are treated as equivalent when accounting for this limit.  Must contain `ipv4`, `ipv6`, or both.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv4** | **List[str]** | A list of IPv4 addresses or networks. Addresses must be in IP/mask format. Must not be an empty list.  If &#x60;0.0.0.0/0&#x60; is included in this list, all IPv4 addresses are affected by this rule. | [optional] 
**ipv6** | **List[str]** | A list of IPv6 addresses or networks. Addresses must be in IP/mask format and must not include zone_id notation as described in [RFC 4007](https://www.rfc-editor.org/rfc/rfc4007). Must not be an empty list.  If &#x60;::/0&#x60; is included in this list, all IPv6 addresses are affected by this rule. | [optional] 

## Example

```python
from openapi_client.models.get_linode_firewalls200_response_data_inner_rules_inbound_inner_addresses import GetLinodeFirewalls200ResponseDataInnerRulesInboundInnerAddresses

# TODO update the JSON string below
json = "{}"
# create an instance of GetLinodeFirewalls200ResponseDataInnerRulesInboundInnerAddresses from a JSON string
get_linode_firewalls200_response_data_inner_rules_inbound_inner_addresses_instance = GetLinodeFirewalls200ResponseDataInnerRulesInboundInnerAddresses.from_json(json)
# print the JSON string representation of the object
print(GetLinodeFirewalls200ResponseDataInnerRulesInboundInnerAddresses.to_json())

# convert the object into a dict
get_linode_firewalls200_response_data_inner_rules_inbound_inner_addresses_dict = get_linode_firewalls200_response_data_inner_rules_inbound_inner_addresses_instance.to_dict()
# create an instance of GetLinodeFirewalls200ResponseDataInnerRulesInboundInnerAddresses from a dict
get_linode_firewalls200_response_data_inner_rules_inbound_inner_addresses_from_dict = GetLinodeFirewalls200ResponseDataInnerRulesInboundInnerAddresses.from_dict(get_linode_firewalls200_response_data_inner_rules_inbound_inner_addresses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


