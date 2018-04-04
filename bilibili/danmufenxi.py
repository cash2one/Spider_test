#! /usr/bin/env python
# -*- coding:utf-8 -*-
with open('danmufenxi.txt','a',encoding='utf-8') as g:
    with open('bilidm.txt',encoding='utf-8') as f:
        contents = f.readlines()
        for content in contents:
            # print(content)
            aid = content.split(',')[0].split(':')[1]
            # print(aid)
            time = content.split('time:')[1]
            # print(time)
            time_dict = dict()
            for p in eval(time):
                d_p_time= int(eval(p.split(',')[0]))
                if d_p_time in time_dict:
                    time_dict[d_p_time] += 1
                else:
                    time_dict[d_p_time] = 1

            for key,value in time_dict.items():
                # print('av'+str(aid)+'视频:'+'%s秒'%key+'有%s个弹幕'%value)
                if max(time_dict.values()) <10:
                    continue
                if value == max(time_dict.values()):
                    minute = value//60
                    second = round((value/60-minute)*60,1)
                    print('av'+str(aid)+'视频:'+'弹幕最多在%s分%s秒，有%s个'%(minute,second,value))
                    t = 'av'+str(aid)+'视频:'+'弹幕最多在%s分%s秒,有%s个'%(minute,second,value)
                    g.write(t)
                    g.write('\n')



            # print(max(time_dict.values()))
