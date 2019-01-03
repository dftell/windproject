from WindPy import *
import numpy as np
import time
def getIdxSet(strIdxCode,endT):

    RecSet = w.wset("sectorconstituent","date="+endT+";sectorid="+strIdxCode)
    return RecSet;
    pass

def getSecsSerial(strSecCodes,items,begT,endT):
    MarketData = w.wsd(strSecCodes, items, begT, endT, "")
    return MarketData;
    pass

def getSecsDaysSerial(strSecCodes,items,endT,Cycs):
    dbegT = ref(endT, -1*Cycs)
    begT = dbegT.strftime("%Y-%m-%d")
    return getSecsSerial(strSecCodes,items,begT,endT)
#print(MarketData)

#MarketSerial = MarketData.Data[0]
def ref(EndT,cycs):
    days = w.tdaysoffset(cycs, EndT, "")
    return days.Data[0][0]

if __name__ == "__main__":
    w.start()
    strIdxName = "a39901011h000000"
    strIdxName = ""
    endT = "2018-12-31"
    TestData = getSecsDaysSerial("000001.SH","Close",endT,100)
    #print(TestData.Data[0])
    dbegT = ref(endT, -100)
    begT = dbegT.strftime("%Y-%m-%d")
    #print(begT)
    AllSecDatas = getIdxSet(strIdxName,endT);
    idxCodes = AllSecDatas.Data[1];
    #print(idxCodes)
    idxDatas = AllSecDatas.Data;
    idxNames = AllSecDatas.Data[2];
    #print(idxNames)
    '''
    MktSerials = getSecsSerial("000001.SH","Close",begT,endT);
    IdxSerials = getSecsSerial(",".join(idxCodes), "Close", begT, endT);
    
    for i in range(len(idxCodes)):
        iS = IdxSerials.Data[i]
        iBegVal = iS[0]
        iEndVal = iS[len(iS)-1]
        iRate = 100*(iEndVal-iBegVal)/iBegVal
        cr = np.corrcoef(MktSerials.Data[0], iS)
        print(idxNames[i], ",", cr[0, 1],iRate)
    '''