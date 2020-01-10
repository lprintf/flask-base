from flask import request


class SubDemo:
    def demo(self, args):
        print('headers:', request.headers)
        print('args:', request.args)  # params
        print('cookies:', request.cookies)
        print('data:', request.data)  # json
        print('form:', request.form)  # form
        return f'This is a demo url return!\n{str(args)}'
