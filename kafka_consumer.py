from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
from search_service.dao.query_from_elasticsearch import ip,port
from add_elasticsearch_article import *
import add_elasticsearch_qa as qa
import add_elasticsearch_article as article
import add_elasticsearch_video as video
import json
def do_es(message):
    values = str(message.value,'utf-8')
    result = json.loads(values)
    if result['table'] == 'video':
        if result['type'] == 'UPDATE':
            video.update_video(result['data'],es)
            pass
        elif result['type'] == 'INSERT':
            video.add_video(result['data'],es)
            pass
        elif result['type'] == 'DELETE':
            video.delete_video(result['data'],es)
            pass
        pass
    elif result['table'] == 'article':
        if result['type'] == 'UPDATE':
            article.update_article(result['data'],es)
            pass
        elif result['type'] == 'INSERT':
            article.add_article(result['data'],es)
            pass
        elif result['type'] == 'DELETE':
            article.delete_article(result['data'],es)
            pass
        pass
    elif result['table'] == 'question':
        if result['type'] == 'UPDATE':
            qa.update_question(result['data'],es)
            pass
        elif result['type'] == 'INSERT':
            qa.add_question(result['data'],es)
            pass
        elif result['type'] == 'DELETE':
            qa.delete_question(result['data'],es)
            pass
        pass
    elif result['table'] == 'answer':
        if result['type'] == 'UPDATE':
            qa.update_answer(result['data'],es)
            pass
        elif result['type'] == 'INSERT':
            qa.add_answer(result['data'],es)
            pass
        elif result['type'] == 'DELETE':
            qa.delete_answer(result['data'],es)
            pass
        pass
    else:
        pass

f_write_error = open('./logs/kafka_error.log','w',encoding='utf-8')
es = Elasticsearch([{'host':ip,'port':port}])
consumer = KafkaConsumer(bootstrap_servers='seu:9092')
consumer.subscribe(['mysql'])
for message in consumer:
    try:
        do_es(message)
    except:
        values = str(message.value, 'utf-8')
        # result = json.loads(values)
        print("出错了，请查看log日志")
        f_write_error.write("出错了："+values+'\n')
        f_write_error.flush()
f_write_error.close()

