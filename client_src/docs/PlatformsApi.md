# swagger_client.PlatformsApi

All URIs are relative to *http://localhost:8080/api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_platform_list**](PlatformsApi.md#get_platform_list) | **GET** /references/platforms | Метод получения списка платформ

# **get_platform_list**
> Platforms get_platform_list()

Метод получения списка платформ

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlatformsApi()

try:
    # Метод получения списка платформ
    api_response = api_instance.get_platform_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformsApi->get_platform_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Platforms**](Platforms.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

