from tkinter import *


def student():
    slave = Toplevel(root)
    slave.grab_set()
    slave.title("student")
    slave.focus_set()
    slave.minsize(200, 80)
    slave.maxsize(200, 80)
    Label(slave, text='Данилюк Денис\n'
                      'група ІВ-82\n'
                      'варіант 19\n', justify=LEFT, font="Arial 14").pack(fill='both')


def from_string_to_list(x):
    x = x.replace(',', ' ')
    x = x.replace(';', ' ')
    x = x.replace(':', ' ')
    x = x.replace('.', ' ')
    x = list(x.split(' '))
    for i in range(x.count('')):
        x.remove('')
    x = [int(i) for i in x]
    return x


def lex(N, K):
    global answ
    n = N
    k = K
    R = [
        "Київ       ", "Харків     ", "Дніпро     ", "Нікополь   ", "Бориспіль  ",
        "Рівне      ", "Сміла      ", "Одеса     ", "Львів      ", "Полтава   ",
        "Тернопіль  ", "Херсон    ", "Черкаси   ", "Чернівці    ", "Житомир   ",
        "Чернігів   "
    ]
    A = []

    for i in range(1, k + 1):
        A.append(i)

    if k == n:
        m = 1
    else:
        m = k

    answer_1 = ""
    answer_2 = ""

    hAnswer = " "
    x = 2
    while m >= 1:
        for i in range(len(A)):
            hAnswer += str(R[A[i] - 1]) + " "
            print(R[A[i] - 1])
        # while len(hAnswer) != 65:
        #     print(len(hAnswer))
        #     hAnswer += " "
        #     if x > 1000:
        #         break
        if x % 2 == 0:
            answer_1 += hAnswer + "\n"
        else:
            answer_2 += hAnswer + "\n"
        x += 1
        hAnswer = " "
        if A[k - 1] == n:
            m -= 1
        else:
            m = k

        if m >= 1:
            print("m: ", m)
            if m >= 1:
                for i in range(k, m - 1, -1):
                    A[i - 1] = A[m - 1] + i - m + 1
        else:
            break
        answ = [answer_1, answer_2]
    return answ


def generabc():
    global n, k, ans

    if lenN.get() == '':
        n = 0
    else:
        n = (int(lenN.get()))

    if lenK.get() == '':
        k = 0
    else:
        k = (int(lenK.get()))

    ans = lex(n, k)
    label_vyvid.configure(text='{}\n'.format(ans[0]))
    label_vyvid_2.configure(text='{}\n'.format(ans[1]))


#############
root = Tk()
root.title('Задати множини')
root.minsize(680, 700)

var = IntVar()
var.set(0)


Label(root, text='Задати', font="Arial 14", width=30, height=2, justify=LEFT) \
    .grid(column=3, row=2, columnspan=3)

Label(root, text='n:').grid(column=3, row=3, sticky=E)
Label(root, text='k:').grid(column=3, row=4, sticky=E)

lenN = Entry(root, width=10, bd=3)
lenN.grid(column=4, row=3, sticky=W)
lenK = Entry(root, width=10, bd=3)
lenK.grid(column=4, row=4, sticky=W)

A = []
n = 0
k = 0
r = 0
ans = [[],[]]

but_OK = Button(root, text='Показати результат', font='Arial 12', command=generabc)
but_OK.grid(column=1, row=9, columnspan=5)

label_vyvid = Label(root, text='{}\n'.format(ans[0]), justify=LEFT, font="Arial 10")
label_vyvid_2 = Label(root, text='{}\n'.format(ans[1]), justify=LEFT, font="Arial 10")

label_vyvid.grid(column=1, row=11, columnspan=10, sticky=W)
label_vyvid_2.grid(column=10, row=11, columnspan=5, sticky=W)


but_student = Button(root, text='Студент', font='Arial 12',
                     command=student)
but_student.grid(column=8, row=0, sticky=E, rowspan=2, columnspan=2)

root.mainloop()
