# GetLinodeFirewalls200ResponseDataInnerRules

The inbound and outbound access rules to apply to the Firewall.  A Firewall may have up to 25 rules across its inbound and outbound rulesets.  Multiple rules are applied in order. If two rules conflict, the first rule takes precedence. For example, if the first rule accepts inbound traffic from an address, and the second rule drops inbound traffic the same address, the first rule applies and inbound traffic from that address is accepted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fingerprint** | **str** | The fingerprint is a 32-bit hash. It represents the firewall rules as an 8 character hex string. You can use &#x60;fingerprint&#x60; to compare rule versions. | [optional] [readonly] 
**inbound** | [**List[GetLinodeFirewalls200ResponseDataInnerRulesInboundInner]**](GetLinodeFirewalls200ResponseDataInnerRulesInboundInner.md) | The inbound rules for the firewall, as a JSON array. | [optional] 
**inbound_policy** | **str** | The default behavior for inbound traffic. This setting can be overridden by [updating](https://techdocs.akamai.com/linode-api/reference/put-firewall-rules) the &#x60;inbound.action&#x60; property of the Firewall Rule. | [optional] 
**outbound** | [**List[GetLinodeFirewalls200ResponseDataInnerRulesInboundInner]**](GetLinodeFirewalls200ResponseDataInnerRulesInboundInner.md) | The outbound rules for the firewall, as a JSON array. | [optional] 
**outbound_policy** | **str** | The default behavior for outbound traffic. This setting can be overridden by [updating](https://techdocs.akamai.com/linode-api/reference/put-firewall-rules) the &#x60;outbound.action&#x60; property of the Firewall Rule. | [optional] 
**version** | **int** | The firewall&#39;s rule version. The first version is &#x60;1&#x60;. The version number is incremented when the firewall&#39;s rules change. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_linode_firewalls200_response_data_inner_rules import GetLinodeFirewalls200ResponseDataInnerRules

# TODO update the JSON string below
json = "{}"
# create an instance of GetLinodeFirewalls200ResponseDataInnerRules from a JSON string
get_linode_firewalls200_response_data_inner_rules_instance = GetLinodeFirewalls200ResponseDataInnerRules.from_json(json)
# print the JSON string representation of the object
print(GetLinodeFirewalls200ResponseDataInnerRules.to_json())

# convert the object into a dict
get_linode_firewalls200_response_data_inner_rules_dict = get_linode_firewalls200_response_data_inner_rules_instance.to_dict()
# create an instance of GetLinodeFirewalls200ResponseDataInnerRules from a dict
get_linode_firewalls200_response_data_inner_rules_from_dict = GetLinodeFirewalls200ResponseDataInnerRules.from_dict(get_linode_firewalls200_response_data_inner_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


