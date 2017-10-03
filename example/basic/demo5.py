#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 题目五：
# 用户交互，显示省市县三级联动的选择

dic = {
    "河北": {
        "石家庄1": ["鹿泉1", "藁城1", "元氏1"],
        "邯郸1": ["永年1", "涉县1", "磁县1"],
    },
    "河南": {
        "石家庄2": ["鹿泉2", "藁城2", "元氏2"],
        "邯郸2": ["永年2", "涉县2", "磁县2"],
    },
    "山西": {
        "石家庄3": ["鹿泉3", "藁城3", "元氏3"],
        "邯郸3": ["永年3", "涉县3", "磁县3"],
    }
}

for k in dic:
    print(k)

inp1 = input('请输入省份:')

for k in dic[inp1]:
    print(k)

inp2 = input('请输入城市:')

for k in dic[inp1][inp2]:
    print(k)
