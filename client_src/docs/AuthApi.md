# swagger_client.AuthApi

All URIs are relative to *http://localhost:8080/api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_auth**](AuthApi.md#post_auth) | **POST** /auth | Метод авторизации

# **post_auth**
> InlineResponse200 post_auth(body)

Метод авторизации

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
body = swagger_client.User() # User | 

try:
    # Метод авторизации
    api_response = api_instance.post_auth(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->post_auth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**User**](User.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

