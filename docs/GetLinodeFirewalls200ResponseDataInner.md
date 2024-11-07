# GetLinodeFirewalls200ResponseDataInner

A resource that controls incoming and outgoing network traffic to a compute service. Only one enabled Firewall can be attached to a particular service at any given time. [Create a firewall device](https://techdocs.akamai.com/linode-api/reference/post-firewall-device) to assign a Firewall to a service. Currently, Firewalls can assigned to Linode compute instances and NodeBalancers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | When this Firewall was created. | [optional] [readonly] 
**id** | **int** | The Firewall&#39;s unique ID. | [optional] [readonly] 
**label** | **str** | The Firewall&#39;s label, for display purposes only.  Firewall labels have the following constraints:    - Must begin and end with an alphanumeric character.   - May only consist of alphanumeric characters, hyphens (&#x60;-&#x60;), underscores (&#x60;_&#x60;) or periods (&#x60;.&#x60;).   - Cannot have two hyphens (&#x60;--&#x60;), underscores (&#x60;__&#x60;) or periods (&#x60;..&#x60;) in a row.   - Must be between 3 and 32 characters.   - Must be unique. | [optional] 
**rules** | [**GetLinodeFirewalls200ResponseDataInnerRules**](GetLinodeFirewalls200ResponseDataInnerRules.md) |  | [optional] 
**status** | **str** | The status of this Firewall.    - When a Firewall is first created its status is &#x60;enabled&#x60;.   - Run the [Update a firewall](https://techdocs.akamai.com/linode-api/reference/put-firewall) operation to set a Firewall&#39;s status to &#x60;enabled&#x60; or &#x60;disabled&#x60;.   - Run the [Delete a firewall](https://techdocs.akamai.com/linode-api/reference/delete-firewall) operation to delete a Firewall. | [optional] [readonly] 
**tags** | **List[str]** | An array of tags applied to this object. Tags are for organizational purposes only. | [optional] 
**updated** | **datetime** | When this Firewall was last updated. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_linode_firewalls200_response_data_inner import GetLinodeFirewalls200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLinodeFirewalls200ResponseDataInner from a JSON string
get_linode_firewalls200_response_data_inner_instance = GetLinodeFirewalls200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetLinodeFirewalls200ResponseDataInner.to_json())

# convert the object into a dict
get_linode_firewalls200_response_data_inner_dict = get_linode_firewalls200_response_data_inner_instance.to_dict()
# create an instance of GetLinodeFirewalls200ResponseDataInner from a dict
get_linode_firewalls200_response_data_inner_from_dict = GetLinodeFirewalls200ResponseDataInner.from_dict(get_linode_firewalls200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


