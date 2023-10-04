import request


#функция для проверки кода 200 и получения токена при успешной авторизации
def authorizatin_assert(field, name):
    user_body = request.auth_body(field, name)
    response_auth = request.authorization(user_body)
    assert response_auth.status_code == 200
    assert response_auth.headers['Content-Type'] == 'application/json'
    assert response_auth.json()["token"] != ""
     

def test_possitive_authorizatin_with_valid_password(): 
    authorizatin_assert("password", "admin")

def test_possitive_authorizatin_with_valid_username(): 
    authorizatin_assert("username", "admin")


#функция для проверки кода 400 при введении несуществующих данных при авторизации
def negative_authorizatin_assert(field, name):
    user_body = request.auth_body(field, name)
    response_auth = request.authorization(user_body)
    assert response_auth.status_code == 400


def test_negative_auth_with_invalid_password(): 
    negative_authorizatin_assert("password", "tester")

def test_negative_auth_with_invalid_username(): 
    negative_authorizatin_assert("username", "tester")


#успешное получение категорий авторизованным пользователем
def test_possitive_get_category():
    response_p_get = request.success_get_category()
    assert response_p_get.status_code == 200
    assert response_p_get.headers['Content-Type'] == 'application/json'
    assert response_p_get.json() != ""


#получение категорий неавторизованным пользователем
def test_negative_get_category():
    response_n_get = request.error_get_category()
    assert response_n_get.status_code ==401 


#проверка создания категории авторизованным пользователем
def create_category_auth_assert(field, name):
    category_body = request.cat_body(field, name) 
    response_create_category = request.success_post_category(category_body)
    assert response_create_category.status_code == 201
    assert response_create_category.headers['Content-Type'] == 'application/json'
    assert response_create_category.json()["name"] == name


def test_possitive_post_category():
    create_category_auth_assert("name", "tester")


#проверка создания категории с некорректными данными авторизованным пользователем
def create_category_auth_negative_assert(field, name):
    category_body = request.cat_body(field, name) 
    response_create_category = request.success_post_category(category_body)
    assert response_create_category.status_code == 400


def test_negative_post_category_duble():
    create_category_auth_negative_assert("name", "tester")


#проверка создания категории неавторизованным пользователем
def create_category_no_auth_assert(field, name):
    category_body = request.cat_body(field, name)
    response_create_category = request.error_post_category(category_body)
    assert response_create_category.status_code == 401


def test_negative_post_category():
    create_category_no_auth_assert("name", "енотовидные")


#получение категории по id авторизованным пользователем
def test_possitive_get_category():
    response_cat_id_get = request.success_get_category_id()
    assert response_cat_id_get.status_code == 200
    assert response_cat_id_get.headers['Content-Type'] == 'application/json'
    assert response_cat_id_get.json() != ""

#получение категории по id неавторизованным пользователем
def test_negative_get_category_id():
    response_get_cat_id = request.error_get_category_id()
    assert response_get_cat_id.status_code ==401 


#получение категорий с некорректным типом данных для id авторизованным пользователем
def test_negative_get_category_id_letter():
    response_get_cat_id = request.error_get_category_with_letter_id()
    assert response_get_cat_id.status_code ==400
    
#получение категорий по несуществующему id авторизованным пользователем
def test_negative_get_category_invalid_id():
    response_get_cat_id = request.error_get_category_with_invalid_id()
    assert response_get_cat_id.status_code ==404


