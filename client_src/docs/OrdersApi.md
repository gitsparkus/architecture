# swagger_client.OrdersApi

All URIs are relative to *http://localhost:8080/api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_order**](OrdersApi.md#create_order) | **POST** /orders | Метод создания заказа
[**delete_order_by_id**](OrdersApi.md#delete_order_by_id) | **DELETE** /orders/{order_id} | Метод отмены заказа по ID
[**get_all_orders**](OrdersApi.md#get_all_orders) | **GET** /orders | Метод получения списка заказов
[**get_order_by_id**](OrdersApi.md#get_order_by_id) | **GET** /orders/{order_id} | Метод получения заказа по ID

# **create_order**
> Order create_order(body)

Метод создания заказа

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrdersApi()
body = swagger_client.Order() # Order | 

try:
    # Метод создания заказа
    api_response = api_instance.create_order(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->create_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Order**](Order.md)|  | 

### Return type

[**Order**](Order.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_order_by_id**
> delete_order_by_id(order_id)

Метод отмены заказа по ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrdersApi()
order_id = 'order_id_example' # str | Идентификатор заказа

try:
    # Метод отмены заказа по ID
    api_instance.delete_order_by_id(order_id)
except ApiException as e:
    print("Exception when calling OrdersApi->delete_order_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Идентификатор заказа | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_orders**
> Orders get_all_orders()

Метод получения списка заказов

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrdersApi()

try:
    # Метод получения списка заказов
    api_response = api_instance.get_all_orders()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->get_all_orders: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Orders**](Orders.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_by_id**
> Order get_order_by_id(order_id)

Метод получения заказа по ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrdersApi()
order_id = 'order_id_example' # str | Идентификатор заказа

try:
    # Метод получения заказа по ID
    api_response = api_instance.get_order_by_id(order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->get_order_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Идентификатор заказа | 

### Return type

[**Order**](Order.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

