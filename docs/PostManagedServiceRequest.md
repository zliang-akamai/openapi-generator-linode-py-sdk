# PostManagedServiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The URL at which this Service is monitored. URL parameters such as &#x60;?no-cache&#x3D;1&#x60; are preserved. URL fragments/anchors such as &#x60;#monitor&#x60; are __not__ preserved. | 
**body** | **str** | What to expect to find in the response body for the Service to be considered up. | [optional] 
**consultation_group** | **str** | The group of ManagedContacts who should be notified or consulted with when an Issue is detected. | [optional] 
**created** | **datetime** | When this Managed Service was created. | [optional] [readonly] 
**credentials** | **List[int]** | An array of ManagedCredential IDs that should be used when attempting to resolve issues with this Service. | [optional] 
**id** | **int** | This Service&#39;s unique ID. | [optional] [readonly] 
**label** | **str** | The label for this Service. This is for display purposes only. | 
**notes** | **str** | Any information relevant to the Service that Linode special forces should know when attempting to resolve Issues. | [optional] 
**region** | **str** | The Region in which this Service is located. This is required if address is a private IP, and may not be set otherwise. | [optional] 
**service_type** | **str** | How this Service is monitored. | 
**status** | **str** | The current status of this Service. | [optional] [readonly] 
**timeout** | **int** | How long to wait, in seconds, for a response before considering the Service to be down. | 
**updated** | **datetime** | When this Managed Service was last updated. | [optional] [readonly] 

## Example

```python
from openapi_client.models.post_managed_service_request import PostManagedServiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostManagedServiceRequest from a JSON string
post_managed_service_request_instance = PostManagedServiceRequest.from_json(json)
# print the JSON string representation of the object
print(PostManagedServiceRequest.to_json())

# convert the object into a dict
post_managed_service_request_dict = post_managed_service_request_instance.to_dict()
# create an instance of PostManagedServiceRequest from a dict
post_managed_service_request_from_dict = PostManagedServiceRequest.from_dict(post_managed_service_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


