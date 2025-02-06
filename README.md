# File Cloud Microservice

**Simple file cloud microservice on FastAPI**

## Stack
- **FastAPI**
- **SQLAlchemy**
- **SQLite + aiosqlite driver**

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/XCraiteX/file-cloud-service.git
```

### 2. Replace links in `data/config.py`

```bash
# Your host link or localhost for tests
HOST_LINK = 'http://localhost:3000'
```

### 3. Run server

```bash
uvicorn app.main:app --port 3300  
```

### 4. Setup nginx 

```nginx
location /cloud/ {
    proxy_pass http://localhost:3300;
    proxy_http_version 1.1;
}
```

### 5. Use your API for your projects
<br>

# Using API

### 1. Upload to Host | `POST` - `HOST_LINK` `/cloud/upload`

- **Parameters**

```json
{
    "file": File
}
```
  
###  > Response

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

### 2. Download from Host | `GET` - `HOST_LINK` `/cloud/file/uuid`

-  Response

```JSON
File Response
```