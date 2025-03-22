# -*- coding: utf-8 -*-

# 引入各个app的相应api
from fastapi import APIRouter

from backend.app.HelloData.api.router import v1 as HelloData_v1

router = APIRouter()

router.include_router(HelloData_v1)