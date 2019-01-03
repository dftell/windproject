# encoding: UTF-8
import httplib

def getNetObjectList(strSubUrl):
    print('调用获取网络对象列表')
    ret = []
    try:
        conn = httplib.HTTPConnection("www.wolfinv.com")
        conn.request("GET", strSubUrl)
        print("成功连接到本地服务器，尝试连接到："+strSubUrl)
    except:
        print("无法连接到本地服务器。")
        return ret
    r1 = conn.getresponse()
    if r1.status != 200:
        print("无法找到该文件。")
        return ret
    data = r1.read()
    lines = data.splitlines(False)
    strHeader = lines[0]
    cols = strHeader.split(",")
    for c in cols:
        print c
    for s in lines[1:]:
        dic = {}
        vals = s.split(",")
        for c in range(len(cols)):
            dic[cols[c]] = vals[c]
        ret.append(dic)
    return ret
    pass

if __name__ == '__main__':
    print '主程序接口'
    ret = getNetObjectList("/Python/Exchange/Subscribe/test/Monitor.txt")
    for d in ret:
        for c in d:
            print d[c]
    pass