from elasticsearch import Elasticsearch
from search_service.dao.query_from_elasticsearch import ip,port
import time
qa_index = "qa"
es = Elasticsearch([{'host':ip,'port':port}])
def create_qa():
    global es
    global qa_index
    _index_mappings = {
        "mappings": {

            "properties": {
                "id": {
                    "type":"long"
                },
                "title": {
                    "type": "text",
                    "index": True,
                    "analyzer": "ik_max_word",
                    "search_analyzer": "ik_max_word",
                    "store": False,
                },
                "body": {
                    "type": "text",
                    "index": True,
                    "analyzer": "ik_max_word",
                    "search_analyzer": "ik_max_word",
                    "store": False,
                },
                "category":{
                    "type":"long"
                },
                "labels": {
                    "type": "text",
                    "index": True,
                    "analyzer": "ik_max_word",
                    "search_analyzer": "ik_max_word",
                    "store": False,
                },
                "creator": {
                    "type": "long",
                },
                "create_time": {
                    "type": "date",
                    "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
                },
                "update_time": {
                    "type": "date",
                    "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
                },
                "commit_time": {
                    "type": "date",
                    "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
                },
                "publish_time": {
                    "type": "date",
                    "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
                },
                "status": {
                    "type": "long",
                },
                "answer":{
                    "type":"object",
                    "properties":{
                        "id":{
                            "type":"long"
                        },
                        "version":{
                            "type":"long"
                        },
                        "qid": {
                            "type": "long"
                        },
                        "body": {
                            "type": "text",
                            "index": True,
                            "analyzer": "ik_max_word",
                            "search_analyzer": "ik_max_word",
                            "store": False,
                        },
                        "author": {
                            "type": "long",
                        },
                        "create_time": {
                            "type": "date",
                            "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
                        },
                        "update_time": {
                            "type": "date",
                            "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
                        },
                        "commit_time": {
                            "type": "date",
                            "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
                        },
                        "publish_time": {
                            "type": "date",
                            "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
                        },
                        "status": {
                            "type": "long",
                        },
                    }
                }
            }
        }
    }
    es.indices.create(index=qa_index,body=_index_mappings)
#     int(round(time.time()*1000))
def add_question(data_list,es):
    for data in data_list:
        data['answer'] = []
        print(data)
        es.index(index=qa_index,id=data['id'],body=data)
    pass
def delete_question(data_list,es):
    for data in data_list:
        es.delete(index=qa_index,id=data['id'])
    pass
def update_question(data_list,es):
    for data in data_list:
        question = es.get(index=qa_index,id=data['id'])
        data['answer'] = question['_source']['answer']
        es.update(index=qa_index,id=data['id'],body={"doc":data})
    pass
def add_answer(data_list,es):
    for data in data_list:
        question = es.get(index=qa_index,id=data['qid'])['_source']
        question['answer'].append(data)
        es.update(index=qa_index,id=data['qid'],body={"doc":question})
    # query_all()
    pass
def delete_answer(data_list,es):
    for data in data_list:
        question = es.get(index=qa_index,id=data['qid'])
        index = 0
        for anwser in question['_source']['answer']:
            if anwser['id'] == data['id']:
                question['_source']['answer'].pop(index)
            index+=1
        es.update(index=qa_index,id=data['qid'],body={"doc":question['_source']})
    pass
def update_answer(data_list,es):
    for data in data_list:
        question = es.get(index=qa_index,id=data['qid'])
        index = 0
        for anwser in question['_source']['answer']:
            if anwser['id'] == data['id']:
                question['_source']['answer'][index] = data
            index+=1
        es.update(index=qa_index,id=data['qid'],body={"doc":question['_source']})
    pass
