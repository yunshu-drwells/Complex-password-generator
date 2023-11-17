# 导入所需的模块
import wx
import sys
import time
import itertools
import pyperclip
from threading import Thread
import get_any_length_dict_to_crack_code as code


# 定义一个窗口类，继承自wx.Frame
class MyFrame(wx.Frame):
    def __init__(self):
        # 调用父类的构造函数，设置窗口标题和大小
        super().__init__(None, title="Complex password generator", size=(800, 560))
        # 设置窗口居中显示
        self.Center()
        # 创建一个面板，作为窗口的容器
        panel = wx.Panel(self)

        # 创建一个静态文本，显示提示信息
        label_len = wx.StaticText(panel, label="请选择一个密码长度：")
        # 创建一个下拉列表框，显示所有密码长度
        self.pwd_len = list(range(1, 257))
        self.choice_pwd_len = wx.Choice(panel, choices=["{}".format(i) for
                                                    i in self.pwd_len])
        self.choice_pwd_len.SetSelection(7)

        self.pwd_lens = [94, 10, 32, 52, 26, 26, 62, 36, 36, 84, 58, 58, 42]  # 各种长度及密码组合的个数
        label_type = wx.StaticText(panel, label="请选择一个密码字符集：")
        # 创建一个下拉列表框，显示所有密码字符集
        self.pwd_type = ["大小写字母+数字+符号", "数字", "符号", "大小写字母", "大写字母", "小写字母", "大小写字母+数字", "大写字母+数字", "小写字母+数字",
                         "大小写字母+符号", "大写字母+符号", "小写字母+符号", "数字+符号"]
        self.choice_pwd_type = wx.Choice(panel, choices=["{}".format(i) for
                                                        i in self.pwd_type])
        self.choice_pwd_type.SetSelection(0)

        # 创建一个静态文本，显示提示信息
        self.label_pwd = wx.StaticText(panel, label="password will show here                   ")
        button_label_pwd_copy = wx.Button(panel, label="复制到剪贴板")
        button_label_pwd_copy.Bind(wx.EVT_BUTTON, self.button_label_pwd_copy)
        # 按钮
        button0 = wx.Button(panel, label="随机生成")
        # 绑定按钮的点击事件，调用on_connect方法
        button0.Bind(wx.EVT_BUTTON, self.generator0_0)

        # 创建一个静态文本，显示提示信息
        label_pwd_len = wx.StaticText(panel, label="请输入要生成的密码长度：")
        self.input_label_pwd_len = wx.TextCtrl(panel, style=wx.TEXT_ATTR_LINE_SPACING)
        label_password = wx.StaticText(panel, label="请输入密钥：")
        self.input_password = wx.TextCtrl(panel, style=wx.TEXT_ATTR_LINE_SPACING)
        label_salt = wx.StaticText(panel, label="请输入盐值：")
        self.input_salt = wx.TextCtrl(panel, style=wx.TEXT_ATTR_LINE_SPACING)
        button1 = wx.Button(panel, label="时间戳迭代次哈希法生成")
        # 绑定按钮的点击事件，调用on_connect方法
        button1.Bind(wx.EVT_BUTTON, self.generator1)
        self.label_1 = wx.StaticText(panel, label="password will show here                   ")
        button_label_1_copy = wx.Button(panel, label="复制到剪贴板")
        button_label_1_copy.Bind(wx.EVT_BUTTON, self.button_label_1_copy)

        # 分隔线
        line0 = wx.StaticLine(panel, style=wx.LI_HORIZONTAL, size=(300, 5))  # size:长，宽

        # 创建一个静态文本，显示提示信息
        self.label_2 = wx.StaticText(panel, label="password will show here                   ")
        label_2_str = wx.StaticText(panel, label="无口令输入，则使用随机口令，支持生成最长64位长度的密码")
        button_label_2_copy = wx.Button(panel, label="复制到剪贴板")
        button_label_2_copy.Bind(wx.EVT_BUTTON, self.button_label_2_copy)
        label_str = wx.StaticText(panel, label="请输入口令：")
        # 输入框 （密码）
        self.input0 = wx.TextCtrl(panel, style=wx.TEXT_ATTR_LINE_SPACING)
        button2 = wx.Button(panel, label="口令哈希密码生成")
        # 绑定按钮的点击事件，调用on_connect方法
        button2.Bind(wx.EVT_BUTTON, self.generator2)

        hbox0 = wx.BoxSizer(wx.HORIZONTAL)
        hbox0.Add(label_len, 40, wx.EXPAND | wx.ALL, 5)
        hbox0.Add(self.choice_pwd_len, 100, wx.EXPAND | wx.ALL, 5)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(label_type, 40, wx.EXPAND | wx.ALL, 5)
        hbox1.Add(self.choice_pwd_type, 100, wx.EXPAND | wx.ALL, 5)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(self.label_pwd, 80, wx.EXPAND | wx.ALL, 5)

        hbox2_0 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2_0.Add(button0, 50, wx.EXPAND | wx.ALL, 5)
        hbox2_0.Add(button_label_pwd_copy, 50, wx.EXPAND | wx.ALL, 5)

        hbox2_3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2_3.Add(label_pwd_len, 40, wx.EXPAND | wx.ALL, 5)
        hbox2_3.Add(self.input_label_pwd_len, 100, wx.EXPAND | wx.ALL, 5)
        hbox2_1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2_1.Add(label_password, 40, wx.EXPAND | wx.ALL, 5)
        hbox2_1.Add(self.input_password, 100, wx.EXPAND | wx.ALL, 5)
        hbox2_2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2_2.Add(label_salt, 40, wx.EXPAND | wx.ALL, 5)
        hbox2_2.Add(self.input_salt, 100, wx.EXPAND | wx.ALL, 5)

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3.Add(self.label_1, 80, wx.EXPAND | wx.ALL, 5)

        hbox3_0 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3_0.Add(button1, 50, wx.EXPAND | wx.ALL, 5)
        hbox3_0.Add(button_label_1_copy, 50, wx.EXPAND | wx.ALL, 5)

        hbox3_2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3_2.Add(line0, 50, wx.EXPAND | wx.ALL, 5)

        hbox3_1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3_1.Add(self.label_2, 80, wx.EXPAND | wx.ALL, 5)
        hbox3_1.Add(label_2_str, 10, wx.EXPAND | wx.ALL, 5)

        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        hbox4.Add(label_str, 10, wx.EXPAND | wx.ALL, 5)
        hbox4.Add(self.input0, 100, wx.EXPAND | wx.ALL, 5)

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        hbox5.Add(button2, 50, wx.EXPAND | wx.ALL, 5)
        hbox5.Add(button_label_2_copy, 50, wx.EXPAND | wx.ALL, 5)

        # 创建一个垂直方向的盒子布局管理器，添加水平布局管理器和按钮，并设置间距和对齐方式
        vbox = wx.BoxSizer(wx.VERTICAL)

        vbox.Add(hbox2_3, 0, wx.EXPAND | wx.ALL, 5)
        vbox.Add(hbox2_1, 0, wx.EXPAND | wx.ALL, 5)
        vbox.Add(hbox2_2, 0, wx.EXPAND | wx.ALL, 5)
        vbox.Add(hbox3, 0, wx.EXPAND | wx.ALL, 5)
        vbox.Add(hbox3_0, 0, wx.EXPAND | wx.ALL, 5)
        vbox.Add(hbox3_2, 0, wx.EXPAND | wx.ALL, 5)
        vbox.Add(hbox0, 0, wx.EXPAND | wx.ALL, 5)
        vbox.Add(hbox4, 0, wx.EXPAND | wx.ALL, 5)
        vbox.Add(hbox3_1, 0, wx.EXPAND | wx.ALL, 5)
        vbox.Add(hbox5, 0, wx.EXPAND | wx.ALL, 5)
        vbox.Add(hbox1, 0, wx.EXPAND | wx.ALL, 5)
        vbox.Add(hbox2, 0, wx.EXPAND | wx.ALL, 5)
        vbox.Add(hbox2_0, 0, wx.EXPAND | wx.ALL, 5)

        # 设置面板的布局管理器为垂直布局管理器
        panel.SetSizer(vbox)
        # 定义一个方法，用于处理按钮的点击事件

    def on_close(self, event):
        print("on_close, The frame is closing")
        # 在这里执行一些自定义的操作
        event.Skip()  # 让默认的关闭行为继续执行s

    def generator0(self, event):
        try:
            t = Thread(target=self.generator0_)
            t.daemon = True
            t.start()

        except:
            print("on_connect Error: unable to start thread")

    def generator0_(self):
        # 密码长度和密码类型
        len_index = self.choice_pwd_len.GetSelection()
        len = int(self.choice_pwd_len.GetString(len_index))
        type_index = self.choice_pwd_type.GetSelection()
        generator = code.password_generator(len, type_index)
        # 获取时间戳
        timestamp = int(time.time())
        # 判断时间戳有没有超出字典中的所有密码数量，超过就取模
        timestamp = timestamp % (self.pwd_lens[type_index]**len)
        pwd = ""
        while timestamp:
            pwd = next(generator, None)
            timestamp -= 1

        # pwd = next(itertools.islice(generator, timestamp, timestamp+1), None)
        # new_generator = itertools.islice(generator, 1700111415, None)
        # pwd = next(new_generator, None)
        # itertools.islice(generator, timestamp, timestamp+1)会创建一个新的迭代器，它从generator的第timestamp个元素开始，到第timestamp+1个元素结束
        # 然后，next()函数会返回这个迭代器的下一个元素，也就是第timestamp个元素
        self.label_pwd.SetLabel(pwd)

    def generator0_0(self, event):
        # 密码长度和密码类型
        len_index = self.choice_pwd_len.GetSelection()
        len = int(self.choice_pwd_len.GetString(len_index))
        type_index = self.choice_pwd_type.GetSelection()
        pwd = code.generate_password(len, type_index)
        # 然后，next()函数会返回这个迭代器的下一个元素，也就是第timestamp个元素
        self.label_pwd.SetLabel(pwd)

    def generator1(self, event):
        # 密码长度
        if self.input_label_pwd_len.GetValue() == "":
            len_index = self.choice_pwd_len.GetSelection()
            len = int(self.choice_pwd_len.GetString(len_index))
        else:
            len = int(self.input_label_pwd_len.GetLineText(0))
        # 获取时间戳
        timestamp = int(time.time())
        password = "my_password"
        salt = "my_salt"
        # 获取password和salt
        pas = self.input_password.GetLineText(0)
        sal = self.input_salt.GetLineText(0)
        if pas != "":
            password = pas
        if sal != "":
            salt = sal
        # hashlib生成任意长度复杂密码
        iterations = timestamp % 1000
        key_length = len
        pwd = code.hash_password(password, salt, iterations, key_length)
        self.label_1.SetLabel(pwd)

    def generator2(self, event):
        # 密码长度
        len_index = self.choice_pwd_len.GetSelection()
        len = int(self.choice_pwd_len.GetString(len_index))
        if self.input0.GetValue() == "":
            str = code.generate_password(len, 0)
        else:
            str = self.input0.GetLineText(0)
        # 基于口令的密码生成器
        pwd = code.generate_password_by_str(str, len)
        self.label_2.SetLabel(pwd)

    def button_label_pwd_copy(self, event):
        pwd = self.label_pwd.GetLabel()
        # 拷贝到剪贴板
        pyperclip.copy(pwd)

    def button_label_1_copy(self, event):
        pwd = self.label_1.GetLabel()
        # 拷贝到剪贴板
        pyperclip.copy(pwd)

    def button_label_2_copy(self, event):
        pwd = self.label_2.GetLabel()
        # 拷贝到剪贴板
        pyperclip.copy(pwd)

