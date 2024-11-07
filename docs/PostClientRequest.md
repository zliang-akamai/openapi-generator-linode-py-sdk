# PostClientRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The OAuth Client ID.  This is used to identify the client, and is a publicly known value (it is not a secret). | [optional] [readonly] 
**label** | **str** | The name of this application.  This will be presented to users when they are asked to grant it access to their Account. | 
**public** | **bool** | If this is a public or private OAuth Client.  Public clients have a slightly different authentication workflow than private clients.  See the [OAuth spec](https://oauth.net/2/) for more details. | [optional] [default to False]
**redirect_uri** | **str** | The location a successful log in from [login.linode.com](https://login.linode.com) should be redirected to for this client.  The receiver of this redirect should be ready to accept an OAuth exchange code and finish the OAuth exchange. | 
**secret** | **str** | The OAuth Client secret, used in the OAuth exchange.  This is returned as &#x60;&lt;REDACTED&gt;&#x60; except when an OAuth Client is created or its secret is reset.  This is a secret, and should not be shared or disclosed publicly. | [optional] [readonly] 
**status** | **str** | The status of this application.  &#x60;active&#x60; by default. | [optional] [readonly] 
**thumbnail_url** | **str** | The URL where this client&#39;s thumbnail may be viewed, or &#x60;null&#x60; if this client does not have a thumbnail set. | [optional] [readonly] 

## Example

```python
from openapi_client.models.post_client_request import PostClientRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostClientRequest from a JSON string
post_client_request_instance = PostClientRequest.from_json(json)
# print the JSON string representation of the object
print(PostClientRequest.to_json())

# convert the object into a dict
post_client_request_dict = post_client_request_instance.to_dict()
# create an instance of PostClientRequest from a dict
post_client_request_from_dict = PostClientRequest.from_dict(post_client_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


