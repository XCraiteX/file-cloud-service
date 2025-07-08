# File Cloud Микросервис

**Простой микросервис для хранения файлов в облаке на FastAPI**

## Стек
- **FastAPI**
- **SQLAlchemy**
- **SQLite + aiosqlite driver**

## Устновка

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/XCraiteX/file-cloud-service.git
```

### 2. Замените ссылки в `data/config.py`

```bash
# Your host link or localhost for tests
HOST_LINK = 'http://localhost:3000'
```

### 3. Запуск сервера

```bash
uvicorn app.main:app --port 3300  
```

### 4. Конфигурация Nginx

```nginx
location /cloud/ {
    proxy_pass http://localhost:3300;
    proxy_http_version 1.1;
}
```

### 5. Используйте API в своих проектах
<br>

# Использование API

### 1. Выгрузка файлов | `POST` - `HOST_LINK` `/cloud/upload`

- **Parameters**

```json
{
    "file": File
}
```
  
###  > Ответ

- Successfull

```json
{ 
    "status": "OK", 
    "details": "File successfully uploaded!", 
    "uuid": link_here 
}
```

- Error

```json
{
    "status": "Error",
    "details": "Internal server error"
}
```

### 2. Скачивание и использование файла | `GET` - `HOST_LINK` `/cloud/file/uuid`

-  Ответ

```JSON
File Response
```
