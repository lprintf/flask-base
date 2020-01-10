from flask import Flask
from lib.node import Node
from node.root import Root

app = Flask(__name__)
app.config.from_pyfile('config.py')
root = Node(Root)


@app.route('/root/<path:sub_path>', methods=['POST', 'GET'])
def mail(sub_path):
    args = sub_path.split('/')
    return root.action(*args)


if __name__ == '__main__':
    app.run(host=app.config['HOST'],
            port=app.config['PORT'],
            debug=app.config['DEBUG'])

# 解决部分端口不能作为http端口
# sudo semanage port -l | grep http_port_t
# sudo semanage port -a -t http_port_t  -p tcp 8024
# setsebool -P httpd_can_network_connect 1

# 生产环境部署
# nohup /venvs/flask/bin/uwsgi --socket 0.0.0.0:8000 --protocol=http -w server:app &

# 邮箱配置
# export SECURITY_EMAIL_SENDER='545641826@qq.com'

# 常用命令
# export py=/venvs/flask/bin/
# cd /projects/flask/
# ${py}python wsgi.py
# http://192.168.169.16:8000/root/
