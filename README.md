# 🚀 **Futurama Favorites**

[![Deployed](https://img.shields.io/badge/Deployed-Live-brightgreen)](https://futurama-fav-app.onrender.com)

Guarda y gestiona tus **personajes favoritos de Futurama** con una interfaz limpia y moderna.

## ✨ **Características**

- **Registro rápido** con 5 personajes favoritos aleatorios
- **Perfil personal** con galería de favoritos
- **Panel administrador** completo
- **Diseño responsive** móvil/tablet/desktop
- **API RESTful** para gestión avanzada

## 🎮 **Cómo usar**

### **1. Registro / Login**
Regístrate → Recibes 5 personajes random
Inicia sesión → Ve tus favoritos

text

### **2. Usuario normal**
Home → Login → Mis Favoritos

text

### **3. Administrador**
Login admin → API Admin Panel

text

## 📱 **Funcionalidades**

| Acción | Usuario | Admin |
|--------|---------|-------|
| Ver favoritos | ✅ | - |
| Galería responsive | ✅ | - |
| Gestión usuarios | - | ✅ |
| API CRUD | - | ✅ |

## 🌐 **Endpoints API**

GET /api/admin → Lista administradores
GET /api/admin/5 → Admin específico
POST /api/admin → Crear administrador
PUT /api/admin/5 → Actualizar
DELETE /api/admin/5 → Eliminar

text

**Autenticación JWT** → Token 20 minutos

## 📱 **Demo en vivo**

**[https://futurama-fav-app.onrender.com](https://futurama-fav-app.onrender.com)**

Usuario demo:
email: user@test.com
password: 123456

Admin demo:
email: admin@test.com
password: 111111

text

## 🎨 **Tecnologías**

Frontend: HTML5 + CSS3 + Jinja2 + Responsive
Backend: Flask + Blueprints
API: RESTful JSON + JWT Authentication
Despliegue: Render.com

text

## 📂 **Estructura**

├── src/app.py # App principal
├── routes/ # Blueprints modulares
├── templates/ # HTML responsive
├── static/styles/ # CSS moderno
└── requirements.txt # Dependencias

text

## 🚀 **Despliegue**

```bash
git clone https://github.com/cdiazcod17/futurama_fav_app.git
pip install -r requirements.txt
python src/app.py
Local: http://localhost:5000
Live: https://futurama-fav-app.onrender.com

👨‍💻 Desarrollado por Carlos Díaz
GitHub: cdiazcod17
