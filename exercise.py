

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
            num = i*100
            for j in num_li:
                if j != i:
                    num += j*10
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
        self.result = False
        self.index_number = 1
        bonus1 = 100000 * 0.1
        bonus2 = bonus1 + 100000 * 0.075
        bonus4 = bonus2 + 200000 * 0.05
        bonus6 = bonus4 + 200000 * 0.03
        bonus10 = bonus6 + 400000 * 0.015
        l = eval(input("请输入利润："))
        if l <= 100000:
            bonus = l * 0.1
        elif 100000 < l <= 200000:
            bonus = bonus1 + (l-100000) * 0.075
        elif 200000 < l <= 400000:
            bonus = bonus2 + (l-200000) * 0.05
        elif 400000 < l <= 600000:
            bonus = bonus4 + (l-400000) * 0.03
        elif 600000 < l <= 1000000:
            bonus = bonus6 + (l-600000) * 0.015
        else:
            bonus = bonus10 + (l-1000000) * 0.01
        print(bonus,bonus10)

if __name__ == '__main__':
    a = Python_exercise()
    a.ex2()
