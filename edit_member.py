import random

user_list = [] #? 存储会员信息表
user_gender = ["男","女"] #? 性别列表
#? 随机生成会员号
def get_mid():
    while True:
        mid = str(random.randint(10000,99999))
        if mid not in [ele["mid_name"] for ele in user_list]:
            return mid
#? 添加会员
def add_mid():
    mid = get_mid()
    print(f"系统生成会员号是{mid}")
    mid_name = input("请输入新会员名字：")
    mid_sex =  input("请输入新会员性别：")
    mid_age = input("请输入新会员年龄:")
    while True:
        if mid_sex!=user_gender[0] and mid_sex!=user_gender[1]:
            print("请输入正确的性别")
            add_mid()
        elif mid_sex==user_gender[0] or mid_sex==user_gender[1]:
            user_list.append({"mid":mid,"mid_name":mid_name,"mid_sex":mid_sex,"mid_age":mid_age})
            #edit.add_member(mid,mid_name,mid_sex,mid_age)
            print("添加成功")
        break

#? 删除会员
def delete_mid():
    del_mid = input("请输入需要删除的会员号")
    #edit.del_member()
    for ele in user_list:
        if del_mid in ele["mid"]:
            user_list.remove(ele)
            print("删除成功！！")
            break
    else:
        print(f"你要删除的会员{del_mid}不存在！！")

#? 查看会员信息
def show_message():
    show_mid = input("请输入要查询的会员号:")
    for ele in user_list:
        if show_mid in ele["mid"]:
            print("会员信息如下~")
            print(ele)
            break
    else:
        print(f"要查询的会员{show_mid}不存在!!")

#? 查看所有会员信息
def show_all():
    print("所有会员信息如下")
    for all in user_list:
        print(all)

#? 会员信息按照年龄信息排序
def sort_mid_age():
    user_list.sort(user_list,key = lambda age:age["mid_age"],reverse=True)
    show_all()
#   修改会员信息
