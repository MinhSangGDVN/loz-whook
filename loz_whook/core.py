import os
import traceback
import requests
from datetime import datetime
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(usecwd=True))

# -*- coding: utf-8 -*-
# Copyright (c) 2026 Minh Sang. All rights reserved.
# Licensed under the MIT License. See LICENSE file in the project root for full license information.
# Github: https://github.com/MinhSangGDVN/loz-whook

def _send_webhook(embeds):
    webhook_url = os.getenv("LOZ_WHOOK_URL")
    webhook_username = os.getenv("LOZ_WHOOK_NAME", "loz-whook")
    webhook_avatar = os.getenv("LOZ_WHOOK_AVATAR")
    if not webhook_url:
        print("[loz-whook] ⚠️ WARNING: LOZ_WHOOK_URL has not been configured in the .env file")
        return
    payload = {
        "username": webhook_username,
        "embeds": embeds
    }
    if webhook_avatar:
        payload["avatar_url"] = webhook_avatar
    try:
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()
    except Exception as e:
        print(f"[loz-whook] ❌ Error submitting webhook: {e}")
def log_error(exc: Exception, context: str = "Unhandled Exception"):
    tb_str = "".join(traceback.format_exception(type(exc), exc, exc.__traceback__))
    if len(tb_str) > 3667:
        tb_str = tb_str[:3667] + "\n...[TRUNCATED]"
    embed = {
        "title": "🚨 System Error Warning",
        "description": f"**Context:** {context}\n```python\n{tb_str}\n```",
        "color": 16711680,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "footer": {
            "text": f"pip install loz-whook • loz-whook Monitor by MinhSangGD"
        }
    }
    _send_webhook([embed])
def log(message: str, title: str = "📝 Custom Log", color: int = 3447003):
    embed = {
        "title": title,
        "description": message,
        "color": color, 
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "footer": {
            "text": "pip install loz-whook • loz-whook Monitor by MinhSangGD"
        }
    }
    _send_webhook([embed])
def monitor(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            log_error(e, context=f"Function: `{func.__name__}`")
            raise e
    return wrapper