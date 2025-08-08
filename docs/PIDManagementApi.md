# pytypid_generated_client.PIDManagementApi

All URIs are relative to *http://typed-pid-maker.datamanager.kit.edu/preview*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pid**](PIDManagementApi.md#create_pid) | **POST** /api/v1/pit/pid/ | Create a new PID record
[**create_pids**](PIDManagementApi.md#create_pids) | **POST** /api/v1/pit/pids | Create a multiple, possibly related PID records
[**find_all**](PIDManagementApi.md#find_all) | **GET** /api/v1/pit/known-pid | Returns all known PIDs. Supports paging, filtering criteria, and different formats.
[**find_by_pid**](PIDManagementApi.md#find_by_pid) | **GET** /api/v1/pit/known-pid/** | Returns a PID and its timestamps from the local store, if available.
[**get_record**](PIDManagementApi.md#get_record) | **GET** /api/v1/pit/pid/** | Get the record of the given PID.
[**update_pid**](PIDManagementApi.md#update_pid) | **PUT** /api/v1/pit/pid/** | Update an existing PID record


# **create_pid**
> PIDRecord create_pid(pid_record, dryrun=dryrun)

Create a new PID record

Create a new PID record using the record information from the request body. The record may contain the identifier(s) of the matching profile(s). Before creating the record, the record information will be validated against the profile. Validation takes some time, depending on the context. It depends a lot on the size of your record and the already cached information. This information is gathered from external services. If there are connection issues or hiccups at these sites, validation may even take up to a few seconds. Usually you can expect the request to be between 100ms up to 1000ms on a fast machine with reliable connections.

### Example


```python
import pytypid_generated_client
from pytypid_generated_client.models.pid_record import PIDRecord
from pytypid_generated_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://typed-pid-maker.datamanager.kit.edu/preview
# See configuration.py for a list of all supported configuration parameters.
configuration = pytypid_generated_client.Configuration(
    host = "http://typed-pid-maker.datamanager.kit.edu/preview"
)


# Enter a context with an instance of the API client
with pytypid_generated_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pytypid_generated_client.PIDManagementApi(api_client)
    pid_record = pytypid_generated_client.PIDRecord() # PIDRecord | The body containing all PID record values as they should be in the new PIDs record.
    dryrun = False # bool | If true, only validation will be done and no PID will be created. No data will be changed and no services will be notified. (optional) (default to False)

    try:
        # Create a new PID record
        api_response = api_instance.create_pid(pid_record, dryrun=dryrun)
        print("The response of PIDManagementApi->create_pid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PIDManagementApi->create_pid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid_record** | [**PIDRecord**](PIDRecord.md)| The body containing all PID record values as they should be in the new PIDs record. | 
 **dryrun** | **bool**| If true, only validation will be done and no PID will be created. No data will be changed and no services will be notified. | [optional] [default to False]

### Return type

[**PIDRecord**](PIDRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.datamanager.pid.simple+json
 - **Accept**: application/json, application/vnd.datamanager.pid.simple+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Validation failed. See body for details. Contains also the validated record. |  -  |
**201** | Created |  -  |
**406** | Provided input is invalid with regard to the supported accept header (Not acceptable) |  -  |
**415** | Provided input is invalid with regard to the supported content types. (Unsupported Mediatype) |  -  |
**409** | If providing an own PID is enabled 409 indicates, that the PID already exists. |  -  |
**503** | Communication to required external service failed. |  -  |
**500** | Server error. See body for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pids**
> BatchRecordResponse create_pids(pid_record, dryrun=dryrun)

Create a multiple, possibly related PID records

Create multiple, possibly related PID records using the record information. This endpoint is a convenience method to create multiple PID records at once. For connecting records, the PID fields must be specified and the value may be used in the value fields of other PIDRecordEntries. The provided PIDs will be overwritten as defined by the PID generator strategy.
Note: This endpoint does not support custom PIDs, as the PID field is used for "placeholder" PIDs to connect records. These placeholder PIDs will be replaced by actual, resolvable PIDs as defined by the PID generator strategy. This goes for the PID referencing a record as well as references from other records, if they are provided as a single attribute value (i.e., not a JSON array within an attribute's value). If you want to create a record with custom PID suffixes, use the endpoint `POST /pid` and configure the Typed PID Maker accordingly.

### Example


```python
import pytypid_generated_client
from pytypid_generated_client.models.batch_record_response import BatchRecordResponse
from pytypid_generated_client.models.pid_record import PIDRecord
from pytypid_generated_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://typed-pid-maker.datamanager.kit.edu/preview
# See configuration.py for a list of all supported configuration parameters.
configuration = pytypid_generated_client.Configuration(
    host = "http://typed-pid-maker.datamanager.kit.edu/preview"
)


# Enter a context with an instance of the API client
with pytypid_generated_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pytypid_generated_client.PIDManagementApi(api_client)
    pid_record = [pytypid_generated_client.PIDRecord()] # List[PIDRecord] | The body containing a list of all PID record values as they should be in the new PID records. To connect records, the PID fields must be specified. This placeholder PID value may then be used in the value fields of other PID Record entries. During creation, these placeholder PIDs whose sole purpose is to connect records will be overwritten with actual, resolvable PIDs as defined by the PID generator strategy.
    dryrun = False # bool | If true, only validation will be done and no PIDs will be created. No data will be changed and no services will be notified. (optional) (default to False)

    try:
        # Create a multiple, possibly related PID records
        api_response = api_instance.create_pids(pid_record, dryrun=dryrun)
        print("The response of PIDManagementApi->create_pids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PIDManagementApi->create_pids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid_record** | [**List[PIDRecord]**](PIDRecord.md)| The body containing a list of all PID record values as they should be in the new PID records. To connect records, the PID fields must be specified. This placeholder PID value may then be used in the value fields of other PID Record entries. During creation, these placeholder PIDs whose sole purpose is to connect records will be overwritten with actual, resolvable PIDs as defined by the PID generator strategy. | 
 **dryrun** | **bool**| If true, only validation will be done and no PIDs will be created. No data will be changed and no services will be notified. | [optional] [default to False]

### Return type

[**BatchRecordResponse**](BatchRecordResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Validation failed. See body for details. Contains also the validated records. |  -  |
**201** | Successfully created all records and resolved references (if they exist). The response contains the created records and the mapping used to map from the user-provided, placeholder PIDs to the actual Handle PIDs created in the process. |  -  |
**406** | Provided input is invalid with regard to the supported accept header (Not acceptable) |  -  |
**415** | Provided input is invalid with regard to the supported content types. (Unsupported Mediatype) |  -  |
**409** | If providing own PIDs is enabled 409 indicates, that the PID already exists. |  -  |
**503** | Communication to required external service failed. |  -  |
**500** | Server error. See body for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all**
> List[KnownPid] find_all(created_after=created_after, created_before=created_before, modified_after=modified_after, modified_before=modified_before, page=page, size=size, sort=sort, accept=accept)

Returns all known PIDs. Supports paging, filtering criteria, and different formats.

Returns all known PIDs, limited by the given page size and number. Several filtering criteria are also available. Known PIDs are defined as being stored in a local store. This store is not a cache! Instead, the service remembers every PID which it created (and resolved, depending on the configuration parameter `pit.storage.strategy` of the service) on request. Use the Accept header to adjust the format.

### Example


```python
import pytypid_generated_client
from pytypid_generated_client.models.known_pid import KnownPid
from pytypid_generated_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://typed-pid-maker.datamanager.kit.edu/preview
# See configuration.py for a list of all supported configuration parameters.
configuration = pytypid_generated_client.Configuration(
    host = "http://typed-pid-maker.datamanager.kit.edu/preview"
)


# Enter a context with an instance of the API client
with pytypid_generated_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pytypid_generated_client.PIDManagementApi(api_client)
    created_after = '2013-10-20T19:20:30+01:00' # datetime | The UTC time of the earliest creation timestamp of a returned PID. (optional)
    created_before = '2013-10-20T19:20:30+01:00' # datetime | The UTC time of the latest creation timestamp of a returned PID. (optional)
    modified_after = '2013-10-20T19:20:30+01:00' # datetime | The UTC time of the earliest modification timestamp of a returned PID. (optional)
    modified_before = '2013-10-20T19:20:30+01:00' # datetime | The UTC time of the latest modification timestamp of a returned PID. (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 20 # int | The size of the page to be returned (optional) (default to 20)
    sort = ['sort_example'] # List[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Returns all known PIDs. Supports paging, filtering criteria, and different formats.
        api_response = api_instance.find_all(created_after=created_after, created_before=created_before, modified_after=modified_after, modified_before=modified_before, page=page, size=size, sort=sort, accept=accept)
        print("The response of PIDManagementApi->find_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PIDManagementApi->find_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created_after** | **datetime**| The UTC time of the earliest creation timestamp of a returned PID. | [optional] 
 **created_before** | **datetime**| The UTC time of the latest creation timestamp of a returned PID. | [optional] 
 **modified_after** | **datetime**| The UTC time of the earliest modification timestamp of a returned PID. | [optional] 
 **modified_before** | **datetime**| The UTC time of the latest modification timestamp of a returned PID. | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[KnownPid]**](KnownPid.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/tabulator+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**200** | If the request was valid. May return an empty list. |  -  |
**500** | Server error. See body for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_by_pid**
> KnownPid find_by_pid()

Returns a PID and its timestamps from the local store, if available.

Returns a PID from the local store. This store is not a cache! Instead, the service remembers every PID which it created (and resolved, depending on the configuration parameter `pit.storage.strategy` of the service) on request. If this PID is known, it will be returned together with the timestamps of creation and modification executed on this PID by this service.

### Example


```python
import pytypid_generated_client
from pytypid_generated_client.models.known_pid import KnownPid
from pytypid_generated_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://typed-pid-maker.datamanager.kit.edu/preview
# See configuration.py for a list of all supported configuration parameters.
configuration = pytypid_generated_client.Configuration(
    host = "http://typed-pid-maker.datamanager.kit.edu/preview"
)


# Enter a context with an instance of the API client
with pytypid_generated_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pytypid_generated_client.PIDManagementApi(api_client)

    try:
        # Returns a PID and its timestamps from the local store, if available.
        api_response = api_instance.find_by_pid()
        print("The response of PIDManagementApi->find_by_pid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PIDManagementApi->find_by_pid: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**KnownPid**](KnownPid.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**200** | If the PID is known and its information was returned. |  -  |
**404** | If the PID is unknown. |  -  |
**500** | Server error. See body for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_record**
> PIDRecord get_record(validation=validation)

Get the record of the given PID.

Get the record to the given PID, if it exists. May also be used to test if a PID exists. No validation is performed by default.

### Example


```python
import pytypid_generated_client
from pytypid_generated_client.models.pid_record import PIDRecord
from pytypid_generated_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://typed-pid-maker.datamanager.kit.edu/preview
# See configuration.py for a list of all supported configuration parameters.
configuration = pytypid_generated_client.Configuration(
    host = "http://typed-pid-maker.datamanager.kit.edu/preview"
)


# Enter a context with an instance of the API client
with pytypid_generated_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pytypid_generated_client.PIDManagementApi(api_client)
    validation = False # bool | If true, validation will be run on the resolved PID. On failure, an error will be returned. On success, the PID will be resolved. (optional) (default to False)

    try:
        # Get the record of the given PID.
        api_response = api_instance.get_record(validation=validation)
        print("The response of PIDManagementApi->get_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PIDManagementApi->get_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validation** | **bool**| If true, validation will be run on the resolved PID. On failure, an error will be returned. On success, the PID will be resolved. | [optional] [default to False]

### Return type

[**PIDRecord**](PIDRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.datamanager.pid.simple+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Validation failed. See body for details. |  -  |
**200** | Found |  -  |
**404** | Not found |  -  |
**503** | Communication to required external service failed. |  -  |
**500** | Server error. See body for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pid**
> PIDRecord update_pid(pid_record, dryrun=dryrun)

Update an existing PID record

Update an existing PID record using the record information from the request body. The record may contain the identifier(s) of the matching profiles. Conditions for a valid record are the same as for creation. Important note: Validation may take some time. For details, see the documentation of "POST /pid/".

### Example


```python
import pytypid_generated_client
from pytypid_generated_client.models.pid_record import PIDRecord
from pytypid_generated_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://typed-pid-maker.datamanager.kit.edu/preview
# See configuration.py for a list of all supported configuration parameters.
configuration = pytypid_generated_client.Configuration(
    host = "http://typed-pid-maker.datamanager.kit.edu/preview"
)


# Enter a context with an instance of the API client
with pytypid_generated_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pytypid_generated_client.PIDManagementApi(api_client)
    pid_record = pytypid_generated_client.PIDRecord() # PIDRecord | The body containing all PID record values as they should be after the update.
    dryrun = False # bool | If true, no PID will be updated. Only validation checks are performed, and the expected response, including the new eTag, will be returned. No data will be changed and no services will be notified. (optional) (default to False)

    try:
        # Update an existing PID record
        api_response = api_instance.update_pid(pid_record, dryrun=dryrun)
        print("The response of PIDManagementApi->update_pid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PIDManagementApi->update_pid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid_record** | [**PIDRecord**](PIDRecord.md)| The body containing all PID record values as they should be after the update. | 
 **dryrun** | **bool**| If true, no PID will be updated. Only validation checks are performed, and the expected response, including the new eTag, will be returned. No data will be changed and no services will be notified. | [optional] [default to False]

### Return type

[**PIDRecord**](PIDRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.datamanager.pid.simple+json
 - **Accept**: application/json, application/vnd.datamanager.pid.simple+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Validation failed. See body for details. |  -  |
**200** | Success. |  -  |
**406** | Provided input is invalid with regard to the supported accept header (Not acceptable) |  -  |
**415** | Provided input is invalid with regard to the supported content types. (Unsupported Mediatype) |  -  |
**412** | ETag comparison failed (Precondition failed) |  -  |
**428** | No ETag given in If-Match header (Precondition required) |  -  |
**503** | Communication to required external service failed. |  -  |
**500** | Server error. See body for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

