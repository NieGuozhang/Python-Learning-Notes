'''面向对象：'''# 所有的类名要求首字母大写，多个单词使用驼峰式命名方法# ValueError TypeError StopIterable'''class 类名[(父类)]:    属性：特征    方法：动作'''# 类中方法：动作# 种类：普通方法，类方法，静态方法，魔术方法'''普通方法格式:def 方法名（self,[参数名...]）:    pass'''class Phone:    # 属性    brand = 'xiaomi'    price = '4999'    type = 'xiaomi 10'    # phone类里面方法：call    def call(self):        print('self', self)        print('正在访问通讯录：')        for person in self.address_book:            print(person.items())        print('正在打电话...')        print('留言:', self.note)phone1 = Phone()phone1.note = '我是phone1的note'phone1.address_book = [{"17720524450": "聂国章"}, {"17722222222": '张三'}]print(phone1, '1')phone1.call()print('*' * 20)phone2 = Phone()phone2.note = '我是phone222222的note'phone2.address_book = [{'17720524451': '王五'}, {'17722222262': '李二'}]print(phone2, '2')phone2.call()