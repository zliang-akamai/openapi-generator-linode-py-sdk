# PutFirewallRulesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fingerprint** | **str** | The fingerprint is a 32-bit hash. It represents the firewall rules as an 8 character hex string. You can use &#x60;fingerprint&#x60; to compare rule versions. | [optional] [readonly] 
**inbound** | **object** |  | [optional] 
**inbound_policy** | **str** | The default behavior for inbound traffic. This setting can be overridden by [updating](https://techdocs.akamai.com/linode-api/reference/put-firewall-rules) the &#x60;inbound.action&#x60; property of the Firewall Rule. | [optional] 
**outbound** | **object** |  | [optional] 
**outbound_policy** | **str** | The default behavior for outbound traffic. This setting can be overridden by [updating](https://techdocs.akamai.com/linode-api/reference/put-firewall-rules) the &#x60;outbound.action&#x60; property of the Firewall Rule. | [optional] 
**version** | **int** | The firewall&#39;s rule version. The first version is &#x60;1&#x60;. The version number is incremented when the firewall&#39;s rules change. | [optional] [readonly] 

## Example

```python
from openapi_client.models.put_firewall_rules_request import PutFirewallRulesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutFirewallRulesRequest from a JSON string
put_firewall_rules_request_instance = PutFirewallRulesRequest.from_json(json)
# print the JSON string representation of the object
print(PutFirewallRulesRequest.to_json())

# convert the object into a dict
put_firewall_rules_request_dict = put_firewall_rules_request_instance.to_dict()
# create an instance of PutFirewallRulesRequest from a dict
put_firewall_rules_request_from_dict = PutFirewallRulesRequest.from_dict(put_firewall_rules_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


