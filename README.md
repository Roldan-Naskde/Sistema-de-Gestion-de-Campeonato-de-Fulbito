# Sistema de Gestión de Campeonato de Fulbito

Aplicación web para gestionar íntegramente un campeonato de fulbito (fútbol 6), inspirada en Google Deportes.

## 🚀 Demo

- **Frontend:** [https://tu-frontend.vercel.app](https://tu-frontend.vercel.app)
- **Backend:** [https://tu-backend.onrender.com/api/](https://tu-backend.onrender.com/api/)

## 🛠️ Tecnologías

- Django + Django REST Framework (backend)
- SimpleJWT (autenticación)
- Vite + React (frontend)
- React Query, React Hook Form, Material UI
- PostgreSQL (base de datos)
- Render (backend), Vercel (frontend)

## 📦 Instalación local

### Backend

```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## ⚙️ Variables de entorno

- Django: `.env` con `SECRET_KEY`, `DEBUG`, `DATABASE_URL`, etc.
- React: `.env` con `VITE_API_URL=https://tu-backend.onrender.com/api/`

## 🗺️ Rutas principales

- `/` Dashboard
- `/equipos`, `/jugadores`, `/calendario`, `/tabla-posiciones`
- `/login` (autenticación JWT)
- `/admin` (panel protegido)
- CRUD para todas las entidades

## 👤 Credenciales de prueba

- Usuario: admin
- Contraseña: admin123

## 📸 Capturas

![Dashboard](screenshots/dashboard.png)
![Equipos](screenshots/equipos.png)
![Formulario](screenshots/formulario.png)

## 🎥 Video demo

[Ver video en YouTube](https://youtu.be/tu-video-demo)

## 📝 Documentación

- [Informe PDF](./Informe_Campeonato_Fulbito.pdf)
- [DER](screenshots/der.png)

## 👨‍💻 Autores

- Nombre Apellido - [@usuarioGitHub](https://github.com/usuarioGitHub)
- ...

## 📄 Licencia

MIT
