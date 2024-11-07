# PostGroupAddLinodeRequest

The compute instances included in a placement group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linodes** | **List[int]** | The &#x60;linodeId&#x60; values for individual compute instances included in the placement group. | [optional] 

## Example

```python
from openapi_client.models.post_group_add_linode_request import PostGroupAddLinodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostGroupAddLinodeRequest from a JSON string
post_group_add_linode_request_instance = PostGroupAddLinodeRequest.from_json(json)
# print the JSON string representation of the object
print(PostGroupAddLinodeRequest.to_json())

# convert the object into a dict
post_group_add_linode_request_dict = post_group_add_linode_request_instance.to_dict()
# create an instance of PostGroupAddLinodeRequest from a dict
post_group_add_linode_request_from_dict = PostGroupAddLinodeRequest.from_dict(post_group_add_linode_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


