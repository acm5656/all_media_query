from elasticsearch import Elasticsearch
ip = '223.3.84.128'
port = 9200
es = Elasticsearch([{'host':ip,'port':port}])
article_index = "article"
video_index = "video"
qa_index = "qa"
print('load--------------es----------------')
def query_keywords(content,start_from,size):
    body = {
        "from":start_from,
        "size":size,
        "query": {
            "multi_match": {
                "query": content,
                "fields": ["title","title.ik_index", "body","keywords","abstract","answer.body","filename","labels"],
                "operator": "or"
            }
        }
    }
    search_list = es.search(index=[article_index,video_index,qa_index],body=body)
    count_body = query_count(body['query'])
    search_count = es.search(index=[article_index,video_index,qa_index],body=count_body)
    return search_list['hits']['hits'],search_count['hits']['total']['value']

def query_article(content,start_from,size):
    body = {
        "from":start_from,
        "size":size,
        "query": {
            "multi_match": {
                "query": content,
                "fields": ["title","title.ik_index", "body","keywords","abstract"],
                "operator": "or"
            }
        }
    }
    article_list = es.search(index=article_index,body=body)
    count_body = query_count(body['query'])
    article_count = es.search(index=article_index,body=count_body)
    return article_list['hits']['hits'],article_count['hits']['total']['value']

def query_video(content,start_from,size):
    body = {
        "from":start_from,
        "size":size,
        "query": {
            "multi_match": {
                "query": content,
                "fields": ["title","title.ik_index","filename","labels"],
                "operator": "or"
            }
        }
    }
    video_list = es.search(index=video_index,body=body)
    count_body = query_count(body['query'])
    video_count= es.search(index=video_index,body=count_body)
    return video_list['hits']['hits'],video_count['hits']['total']['value']
def query_qa(content,start_from,size):
    body = {
        "from":start_from,
        "size":size,
        "query": {
            "multi_match": {
                "query": content,
                "fields": ["title","title.ik_index","body","labels","answer.body"],
                "operator": "or"
            }
        }
    }
    qa_list = es.search(index=qa_index,body=body)
    count_body = query_count(body['query'])
    qa_count = es.search(index=qa_index,body=count_body)
    return qa_list['hits']['hits'],qa_count['hits']['total']['value']
def query_count(query_str):
    body = {
        'query': {
            'bool': {
            'must': [query_str],
            }
        },
        'size': 0
    }
    return body
if __name__ == '__main__':
    result = query_keywords("测试",0,10)
    print(result)