# swagger_client.ModelConfigurationsApi

All URIs are relative to *https://app.micromechanicalmodeling.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_configuration**](ModelConfigurationsApi.md#create_configuration) | **POST** /configuration | Creates a model configuration.
[**download_configuration**](ModelConfigurationsApi.md#download_configuration) | **GET** /configuration/{_id}/download | Retreive signed url to download binary
[**get_configuration**](ModelConfigurationsApi.md#get_configuration) | **GET** /configuration/{_id} | Returns a model configuration
[**launch_configuration**](ModelConfigurationsApi.md#launch_configuration) | **PATCH** /configuration/{_id} | Launch a configuration to one of the workers to be processed.
[**update_configuration**](ModelConfigurationsApi.md#update_configuration) | **PUT** /configuration/{_id} | Update and replace a model configuration

# **create_configuration**
> ParamSetResponse create_configuration(body=body)

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
body = swagger_client.ParamSet() # ParamSet | Model Configuration to add (optional)

try:
    # Creates a model configuration.
    api_response = api_instance.create_configuration(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelConfigurationsApi->create_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ParamSet**](ParamSet.md)| Model Configuration to add | [optional] 

### Return type

[**ParamSetResponse**](ParamSetResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_configuration**
> InlineResponse200 download_configuration(id)

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
    api_response = api_instance.download_configuration(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelConfigurationsApi->download_configuration: %s\n" % e)
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

# **get_configuration**
> ParamSetResponse get_configuration(id, status_only=status_only)

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
status_only = true # bool | pass an optional statusOnly to just retun status for polling. (optional)

try:
    # Returns a model configuration
    api_response = api_instance.get_configuration(id, status_only=status_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelConfigurationsApi->get_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **status_only** | **bool**| pass an optional statusOnly to just retun status for polling. | [optional] 

### Return type

[**ParamSetResponse**](ParamSetResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **launch_configuration**
> launch_configuration(id)

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
    api_instance.launch_configuration(id)
except ApiException as e:
    print("Exception when calling ModelConfigurationsApi->launch_configuration: %s\n" % e)
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

# **update_configuration**
> ParamSetResponse update_configuration(id, body=body)

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
body = swagger_client.ParamSet() # ParamSet | Model Configuration parameters to update. (optional)

try:
    # Update and replace a model configuration
    api_response = api_instance.update_configuration(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelConfigurationsApi->update_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**ParamSet**](ParamSet.md)| Model Configuration parameters to update. | [optional] 

### Return type

[**ParamSetResponse**](ParamSetResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

