# PutDatabasesPostgreSqlInstanceRequest

Updated information for the Managed PostgreSQL Database.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_list** | **List[str]** | A list of IP addresses that can access the Managed Database. Each item can be a single IP address or a range in CIDR format.  By default, this is an empty array (&#x60;[]&#x60;), which blocks all connections (both public and private) to the Managed Database.  If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database. | [optional] 
**label** | **str** | A unique, user-defined string referring to the Managed Database. | [optional] 
**type** | **str** | Request re-sizing of your cluster to a Linode Type with more disk space. For example, you could request a Linode Type that uses a higher plan.  - Needs to be a Linode Type with more disk space than your current Linode.  - Resizing to a larger Linode Type can accrue additional cost. Review the &#x60;price&#x60; output from the [List types](https://techdocs.akamai.com/linode-api/reference/get-linode-types) operation for more information.  - You can&#39;t update the &#x60;allow_list&#x60; and set a new &#x60;type&#x60; in the same request.  - Any active updates to your cluster need to complete before you can request a resize. The reverse is also true: An active resizing needs to complete before you can perform any other update. | [optional] 
**updates** | [**GetDatabasesInstances200ResponseAllOfDataInnerUpdates**](GetDatabasesInstances200ResponseAllOfDataInnerUpdates.md) |  | [optional] 

## Example

```python
from openapi_client.models.put_databases_postgre_sql_instance_request import PutDatabasesPostgreSqlInstanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutDatabasesPostgreSqlInstanceRequest from a JSON string
put_databases_postgre_sql_instance_request_instance = PutDatabasesPostgreSqlInstanceRequest.from_json(json)
# print the JSON string representation of the object
print(PutDatabasesPostgreSqlInstanceRequest.to_json())

# convert the object into a dict
put_databases_postgre_sql_instance_request_dict = put_databases_postgre_sql_instance_request_instance.to_dict()
# create an instance of PutDatabasesPostgreSqlInstanceRequest from a dict
put_databases_postgre_sql_instance_request_from_dict = PutDatabasesPostgreSqlInstanceRequest.from_dict(put_databases_postgre_sql_instance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


