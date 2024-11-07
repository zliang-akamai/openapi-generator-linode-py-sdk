# GetManagedServices200ResponseDataInner

A service that Linode is monitoring as part of your Managed services. If issues are detected with this service, a ManagedIssue will be opened and, optionally, Linode special forces will attempt to resolve the Issue.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The URL at which this Service is monitored. URL parameters such as &#x60;?no-cache&#x3D;1&#x60; are preserved. URL fragments/anchors such as &#x60;#monitor&#x60; are __not__ preserved. | [optional] 
**body** | **str** | What to expect to find in the response body for the Service to be considered up. | [optional] 
**consultation_group** | **str** | The group of ManagedContacts who should be notified or consulted with when an Issue is detected. | [optional] 
**created** | **datetime** | When this Managed Service was created. | [optional] [readonly] 
**credentials** | **List[int]** | An array of ManagedCredential IDs that should be used when attempting to resolve issues with this Service. | [optional] 
**id** | **int** | This Service&#39;s unique ID. | [optional] [readonly] 
**label** | **str** | The label for this Service. This is for display purposes only. | [optional] 
**notes** | **str** | Any information relevant to the Service that Linode special forces should know when attempting to resolve Issues. | [optional] 
**region** | **str** | The Region in which this Service is located. This is required if address is a private IP, and may not be set otherwise. | [optional] 
**service_type** | **str** | How this Service is monitored. | [optional] 
**status** | **str** | The current status of this Service. | [optional] [readonly] 
**timeout** | **int** | How long to wait, in seconds, for a response before considering the Service to be down. | [optional] 
**updated** | **datetime** | When this Managed Service was last updated. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_managed_services200_response_data_inner import GetManagedServices200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetManagedServices200ResponseDataInner from a JSON string
get_managed_services200_response_data_inner_instance = GetManagedServices200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetManagedServices200ResponseDataInner.to_json())

# convert the object into a dict
get_managed_services200_response_data_inner_dict = get_managed_services200_response_data_inner_instance.to_dict()
# create an instance of GetManagedServices200ResponseDataInner from a dict
get_managed_services200_response_data_inner_from_dict = GetManagedServices200ResponseDataInner.from_dict(get_managed_services200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


