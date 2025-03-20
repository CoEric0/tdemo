|--app/ 
    |--子包 1       项目主目录（只有一个app）
        |--api/         API目录，如路由、控制器 。      视图/controller
            |--v1/
                |               各个功能的路由实现（可以根据功能继续划分）
        |--models/      数据模型目录                   数据库/model/entity
        |--cruds/       CRUD：创建、读取、更新、删除）  数据库访问/dao/mapper
        |--schemas/     数据模型验证,请求响应验证。     数据传输/dto
        |--services/    业务逻辑目录。                 业务逻辑/service+impl
|
|
|--utils/       工具目录
|--core/        核心目录，如配置、安全、register
|--databse/     数据库基础设置
|
|
|--main.py    入口文件，引入app
