import tkinter as tk
# 功能
#追加数字
def append_num(i):
    lists.append(i)
    result_num.set(''.join(lists))
# 选择运算符号
def operator(i):
    if len(lists) > 0:
        if lists[-1] in ['+','-','*','/']:
            lists[-1] = i
        else:
            lists.append(i)
        result_num.set(''.join(lists))
# 清零
def clear():
    lists.clear()
    result_num.set(0)
#退格
def back():
    del lists[-1]
    result_num.set(lists)
#计算
def equal():
    #异常捕获，在进行数据运算结果时如果出现异常进行处理
    try:
        a = ''.join(lists)
        end_num = eval(a)
    except Exception:
        result_num.set('输入有误')
    else:
        result_num.set(end_num)
        lists.clear()
        lists.append(str(end_num))
# 界面
# 实例化一个窗口对象
root = tk.Tk()
# 标题
root.title('简易计算器')
# 设置默认大小
root.geometry("295x280+150+150")
# 透明度
root.attributes("-alpha", 0.9)
root['background'] = "#ffffff"
#
lists = []
result_num = tk.StringVar()
result_num.set(0)
# 标签
label1 = tk.Label(root, textvariable=result_num, width=20, height=2, font=("宋体", 20), justify='left', background='#ffffff',
                  anchor='se')
# 布局
label1.grid(row=0, column=0, columnspan=4)
# 按钮
button_clear = tk.Button(root, text='c', width=5, font=("宋体", 16), relief='flat', background='#C0C0C0',command=lambda :clear())
button_clear.grid(padx=4, pady=3, row=1, column=0)

button_back = tk.Button(root, text='←', width=5, font=("宋体", 16), relief='flat', background='#C0C0C0',command=lambda :back())
button_back.grid(padx=4, row=1, column=1)

button_division = tk.Button(root, text='/', width=5, font=("宋体", 16), relief='flat', background='#C0C0C0',command=lambda :operator('/'))
button_division.grid(padx=4, row=1, column=2)

button_multiplication = tk.Button(root, text='x', width=5, font=("宋体", 16), relief='flat', background='#C0C0C0',command=lambda :operator('*'))
button_multiplication.grid(padx=4, row=1, column=3)

button_zero = tk.Button(root, text='0', width=12, font=("宋体", 16), relief='flat', background='#b3d4fc',command=lambda :append_num('0'))
button_zero.grid(padx=4, pady=4, row=5, column=0, columnspan=2)

button_one = tk.Button(root, text='1', width=5, height=0, font=("宋体", 16), relief='flat', background='#b3d4fc',command=lambda :append_num('1'))
button_one.grid(padx=4, row=4, column=0)

button_two = tk.Button(root, text='2', width=5, font=("宋体", 16), relief='flat', background='#b3d4fc',command=lambda :append_num('2'))
button_two.grid(padx=4, row=4, column=1)

button_three = tk.Button(root, text='3', width=5, font=("宋体", 16), relief='flat', background='#b3d4fc',command=lambda :append_num('3'))
button_three.grid(padx=4, row=4, column=2)

button_four = tk.Button(root, text='4', width=5, font=("宋体", 16), relief='flat', background='#b3d4fc',command=lambda :append_num('4'))
button_four.grid(padx=4, pady=4, row=3, column=0)

button_five = tk.Button(root, text='5', width=5, font=("宋体", 16), relief='flat', background='#b3d4fc',command=lambda :append_num('5'))
button_five.grid(padx=4, row=3, column=1)

button_six = tk.Button(root, text='6', width=5, font=("宋体", 16), relief='flat', background='#b3d4fc',command=lambda :append_num('6'))
button_six.grid(padx=4, row=3, column=2)

button_seven = tk.Button(root, text='7', width=5, font=("宋体", 16), relief='flat', background='#b3d4fc',command=lambda :append_num('7'))
button_seven.grid(padx=4, row=2, column=0)

button_eight = tk.Button(root, text='8', width=5, font=("宋体", 16), relief='flat', background='#b3d4fc',command=lambda :append_num('8'))
button_eight.grid(padx=4, row=2, column=1)

button_nine = tk.Button(root, text='9', width=5, font=("宋体", 16), relief='flat', background='#b3d4fc',command=lambda :append_num('9'))
button_nine.grid(padx=4, row=2, column=2)

button_addition = tk.Button(root, text='+', width=5, height=-1, font=("宋体", 16), relief='flat', background='#C0C0C0',command=lambda :operator('+'))
button_addition.grid(padx=4, row=3, column=3)

button_reduce = tk.Button(root, text='-', width=5, font=("宋体", 16), relief='flat', background='#C0C0C0',command=lambda :operator('-'))
button_reduce.grid(padx=4, row=2, column=3)

button_equal = tk.Button(root, text='=', width=5, height=3, font=("宋体", 16), relief='flat', background='#00CED1',command=lambda :equal())
button_equal.grid(padx=4, row=4, column=3, rowspan=5)

button_decimal = tk.Button(root, text='.', width=5, font=("宋体", 16), relief='flat', background='#b3d4fc',command=lambda :operator('.'))
button_decimal.grid(padx=4, row=5, column=2)

# 消息循环
root.mainloop()
