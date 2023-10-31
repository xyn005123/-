# 来自github，用于获取屏幕真实分辨率
import sys

from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
screen_resolution = app.desktop().screenGeometry()
Res_xs, Res_ys = screen_resolution.width(), screen_resolution.height()
Res_x = int(Res_xs)  # 屏幕真实分辨率
Res_y = int(Res_ys)
win_pix_x = int(Res_x * 0.6)  # 窗口分辨率
win_pix_y = int(Res_y * 0.6)
win_pix_xs = int(Res_x * 0.5 - win_pix_x * 0.5)
win_pix_ys = int(Res_y * 0.5 - win_pix_y * 0.5)

# 变量设定区（废弃）
"""
num = [None]  # 排序编号
name = [None]  # 姓名
ID = [None]  # 内部编号
gender = [None]  # 性别
num_phone = [None]  # 手机号
other = [None]  # 其他信息
"""
word = ["默认内容", "提示", "未检索到目标信息"]  # 文字显示框的文字 # 提示框的文字

# 导入数据
num_txt = open("num.txt", "r", encoding="UTF-8")
name_txt = open("name.txt", "r", encoding="UTF-8")
ID_txt = open("ID.txt", "r", encoding="UTF-8")
gender_txt = open("gender.txt", "r", encoding="UTF-8")
num_phone_txt = open("num_phone.txt", "r", encoding="UTF-8")
other_txt = open("other.txt", "r", encoding="UTF-8")
num = num_txt.readlines()
name = name_txt.readlines()
ID = ID_txt.readlines()
gender = gender_txt.readlines()
num_phone = num_phone_txt.readlines()
other = other_txt.readlines()


# 函数编写区
def main():
    return None


def f1():  # “添加”的主函数
    a = len(num)
    # print(a)
    hide()
    f1_1()
    word[1] = "输入姓名"
    wor2.set(str(f"{word[1]}"))

    def f1a():  # f1a-f1e为“添加”的逻辑函数，用于进行添加数据
        num.append(str(a + 1))
        name.append(ent.get())
        word[1] = "编写ID"
        wor2.set(str(f"{word[1]}"))
        but_f1_con.config(command=f1b)
        return None

    but_f1_con.config(command=f1a)

    def f1b():
        ID.append(ent.get())
        word[1] = "输入性别"
        wor2.set(str(f"{word[1]}"))
        but_f1_con.config(command=f1c)
        return None

    def f1c():
        gender.append(ent.get())
        word[1] = "输入手机号"
        wor2.set(str(f"{word[1]}"))
        but_f1_con.config(command=f1d)
        return None

    def f1d():
        num_phone.append(ent.get())
        word[1] = "输入其他信息"
        wor2.set(str(f"{word[1]}"))
        but_f1_con.config(command=f1e)
        return None

    def f1e():
        other.append(ent.get())
        word[1] = "......"
        wor2.set(str(f"{word[1]}"))
        f1f()
        but_f1_con.config(command=f1f)
        return None

    def f1f():  # 本函数用于防止用户忘记清空文字框
        bq1 = ID[a]
        if ID[a] == name[a] or ID[a] is "":
            ID.pop(a - 1)
            ID.append("暂无")
        bq2 = gender[a]
        if gender[a] == bq1 or gender[a] is "":
            gender.pop(a - 1)
            gender.append("暂无")
        bq1 = num_phone[a]
        if num_phone[a] == bq2 or num_phone[a] is "":
            num_phone.pop(a - 1)
            num_phone.append("暂无")

        if other[a] == bq1 or other[a] is "":
            other.pop(a - 1)
            other.append("暂无")
        if True:
            print(ID[a])
            print(gender[a])

        return None

    win.update()

    return None


def f2():
    hide()
    f2_1()
    # name_txt = open("name.txt", "a", encoding="UTF-8")
    # name_txt.write("\n老八")
    # name_txt.flush()
    word[1] = "输入姓名进行检索"
    wor2.set(str(f"{word[1]}"))

    def f2s():
        temp_ent = ent.get()
        temp_int = int(name.index(temp_ent))
        word[1] = f"确认删除{temp_ent}?\n(如果{temp_ent}存在的话)"
        wor2.set(str(f"{word[1]}"))

        def f2ss():
            num.pop(temp_int)
            name.pop(temp_int)
            ID.pop(temp_int)
            gender.pop(temp_int)
            num_phone.pop(temp_int)
            other.pop(temp_int)

        but_f2_con.config(command=f2ss)
        return None

    but_f2_con.config(command=f2s)

    return None


