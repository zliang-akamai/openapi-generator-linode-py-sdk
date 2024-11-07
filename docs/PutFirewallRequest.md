# PutFirewallRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The Firewall&#39;s label, for display purposes only.  Firewall labels have the following constraints:    - Must begin and end with an alphanumeric character.   - May only consist of alphanumeric characters, hyphens (&#x60;-&#x60;), underscores (&#x60;_&#x60;) or periods (&#x60;.&#x60;).   - Cannot have two hyphens (&#x60;--&#x60;), underscores (&#x60;__&#x60;) or periods (&#x60;..&#x60;) in a row.   - Must be between 3 and 32 characters.   - Must be unique. | [optional] 
**status** | **str** | The status to be applied to this Firewall.   - When a Firewall is first created its status is &#x60;enabled&#x60;.  - Run the [Delete a firewall](https://techdocs.akamai.com/linode-api/reference/delete-firewall) operation to delete a Firewall. | [optional] 
**tags** | **List[str]** | An array of tags applied to this object. Tags are for organizational purposes only. | [optional] 

## Example

```python
from openapi_client.models.put_firewall_request import PutFirewallRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutFirewallRequest from a JSON string
put_firewall_request_instance = PutFirewallRequest.from_json(json)
# print the JSON string representation of the object
print(PutFirewallRequest.to_json())

# convert the object into a dict
put_firewall_request_dict = put_firewall_request_instance.to_dict()
# create an instance of PutFirewallRequest from a dict
put_firewall_request_from_dict = PutFirewallRequest.from_dict(put_firewall_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


