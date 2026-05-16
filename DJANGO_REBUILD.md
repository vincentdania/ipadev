# IPADEV Django Deployment Notes

The legacy React, PHP, OctoberCMS, and Strapi artifacts have been removed. Django is now the confirmed deployment target.

## First Deployment Checklist

1. Create a Python 3.9.23 environment.
2. Install dependencies:

```bash
pip install -r requirements/base.txt
```

3. Configure `.env` from `.env.example`.
4. Run migrations:

```bash
python manage.py migrate
```

5. Seed initial editable content:

```bash
python manage.py seed_site
```

6. Create admin user:

```bash
python manage.py createsuperuser
```

7. Collect static files:

```bash
python manage.py collectstatic --noinput
```

8. Start Gunicorn and Celery:

```bash
gunicorn config.wsgi:application
celery -A config worker --loglevel=info
```

## Required Services

- PostgreSQL
- Redis
- SMTP account for contact notifications
- Optional S3-compatible media storage

## Notes

The contact form saves submissions even if Redis/Celery is temporarily unavailable. Notification queue failures are logged so user submissions are not lost.
