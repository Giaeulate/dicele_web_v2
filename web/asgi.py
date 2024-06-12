""" Asgi """
# pylint: disable=too-few-public-methods, missing-class-docstring, missing-function-docstring, unused-import, wrong-import-position
import os
from django.apps import apps
from django.conf import settings
from django.core.wsgi import get_wsgi_application
from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.wsgi import WSGIMiddleware
from starlette.middleware.cors import CORSMiddleware


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")
apps.populate(settings.INSTALLED_APPS)

from core.router import router as core_router
# from web.utils import JwtBearer
# from importlib.util import find_spec


# graphql
# import strawberry
# from strawberry.asgi import GraphQL
# from strawberry.tools import merge_types


def get_application() -> FastAPI:
    app_fastapi = FastAPI(title=settings.PROJECT_NAME, debug=settings.DEBUG,
                          openapi_url="/api/v1/openapi.json")

    app_fastapi.mount(
        "/static", StaticFiles(directory="static"), name="static")
    app_fastapi.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # app.include_router(core_router, prefix="/api/core", dependencies=[Depends(JwtBearer())])
    app_fastapi.include_router(
        core_router, prefix="/api/core", dependencies=[])
    app_fastapi.mount("/", WSGIMiddleware(get_wsgi_application()))

    return app_fastapi


app = get_application()
