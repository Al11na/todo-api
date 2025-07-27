# ToDo REST API

Django REST API для управления задачами (To-Do List) с JWT аутентификацией.

## Возможности
🔐 JWT аутентификация                                                                          
👥 Регистрация и управление пользователями                                                                                      
📝 Управление задачами                                                                   
🔍 Фильтрация и поиск задач                                                                    
📄 Пагинация                                                                   
📊 Swagger/OpenAPI документация                                                                        

## Установка

1. Создайте и активируйте виртуальное окружение:                                                                   
python -m venv venv                                    
venv\Scripts\activate                      

2. Установите зависимости:                                           
pip install -r requirements.txt

3. Выполните миграции:                                                      
python manage.py makemigrations                                       
python manage.py migrate

4. Создайте суперпользователя:                                   
python manage.py createsuperuser

5. Запустите  сервер:                                              
python manage.py runserver

## Эндпоинты API
#### Аутентификация

POST /api/register/ - регистрация пользователя
POST /api/token/ - получение JWT-токена
POST /api/token/refresh/ - обновление JWT токена

#### Управление задачами
GET /api/tasks/ - список всех задач

POST /api/tasks/ - создание новой задачи

GET /api/tasks/{id}/ - получение задачи по ID

PUT /api/tasks/{id}/ - полное обновление задачи

PATCH /api/tasks/{id}/ - частичное обновление задачи

DELETE /api/tasks/{id}/ - удаление задачи

#### Параметры фильтрации и поиска

completed=true|false - фильтрация по статусу задачи

search=<string> - поиск по title и description

page=<number> - номер страницы (по 10 задач)

#### Использование JWT
Зарегистрируйтесь: POST /api/register/ → { "username": ..., "email": ..., "password": ..., "password2": ... }

Получите токен: POST /api/token/ → { "username": ..., "password": ... } → ответ содержит access, refresh

Добавьте заголовок ко всем защищённым запросам:

Authorization: Bearer <access_token>

## Swagger/OpenAPI

JSON/YAML: http://127.0.0.1:8000/swagger/?format=json или format=yaml

UI: http://127.0.0.1:8000/swagger/

## Тестирование (Postman)

- Импортируйте коллекцию: postman/to-do.postman_collection.json
- Создайте окружение с переменными:
 baseUrl = http://127.0.0.1:8000/api
 jwt_token 
- Запустите User Registration, затем Token Create, и прогоните всю коллекцию через Runner.



