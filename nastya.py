from tkinter import *


def student():
    slave = Toplevel(root)
    slave.grab_set()
    slave.title("student")
    slave.focus_set()
    slave.minsize(200, 80)
    slave.maxsize(200, 80)
    Label(slave, text='Головаш Анастасия\n'
                      'група ІВ-82\n'
                      'варіант 17\n', justify=LEFT, font="Arial 14").pack(fill='both')


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


def lex(N, K, R, arr):

    n = N
    k = K
    r = R
    A2 = arr
    A = []
    m = 0

    while m != k - 1:
        if len(arr) == 0:
            break
        if A2[m] < A2[m + 1]:
            A.append(A2[m])
            m += 1
        else:
            print("ERROR")
            A = []
            break

    if len(A) != 0:
        A.append(A2[m])

    if k == n:
        m = 1
    else:
        m = k

    stri = " "

    while m >= 1:
        if len(arr) == 0:
            break

        stri += str(A) + " "

        r -= 1
        if r == 0:
            break
        else:
            if A[k - 1] == n:
                m -= 1
            else:
                m = k
            if m >= 1:
                for i in range(k, m - 1, -1):
                    A[i - 1] = A[m - 1] + i - m + 1

        print(stri)
    return stri


def generabc():
    global A, n, k, r, ans

    if entA.get() == '':
        A = []
    else:
        A = from_string_to_list(entA.get())

    if lenN.get() == '':
        n = 0
    else:
        n = (int(lenN.get()))

    if lenK.get() == '':
        k = 0
    else:
        k = (int(lenK.get()))

    if lenR.get() == '':
        r = 0
    else:
        r = (int(lenR.get()))

    ans = lex(n, k, r, A)
    label_vyvid.configure(text='A = {}\n'.format(ans))


#############
root = Tk()
root.title('Задати множини')
root.minsize(680, 450)

var = IntVar()
var.set(0)

Label(root, text='Задати початкову множину', font="Arial 14", width=25, height=2, justify=LEFT) \
    .grid(column=0, row=2, columnspan=3)

Label(root, text='A:').grid(column=0, row=3, sticky=E)

entA = Entry(root, width=29, bd=3)
entA.grid(column=1, row=3, sticky=W)

Label(root, text='Задати', font="Arial 14", width=30, height=2, justify=LEFT) \
    .grid(column=3, row=2, columnspan=3)

Label(root, text='n:').grid(column=3, row=3, sticky=E)
Label(root, text='k:').grid(column=3, row=4, sticky=E)
Label(root, text='r:').grid(column=3, row=5, sticky=E)

lenN = Entry(root, width=10, bd=3)
lenN.grid(column=4, row=3, sticky=W)
lenK = Entry(root, width=10, bd=3)
lenK.grid(column=4, row=4, sticky=W)
lenR = Entry(root, width=10, bd=3)
lenR.grid(column=4, row=5, sticky=W)

A = []
n = 0
k = 0
r = 0
ans = []

but_OK = Button(root, text='Показати результат', font='Arial 12', command=generabc)
but_OK.grid(column=1, row=9, columnspan=4)


label_vyvid = Label(root, text='A = {}\n'.format(ans))
label_vyvid.grid(column=1, row=11, columnspan=100, sticky=W)

but_student = Button(root, text='Студент', font='Arial 12',
                     command=student)
but_student.grid(column=5, row=0, sticky=E, rowspan=2, columnspan=2)

root.mainloop()
