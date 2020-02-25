# swagger_client.ModelConfigurationsApi

All URIs are relative to *https://app.micromechanicalmodeling.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configuration_id_download_get**](ModelConfigurationsApi.md#configuration_id_download_get) | **GET** /configuration/{_id}/download | Retreive signed url to download binary
[**configuration_id_get**](ModelConfigurationsApi.md#configuration_id_get) | **GET** /configuration/{_id} | Returns a model configuration
[**configuration_id_patch**](ModelConfigurationsApi.md#configuration_id_patch) | **PATCH** /configuration/{_id} | Launch a configuration to one of the workers to be processed.
[**configuration_id_put**](ModelConfigurationsApi.md#configuration_id_put) | **PUT** /configuration/{_id} | Update and replace a model configuration
[**configuration_post**](ModelConfigurationsApi.md#configuration_post) | **POST** /configuration | Creates a model configuration.

# **configuration_id_download_get**
> InlineResponse200 configuration_id_download_get(id)

Retreive signed url to download binary

In order to download the computer binary from S3, you need to get a signed url (as the bucket is private). 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ModelConfigurationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Retreive signed url to download binary
    api_response = api_instance.configuration_id_download_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelConfigurationsApi->configuration_id_download_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_id_get**
> Configuration configuration_id_get(id, status_only=status_only)

Returns a model configuration

By passing in the appropriate options, you can search for available model configurations in the system 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ModelConfigurationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
status_only = 'status_only_example' # str | pass an optional statusOnly to just retun status for polling. (optional)

try:
    # Returns a model configuration
    api_response = api_instance.configuration_id_get(id, status_only=status_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelConfigurationsApi->configuration_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **status_only** | **str**| pass an optional statusOnly to just retun status for polling. | [optional] 

### Return type

[**Configuration**](Configuration.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_id_patch**
> configuration_id_patch(id)

Launch a configuration to one of the workers to be processed.

Patching the model configuration, will put a job in an AWS SQS Queue. Worker computers poll the job Queue. And when a job is found it will process, and then upload the binary to S3. To grab the binary access the GET /configuration/{uuid}/download for signed S3 urls. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ModelConfigurationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Launch a configuration to one of the workers to be processed.
    api_instance.configuration_id_patch(id)
except ApiException as e:
    print("Exception when calling ModelConfigurationsApi->configuration_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_id_put**
> Configuration configuration_id_put(id, body=body)

Update and replace a model configuration

By passing in the appropriate options, you can update an existing model configuration 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ModelConfigurationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
body = swagger_client.Configuration() # Configuration | Model Configuration parameters to update. (optional)

try:
    # Update and replace a model configuration
    api_response = api_instance.configuration_id_put(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelConfigurationsApi->configuration_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**Configuration**](Configuration.md)| Model Configuration parameters to update. | [optional] 

### Return type

[**Configuration**](Configuration.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_post**
> Configuration configuration_post(body=body)

Creates a model configuration.

Adds an item to the system

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ModelConfigurationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Configuration() # Configuration | Model Configuration to add (optional)

try:
    # Creates a model configuration.
    api_response = api_instance.configuration_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelConfigurationsApi->configuration_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Configuration**](Configuration.md)| Model Configuration to add | [optional] 

### Return type

[**Configuration**](Configuration.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