def f3():
    hide()
    f3_1()
    word[1] = f"输入姓名检索"
    wor2.set(str(f"{word[1]}"))

    def f3s():
        temp_ent = ent.get()
        temp_int = int(name.index(temp_ent))
        ids = ID[temp_int]
        genders = gender[temp_int]
        num_phones = num_phone[temp_int]
        others = other[temp_int]
        word[1] = f"更改id"
        wor2.set(str(f"{word[1]}"))

        def f3s1():
            ID.insert(temp_int, ent.get())
            word[1] = "输入性别"
            wor2.set(str(f"{word[1]}"))
            but_f3_con.config(command=f3s2)
            return None

        but_f3_con.config(command=f3s1)

        def f3s2():
            gender.insert(temp_int, ent.get())
            word[1] = "输入手机号"
            wor2.set(str(f"{word[1]}"))
            but_f3_con.config(command=f3s3)
            return None

        def f3s3():
            num_phone.insert(temp_int, ent.get())
            word[1] = "输入其他信息"
            wor2.set(str(f"{word[1]}"))
            but_f3_con.config(command=f3s4)
            return None

        def f3s4():
            other.insert(temp_int, ent.get())
            word[1] = "......"
            wor2.set(str(f"{word[1]}"))
            f3f()
            but_f3_con.config(command=f3f)

        def f3f():
            bq1 = ID[temp_int]
            if ID[temp_int] == name[temp_int]:
                ID.pop(temp_int - 1)
                ID.append(ids)
            bq2 = gender[temp_int]
            if gender[temp_int] == bq1:
                gender.pop(temp_int - 1)
                gender.append(genders)
            bq1 = num_phone[temp_int]
            if num_phone[temp_int] == bq2:
                num_phone.pop(temp_int - 1)
                num_phone.append(num_phones)

            if other[temp_int] == bq1:
                other.pop(temp_int - 1)
                other.append(others)
            if True:
                print(other[temp_int])
                print(gender[temp_int])

            return None

        return None

    but_f3_con.config(command=f3s)
    return None


def f4():
    hide()
    f4_1()
    word[1] = "输入姓名检索\n（导出以查看完整信息）"
    wor2.set(str(f"{word[1]}"))
    return None


def f5():
    hide()
    f5_1()

    def f5s():
        g = int(ent.get())
        if g == 1:
            f1()
        elif g == 2:
            f2()
        elif g == 3:
            f3()
        elif g == 4:
            f4()
        return None

    but_f5_con.config(command=f5s)
    return None


def fin():  # 脱离卡死函数
    pre()
    sys.exit(1)
    # quit()


def pre():
    num_txt = open("num.txt", "w", encoding="UTF-8")
    name_txt = open("name.txt", "w", encoding="UTF-8")
    ID_txt = open("ID.txt", "w", encoding="UTF-8")
    gender_txt = open("gender.txt", "w", encoding="UTF-8")
    num_phone_txt = open("num_phone.txt", "w", encoding="UTF-8")
    other_txt = open("other.txt", "w", encoding="UTF-8")
    a = len(num)
    c = 0
    while c < a:
        num_txt.write(num[c])
        name_txt.write(name[c])
        ID_txt.write(ID[c])
        gender_txt.write(gender[c])
        num_phone_txt.write(num_phone[c])
        other_txt.write(other[c])
        num_txt.flush()
        name_txt.flush()
        ID_txt.flush()
        gender_txt.flush()
        num_phone_txt.flush()
        other_txt.flush()
        c += 1
    return None


def hide():
    but_f1_con.place_forget()
    but_f2_con.place_forget()
    but_f3_con.place_forget()
    lab.place_forget()
    labs.place_forget()
    lab_b.place_forget()
    but_f5_con.place_forget()
    return None


b = []
e = [""]


def show():
    a = len(num)
    print(a)
    c = 0
    # d = 0
    while c < a:
        b.append(name[c])
        # d += 1
        b.append(ID[c])
        # d += 1
        b.append(gender[c])
        # d += 1
        b.append(num_phone[c])
        # d += 1
        b.append(other[c])
        # d += 1
        c += 1
        print(a)
    print(7)

    def shows():
        a = 5 * len(num)
        c = 0
        es = ""
        while c < a:
            es = f"{es} \n {b[c]}"
            e[0] = es
            c += 1
        return None

    shows()
    return None


show()


def Import():
    pre()
    show()
    txt = open("D:/信息.txt", "w", encoding="UTF-8")
    txt.write(e[0])
    txt.flush()
    return None


# GUI编写区
import tkinter as tki

win = tki.Tk()  # 窗口管理区
win.title("结课作业")
win.geometry(f"{win_pix_x}x{win_pix_y}+{win_pix_xs}+{win_pix_ys}")

print(6)
# img = tki.PhotoImage(file="测试.9.png")

wor1 = tki.StringVar()  # 可变字符串
wor1.set(str(f"{word[0]}"))
wor2 = tki.StringVar()
wor2.set(str(f"{word[1]}"))
wor3 = tki.StringVar()
wor3.set(str(f"{word[2]}"))
fig = tki.IntVar()  # 可变数字，用于f3及其子函数
fig.set(int())
scr = tki.Scrollbar(win, )

