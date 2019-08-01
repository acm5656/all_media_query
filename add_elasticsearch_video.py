from elasticsearch import Elasticsearch
from search_service.dao.query_from_elasticsearch import ip,port
import time
import json
video_index = "video"
def create_video():
    global es
    global video_index
    _index_mappings = {
        "mappings": {
            "properties": {
                "id":{
                    "type": "long",
                },
                "title": {
                    "type": "text",
                    "index": True,
                    "analyzer": "ik_max_word",
                    "search_analyzer": "ik_max_word",
                    "store": False,
                },
                "author": {
                    "type": "long",
                },
                "filename": {
                    "type": "text",
                    "index": True,
                    "analyzer": "ik_max_word",
                    "search_analyzer": "ik_max_word",
                    "store": False,
                },
                "duration": {
                    "type": "long",
                },
                "mine_type": {
                    "type": "long",
                },
                "width": {
                    "type": "long",
                },
                "height": {
                    "type": "long",
                },
                "size": {
                    "type": "text",
                },
                "down_path": {
                    "type": "text",
                },
                "frame_path": {
                    "type": "text",
                },
                "vbit": {
                    "type": "text",
                },
                "frame_rate": {
                    "type": "text",
                },
                "category": {
                    "type": "text",
                },
                "labels": {
                    "type": "text",
                    "index": True,
                    "analyzer": "ik_max_word",
                    "search_analyzer": "ik_max_word",
                    "store": False,
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
    es.indices.create(index=video_index,body=_index_mappings)

def add_video(data_list,es):
    for data in data_list:
        es.index(index=video_index,id=data['id'],body=data)
    pass
def delete_video(data_list,es):
    for data in data_list:
        es.delete(index=video_index,id=data['id'])
    pass
def update_video(data_list,es):
    for data in data_list:
        es.update(index=video_index,id=data['id'],body={"doc":data})
    pass
# create_video()