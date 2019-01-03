# encoding: UTF-8
import NetFileAccess
def InitClass(self):
    self.writeLog("初始化类")
    self.vtSymbols = []
    self.targetSetting = {}  # 个股交易目标字典
    self.ordersizeSetting = {}  # 每次委托数量字典
    pass

def Init(self):
    self.writeLog("初始化策略")
    """初始化策略（必须由用户继承实现）"""
    setting = NetFileAccess.getNetObjectList("/Python/Exchange/Subscribe/test/Monitor.txt")
    if not setting:
        self.writeLog(u'配置文件加载失败，请检查')
        return
    # 订阅行情
    for d in setting:
        vtSymbol = '.'.join([d['symbol'], d['exchange']])
        self.vtSymbols.append(vtSymbol)
        self.subscribe(vtSymbol)
        self.writeLog("Load:"+vtSymbol)
        # self.targetSetting[vtSymbol] = int(d['target'])
        # self.ordersizeSetting[vtSymbol] = int(d['ordersize'])
    self.writeLog("订阅完所有行情")
    pass

def onStart(self):
    self.writeLog("开始运行")
    pass

def onStop(self):
    self.writeLog("停止运行")
    pass

def getExchangeList(self):
    self.writeLog("获得交易细节清单")

    pass

def AllowExchange(self):
    self.writeLog("允许交易")
    pass

