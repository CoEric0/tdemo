|--app/ 
    |--子包 1       项目主目录（只有一个app）
        |--api/         API目录，如路由、控制器 。      视图/controller
            |--v1/
                |               各个功能的路由实现（可以根据功能继续划分），主要负责调用services
        |--models/      数据库模型目录                 数据库/model/entity,负责数据持久化（数据库结构-类 对应关系）
        |--cruds/       CRUD：创建、读取、更新、删除）  数据库访问/dao/mapper，model和schema定义后在此使用
        |--schemas/     数据模型验证,请求响应验证。     数据传输/dto，数据的响应模式，定义API输入、输出格式，在“API-内部”间检查并转化数据
        |--services/    业务逻辑目录。                 业务逻辑/service+impl，负责调用CRUD+其他逻辑
|
|
|--common/      抽象模型，通用常量等
|--utils/       工具目录
|--core/        核心目录，如配置、安全、register
|--databse/     数据库基础设置
|
|
|--main.py    入口文件，引入app
