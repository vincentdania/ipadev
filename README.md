# IPADEV Website

Official website for the Inclusive Pathway Development Initiative (IPADEV).

The project is now a server-rendered Django website with a premium donor-facing UI inspired by the Google Stitch redesign.

## Stack

- Python 3.12
- Django 4.2
- Django Templates
- Tailwind via CDN
- HTMX
- Alpine.js
- PostgreSQL
- Celery + Redis
- django-allauth
- Django REST Framework
- django-environ
- django-storages + boto3
- Gunicorn
- Pillow
- ReportLab

## Local Setup

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements/dev.txt
cp .env.example .env
python manage.py migrate
python manage.py seed_site
python manage.py createsuperuser
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

## Main Routes

- `/`
- `/about/`
- `/areas-of-focus/`
- `/team/`
- `/impact/`
- `/news/`
- `/get-involved/`
- `/contact/`
- `/admin/`
- `/api/`

## Deployment Notes

- Use PostgreSQL for `DATABASE_URL`.
- Use Redis for `REDIS_URL`.
- Run web with Gunicorn:

```bash
gunicorn config.wsgi:application
```

- Run background jobs with Celery:

```bash
celery -A config worker --loglevel=info
```

- Run `collectstatic` before serving static files:

```bash
python manage.py collectstatic --noinput
```

- If using S3-compatible media storage, set `USE_S3=True` and provide the AWS/S3 environment variables in `.env`.
