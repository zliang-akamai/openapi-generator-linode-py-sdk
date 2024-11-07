# ProxyUserToken

The token generated manually for a child account so its proxy user can access the API and CLI without going through an OAuth login.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | The date and time this token was created. | [optional] [readonly] 
**expiry** | **datetime** | When this token expires. This is default set to 15 minutes from the time of creation. Proxy user tokens can&#39;t be renewed. After this time, Akamai revokes the token and you need to generate a new one. | [optional] [readonly] 
**id** | **int** | The proxy user token&#39;s unique ID, which can be used to revoke it. | [optional] [readonly] 
**label** | **str** | The name of the token. The API automatically sets this to &#x60;&lt;username&gt;_&lt;uid&gt;_&lt;time&gt;&#x60;. It&#39;s composed of the &#x60;username&#x60; for your parent account user, the unique &#x60;uid&#x60; Akamai assigned to identify your user, and the &#x60;time&#x60; the API generated the token. This is for display purposes only, but you can use it to help track how you&#39;re using each proxy user token. | [optional] 
**scopes** | **str** | The scopes this token was created with. Defaults to &#x60;*&#x60;. Proxy user tokens automatically inherit all the permissions of the proxy user. | [optional] [readonly] 
**token** | **str** | The proxy user token that can be used to access the API and CLI. After you [create](https://techdocs.akamai.com/linode-api/reference/post-child-account-token) a token, you can see the full token in the response. All other operations that contain this token only show the first 16 characters in their response. | [optional] [readonly] 

## Example

```python
from openapi_client.models.proxy_user_token import ProxyUserToken

# TODO update the JSON string below
json = "{}"
# create an instance of ProxyUserToken from a JSON string
proxy_user_token_instance = ProxyUserToken.from_json(json)
# print the JSON string representation of the object
print(ProxyUserToken.to_json())

# convert the object into a dict
proxy_user_token_dict = proxy_user_token_instance.to_dict()
# create an instance of ProxyUserToken from a dict
proxy_user_token_from_dict = ProxyUserToken.from_dict(proxy_user_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


