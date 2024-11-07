# GetDatabasesPostgreSqlInstances200ResponseAllOfDataInnerHosts

The primary and secondary hosts for the Managed Database. These are assigned after provisioning is complete.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary** | **str** | The primary host for the Managed Database. | [optional] 
**secondary** | **str** | The secondary/private network host for the Managed Database.  A private network host and a private IP can only be used to access a Database Cluster from Linodes in the same data center and will not incur transfer costs.  __Note__. The secondary hostname is publicly viewable and accessible. | [optional] 

## Example

```python
from openapi_client.models.get_databases_postgre_sql_instances200_response_all_of_data_inner_hosts import GetDatabasesPostgreSqlInstances200ResponseAllOfDataInnerHosts

# TODO update the JSON string below
json = "{}"
# create an instance of GetDatabasesPostgreSqlInstances200ResponseAllOfDataInnerHosts from a JSON string
get_databases_postgre_sql_instances200_response_all_of_data_inner_hosts_instance = GetDatabasesPostgreSqlInstances200ResponseAllOfDataInnerHosts.from_json(json)
# print the JSON string representation of the object
print(GetDatabasesPostgreSqlInstances200ResponseAllOfDataInnerHosts.to_json())

# convert the object into a dict
get_databases_postgre_sql_instances200_response_all_of_data_inner_hosts_dict = get_databases_postgre_sql_instances200_response_all_of_data_inner_hosts_instance.to_dict()
# create an instance of GetDatabasesPostgreSqlInstances200ResponseAllOfDataInnerHosts from a dict
get_databases_postgre_sql_instances200_response_all_of_data_inner_hosts_from_dict = GetDatabasesPostgreSqlInstances200ResponseAllOfDataInnerHosts.from_dict(get_databases_postgre_sql_instances200_response_all_of_data_inner_hosts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


