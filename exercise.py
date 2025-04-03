from math import sqrt


class Python_exercise(object):

    def ex1(self):

        """
        题 ⽬ ： 有 1 、 2 、 3 、 4 个 数 字 ，能 组 成 多 少 个 互 不 相 同 且 ⽆ 重 复 数 字 的 三 位 数 ？ 都 是 多 少 ？
        """
        self.result = False
        self.index_number = 1
        num_li = list(eval("1,2,3,4"))
        count = 0
        for i in num_li:
            num = i * 100
            for j in num_li:
                if j != i:
                    num += j * 10
                    for k in num_li:
                        if k != j and k != i:
                            num += k
                            count += 1
                            print(num)
        # print(count)

    def ex2(self):
        """题 ⽬ ： 企 业 发 放 的 奖 ⾦ 根 据 利 润 提 成 。 利 润 （ 低 于 或 等 于 1 0 万 元 时 ， 奖 ⾦ 可 提 1 0 % ； 利 润
⾼于 1 0 万 元 ， 低 于 2 0 万 元 时 ， 低 于 1 0 万 元 的 部 分 按 1 0 % 提 成 ， ⾼ 于 1 0 万 元 的 部 分 ，可 可 提成 7 . 5 % ：
2 0 万 到 4 0 万 之 间 时 ， ⾼ 于 2 0 万 元 的 部 分 ， 可 提 成 5 % ： 4 0 万 到 6 0 万 之 间
时 ⾼ 于4 0 万 元 的 部 分 ， 可 提 成 3 % ： 6 0 万 到 1 0 0 万 之 间 时 ， ⾼ 于 6 0 万 元 的 部 分 ， 可 提 成 1 . 5 % ，
⾼ 于1 0 0 万 元 时 ， 超 过 1 0 0 万 元 的 部 分 按 1 % 提 成 ， 从 键 盘 输 ⼊ 当 ⽉ 利 润 | ， 求 应 发 放 奖 ⾦
总 数 ？"""
        self.result = True
        self.index_number = 2
        bonus1 = 100000 * 0.1
        bonus2 = bonus1 + 100000 * 0.075
        bonus4 = bonus2 + 200000 * 0.05
        bonus6 = bonus4 + 200000 * 0.03
        bonus10 = bonus6 + 400000 * 0.015
        l = eval(input("请输入利润："))
        if l <= 100000:
            bonus = l * 0.1
        elif 100000 < l <= 200000:
            bonus = bonus1 + (l - 100000) * 0.075
        elif 200000 < l <= 400000:
            bonus = bonus2 + (l - 200000) * 0.05
        elif 400000 < l <= 600000:
            bonus = bonus4 + (l - 400000) * 0.03
        elif 600000 < l <= 1000000:
            bonus = bonus6 + (l - 600000) * 0.015
        else:
            bonus = bonus10 + (l - 1000000) * 0.01
        print(bonus)

    def ex3(self):
        """
         ⼀ 个 整 数 ， 它 加 上 1 0 0 后 是 ⼀ 个 完 全 平 ⽅ 数 ， 再 加 上 2 6 8 又 是 ⼀ 个 完 全 平 ⽅ 数 ， 请 该 数 是 多 少 ？
        """
        #这一题目主要学到了两个知识点：1.开方函数sqrt()   2.判断一个数是不是完全平方数，可以使用开方后转为整形再平方与这个数本身比较
        self.result = False
        self.index_number = 3
        for i in range(100000):
            x = int(sqrt(i + 100))
            y = int(sqrt(i + 268))
            if (x * x == i + 100) and (y * y == i + 268):
                print(i)

    def ex4(self):
        """
         输 ⼊ 某 年 某 ⽉ 某 ⽇ ， 判 断 这 ⼀ 天 是 这 ⼀ 年 的 第 ⼏ 天
        """
        self.result = False
        self.index_number = 4
        year = int(input("输入年份"))
        month = int(input("输入月份"))
        day = int(input("输入日"))
        february_day = 28
        if month > 2 and ((year % 400 == 0) or (year % 4 == 0 and (year % 100 != 0))):
            february_day = 29
        month_31 = month // 2
        month_30 = month - 1 - month_31
        day_num = 30 * month_30 + 31 * month_31 + day
        if february_day == 28 and month >= 3:
            day_num = day_num - 2
        elif february_day == 29 and month >= 3:
            day_num = day_num - 1
        print(day_num)

        #ds写法
        # self.result = False
        # self.index_number = 4
        # try:
        #     year = int(input("输入年份: "))
        #     month = int(input("输入月份: "))
        #     day = int(input("输入日: "))
        # except ValueError:
        #     print("请输入有效的整数日期。")
        #     return
        #
        # # 定义每个月的天数
        # month_days = [31, 28, 31, 30, 31, 30,
        #               31, 31, 30, 31, 30, 31]
        #
        # # 判断是否为闰年，并调整2月天数
        # if ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)):
        #     month_days[1] = 29
        #
        # # 检查输入的月份和日期是否有效
        # if month < 1 or month > 12:
        #     print("月份应在1到12之间。")
        #     return
        # if day < 1 or day > month_days[month - 1]:
        #     print(f"{year}年{month}月没有{day}日。")
        #     return

        # 计算这一天是这一年的第几天
        # day_num = sum(month_days[:month - 1]) + day
        # print(f"{year}年{month}月{day}日是这一年的第{day_num}天。")

if __name__ == '__main__':
    a = Python_exercise()
    a.ex4()
