# PostPlacementGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | A unique name for the placement group. A placement group &#x60;label&#x60; has the following constraints:  - It needs to begin and end with an alphanumeric character. - It can only consist of alphanumeric characters, hyphens (&#x60;-&#x60;), underscores (&#x60;_&#x60;), or periods (&#x60;.&#x60;). | 
**placement_group_policy** | **str** | How requests to add future compute instances to your placement group are handled:  - &#x60;strict&#x60;. Don&#39;t add a compute instance if it breaks the grouped-together or spread-apart model set by your &#x60;placement_group_type&#x60;. For example, with &#x60;anti-affinity:local&#x60; as your &#x60;placement_group_type&#x60;, assume it already has three qualifying compute instances on separate hosts, to support the spread-apart model. If a fourth compute instance is assigned that&#39;s on the same host as one of the existing three, an error is thrown and the system won&#39;t add it. Ensures the placement group stays compliant with your selected model. - &#x60;flexible&#x60;. Add a new compute instance, even if it breaks the grouped-together or spread-apart model set by your &#x60;placement_group_type&#x60;. Breaking the model makes the placement group non-compliant. You need to wait for Akamai to move the offending compute instances to make the group compliant again, once the necessary capacity is available in the region. Offers flexibility to add future compute instances if compliance isn&#39;t an immediate concern.  &gt; 📘 &gt; &gt; Once you create a placement group, you can&#39;t change its &#x60;placement_group_policy&#x60; setting. | 
**placement_group_type** | **str** | How compute instances are distributed in your placement group. A &#x60;placement_group_type&#x60; using anti-affinity (&#x60;anti-affinity:local&#x60;) places compute instances in separate hosts, but still in the same region. This best supports the spread-apart model for high availability. A &#x60;placement_group_type&#x60; using affinity places compute instances physically close together, possibly on the same host. This supports the grouped-together model for low-latency.  &gt; 📘 &gt; &gt; Currently, only &#x60;anti_affinity:local&#x60; is available for &#x60;placement_group_type&#x60;. | 
**region** | **str** | The data center that houses the compute instances you want to add to your placement group. Run the [List Linodes](https://techdocs.akamai.com/linode-api/reference/get-linode-instances) operation to view your compute instances and store the &#x60;region&#x60; identifier. | 

## Example

```python
from openapi_client.models.post_placement_group_request import PostPlacementGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostPlacementGroupRequest from a JSON string
post_placement_group_request_instance = PostPlacementGroupRequest.from_json(json)
# print the JSON string representation of the object
print(PostPlacementGroupRequest.to_json())

# convert the object into a dict
post_placement_group_request_dict = post_placement_group_request_instance.to_dict()
# create an instance of PostPlacementGroupRequest from a dict
post_placement_group_request_from_dict = PostPlacementGroupRequest.from_dict(post_placement_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


