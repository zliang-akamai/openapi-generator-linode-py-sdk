# GetDatabasesPostgreSqlInstances200ResponseAllOfDataInner

Managed PostgreSQL Databases object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_list** | **List[str]** | A list of IP addresses that can access the Managed Database. Each item can be a single IP address or a range in CIDR format.  By default, this is an empty array (&#x60;[]&#x60;), which blocks all connections (both public and private) to the Managed Database.  If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database. | [optional] 
**cluster_size** | **int** | The number of Linode Instance nodes deployed to the Managed Database.  Choosing 3 nodes creates a high availability cluster consisting of 1 primary node and 2 replica nodes. | [optional] [default to 1]
**created** | **datetime** | When this Managed Database was created. | [optional] [readonly] 
**encrypted** | **bool** | Whether the Managed Databases is encrypted. | [optional] [default to False]
**engine** | **str** | The Managed Database engine type. | [optional] [readonly] 
**hosts** | [**GetDatabasesPostgreSqlInstances200ResponseAllOfDataInnerHosts**](GetDatabasesPostgreSqlInstances200ResponseAllOfDataInnerHosts.md) |  | [optional] 
**id** | **int** | A unique ID that can be used to identify and reference the Managed Database. | [optional] [readonly] 
**label** | **str** | A unique, user-defined string referring to the Managed Database. | [optional] 
**port** | **int** | The access port for this Managed Database. | [optional] 
**region** | **str** | The [Region](https://techdocs.akamai.com/linode-api/reference/get-regions) ID for the Managed Database. | [optional] 
**replication_commit_type** | **str** | The synchronization level of the replicating server.  Must be &#x60;local&#x60; or &#x60;off&#x60; for the &#x60;asynch&#x60; replication type. | [optional] [default to 'local']
**replication_type** | **str** | The replication method used for the Managed Database.  Defaults to &#x60;none&#x60; for a single cluster and &#x60;asynch&#x60; for a high availability cluster.  Must be &#x60;none&#x60; for a single node cluster.  Must be &#x60;asynch&#x60; for a high availability cluster. | [optional] 
**ssl_connection** | **bool** | Whether to require SSL credentials to establish a connection to the Managed Database.  Run the [Get managed PostgreSQL database credentials](https://techdocs.akamai.com/linode-api/reference/get-databases-postgre-sql-instance-credentials) operation for access information. | [optional] [default to True]
**status** | **str** | The operating status of the Managed Database. | [optional] [readonly] 
**total_disk_size_gb** | **int** | The total disk size of the database in GB. | [optional] 
**type** | **str** | The Linode Instance type used by the Managed Database for its nodes. | [optional] 
**updated** | **datetime** | When this Managed Database was last updated. | [optional] [readonly] 
**updates** | [**GetDatabasesInstances200ResponseAllOfDataInnerUpdates**](GetDatabasesInstances200ResponseAllOfDataInnerUpdates.md) |  | [optional] 
**used_disk_size_gb** | **int** | The used space of the database in GB. | [optional] 
**version** | **str** | The Managed Database engine version. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_databases_postgre_sql_instances200_response_all_of_data_inner import GetDatabasesPostgreSqlInstances200ResponseAllOfDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetDatabasesPostgreSqlInstances200ResponseAllOfDataInner from a JSON string
get_databases_postgre_sql_instances200_response_all_of_data_inner_instance = GetDatabasesPostgreSqlInstances200ResponseAllOfDataInner.from_json(json)
# print the JSON string representation of the object
print(GetDatabasesPostgreSqlInstances200ResponseAllOfDataInner.to_json())

# convert the object into a dict
get_databases_postgre_sql_instances200_response_all_of_data_inner_dict = get_databases_postgre_sql_instances200_response_all_of_data_inner_instance.to_dict()
# create an instance of GetDatabasesPostgreSqlInstances200ResponseAllOfDataInner from a dict
get_databases_postgre_sql_instances200_response_all_of_data_inner_from_dict = GetDatabasesPostgreSqlInstances200ResponseAllOfDataInner.from_dict(get_databases_postgre_sql_instances200_response_all_of_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


