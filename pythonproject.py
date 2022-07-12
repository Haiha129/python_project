# tạo đăng nhập/ đăng ký

import tkinter as tk
import os
wordlist ={'mom': 'mẹ', 'dad': 'bố'}
default_name= 'haiha'
default_pass= '1234'
#đăng ký
def signup_user():
    username_info = username.get()
    password_info = password.get()

    file=open(username_info,'w')
    file.write(username_info+'\n')
    file.write(password_info)
    file.close()

    my_entry2_username.delete(0,tk.END)
    my_entry2_password.delete(0,tk.END)
    mylabel_success=tk.Label(win2, text='Registration completed successful')
    mylabel_success.grid(row=5, column=3)


def popup_signup():
    global win2
    win2 = tk.Toplevel(win)
    win2.geometry('500x300')

    label2 = tk.Label(win2, text="SIGN UP")
    label2.grid(row=0, column=2)
    
   

#label cửa sổ sign up:   
    global username
    global password
    global my_entry2_username
    global my_entry2_password
    my_lbl2=tk.Label(win2,text='Username')
    my_lbl2.grid(row=1,column=1)
    my_lbl2=tk.Label(win2,text='Password')
    my_lbl2.grid(row=2,column=1)

#entry cửa sổ sign up:
    username=tk.StringVar()
    my_entry2_username=tk.Entry(win2, textvariable = username)
    my_entry2_username.grid(row=1,column=2)
    password=tk.StringVar()
    my_entry2_password=tk.Entry(win2, textvariable = password, show = '*')
    my_entry2_password.grid(row=2,column=2)

    button2 = tk.Button(win2, text='SUBMIT', command=signup_user)
    button2.grid(row=3,column=2)    

#xóa các cửa sổ signup và cửa sổ login thành công
def clear_window():
    win3.destroy()
    win1.destroy()
    open_screen_word()

#màn hình chính tạo các chức năng thêm/sửa/xóa từ:
def open_screen_word():
    global win4
    win4 = tk.Toplevel(win)
    win4.geometry('500x300')
    win4_button1=tk.Button(win4, text='Add', command = add_word)
    win4_button1.pack()
    win4_button1=tk.Button(win4, text='Delete',command= delete)
    win4_button1.pack()
    win4_button1=tk.Button(win4, text='Search', command = search)
    win4_button1.pack()
    win4_button1=tk.Button(win4, text='Modify',command=modify)
    win4_button1.pack()

# thông báo add từ thành công
def save():
    if word.get() in wordlist:
        win5_lbl4=tk.Label(win5,text="Already exists")
        win5_lbl4.grid(row=6,column=2)
        win5_entry1.delete(0,tk.END)
        win5_entry2.delete(0,tk.END)
    else:   
        wordlist.update({word.get():meaning.get()})
        win5_lbl3=tk.Label(win5,text='Successful Added')
        win5_lbl3.grid(row=5,column=2)
        win5_lbl4=tk.Label(win5,text="Your word added: "+"\n"+str(word.get())+': '+str(meaning.get()))
        win5_lbl4.grid(row=6,column=2)
        win5_entry1.delete(0,tk.END)
        win5_entry2.delete(0,tk.END)    

#kết quả xóa từ:
def show_result_del():
    word_enter=word.get()
    if word.get() in wordlist:  
        del wordlist[word.get()]
        win7_lbl2= tk.Label(win7, text ='Deleted')
        win7_lbl2.pack()    
    else:
        win7_lbl2= tk.Label(win7, text = "Not Found")
        win7_lbl2.pack()


#chức năng xóa từ:
def delete():
    global win7
    global word
    win7=tk.Toplevel(win4)
    win7.geometry('500x300')
    win7_lbl1= tk.Label(win7, text='Enter the key')
    win7_lbl1.pack()
    word = tk.StringVar()
    win7_entry1=tk.Entry(win7, textvariable = word)
    win7_entry1.pack()


    win7_btn1=tk.Button(win7, width=5,heigh=1, text='Delele',command= show_result_del)
    win7_btn1.pack()


# show result tìm kiếm
def show_answer_search():
    word_enter=word.get()
    if word.get() in wordlist:
        result=wordlist[word.get()]
        win6_lbl2= tk.Label(win6, text = "Meaning: "+str(result))
        win6_lbl2.pack()
    else:
        win6_lbl2= tk.Label(win6, text = "Not Found")
        win6_lbl2.pack()

# sửa từ
def search():
    global win6
    global word
    global meaning
    win6=tk.Toplevel(win4)
    win6.geometry('500x300')
    win6_lbl1= tk.Label(win6, text='Enter the key')
    win6_lbl1.pack()
    word = tk.StringVar()
    win6_entry1=tk.Entry(win6, textvariable = word)
    win6_entry1.pack()


    win6_btn1=tk.Button(win6, width=5,heigh=1, text='Search',command=show_answer_search)
    win6_btn1.pack()

