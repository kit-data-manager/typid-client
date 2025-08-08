# pytypid_generated_client.ActuatorApi

All URIs are relative to *http://typed-pid-maker.datamanager.kit.edu/preview*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health**](ActuatorApi.md#health) | **GET** /actuator/health | Actuator web endpoint &#39;health&#39;
[**info**](ActuatorApi.md#info) | **GET** /actuator/info | Actuator web endpoint &#39;info&#39;
[**links**](ActuatorApi.md#links) | **GET** /actuator | Actuator root web endpoint


# **health**
> object health()

Actuator web endpoint 'health'

### Example


```python
import pytypid_generated_client
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
    api_instance = pytypid_generated_client.ActuatorApi(api_client)

    try:
        # Actuator web endpoint 'health'
        api_response = api_instance.health()
        print("The response of ActuatorApi->health:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActuatorApi->health: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/vnd.spring-boot.actuator.v3+json, application/vnd.spring-boot.actuator.v2+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **info**
> object info()

Actuator web endpoint 'info'

### Example


```python
import pytypid_generated_client
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
    api_instance = pytypid_generated_client.ActuatorApi(api_client)

    try:
        # Actuator web endpoint 'info'
        api_response = api_instance.info()
        print("The response of ActuatorApi->info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActuatorApi->info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/vnd.spring-boot.actuator.v3+json, application/vnd.spring-boot.actuator.v2+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **links**
> Dict[str, Dict[str, Link]] links()

Actuator root web endpoint

### Example


```python
import pytypid_generated_client
from pytypid_generated_client.models.link import Link
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
    api_instance = pytypid_generated_client.ActuatorApi(api_client)

    try:
        # Actuator root web endpoint
        api_response = api_instance.links()
        print("The response of ActuatorApi->links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActuatorApi->links: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, Dict[str, Link]]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/vnd.spring-boot.actuator.v3+json, application/vnd.spring-boot.actuator.v2+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

