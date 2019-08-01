from elasticsearch import Elasticsearch
from search_service.dao.query_from_elasticsearch import ip,port
import time
article_index = "article"
es = Elasticsearch([{'host':ip,'port':port}])
def create_article():
    global es
    global article_index
    _index_mappings = {
        "mappings": {
            "properties": {
                "id":{
                    "type": "long",
                },
                "version": {
                    "type": "long",
                },
                "title": {
                    "type": "text",
                    "index": True,
                    "store": True,
                    "analyzer":"standard",
                    "search_analyzer": "ik_smart",
                    "fields":{
                        "ik_index":{
                            "type":"text",
                            "analyzer": "ik_max_word",
                            "search_analyzer": "ik_smart"
                        }
                    },
                },
                "author": {
                    "type": "long",
                },
                "body": {
                    "type": "text",
                    "index": True,
                    "analyzer": "ik_max_word",
                    "search_analyzer": "ik_max_word",
                    "store": False,
                },
                "abstract": {
                    "type": "text",
                    "index": True,
                    "analyzer": "ik_max_word",
                    "search_analyzer": "ik_max_word",
                    "store": False,
                },
                "keywords": {
                    "type": "text",
                    "index": True,
                    "analyzer": "ik_max_word",
                    "search_analyzer": "ik_max_word",
                    "store": False,
                },
                "entities": {
                    "type": "text",
                    "index": True,
                    "analyzer": "ik_max_word",
                    "search_analyzer": "ik_max_word",
                    "store": False,
                },
                "pictures":{
                    "type":"text"
                },
                "level": {
                    "type": "long",
                },
                "source": {
                    "type": "text",
                    "index": True,
                    "analyzer": "ik_max_word",
                    "search_analyzer": "ik_max_word",
                    "store": False,
                },
                "category": {
                    "type": "text",
                },
                "subcategory": {
                    "type": "text",
                },
                "is_original": {
                    "type": "long",
                },
                "copyright_id": {
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
                }
            }
        }
    }
    es.indices.create(index=article_index,body=_index_mappings)
def add_article_test():
    body1={"title":"文章1","version":"1","author":"1","body":"文章测试，华为手机等",
          "abstract":"摘要","keywords":"关键词组","entities":"实体词组","level":"1",
          "source":"来源","category":"一级类别","subcategory":"二级类别","is_original":"1",
          "copyright_id":"1","create_time":int(round(time.time()*1000)),"update_time":int(round(time.time()*1000)),"commit_time":int(round(time.time()*1000)),
          "publish_time":int(round(time.time()*1000)),"status":1}
    body2={"title":"文章2文","version":"1","author":"1","body":"文章测试，华为手机等",
          "abstract":"摘要","keywords":"关键词组","entities":"实体词组","level":"1",
          "source":"来源","category":"一级类别","subcategory":"二级类别","is_original":"1",
          "copyright_id":"1","create_time":int(round(time.time()*1000)),"update_time":int(round(time.time()*1000)),"commit_time":int(round(time.time()*1000)),
          "publish_time":int(round(time.time()*1000)),"status":1}
    body3={"title":"文章3文章","version":"1","author":"1","body":"文章测试，华为手机等",
          "abstract":"摘要","keywords":"关键词组","entities":"实体词组","level":"1",
          "source":"来源","category":"一级类别","subcategory":"二级类别","is_original":"1",
          "copyright_id":"1","create_time":int(round(time.time()*1000)),"update_time":int(round(time.time()*1000)),"commit_time":int(round(time.time()*1000)),
          "publish_time":int(round(time.time()*1000)),"status":1}
    body4={"title":"文章4","version":"1","author":"1","body":"文章测试，华为手机等",
          "abstract":"摘要","keywords":"关键词组","entities":"实体词组","level":"1",
          "source":"来源","category":"一级类别","subcategory":"二级类别","is_original":"1",
          "copyright_id":"1","create_time":int(round(time.time()*1000)),"update_time":int(round(time.time()*1000)),"commit_time":int(round(time.time()*1000)),
          "publish_time":int(round(time.time()*1000)),"status":1}
    body5={"title":"文章5","version":"1","author":"1","body":"文章测试，华为手机等",
          "abstract":"摘要","keywords":"关键词组","entities":"实体词组","level":"1",
          "source":"来源","category":"一级类别","subcategory":"二级类别","is_original":"1",
          "copyright_id":"1","create_time":int(round(time.time()*1000)),"update_time":int(round(time.time()*1000)),"commit_time":int(round(time.time()*1000)),
          "publish_time":int(round(time.time()*1000)),"status":1}
    global es,article_index
    es.index(index=article_index,body=body1)
    es.index(index=article_index, body=body2)
    es.index(index=article_index, body=body3)
    es.index(index=article_index, body=body4)
    es.index(index=article_index, body=body5)
def show_result(show_list):
    for show_item in show_list['hits']['hits']:
        print(show_item)
def query_all():
    body={
        "from": 0, "size": 100 ,
        "query":{"match_all":{}}
    }
    test = es.search(index=article_index,body=body)
    # print(test)
    show_result(test)
def query_key_word():
    body={
        "query": {
            "multi_match": {
                "query": '文',
                "fields": ["title", "body", "keywords", "abstract"],
                "operator": "or",
            }
        }
    }
    article_list = es.search(index=article_index,body=body)
    show_result(article_list)
# create_article()
# add_article()
def test_key_word():
    body={
        "query": {
            "multi_match": {
                "query": '文',
                "fields": ["title","title.ik_index"],
                "operator": "or",
            }
        },
        "highlight":{
            "fields":{
                "title.ik_index":{},
                "title":{},
            }
        }
    }
    article_list = es.search(index=article_index,body=body)
    show_result(article_list)
def test_count():
    body = {
        'query': {
            'bool': {
            'must': [{"multi_match": {
                "query": '文',
                "fields": ["title","title.ik_index"],
                "operator": "or",
            }}],
            }
        },
        'size': 0
    }
    article_list = es.search(index=article_index,body=body)
    print(article_list)