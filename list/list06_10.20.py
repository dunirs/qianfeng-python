# 游戏
"""
1.选择人物
2.购买武器 金币
3.打仗 赢 得金币
4.选择删除武器
5.查看武器
6.退出游戏
"""
import  random
print('*'*40)
print('\t欢迎来到王者荣耀')
print('*'*40)
role = input('请选择游戏人物：(1.鲁班 2.后羿 3.李白 4.孙尚香 5.貂蝉 6.诸葛亮 )')
coins = 1000

weapon_list = []  # 自己的武器库
print('欢迎{0} 来到王者荣耀，当前金币为：{1}'.format(role, coins))
while True:
    choice = int(input('\n 请选择：\n 1.购买武器\n 2.打仗\n 3.删除武器\n 4.查看武器\n 5.退出游戏\n'))
    if choice == 1:
        # 购买武器
        print('欢迎来到武器库：')
        weapons = {'刀': 500, '枪': 1000, '剑': 400, '棍': 300}
        for weapon, value in weapons.items():
            print(weapon + ':' + str(value))
        weaponname = input('请输入要购买的武器名称:')
        # 1 原来有没有买过该武器 2。 输入的武器名是否在武器库中
        if weaponname not in weapon_list:
            for weapon, value in weapons.items():
                if weaponname == weapon:
                    # 购买武器
                    if coins >= value:
                        coins -= value
                        weapon_list.append(weapon)
                        print('{}购买{}成功'.format(role, weaponname))
                        break
                    else:
                        print('金币不足')
                        break
            else:
                print('输入武器错误')
        else:
            print('当前输入武器已存在')
    elif choice == 2:
        # 打仗 假设你有多个武器
        if len(weapon_list) > 0:
            print('进入战场......')
            # 选择武器
            print('{}拥有的武器如下：'.format(role))
            for weapon in weapon_list:
                print(weapon)
            weaponname = input('请选择：')
            while True:
                if weaponname in weapon_list:
                    # 进入战场 默认与张飞对战
                    ran1 = random.randint(1, 20)  # 张飞的战力
                    ran2 = random.randint(1, 20)  # 你的战力
                    if ran1 > ran2:
                        print('此局对战：张飞胜，{}拥有金币:{}'.format(role, coins))
                    else:
                        coins += 200
                        print('此局对战:{}胜,金币:{}'.format(role, coins))
                    break
                else:
                    print('选择的武器不存在，请重新选择')
        else:
            print('暂时还没武器，请购买武器')
    elif choice == 3:
        # 删除武器
        # 选择武器
        if len(weapon_list) > 0:
            print('{}拥有的武器如下：'.format(role))
            for weapon in weapon_list:
                print(weapon)
            weaponname = input('请选择要删除的武器：')
            while True:
                if weaponname in weapon_list:
                    weapon_list.remove(weaponname)
                    coins += weapons[weaponname]   # 删除武器 金币增加
                    print('{}现在拥有金币:{}'.format(role,coins))
                    break   # 退出while循环
                else:
                    print('选择的武器不存在，请重新选择')
        else:
            print('暂时还没武器，请购买武器')

    elif choice == 4:
        # 查看武器
        print('{}拥有的武器如下：'.format(role))
        for weapon in weapon_list:
            print(weapon)
    elif choice == 5:
        answer = input('确定要离开吗（yes/no）')
        if answer.lower() == 'yes':
            print('game over')
            break
    else:
        print('输入错误，请重新输入:')
