class return_info():
    def __init__(self,result=True,msg="",data=[],count = 0):
        self.result = result
        self.msg = msg
        self.data = data
        self.count = count

def result2dict(result):
    return {
        'result':result.result,
        'msg':result.msg,
        'count': result.count,
        'data':result.data,

    }
