import os

from pathlib import Path

# 获取项目根目录
# 或使用绝对路径，指到backend目录为止，例如windows：BasePath = D:\git_project\fastapi_mysql\backend
BasePath = Path(__file__).resolve().parent.parent

# alembic 迁移文件存放路径
ALEMBIC_VERSION_DIR = os.path.join(BasePath, 'alembic', 'versions')

# 日志文件路径
LOG_DIR = os.path.join(BasePath, 'log')

# 离线 IP 数据库路径
IP2REGION_XDB = os.path.join(BasePath, 'static', 'ip2region.xdb')

# 静态资源目录
STATIC_DIR = os.path.join(BasePath, 'static')

# 上传文件目录
UPLOAD_DIR = os.path.join(BasePath, 'static', 'upload')

# jinja2 模版文件路径
JINJA2_TEMPLATE_DIR = os.path.join(BasePath, 'templates')

# 插件目录
PLUGIN_DIR = os.path.join(BasePath, 'plugin')