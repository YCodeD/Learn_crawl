# 请独立完成这个产品吧，我相信你可以的！
import random

while True:
    choice = input('''
    ------------
    1.今天不知道吃什么 -_-
    2.今天不知道去哪里吃 ?_?
    ------------
    请输入你的选择：
    ''')

    if choice == '1':
        #---可将列表作为全局变量
        menu_list = ['龙须菜','炝冬笋','糖熘儿',' 白菜锅子','焖扁豆','麻辣野鸡']
        while True:
            #---使用random.choice(menu_list)会更方便
            x = random.randint(0,5)
            print('''
            为你选择的一道菜：
            %s
            是否重新选？  y--是  任意输入--否
            ''' % menu_list[x])
            choose = input()

            if choose == 'y':
                continue
            else:
                print('byebye')
                break
    elif choice == '2':
        #---可将列表作为全局变量
        choice = []
        sum_choice = 0
        print('''请输入你纠结的选项
                输入一个，按一次回车，输入n结束输入
                ''')
        while True:
            item = input()
            if item != 'n':
                choice.append(item)
                sum_choice += 1
                continue
            else:
                break

        x = random.randint(0, sum_choice)
        print('为你选择：' + choice[x])
        break
    else:
        print('输入有误，请重新输入')

    
    
# # 帮你做选择之我要吃什么
# import random

# # 将需要用到的表格和变量放在开头
# list_food = ['KFC', '蒸菜馆', '楼下快餐店', '桂林米粉', '东北饺子', '金牌猪脚饭', '三及第汤饭']  # 备选菜单，可自定义。
# list_choice = []

# # 由于两个原因都包含判断过程，所以，为了让代码更简洁，可将其封装成函数。
# def choose(list):
#     while True:
#         food = random.choice(list)
#         judgement = input('去吃【%s】好不好啊？同意的话输入y，不想吃直接回车即可。'%(food))
#         if judgement == 'y':
#             print('去吃【%s】！就这么愉快地决定啦！'%(food)) 
#             break

# # 判断环节
# reason = int(input('你不知道吃什么的原因是：1.完全不知道吃什么；2.在几家店之间徘徊（请输入1或2）：'))
# if reason == 1:
#     choose(list_food)
# elif reason == 2:
#     add = True
#     while add:
#         choice = input('请输入让你犹豫的店名（注：一家一家输，完成后输入y）：')
#         if choice != 'y':  # 这个判断语句，是为了不将 y 也添加到菜单里。
#             list_choice.append(choice)
#         if choice == 'y':
#             add = False
#     choose(list_choice)          
# else:
#     print('抱歉，目前还不支持第三种情况——不过，你可以加代码哦。')


    