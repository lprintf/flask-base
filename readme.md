# flask-base

flask API服务器,待完善的试验框架,刚接触的开发者只需修改node/main文件的内容.对框架深入了解后可进行路由节点嵌套等工程化操作. 

---


## 开发规则

函数名即路由名,用户不需要定义路由. 

根路由为tide/.根路由不为空对端口复用有重要意义.

requirements.txt存在前瞻性必须模块,直接pip install便可,请谨慎修改.

### 模块依赖讨论区
```txt
Jinja2模块可以删下试试,毕竟api服务器似乎用不到.
py-ecc模块是椭圆曲线加密的,效率很低,实验用的,可以删.
flask-jwt模块过度封装,实验后舍弃,使用py-jwt代替但暂未应用.
mongo-engine是对pymogo的封装,用起来很麻烦,考虑要不要集成,毕竟pymongo简单易用.
```

## 运行

开发环境`python server.py`

生产环境下需去掉server中的debug参数,并使用wsgi运行,自带wsgi和django半斤八两.
`nohup /venvs/flask/bin/uwsgi --socket 0.0.0.0:8000 --protocol=http -w wsgi:app &`

## 安全

应严格区分公用成员和私有成员,不想被前端直接访问的成员必须以"__"开头.(本项目暂时没注意这点)

## 迭代方向

- 集成JWT

- 集成ODM

- 优化Debug面板配置

- 集成自动化测试

- 进一步优化代码风格

- 快速容器化应用

- 收尾,总结框架开发流程,整理文档模板,编写自动化脚本.