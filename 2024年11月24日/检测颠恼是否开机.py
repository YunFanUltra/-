import tkinter
from ttkbootstrap import Style

style = Style(theme='sandstone')

login = tkinter.Tk()
login.title("login")
login.geometry("300x400+20+20")

def czmm():

    def czmm1():
        pw_rt = pw_r.get()


    login.destroy()

    czm = tkinter.Tk()
    czm.title("重置密码")
    czm.geometry("300x400+20+20")
    czm.iconbitmap("icon.ico")
    czm.wm_iconbitmap("icon.ico")

    czm_w1 = tkinter.Label(czm, text="账号", font=("Misans", 20), fg="black")
    czm_w1.pack()

    pw_r = tkinter.Entry(czm, font=("kaiti", 20))
    pw_r.pack()

    czm_w2 = tkinter.Label(czm, text="密码", font=("kaiti", 20), fg="black")
    czm_w2.pack()

    pw_r2 = tkinter.Entry(czm, font=("kaiti", 20))
    pw_r2.pack()

    czm_w3 = tkinter.Label(czm, text="重复密码", font=("kaiti", 20), fg="black")
    czm_w3.pack()

    pw_r3 = tkinter.Entry(czm, font=("kaiti", 20))
    pw_r3.pack()

    czm1 = tkinter.Button(czm, text="确认", font=("kaiti", 20), command=czmm1)
    czm1.pack()



def mainwin():
    windows = tkinter.Tk()
    windows.title("Hello world")
    windows.geometry("700x500+600+300")
    windows.iconbitmap("icon.ico")
    windows.wm_iconbitmap("icon.ico")

    l = tkinter.Label(windows, text="电脑是否开机检测器", font=("kaiti", 20), fg="black")
    l.pack()



    def button_jc_down():
        b.config(state="normal")
        c.config(state="disabled")
        d.config(state="normal")

    def button_jc_stop():
        b.config(state="disabled")
        c.config(state="normal")
        d.config(state="disabled")

    def button_exit():
        windows.destroy()


    def button_dn_down():
        l2 = tkinter.Label(windows, text="经检测，颠恼已开机", font=("kaiti", 20), fg="green")
        l2.pack()


    b = tkinter.Button(windows, text="点击进行测试颠恼是否开机", font=("youyan", 20), command=button_dn_down)
    b.config(state="disabled")
    b.pack()

    c = tkinter.Button(windows, text="开始", font=("youyan", 20), command=button_jc_down)
    c.config(state="normal")
    c.pack()

    d = tkinter.Button(windows, text="停止", font=("youyan", 20), command=button_jc_stop)
    d.config(state="disabled")
    d.pack()

    exitt = tkinter.Button(windows, text="退出", font=("youyan", 20), command=button_exit)
    exitt.pack()
    windows.mainloop()

def paser(tit, txt):
    pse = tkinter.Tk()
    pse.title("消息: "+tit)
    pse.geometry("300x100+400+300")
    wd1 = tkinter.Label(pse, text=txt, font=("kaiti", 20))
    wd1.pack()



def log():
    password = pw_s.get()
    username = un_s.get()
    if username == "1":
        if password == "1":
            login.destroy()
            paser("提示！", "登录成功！")
            mainwin()
        else:
            paser("错误！", "用户名或密码错误！")
    else:
        paser("错误", "用户名或密码错误")

un = tkinter.Label(login, text="用户名：", font=("kaiti", 20))
un.pack()

un_s = tkinter.Entry(login, font=("kaiti", 20))
un_s.pack()

pw = tkinter.Label(login, text="密码：", font=("kaiti", 20))
pw.pack()

pw_s = tkinter.Entry(login, font=("kaiti", 20))
pw_s.pack()

qrm = tkinter.Button(login, text="登录", font=("kaiti", 20), command=log)
qrm.pack()

error = tkinter.Label(login, text="用户名：", font=("kaiti", 20))
un.pack()

cznmm = tkinter.Button(login, text="重置账号密码", font=("kaiti", 20), command=czmm)
cznmm.pack()

login.mainloop()