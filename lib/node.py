class Node:
    def __init__(self, factory):
        self.funcs = factory()
        self.accept_list = []
        for x in dir(factory):
            if x[:2] != '__' and x != 'action':
                self.accept_list.append(x)

    # 执行函数
    def action(self, name="", *args):
        if name in self.accept_list:
            return getattr(self.funcs, name)(args)
        else:
            return '404 Not Found'
