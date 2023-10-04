import requests as requests
import configuration
import data


#создаю переменную для полей авторизации
def auth_body(field, name): 
    create_body = data.user_body.copy()
    create_body[field] = name 
    return create_body 


#функция для авторизации
def authorization(user_body): 
    return requests.post(url=configuration.URL + configuration.USER_PATH, json=user_body, headers=data.headers) 


#функция для получения всех категорий авторизованным пользователем
def success_get_category():
    return requests.get(url=configuration.URL + configuration.ALL_ANIMALS_CATEGORY, headers=data.headers, auth=('admin', 'admin'))
response_all_category = success_get_category()



#функция для получения всех категорий неавторизованным пользователем
def error_get_category():
    return requests.get(url=configuration.URL + configuration.ALL_ANIMALS_CATEGORY, headers=data.headers)


#переменная для названия категории
def cat_body(field, name): 
    create_cat_body = data.create_category_body.copy()
    create_cat_body[field] = name 
    return create_cat_body


#функция для создания категории авторизованным пользователем
def success_post_category(category_body):
    return requests.post(url=configuration.URL + configuration.ALL_ANIMALS_CATEGORY, auth=('admin', 'admin'), json=category_body, 
                         headers=data.headers)


#функция для создания категории неавторизованным пользователем
def error_post_category(category_body):
    return requests.post(url=configuration.URL + configuration.ALL_ANIMALS_CATEGORY, json=category_body, headers=data.headers)
    



#ограничение данных в теле ответа
query_params = {
    "limit": 1
} 

#получение существующиего id для дальнейших запросов
def success_get_category():
    return requests.get(url=configuration.URL + configuration.ALL_ANIMALS_CATEGORY, 
                        headers=data.headers, auth=('admin', 'admin'), params=query_params)
response_all_category = success_get_category()
category_id = response_all_category.json()["results"][0]["id"]
url_id = {'id': category_id}

#функция для получения категории по id авторизованным пользователем
def success_get_category_id():
    return requests.get(url=configuration.URL + configuration.ALL_ANIMALS_CATEGORY, params=url_id, headers=data.headers, 
                        auth=('admin', 'admin'))


#функция для получения категории по id не авторизованным пользователем
def error_get_category_id():
    return requests.get(url=configuration.URL + configuration.ALL_ANIMALS_CATEGORY, params=url_id, headers=data.headers)


u_id = {'id': "id"}
#функция для получения категории c некорректным типом данных авторизованным пользователем
def error_get_category_with_letter_id():
    return requests.get(url=configuration.URL + configuration.ALL_ANIMALS_CATEGORY, params=u_id, headers=data.headers, 
                        auth=('admin', 'admin'))


ur_id = {'id': 3978785656538496}
#функция для получения категории c некорректным id авторизованным пользователем
def error_get_category_with_invalid_id():
    return requests.get(url=configuration.URL + configuration.ALL_ANIMALS_CATEGORY, params=ur_id, headers=data.headers, 
                        auth=('admin', 'admin'))



