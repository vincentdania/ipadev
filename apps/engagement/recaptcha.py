import json
import logging
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from django.conf import settings

logger = logging.getLogger(__name__)


def recaptcha_is_configured():
    return bool(settings.RECAPTCHA_SITE_KEY and settings.RECAPTCHA_SECRET_KEY)


def verify_recaptcha(token, remote_ip=None):
    if settings.DEBUG and not recaptcha_is_configured():
        return True

    if not settings.RECAPTCHA_SECRET_KEY:
        logger.warning("reCAPTCHA secret key is not configured.")
        return False

    if not token:
        return False

    payload = {
        "secret": settings.RECAPTCHA_SECRET_KEY,
        "response": token,
    }
    if remote_ip:
        payload["remoteip"] = remote_ip

    request = Request(
        settings.RECAPTCHA_VERIFY_URL,
        data=urlencode(payload).encode(),
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        method="POST",
    )

    try:
        with urlopen(request, timeout=5) as response:
            result = json.loads(response.read().decode("utf-8"))
    except (OSError, URLError, ValueError):
        logger.exception("Unable to verify reCAPTCHA response.")
        return False

    return bool(result.get("success"))
