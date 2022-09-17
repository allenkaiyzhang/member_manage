import edit_member
import edit_member_info as edit


#? 指定唯一用户名和唯一密码
only_admin = "admin"
only_password ="admin"

def print_the_UI():
    for num in range(3):
        print("请输入用户名：")
        user_admin = input()#? 输入用户名
        print("请输入密码：")
        user_password = input() #? 输入密码
        if user_admin == only_admin and user_password == only_password:
            print("管理员登录成功！！！")
            print("欢迎进入会员系统！将为您展示以下功能")
            while True:
                print("""该系统有如下功能：
                    1.添加会员信息
                    2.删除会员信息
                    3.查看指定的会员信息
                    4.查看所有会员信息
                    5.对会员按照年龄降序排序
                    6.退出系统""")
                Feature_sel = int(input("请输入对应功能的数字"))
                if Feature_sel ==1:
                    try:
                        edit_member.add_mid()
                    except:
                        print("添加会员失败")
                elif Feature_sel ==2:
                    try:
                        edit_member.delete_mid()
                    except:
                        print("删除会员失败")
                elif Feature_sel ==3:
                    try:
                        edit_member.show_message()
                    except:
                        print("查看信息失败")
                elif Feature_sel == 4:
                    try:
                        edit_member.show_all()
                    except:
                        print("查看信息失败")
                elif Feature_sel == 5:
                    try:
                        edit_member.sort_mid_age()
                    except:
                        print("排序失败")
                elif Feature_sel == 6:
                    print("欢迎再次使用~~")
                    break           
                elif Feature_sel==7:
                    edit.test()
            break
        else:
            print("用户名或密码错误！请重新输入")
    else:
        print("三次输入错误,禁止登录")