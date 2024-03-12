# 咖啡豆庫存管理系統

這是一個使用 Vue 3 和 Django REST Framework 構建的咖啡豆庫存管理系統，支持咖啡豆的增刪改查操作，並實現了用戶管理功能。

## 功能特性

- 支持咖啡豆資訊的添加、編輯、刪除和查看。
- 支持用戶管理，包括用戶的創建、編輯和刪除。

## 技術堆疊

- **前端**：Vue 3, Vuex, Vue Router, SCSS
- **後端**：Django, Django REST Framework
- **資料庫**：MySQL


## 運行

### 前端

進入前端項目目錄：

```bash
cd coffee_beans_frontend/
```
運行
```bash
npm run serve
```

### 後端

進入後端項目目錄：

```bash
cd coffee_beans_api_django/
```
安裝依賴
```bash
pip install -r requirements.txt
```
資料庫遷移
```bash
python manage.py migrate
```
運行
```bash
python manage.py runserver
```

## 使用指南
- 訪問前端（默認：http://localhost:8080），進行咖啡豆庫存的管理操作。
- 使用超級用戶登入系統可進行用戶和權限的管理。
- 非超級用戶將根據其角色和權限進行相應的操作限制。

### 創建超級用戶
```bash
python manage.py createsuperuser
```