def add_article():
    body1={"title":"问题1,关于华为的","body":"测试内容，华为的手机东西","category":"1","labels":"问答","creator":"1","create_time":int(round(time.time()*1000)),
           "update_time":int(round(time.time()*1000)),"commit_time":int(round(time.time()*1000)),"publish_time":int(round(time.time()*1000)),"status":"1",
           "answer":[{"id":1,"version":1,"qid":"2","body":"诺基亚手机测试不怎么样","author":"1","create_time":int(round(time.time()*1000)),
           "update_time":int(round(time.time()*1000)),"commit_time":int(round(time.time()*1000)),"publish_time":int(round(time.time()*1000)),"status":"1"}]
           }
    body2={"title":"问题1,关于苹果的","body":"测试内容，华为的手机东西","category":"1","labels":"问答","creator":"1","create_time":int(round(time.time()*1000)),
           "update_time":int(round(time.time()*1000)),"commit_time":int(round(time.time()*1000)),"publish_time":int(round(time.time()*1000)),"status":"1",
           "answer":[{"id":1,"version":1,"qid":"2","body":"诺基亚手机测试不怎么样","author":"1","create_time":int(round(time.time()*1000)),
           "update_time":int(round(time.time()*1000)),"commit_time":int(round(time.time()*1000)),"publish_time":int(round(time.time()*1000)),"status":"1"}]
           }
    body3={"title":"问题1,关于华为的","body":"测试内容，华为的手机东西","category":"1","labels":"问答","creator":"1","create_time":int(round(time.time()*1000)),
           "update_time":int(round(time.time()*1000)),"commit_time":int(round(time.time()*1000)),"publish_time":int(round(time.time()*1000)),"status":"1",
           "answer":[{"id":1,"version":1,"qid":"2","body":"任正非手机测试不怎么样","author":"2","create_time":int(round(time.time()*1000)),
           "update_time":int(round(time.time()*1000)),"commit_time":int(round(time.time()*1000)),"publish_time":int(round(time.time()*1000)),"status":"1"}]
           }
    body4={"title":"问题1,关于华为的","body":"测试内容，小米的手机东西","category":"1","labels":"问答","creator":"1","create_time":int(round(time.time()*1000)),
           "update_time":int(round(time.time()*1000)),"commit_time":int(round(time.time()*1000)),"publish_time":int(round(time.time()*1000)),"status":"1",
           "answer":[{"id":1,"version":1,"qid":"2","body":"乔布斯手机测试不怎么样","author":"2","create_time":int(round(time.time()*1000)),
           "update_time":int(round(time.time()*1000)),"commit_time":int(round(time.time()*1000)),"publish_time":int(round(time.time()*1000)),"status":"1"}]
           }
    body5={"title":"问题1,关于oppo的","body":"测试内容，锤子的手机东西","category":"1","labels":"问答","creator":"1","create_time":int(round(time.time()*1000)),
           "update_time":int(round(time.time()*1000)),"commit_time":int(round(time.time()*1000)),"publish_time":int(round(time.time()*1000)),"status":"1",
           "answer":[{"id":1,"version":1,"qid":"2","body":"vivo手机测试不怎么样","author":"1","create_time":int(round(time.time()*1000)),
           "update_time":int(round(time.time()*1000)),"commit_time":int(round(time.time()*1000)),"publish_time":int(round(time.time()*1000)),"status":"1"}]
           }
    global es,qa_index
    es.index(index=qa_index,body=body1)
    es.index(index=qa_index, body=body2)
    es.index(index=qa_index, body=body3)
    es.index(index=qa_index, body=body4)
    es.index(index=qa_index, body=body5)
def show_result(show_list):
    for show_item in show_list['hits']['hits']:
        print(show_item)
def query_all():
    body={
        "from": 0, "size": 100 ,
        "query":{"match_all":{}}
    }
    test = es.search(index=qa_index,body=body)
    # print(test)
    show_result(test)
# create_article()
# add_article()
# query_all()
# create_qa()
query_all()
# test = {'id': '2', 'title': 'yreyer', 'body': 'yyeryery', 'category': '0', 'labels': 'yeryeryer', 'creator': '6', 'create_time': '2019-06-26 20:39:30', 'update_time': None, 'commit_time': None, 'publish_time': None, 'status': '0', 'answer': []}
# test = {'id': '1', 'title': 'testqqqq', 'body': 'qqqq', 'category': '0', 'labels': 'qqqqq', 'creator': '6', 'create_time': '2019-06-26 20:30:18', 'update_time': None, 'commit_time': None, 'publish_time': None, 'status': '0', 'answer': [{'id': '2', 'version': '0', 'qid': '1', 'body': 'aaaaaaaaaaa2222', 'author': '6', 'create_time': '2019-06-26 20:31:34', 'update_time': None, 'commit_time': None, 'publish_time': None, 'status': '0'}]}
# es.update(index=qa_index,id=test['id'],body=test)
