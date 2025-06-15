Linux commands
**************
python3 -m venv newenv
source newenv/bin/activate
pip install -r requirements.txt

**********************************************************************************************************************


Folder strucutre for svx_main
*****************************

svx_main/
│
├── templates/                # (Optional) Django templates (if using any)
│   └── svx_main/
│       └── base.html         # Base template (if admin/site pages needed)
│
├── static/                   # (Optional) Static files (CSS/JS/img if using Django templates)
│   └── css/
│   └── js/
│
├── migrations/               # Django-managed DB migrations
│
├── models/                   # Split business entities
│   ├── __init__.py
│   ├── university.py
│   ├── profile.py
│   └── job.py
│
├── views/                    # Views for public/admin routes (Django TemplateView or admin)
│   ├── __init__.py
│   ├── homepage.py
│   ├── careers.py
│   └── about.py
│
├── urls/                     # URL routing specific to svx_main
│   ├── __init__.py
│   └── public_routes.py
│
├── services/                 # Custom business logic (e.g., ranking logic, job matching)
│   └── university_service.py
│
├── admin.py                  # Django admin config
├── apps.py                   # Django app config
├── tests/                    # Unit tests for this app
│   └── test_models.py
├── __init__.py


**********************************************************************************************************




Folder structure for svx_api
*****************************

svx_api/
│
├── models/
│   ├── __init__.py
│   ├── post.py
│   ├── media.py
│   └── user.py
│
├── views/
│   ├── __init__.py
│   ├── post_views.py
│   ├── media_views.py
│
├── serializers/
│   ├── __init__.py
│   ├── post_serializers.py
│   ├── media_serializers.py
│
├── urls/
│   ├── __init__.py
│   └── api_routes.py
│
├── services/
│   └── post_service.py  # for custom logic


****************************************************************************************************