labs = tki.Label(win,  # 首页显示标签组件
                 bg="#bebebe",
                 text="欢迎使用学生信息管理系统\n本程序使用Python编写\n\n\n\n\n\n\n点击功能菜单使用本程序",
                 font=("", 18),
                 width=50,
                 height=15,
                 anchor="n")
lab_a = tki.Label(win,  # 操作提示标签组件
                  textvariable=wor2,
                  bg="#76cafe",
                  width=35,
                  height=2,
                  )
lab = tki.Label(win,  # 数据显示标签组件
                bg="#bebebe",
                width=40,
                height=5000,
                text=e[0],
                anchor="nw",
                )
lab_b = tki.Label(win,
                  text="1.添加\n2.删除\n3.修改\n4.查看",
                  bg="#bebebe")

ent = tki.Entry(win)  # 文本框

men = tki.Menu(win)  # 菜单编写区
mens1 = tki.Menu(men)
mens2 = tki.Menu(men)
mens1.add_command(label="1添加", command=f1)
mens1.add_command(label="2删除", command=f2)
mens1.add_command(label="3修改", command=f3)
mens1.add_command(label="4查看", command=f4)
mens1.add_command(label="使用编号模式", command=f5)
mens2.add_command(label="导出为txt", command=Import)
mens2.add_command(label="关于", )
men.add_cascade(label="功能菜单", menu=mens1)
men.add_cascade(label="更多", menu=mens2)

but_f1_con = tki.Button(win,  # 添加界面的确认按钮
                        text="确认添加")
but_f2_con = tki.Button(win,
                        text="确认删除")
but_f3_con = tki.Button(win,
                        text="确认修改")
but_f4_con = tki.Button(win,
                        text="确认搜索")
but_f5_con = tki.Button(win,
                        text="确认")
redi_f3_s1 = tki.Radiobutton(win,
                             text="姓名",
                             value="", )
# variable=a
but_fin = tki.Button(win,  # 脱离卡死按钮
                     text="保存并退出",
                     )


def f1_1():  # 添加的副函数
    win.update()
    ent.place(x=win_pix_x * 0.55, y=win_pix_y * 0.4)
    but_f1_con.place(x=win_pix_x * 0.6, y=win_pix_y * 0.55)
    lab.place(x=win_pix_x * 0.05, y=win_pix_y * 0.05)
    lab_a.place(x=win_pix_x * 0.5, y=win_pix_y * 0.2)
    win.update()
    return None


def f2_1():  # 删除的副函数
    win.update()
    ent.place(x=win_pix_x * 0.55, y=win_pix_y * 0.4)
    but_f2_con.place(x=win_pix_x * 0.6, y=win_pix_y * 0.55)
    lab.place(x=win_pix_x * 0.05, y=win_pix_y * 0.05)
    lab_a.place(x=win_pix_x * 0.5, y=win_pix_y * 0.2)
    win.update()
    return None


def f3_1():  # 修改的副函数
    win.update()
    ent.place(x=win_pix_x * 0.55, y=win_pix_y * 0.4)
    but_f3_con.place(x=win_pix_x * 0.6, y=win_pix_y * 0.55)
    lab.place(x=win_pix_x * 0.05, y=win_pix_y * 0.05)
    lab_a.place(x=win_pix_x * 0.5, y=win_pix_y * 0.2)
    win.update()
    return None


def f4_1():  # 查看的副函数
    win.update()
    ent.place(x=win_pix_x * 0.55, y=win_pix_y * 0.4)
    but_f4_con.place(x=win_pix_x * 0.6, y=win_pix_y * 0.55)
    lab.place(x=win_pix_x * 0.05, y=win_pix_y * 0.05)
    lab_a.place(x=win_pix_x * 0.5, y=win_pix_y * 0.2)
    win.update()
    return None


def f5_1():  # 数字检索的副函数
    ent.place(x=win_pix_x * 0.4, y=win_pix_y * 0.45)
    but_f5_con.place(x=win_pix_x * 0.47, y=win_pix_y * 0.55)
    lab_b.place(x=win_pix_x * 0.47, y=win_pix_y * 0.2)
    return None


print(2)

labs.place(x=win_pix_x * 0.1, y=win_pix_y * 0.1)  # 固定组件和一次性显示组件的放置
but_fin.config(command=fin)  # “保存并退出”按钮的绑定
but_fin.place(x=win_pix_x * 0.9, y=win_pix_y * 0.05)
scr.place(x=win_pix_x * 0.96, y=win_pix_y * 0.87)
scr.config()  # 滑动条（无效）
win.config(menu=men)
win.mainloop()
"""
while True:
    lab_a.update()
"""
