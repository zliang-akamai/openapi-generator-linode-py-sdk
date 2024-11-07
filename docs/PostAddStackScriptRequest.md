# PostAddStackScriptRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | The date this StackScript was created. | [optional] [readonly] 
**deployments_active** | **int** | Count of currently active, deployed Linodes created from this StackScript. | [optional] [readonly] 
**deployments_total** | **int** | The total number of times this StackScript has been deployed. | [optional] [readonly] 
**description** | **str** | A description for the StackScript. | [optional] 
**id** | **int** | The unique ID of this StackScript. | [optional] [readonly] 
**images** | **List[str]** | An array of Image IDs. These are the Images that can be deployed with this StackScript.  &#x60;any/all&#x60; indicates that all available Images, including private Images, are accepted. | 
**is_public** | **bool** | This determines whether other users can use your StackScript. __Once a StackScript is made public, it cannot be made private.__ | [optional] 
**label** | **str** | The StackScript&#39;s label is for display purposes only. | 
**mine** | **bool** | Returns &#x60;true&#x60; if this StackScript is owned by the account of the user making the request, and the user making the request is unrestricted or has access to this StackScript. | [optional] [readonly] 
**rev_note** | **str** | This field allows you to add notes for the set of revisions made to this StackScript. | [optional] 
**script** | **str** | The script to execute when provisioning a new Linode with this StackScript. | 
**updated** | **datetime** | The date this StackScript was last updated. | [optional] [readonly] 
**user_defined_fields** | [**List[GetStackScripts200ResponseDataInnerUserDefinedFieldsInner]**](GetStackScripts200ResponseDataInnerUserDefinedFieldsInner.md) | This is a list of fields defined with a special syntax inside this StackScript that allow for supplying customized parameters during deployment. See [Declare User-Defined Fields (UDFs)](https://www.linode.com/docs/products/tools/stackscripts/guides/write-a-custom-script/#declare-user-defined-fields-udfs) for more information. | [optional] [readonly] 
**user_gravatar_id** | **str** | The Gravatar ID for the User who created the StackScript. | [optional] [readonly] 
**username** | **str** | The User who created the StackScript. | [optional] [readonly] 

## Example

```python
from openapi_client.models.post_add_stack_script_request import PostAddStackScriptRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostAddStackScriptRequest from a JSON string
post_add_stack_script_request_instance = PostAddStackScriptRequest.from_json(json)
# print the JSON string representation of the object
print(PostAddStackScriptRequest.to_json())

# convert the object into a dict
post_add_stack_script_request_dict = post_add_stack_script_request_instance.to_dict()
# create an instance of PostAddStackScriptRequest from a dict
post_add_stack_script_request_from_dict = PostAddStackScriptRequest.from_dict(post_add_stack_script_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


