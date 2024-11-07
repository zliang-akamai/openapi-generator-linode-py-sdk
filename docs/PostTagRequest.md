# PostTagRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | **List[int]** | A list of Domain IDs to apply the new Tag to.  You must be allowed to &#x60;read_write&#x60; all of the requested Domains, or the Tag will not be created and an error will be returned. | [optional] 
**label** | **str** | The new Tag. | 
**linodes** | **List[int]** | A list of Linode IDs to apply the new Tag to.  You must be allowed to &#x60;read_write&#x60; all of the requested Linodes, or the Tag will not be created and an error will be returned. | [optional] 
**nodebalancers** | **List[int]** | A list of NodeBalancer IDs to apply the new Tag to. You must be allowed to &#x60;read_write&#x60; all of the requested NodeBalancers, or the Tag will not be created and an error will be returned. | [optional] 
**volumes** | **List[int]** | A list of Volume IDs to apply the new Tag to.  You must be allowed to &#x60;read_write&#x60; all of the requested Volumes, or the Tag will not be created and an error will be returned. | [optional] 

## Example

```python
from openapi_client.models.post_tag_request import PostTagRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostTagRequest from a JSON string
post_tag_request_instance = PostTagRequest.from_json(json)
# print the JSON string representation of the object
print(PostTagRequest.to_json())

# convert the object into a dict
post_tag_request_dict = post_tag_request_instance.to_dict()
# create an instance of PostTagRequest from a dict
post_tag_request_from_dict = PostTagRequest.from_dict(post_tag_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


