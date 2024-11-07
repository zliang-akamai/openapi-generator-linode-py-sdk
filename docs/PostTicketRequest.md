# PostTicketRequest

An object representing a created Support Ticket - a question or issue and request for help from the Linode support team. Only one of the ID attributes (`linode_id`, `domain_id`, etc.) can be set on a single Support Ticket.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database_id** | **int** | The ID of the Managed Database this ticket is regarding, if relevant. | [optional] 
**description** | **str** | The full details of the issue or question. | 
**domain_id** | **int** | The ID of the Domain this ticket is regarding, if relevant. | [optional] 
**firewall_id** | **int** | The ID of the Firewall this ticket is regarding, if relevant. | [optional] 
**linode_id** | **int** | The ID of the Linode this ticket is regarding, if relevant. | [optional] 
**lkecluster_id** | **int** | The ID of the Kubernetes cluster this ticket is regarding, if relevant. | [optional] 
**longviewclient_id** | **int** | The ID of the Longview client this ticket is regarding, if relevant. | [optional] 
**managed_issue** | **bool** | Designates if this ticket is related to a [Managed service](https://www.linode.com/products/managed/). If &#x60;true&#x60;, the following constraints will apply:  - No ID attributes (i.e. &#x60;linode_id&#x60;, &#x60;domain_id&#x60;, etc.) should be provided with this request. - Your account must have a managed service [enabled](https://techdocs.akamai.com/linode-api/reference/post-enable-managed-service). | [optional] 
**nodebalancer_id** | **int** | The ID of the NodeBalancer this ticket is regarding, if relevant. | [optional] 
**region** | **str** | The [Region](https://techdocs.akamai.com/linode-api/reference/get-regions) ID for the associated VLAN this ticket is regarding.  Only allowed when submitting a VLAN ticket. | [optional] 
**summary** | **str** | The summary or title for this SupportTicket. | 
**vlan** | **str** | The label of the VLAN this ticket is regarding, if relevant. To view your VLANs, run the [List VLANs](https://techdocs.akamai.com/linode-api/reference/get-vlans)) operation.  Requires a specified &#x60;region&#x60; to identify the VLAN. | [optional] 
**volume_id** | **int** | The ID of the Volume this ticket is regarding, if relevant. | [optional] 
**vpc_id** | **int** | The ID of the VPC this ticket is regarding, if relevant. | [optional] 

## Example

```python
from openapi_client.models.post_ticket_request import PostTicketRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostTicketRequest from a JSON string
post_ticket_request_instance = PostTicketRequest.from_json(json)
# print the JSON string representation of the object
print(PostTicketRequest.to_json())

# convert the object into a dict
post_ticket_request_dict = post_ticket_request_instance.to_dict()
# create an instance of PostTicketRequest from a dict
post_ticket_request_from_dict = PostTicketRequest.from_dict(post_ticket_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


