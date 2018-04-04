# -*- coding:utf-8 -*-

import requests

class E_1(object):
    def __init__(self):
        self.url = 'http://www.ezcarry.com/OceanFreight/OceanFreightSedAjax'
        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Length': '812',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie':'ASP.NET_SessionId=0gmofbkrbiazayl5kco3kip2; Language=zh-cn; Hm_lvt_e83b562c027fe42cbacc45053c97dbfa=1520396387,1521035381; ButtonStr=BS=DFBCB69776BA9264444A798462B3D1422BA295433732699A1755901AD7DCD11E1924145B2128D8F9; Hm_lpvt_e83b562c027fe42cbacc45053c97dbfa=1521035403',
            'Host': 'www.ezcarry.com',
            'Origin': 'http://www.ezcarry.com',
            'Referer': 'http://www.ezcarry.com/OceanFreight/OceanFreight',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }
        self.post_data = {
            'load': None,
            'discharge': None,
            'country': None,
            'ShippingLineName': None,
            'shippingLineId': None,
            'companyCode': None,
            'seqStr': None,
            'oecanCarrierName': 'AN TONG,ANL,APL,ASL,BENLINE,BOHAI,CCL,CKS,CMA,CNC,CO-HEUNG,COSCO,CSCL,CUL,CWL,DJS,DYS,EAS,EMC,EMK,ESL,FESCO,FLINE,FPMC,HAM-SUD,HANSUNG,HARBOUR,HASCO,HDS,HEUNG-A,HMM,HPL,IAL,JIAODONG,JJ,KKC,K-LINE,KMTC,MCC,MCL,MEL,MOL,MSC,MSK,MSL,NAMSUNG,NDS,NOS,NYK,NZL,ONTO,OOCL,PAN CON,PIL,QMNS,RCL,RPS,RZF,SAF,SAMUDERA,SCI,SG,SINOKOR,SINOTRANS,SITC,SML,STAROCEAN,STX,SWIRE,TCLC,TIANHAI,TSLINE,TYS,UCL,UWS,WANHAI,WEIDONG,WFL,WOSCO,YANGZIJIANG,YML,ZIM,',
            'loadingTerminal': None,
            'dischargeTerminal': None,
            'transhipPort': None,
            'etd': None,
            'eta': None,
            'isVip': None,
            'isPrise': None,
            'page': 2,
            'sortName': None,
            'sortType': None,
            'queryType': None,
        }

        temp = 'ASP.NET_SessionId=0gmofbkrbiazayl5kco3kip2; Language=zh-cn; Hm_lvt_e83b562c027fe42cbacc45053c97dbfa=1520396387,1521035381; ButtonStr=BS=DFBCB69776BA9264444A798462B3D1422BA295433732699A1755901AD7DCD11E1924145B2128D8F9; Hm_lpvt_e83b562c027fe42cbacc45053c97dbfa=1521035403'

        self.cookies = {}
        for i in temp.split('; '):
            self.cookies[i.split('=')[0]] = i.split('=')[-1]

    def get_url(self):
        # session = requests.session()
        response = requests.post(self.url, headers=self.headers)
        # response = session.post(self.url, headers=self.headers, data=self.post_data)
        print(self.cookies)

        print(response.content.decode())
        return response.content.decode()

    def run(self):
        # 请求url
        self.get_url()


if __name__ == '__main__':
    e = E_1()
    e.run()
