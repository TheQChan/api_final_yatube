# API
Тренировочный проект по созданию API. Включает в себя авторизацию, разграничение прав, лимиты и т. д.
## Установка
Клонируем репозиторий  
```  
git clone git@github.com:TheQChan/api_final_yatube.git  
```
Переходим в папку, создаем и активируем виртуальное окружение
```  
python -m venv venv
```
```  
source venv/Scripts/activate
```
Обновляем pip и устанавливаем зависимости
```  
python -m pip install --upgrade pip
```
```  
pip install -r requirements.txt
```
Выполнение миграций
```  
python manage.py migrate
```
Запуск проекта
```  
python manage.py runserver
```
## Примеры запросов
> GET /api/v1/posts/
```  
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
> POST /api/v1/posts/
```  
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
Ответ
```  
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2022-09-21T19:57:45.329Z",
  "image": "string",
  "group": 0
}
```
---
Документация \api_final_yatube\yatube_api\static\redoc.yaml
