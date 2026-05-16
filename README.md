# IPADEV Website

Official website for the Inclusive Pathway Development Initiative (IPADEV).

The project is now a server-rendered Django website with a premium donor-facing UI inspired by the Google Stitch redesign.

## Stack

- Python 3.9.23
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
python3.9 -m venv .venv
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
- For `ipadev.ng`, set:

```text
DJANGO_ALLOWED_HOSTS=ipadev.ng,www.ipadev.ng
DJANGO_CSRF_TRUSTED_ORIGINS=https://ipadev.ng,https://www.ipadev.ng
DJANGO_DEBUG=False
```

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

### cPanel / LiteSpeed Notes

The public site must be connected to the Django application, not an empty document root. In cPanel:

1. Open **Setup Python App** and create/select the app for `ipadev.ng`.
2. Set the app root to the deployed repository directory.
3. Set the startup file to `passenger_wsgi.py` and the callable to `application`.
4. Install `requirements/base.txt` in the app virtual environment.
5. Run:

```bash
python manage.py migrate --noinput
python manage.py seed_site
python manage.py collectstatic --noinput
```

6. In **SSL/TLS Status** or **AutoSSL**, issue a certificate that includes both `ipadev.ng` and `www.ipadev.ng`. The current browser error means the server is presenting a certificate for `ipadev.ng.hyrax.ng`, which cannot be fixed from Django code.
