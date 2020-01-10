from flask import request
from lib.node import Node
from middle.sub_demo import SubDemo


class Root:
    # region 用户自定义函数区域
    def __init__(self):
        self.sub_demo = Node(SubDemo)
        pass

    @staticmethod
    def demo(args):
        form = request.form.to_dict()
        except_keys = ['argument1', 'argument2']
        real_keys = form.keys()
        attachment = request.files.get("attachment")
        if except_keys == list(real_keys) and attachment is not None:
            return
        else:
            print(args)
            print(form)
            return {'code': 500, 'msg': '参数错误'}

    @staticmethod
    def data_demo(args):
        print('headers:', request.headers)
        print('args:', request.args)  # params
        print('cookies:', request.cookies)
        print('data:', request.data)  # json
        print('form:', request.form)  # form
        return f'This is a demo url return!\n{str(args)}'

    def sub_demo(self, args):
        form = request.form.to_dict()
        except_keys = ['argument1', 'argument2']
        real_keys = form.keys()
        if except_keys == list(real_keys):
            return {'code': 200, 'msg': '参数错误', 'data': 1000}
        else:
            print(form)
            return self.sub_demo.action(*args)


    # endregion
