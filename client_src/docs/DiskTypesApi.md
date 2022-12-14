# swagger_client.DiskTypesApi

All URIs are relative to *http://localhost:8080/api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_disk_types_list**](DiskTypesApi.md#get_disk_types_list) | **GET** /references/disctypes | Метод получения списка типов дисков

# **get_disk_types_list**
> DiskTypes get_disk_types_list()

Метод получения списка типов дисков

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DiskTypesApi()

try:
    # Метод получения списка типов дисков
    api_response = api_instance.get_disk_types_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiskTypesApi->get_disk_types_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DiskTypes**](DiskTypes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

