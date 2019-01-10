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
#check out the file
def getSecsDaysSerial(strSecCodes,items,endT,Cycs):
    dbegT = ref(endT, -1*Cycs)
    begT = dbegT.strftime("%Y-%m-%d")
    return getSecsSerial(strSecCodes,items,begT,endT)

def ref(EndT,cycs):
    days = w.tdaysoffset(cycs, EndT, "")
    return days.Data[0][0]

def getHyWeightList(strSecCode,endT):
    data = w.wset("indexconstituent", "date="+endT+";windcode="+strSecCode)
    #print(data)
    return data.Data[1:4]
if __name__ == "__main__":
    w.start()
    strIdxName = "a39901011h000000"
    endT = "2018-12-31"
    dbegT = ref(endT, -100)
    begT = dbegT.strftime("%Y-%m-%d")
    AllSecDatas = getIdxSet(strIdxName, endT);
    idxCodes = AllSecDatas.Data[1];
    #print(AllSecDatas.Data[1:2])
    for i in range(len(idxCodes)):
        if(i>0):
            break
        strIdex = idxCodes[i]
        IdxSerials = getSecsSerial(strIdex, "Close", begT, endT);
        data = getHyWeightList(strIdex,endT)
        for j in range(len(data[0])):
            SecCode = data[0][j]
            SecName = data[1][j]
            #print(data)
            SecWeight = data[2][j]
            SecSerials = getSecsSerial(SecCode, "Close", begT, endT);
            cr = np.corrcoef(IdxSerials.Data[0], SecSerials.Data[0])
            print(SecCode,SecWeight,SecName,cr[1,0])
        #print(data)
    '''
    
    #strIdxName = ""
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