from fastapi import FastAPI
from fastapi_amis_admin.admin import AdminApp


def setup(app: FastAPI):
    # 1. 导入管理应用
    # 2. 注册普通路由
    from . import admin, apis, events

    app.include_router(apis.router)
