# -*- coding: utf-8 -*-
"""
@Time ： 2023/11/3 13:18
@Auth ： fengtuotuo
@File ：bot.py
@IDE ：pycharm

"""
import requests
import json
import random
import time
import re


def gen_context():
    context_list = [
        "新来的朋友要关注以下几点1.好好聊天 不要FUD 认真解答问题 2.不准发Galaxy Quiz的答案 3.不要谈ZZ 树就会有!4.角色获取和加入时间没有关系 只跟你贡献和活跃程度有关！5.有了角色还是可能被回收的！",
        "友情提醒大家一下，领水的任务可以每天都可以做，准确的说是八小时!",
        "再提示下新盆友，SWAP ERROR报错社区给出的解决方案是1.加大Gas 2.如果还是不行，最好就等人少时候交互3.或者等待RPC完全修复4.术大牛可以自己搭个RPC!",
        "祝愿项目越来越好吧",
        "说实话，这个社区的氛围我感觉是我接触到社区里面已经算是很好的了",
        "还有没有需要帮助的新朋友啊，社区老人都很热心呢",
        "银河只有几个简单的任务，但是目前项目的任务都在银河，没有在zealy，大家注意分别",
        "任务里面有不明白的，新人可以问哈",
        "多回答大家的问题也是有帮助的",
        "这个项目的三币模型非常有创意，大家可以去读一下他的白皮书",
        "感觉交互起来越来越流畅了，项目方在做事啊",
        "熊弟们，你们仔细看过白皮书和经济模型吗，我感觉挺有创意的",
        "你们组池子在哪个网站上，我还没找到",
        "我想把里面的应用都体验下，找BUG出来是不是就能长树了哈",
        "项目方是懂营销的，产品也不错",
        "现在感觉流畅多了~",
        "新来的熊弟们可以先看下置顶留言",
        "你们今天又领水了吗，可以每天领取的",
        "兄弟们，有个问题，BGT是不是无法空投获得，只能组池子",
        "新来的朋友要注意不要FUD，认真解答问题  不要发Galaxy Quiz的答案 认真回答问题会有惊喜哈",
        "今天程序很丝滑，大家可以去感受下",
        "今天你们领水了没，现在能领到",
        "领不到水的多试几次，一般都能成，我刚才就是",
        "在提示下，前两天交互失败的现在可以去试试，丝滑了不少，项目方在做事哦",
        "我看还有问总是聊天怎么还没得到树这个问题的，大家放平心态，有时间就说几句，主要是活跃氛围，能给新人解决问题",
        "社区氛围很好，这在其他项目不多见啊，看好这个项目，带社区成员起飞",
        "如果领水报错，可以尝试换个节点，我试了，很好用"
    ]
    text = random.choice(context_list)
    return text


def get_context(chanel):
    chanel_list = ['','','']
    headr = {
        "Authorization": "",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
    }
    chanel_id = chanel
    url = "https://discord.com/api/v9/channels/{}/messages?limit=30".format(
        chanel_id)
    res = requests.get(url=url, headers=headr)
    result = json.loads(res.content)
    result_list = []
    id_list=[]
    for context in result:
        if ('<') not in context['content']:
            if ('@') not in context['content']:
                if ('http') not in context['content']:
                    if ('?') not in context['content']:
                        result_list.append(context['content'])
                        id_list.append(context['id'])

    return random.choice(result_list),random.choice(id_list)


def chat():
    chanel_list = ['']
    authorization_list = [
        '']
    for authorization in authorization_list:
        header = {
            "Authorization": authorization,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
        }

        for chanel_id in chanel_list:
            # 随机回复
            # str1,id=get_context(chanel_id)
            # msg = {
            #
            #     "content": str1,
            #     "message_reference": {"guild_id": "1060190166880370729", "channel_id": chanel_id, "message_id":id },
            #     "nonce": "82329451214{}33232234".format(random.randrange(0, 1000)),
            #     "tts": False
            #
            # }


            # 在已有文档里面挑选
            str1 = gen_context()
            msg = {

                "content": str1,
                # "message_reference": {"guild_id": "1060190166880370729", "channel_id": chanel_id, "message_id": id},
                "nonce": "82329451214{}33232234".format(random.randrange(0, 1000)),
                # "nonce": "1199176619843911680".format(random.randrange(0, 1000)),
                "tts": False

            }


            url = 'https://discord.com/api/v9/channels/{}/messages'.format(
                chanel_id)
            try:
                res = requests.post(url=url, headers=header,
                                    data=json.dumps(msg))
                print(res.content)
            except Exception:
                print(Exception)
            continue
        # 取100秒到160之间的一个随机数，作为循环的间隔时间。
        time.sleep(random.randrange(100, 160))


if __name__ == '__main__':
    while True:
        try:
            print('start')
            chat()
            # 取150秒到240之间的一个随机数，作为机器人发送消息的间隔时间。
            sleeptime = random.randrange(150, 240)
            time.sleep(sleeptime)
        except:
            pass
        continue
