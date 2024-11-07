# PostFirewallsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | When this Firewall was created. | [optional] [readonly] 
**id** | **int** | The Firewall&#39;s unique ID. | [optional] [readonly] 
**label** | **str** | The Firewall&#39;s label, for display purposes only.  Firewall labels have the following constraints:    - Must begin and end with an alphanumeric character.   - May only consist of alphanumeric characters, hyphens (&#x60;-&#x60;), underscores (&#x60;_&#x60;) or periods (&#x60;.&#x60;).   - Cannot have two hyphens (&#x60;--&#x60;), underscores (&#x60;__&#x60;) or periods (&#x60;..&#x60;) in a row.   - Must be between 3 and 32 characters.   - Must be unique. | [optional] 
**rules** | [**PostFirewallsRequestAllOfRules**](PostFirewallsRequestAllOfRules.md) |  | 
**status** | **str** | The status of this Firewall.    - When a Firewall is first created its status is &#x60;enabled&#x60;.   - Run the [Update a firewall](https://techdocs.akamai.com/linode-api/reference/put-firewall) operation to set a Firewall&#39;s status to &#x60;enabled&#x60; or &#x60;disabled&#x60;.   - Run the [Delete a firewall](https://techdocs.akamai.com/linode-api/reference/delete-firewall) operation to delete a Firewall. | [optional] [readonly] 
**tags** | **List[str]** | An array of tags applied to this object. Tags are for organizational purposes only. | [optional] 
**updated** | **datetime** | When this Firewall was last updated. | [optional] [readonly] 
**devices** | [**PostFirewallsRequestAllOfDevices**](PostFirewallsRequestAllOfDevices.md) |  | [optional] 

## Example

```python
from openapi_client.models.post_firewalls_request import PostFirewallsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostFirewallsRequest from a JSON string
post_firewalls_request_instance = PostFirewallsRequest.from_json(json)
# print the JSON string representation of the object
print(PostFirewallsRequest.to_json())

# convert the object into a dict
post_firewalls_request_dict = post_firewalls_request_instance.to_dict()
# create an instance of PostFirewallsRequest from a dict
post_firewalls_request_from_dict = PostFirewallsRequest.from_dict(post_firewalls_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


