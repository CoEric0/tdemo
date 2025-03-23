from fastapi import FastAPI
from backend.core.conf import settings

# app注册器
def register_app():
    # FastAPI
    app = FastAPI(
        title=settings.PROJECT_NAME
    )

    # socketio
    # register_socket_app(app)

    # # 日志
    # register_logger()

    # # 静态文件
    # register_static_file(app)

    # # 中间件
    # register_middleware(app)

    # 路由
    register_router(app)

    # # 分页
    # register_page(app)

    # # 全局异常处理
    # register_exception(app)

    return app

# 其他注册器……

# 路由注册器
def register_router(app: FastAPI):
    # 插件路由

    # 本体路由
    from backend.app.router import router
    app.include_router(router)

    # Extra
    # 确保路由名称唯一
    # 简化api名称