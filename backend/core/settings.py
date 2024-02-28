import os
import sys
from pathlib import Path
from typing import List, Optional

from fastapi_amis_admin.admin.settings import Settings as AmisSettings


BACKEND_DIR = Path(__file__).resolve().parent.parent
sys.path.append(BACKEND_DIR.__str__())

class Settings(AmisSettings):
    name: str = 'Hr'
    host: str = '127.0.0.1'
    port: int = 8000
    secret_key: str = ''
    allow_origins: Optional[List[str]] = None
    language: str = "en_US"

# 设置FAA_GLOBALS环境变量
os.environ.setdefault("FAA_GLOBALS", "core.globals")

settings = Settings(_env_file=os.path.join(BACKEND_DIR, '.env'))
