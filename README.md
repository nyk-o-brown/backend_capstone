```markdown
# backend_capstone / property_manager_backend
This repository contains a Django project scaffold for a Property Manager backend.

Structure has been split to use a settings package and application packages under `apps/`.

See `property_manager_backend/` for project code and `apps/` for individual Django apps.

```
# backend_capstone
this is a project for the project manager backend in python django and my sql



🏠 Property Manager – Django Web App
A scalable, modular property management system built with Django. Designed to support CRUD operations for properties, units, and users, with role-based access and a clean UI for managing tenants and assets.

🚀 Features
🏢 Property CRUD: Add, edit, delete, and view properties

🧱 Unit Management: Each property can have multiple units with floor and tenant info

👥 User Management: View and assign tenants to units

📊 Per-property tenant views

🖼️ Image upload for properties

🔐 Role-based access (admin, tenant)

🧪 Mock data generation using Faker

🎨 Bootstrap-styled frontend with custom CSS

🛠️ Tech Stack
Layer	Tools
Backend	Django, Django REST Framework
Frontend	Django Templates, Bootstrap
Database	SQLite (default) or PostgreSQL
Dev Tools	Faker, Django Admin, Management Commands
📦 Installation
bash
git clone https://github.com/your-username/property-manager.git
cd property-manager
python -m venv env
source env/bin/activate  # or .\env\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
🧪 Generate Mock Data
bash
python manage.py generate_users
python manage.py generate_properties
python manage.py generate_units
These commands use Faker to populate the database with realistic test data.

🧭 Navigation
/ → Home page with links to Users and Properties

/users-ui/ → View all users

/properties-ui/ → View all properties and their units

/property/<id>/users/ → View tenants for a specific property

📁 Project Structure
Code
apps/
├── users/
│   ├── models.py
│   ├── views.py
│   └── forms.py
├── property/
│   ├── models.py
│   ├── views.py
│   └── forms.py
frontend/
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── users.html
│   ├── properties.html
│   └── property_users.html
🧠 Development Goals
✅ Validate business model assumptions through pilot testing

✅ Modularize architecture for scalability

🔜 Add payments, maintenance tracking, and reporting

🔜 Integrate government APIs for location and compliance data

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.