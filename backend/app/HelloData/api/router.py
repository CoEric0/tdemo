#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 在app内引入api

from fastapi import APIRouter

from backend.app.HelloData.api.v1.items import router as items_router
from backend.app.HelloData.api.v1.price import router as price_router
from backend.app.HelloData.api.v1.helloworld import router as helloworld_router
# from backend.core.conf import settings

v1 = APIRouter()

v1.include_router(items_router)
v1.include_router(price_router)
v1.include_router(helloworld_router)
