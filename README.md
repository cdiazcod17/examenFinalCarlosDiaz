🚀 Futurama Favorites
[

Guarda y gestiona tus personajes favoritos de Futurama con una interfaz limpia y moderna.

✨ Características
Registro rápido con 5 personajes favoritos aleatorios

Perfil personal con galería de favoritos

Panel administrador completo

Diseño responsive móvil/tablet/desktop

API RESTful para gestión avanzada

🎮 Cómo usar
1. Registro / Login
text
1. Regístrate → Recibes 5 personajes random
2. Inicia sesión → Ve tus favoritos
2. Usuario normal
Home → Login → Mis Favoritos
3. Administrador
Login admin → API Admin Panel
📱 Funcionalidades
Acción	Usuario	Admin
Ver favoritos	✅	✅
Galería responsive	✅	✅
Gestión usuarios	-	✅
API CRUD	-	✅
🌐 Endpoints API
text
GET /api/admin        → Lista administradores
GET /api/admin/5      → Admin específico
POST /api/admin       → Crear administrador
PUT /api/admin/5      → Actualizar
DELETE /api/admin/5   → Eliminar
Autenticación JWT → Token 20 minutos

📱 Demo en vivo
https://examenfinalcarlosdiaz.onrender.com

text
Usuario demo:
email: user@test.com
password: 123456

Admin demo:
email: admin@test.com  
password: admin123
🎨 Tecnologías
text
Frontend: HTML5 + CSS3 + Jinja2 + Responsive
Backend: Flask + Blueprints
API: RESTful JSON + JWT Authentication
Despliegue: Render.com
📂 Estructura
text
├── src/app.py           # App principal
├── routes/              # Blueprints modulares
├── templates/           # HTML responsive
├── static/styles/       # CSS moderno
└── requirements.txt     # Dependencias
🚀 Despliegue
text
1. git clone https://github.com/cdiazcod17/futurama_fav_app.git
2. pip install -r requirements.txt
3. python src/app.py
4. http://localhost:5000
Live: https://futurama-fav-app.onrender.com/