# # #show kết quả sửa:
# def modify_result():
#     meaning_enter = meaning.get()
#     win8_lbl4=tk.Label(win8, text='Saved Change. Result: '+str(word.get())+': '+str(meaning.get()))
#     win8_lbl4.pack()


# #trả kết quả tìm kiếm trước khi sửa:
# def search_mod():
#     win8_lbl2=tk.Label(win8, text='Result')
#     win8_lbl2.pack()
#     result=wordlist[word.get()]
#     win8_entry2=tk.Entry(win8, textvariable =result)
#     win8_entry2.pack()
#     win8_lbl3=tk.Label(win8, text='Modify')
#     win8_lbl3.pack()
#     win8_entry3=tk.Entry(win8, text='Modify')
#     win8_entry3.pack()
#     win8_button2=tk.Button(win8, text='Modify',command = modify_result)
#     win8_button2.pack()



# # #sửa từ
# def modify():
#     global win8
#     win8=tk.Toplevel(win4)   
#     win8.geometry('500x300')
#     word_enter=word.get()
#     win8_lbl1= tk.Label(win8, text='Word')
#     win8_lbl1.pack()
#     win8_entry1=tk.Entry(win8, textvariable = word)
#     win8_entry1.pack()

#     win8_button1=tk.Button(win8, text='Process',command = search_mod)
#     win8_button1.pack()

    

   
   
#thêm từ
def add_word():
    global win5
    win5=tk.Toplevel(win4)   
    win5.geometry('500x300') 

    global word
    global meaning
    global win5_entry1
    global win5_entry2
    word=tk.StringVar()
    meaning=tk.StringVar()
    word_enter=word.get()
    meaning_enter=meaning.get()
    
    win5_lbl1= tk.Label(win5, text='Word')
    win5_lbl1.grid(row=1, column=1)
    win5_lbl2=tk.Label(win5, text='Meaning')
    win5_lbl2.grid(row=2, column=1)
    
    win5_entry1=tk.Entry(win5, textvariable = word)
    win5_entry1.grid(row=1, column=2)
    
    win5_entry2=tk.Entry(win5, textvariable = meaning)
    win5_entry2.grid(row=2, column=2)
    win5_button1=tk.Button(win5, text='Add',command = save)
    win5_button1.grid(row=3, column=2)
  

#thông báo login thành công
def login_success():
    global win3
    win3=tk.Toplevel(win1)
    win3.geometry('300x200')
    win3_lbl1=tk.Label(win3, text='Welcome!')
    win3_lbl1.pack()
    win3_btn1=tk.Button(win3, text='OK', command= clear_window)
    win3_btn1.pack()

#thông báo login thất bại do sai mật khẩu:
def login_fail():
    win1_lbl3=tk.Label(win1, text='Incorrect password, please check again.')
    win1_lbl3.grid(row=5, column=2)

#thông báo tài khoản không tồn tại
def user_not_exist():
    win1_lbl4=tk.Label(win1, text='User not found. Have you create your account yet?')
    win1_lbl4.grid(row=5, column=2)   

#đăng nhập
def signin_user():
    username_signin= username_verify.get()
    password_signin= password_verify.get()
    my_entry1_username.delete(0,tk.END)
    my_entry1_password.delete(0,tk.END)
    if username_signin == default_name:
        if password_signin == default_pass:
            login_success()
        else:
            login_fail()   
    else:
        user_not_exist()      

def popup_signin():
    global win1
    win1 = tk.Toplevel(win)
    win1.geometry('500x300')

    label1 = tk.Label(win1, text="SIGN IN")
    label1.grid(row=0, column=2)

#label cửa sổ sign in:   
    my_lbl1_username=tk.Label(win1,text='Username')
    my_lbl1_username.grid(row=1,column=1)
    my_lbl1_password=tk.Label(win1,text='Password')
    my_lbl1_password.grid(row=2,column=1)

#entry cửa sổ sign in:
    global username_verify
    global password_verify
    global my_entry1_password
    global my_entry1_username
    username_verify=tk.StringVar()
    my_entry1_username=tk.Entry(win1, textvariable = username_verify)
    my_entry1_username.grid(row=1,column=2)
    password_verify=tk.StringVar()
    my_entry1_password=tk.Entry(win1, textvariable = password_verify, show = '*')
    my_entry1_password.grid(row=2,column=2)

    button1 = tk.Button(win1, text='LOG IN', command=signin_user)
    win1.destroy
    button1.grid(row=3,column=2)    


#Màn hình chính
win = tk.Tk()
win.title('Learning new word everyday')
win.geometry('700x500')

button_signup = tk.Button(win, text='SIGN UP', command=popup_signup)
button_signup.pack()
button_signin = tk.Button(win, text='SIGN IN', command=popup_signin)
button_signin.pack()

win.mainloop()