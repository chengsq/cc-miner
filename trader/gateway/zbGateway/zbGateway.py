# encoding: UTF-8

'''
vn.zb的gateway接入
'''
import os
import json
from datetime import datetime
from time import sleep
from copy import copy
from threading import Condition
from Queue import Queue
from threading import Thread
from time import sleep
from trader.gateway.vtEvent import  *

EXCHANGE_ZB = 'ZB'

class zbGateway():
    #----------------------------------------------------------------------
    def __init__(self, eventEngine2,zb_api,zb_market,gatewayName='ZB'):
        """Constructor"""

        self.api_spot = zb_api
        self.market = zb_market

        self.connected = False

        self.eventEngine = eventEngine2
        self.gatewayName = gatewayName

        self.qryEnabled = True

        self.countTimer = 0
        self.localTimeDelay = 3

        # 启动查询
        self.initQuery()
        self.startQuery()

    #----------------------------------------------------------------------
    def connect(self):
        """连接"""
        pass
    #----------------------------------------------------------------------
    def subscribe(self, subscribeReq):
        """订阅行情"""
        self.api_spot.subscribe(subscribeReq)

    #----------------------------------------------------------------------
    def sendOrder(self, orderReq):
        """发单"""
        return self.api_spot.spotSendOrder(orderReq)
    #----------------------------------------------------------------------
    def cancelOrder(self, cancelOrderReq):
        """撤单"""
        self.api_spot.spotCancel(cancelOrderReq)

    #----------------------------------------------------------------------
    def qryAccount(self):
        """查询账户资金"""
        self.api_spot.spotUserInfo()

    #----------------------------------------------------------------------
    def qryOrderInfo(self):
        self.api_spot.spotAllOrders()

    #----------------------------------------------------------------------
    def qryPosition(self):
        """查询持仓"""
        pass

    #----------------------------------------------------------------------
    def close(self):
        """关闭"""
        self.api_spot.active = False
        self.api_spot.close()

    #----------------------------------------------------------------------
    def initQuery(self):
        """初始化连续查询"""
        if self.qryEnabled:
            # 需要循环的查询函数列表
            #self.qryFunctionList = [self.qryAccount , self.qryOrderInfo]
            self.qryFunctionList = [ self.qryOrderInfo]
            #self.qryFunctionList = []

            self.qryCount = 0           # 查询触发倒计时
            self.qryTrigger = 2         # 查询触发点
            self.qryNextFunction = 0    # 上次运行的查询函数索引

    #----------------------------------------------------------------------
    def query(self, event):
        """注册到事件处理引擎上的查询函数"""
        tick = self.market.get_tick()
        print tick
        d = self.market.get_depth(3)
        t = self.market.get_trade()
        print t



    #----------------------------------------------------------------------
    def startQuery(self):
        """启动连续查询"""
        self.eventEngine.register(EVENT_TIMER, self.query)

    #----------------------------------------------------------------------
    def setQryEnabled(self, qryEnabled):
        """设置是否要启动循环查询"""
        self.qryEnabled = qryEnabled

class ZB_API_Spot():
    """ zb 的 API实现 """
    #----------------------------------------------------------------------
    def __init__(self, gateway):
        """Constructor"""
        #super(, self).__init__()

        self.gateway = gateway                  # gateway对象
        self.gatewayName = gateway.gatewayName  # gateway对象名称        
        self.active = False             # 若为True则会在断线后自动重连

        self.cbDict = {}
        self.tickDict = {}
        self.orderDict = {}

        self.channelSymbolMap = {}

        self.localNo = 0                # 本地委托号
        self.localNoQueue = Queue()     # 未收到系统委托号的本地委托号队列
        self.localNoDict = {}           # key为本地委托号，value为系统委托号
        self.orderIdDict = {}           # key为系统委托号，value为本地委托号
        self.cancelDict = {}            # key为本地委托号，value为撤单请求

        self.recordOrderId_BefVolume = {}       # 记录的之前处理的量

        self.tradeID = 0

        self.local_status_dict = {}
        self.registerSymbolPairArray = set([])

        self.initCallback()

    #----------------------------------------------------------------------
    def subscribe(self ,subscribeReq):
        """订阅行情"""
        pass

    #----------------------------------------------------------------------
    def onMessage(self, ws, evt):
        """信息推送"""
        # print evt
        pass

    #----------------------------------------------------------------------
    def onError(self, ws, evt):
        """错误推送"""
    pass
    #----------------------------------------------------------------------
    def onError(self, data):
        pass

    #----------------------------------------------------------------------
    def onClose(self, ws):
        """接口断开"""
        # 如果尚未连上，则忽略该次断开提示
        pass


    #----------------------------------------------------------------------
    def onOpen(self, ws):
        """连接成功"""
        pass

    #----------------------------------------------------------------------
    def initCallback(self):
        pass

    #----------------------------------------------------------------------
    def writeLog(self, content):
        """快速记录日志"""
        pass

    #----------------------------------------------------------------------
    def onTicker(self, data):
        """"""
        pass
    #----------------------------------------------------------------------
    def onDepth(self, data):
        """"""
        pass


    #----------------------------------------------------------------------
    def onTrades(self, data):
        pass
        # try:
        #     channel = data['channel']
        #     symbol = self.channelSymbolMap[channel]
        # except Exception,ex:
        #     symbol = None

        # if symbol == None:
        #     return

    #----------------------------------------------------------------------
    def spotAllOrders(self):
        pass

    #----------------------------------------------------------------------
    def onSpotOrder(self, data):
        pass
    #----------------------------------------------------------------------
    def onSpotCancelOrder(self, data):
        pass

    #----------------------------------------------------------------------
    def spotSendOrder(self, req):
        """发单"""
        pass
    #----------------------------------------------------------------------
    def spotCancel(self, req):
        """撤单"""
        pass

    #----------------------------------------------------------------------
    def onSpotGetOrder(self , data):
        """生成时间"""
        pass

    #----------------------------------------------------------------------
    def onSpotGetOrders(self, data):
        pass



    #----------------------------------------------------------------------
    def onSpotUserInfo(self, data):
        pass
    #----------------------------------------------------------------------
    def generateDateTime(self, s):
        """生成时间"""
        dt = datetime.fromtimestamp(float(s)/1e3)
        time = dt.strftime("%H:%M:%S.%f")
        date = dt.strftime("%Y%m%d")
        return date, time

    #----------------------------------------------------------------------
    def generateDateTimeAccordingLocalTime(self):
        dt = datetime.now()
        time = dt.strftime("%H:%M:%S.%f")
        date = dt.strftime("%Y%m%d")
        return date, time
        