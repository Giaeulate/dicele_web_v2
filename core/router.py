""" Router """
# pylint: disable=too-few-public-methods, unused-import, unused-wildcard-import, no-member, missing-function-docstring
import uuid
from fastapi import APIRouter, Body, Depends, HTTPException, Path
from django.contrib.auth import get_user_model
# from web.utils import JwtBearer
from web.helpers import convert_to_json
from .models_fastapi import LemaModel
from .models import Lema

router = APIRouter()


@router.get("/lemas", tags=["Lema"], summary="Get Lemas")
def get_lemas():
    return convert_to_json(Lema.objects.all())
