""" Fastapi Model """
# pylint: disable=too-few-public-methods, missing-class-docstring, protected-access, no-member, wildcard-import, unused-wildcard-import
# from typing import Optional
from pydantic import BaseModel


class AutoDateTimeAbstract(BaseModel):
    id: int
    active: bool
    created: str
    updated: str


class LemaModel(AutoDateTimeAbstract):
    name: str
    regular_form: str