# 定义一个应用程序类，继承自wx.App
class MyApp(wx.App):
    def OnInit(self):
        # 创建窗口对象并显示
        frame = MyFrame()
        frame.Show()
        return True

    def loop(self):
        print("hello")

    # 重构 def closeEvent(self, event)——在UI线程销毁的时候，需要把后台线程也销毁掉
    def closeEvent(self, event):
        # self.stop_event.set()
        sys.exit(app.exec_())


# 如果是主模块，则运行应用程序对象的主循环
if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()

# 加密方式
'''
- **WEP**（Wired Equivalent Privacy）：这是最早的一种Wifi加密协议，它使用相同的密钥对数据进行加密和解密，属于对称加密¹。但是，由于WEP的密钥容易被破解，它已经被认为是不安全的，不建议使用²。
- **WPA**（Wi-Fi Protected Access）：这是一种改进的Wifi加密协议，它使用动态的密钥分配和认证机制，提高了数据的安全性。WPA有两个版本，分别是WPA-Personal（适用于个人和家庭用户）和WPA-Enterprise（适用于企业和组织用户）²。
- **WPA2**：这是WPA的升级版，它使用了更高级的加密算法（AES）和更强大的认证协议（802.1X），提供了更高的安全性。WPA2也有两个版本，分别是WPA2-Personal和WPA2-Enterprise²。
- **WPA3**：这是最新的一种Wifi加密协议，它在WPA2的基础上增加了更多的安全特性，例如更强的密码保护、更好的隐私保护、更高的加密强度等。WPA3同样有两个版本，分别是WPA3-Personal和WPA3-Enterprise³。
'''
