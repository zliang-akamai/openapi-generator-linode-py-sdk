# Linode1PlacementGroup

Details on the [placement group](https://www.linode.com/docs/products/compute/compute-instances/guides/placement-groups/) that this Linode belongs to. Empty if the Linode isn't in a placement group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The placement group&#39;s ID. You need to provide it for all operations that affect it. | [optional] 
**label** | **str** | The unique name set for the placement group. A label has these constraints:  - It needs to begin and end with an alphanumeric character. - It can only consist of alphanumeric characters, hyphens (&#x60;-&#x60;), underscores (&#x60;_&#x60;) or periods (&#x60;.&#x60;). | [optional] 
**placement_group_policy** | **str** | How requests to add future compute instances to your placement group are handled, and whether it remains compliant:  - &#x60;strict&#x60;. Don&#39;t assign a new compute instance if it breaks the grouped-together or spread-apart model set by the &#x60;placement_group_type&#x60;. Use this to ensure the placement group stays compliant (&#x60;is_compliant: true&#x60;). - &#x60;flexible&#x60;. Assign a new compute instance, even if it breaks the grouped-together or spread-apart model set by the &#x60;placement_group_type&#x60;. This makes the group non-compliant (&#x60;is_compliant: false&#x60;). You need to wait for Akamai to move the offending compute instance to make it compliant again, once the necessary capacity is available in the region. Offers flexibility to add future compute instances if compliance isn&#39;t an immediate concern.  &lt;&lt;LB&gt;&gt;  &gt; 📘 &gt; &gt; In rare cases, non-compliance can occur with a &#x60;strict&#x60; placement group if Akamai needs to failover or migrate your compute instances for maintenance. Fixing non-compliance for a &#x60;strict&#x60; placement group is prioritized over a &#x60;flexible&#x60; group. | [optional] 
**placement_group_type** | **str** | How compute instances are distributed in your placement group. A &#x60;placement_group_type&#x60; using anti-affinity (&#x60;anti-affinity:local&#x60;) places compute instances in separate hosts, but still in the same region. This best supports the spread-apart model for high availability. A &#x60;placement_group_type&#x60; using affinity places compute instances physically close together, possibly on the same host. This supports the grouped-together model for low-latency.  &gt; 📘 &gt; &gt; Currently, only &#x60;anti_affinity:local&#x60; is available for &#x60;placement_group_type&#x60;. | [optional] [readonly] 

## Example

```python
from openapi_client.models.linode1_placement_group import Linode1PlacementGroup

# TODO update the JSON string below
json = "{}"
# create an instance of Linode1PlacementGroup from a JSON string
linode1_placement_group_instance = Linode1PlacementGroup.from_json(json)
# print the JSON string representation of the object
print(Linode1PlacementGroup.to_json())

# convert the object into a dict
linode1_placement_group_dict = linode1_placement_group_instance.to_dict()
# create an instance of Linode1PlacementGroup from a dict
linode1_placement_group_from_dict = Linode1PlacementGroup.from_dict(linode1_placement_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


