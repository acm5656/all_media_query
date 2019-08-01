from search_service.dao import query_from_elasticsearch as dao
from search_service.bean.return_data import *
def get_article_dict(article):
    article_dict = {}
    article_dict['id'] = article['_id']
    article_dict['img_url'] = article['_source']['pictures']
    article_dict['title'] = article['_source']['title']
    article_dict['time'] = article['_source']['create_time']
    article_dict['abstract'] = article['_source']['abstract']
    article_dict['key_word'] = article['_source']['keywords']
    article_dict['author'] = article['_source']['author']
    article_dict['like_num'] = "10"
    return article_dict
def query_article_service(content,current_page,item):
    current_page-=1
    start_from = item*current_page
    size = item
    result = return_info(result=False,msg="查询出错,请稍后再试",data=[])
    article_list,count = dao.query_article(content,start_from,size)
    result.count = count
    if article_list != None and len(article_list)!=0:
        result.result = True
        result.msg = "查询成功"
        for article in article_list:
            result.data.append(get_article_dict(article))
    else:
        result.result=False
        result.msg="查询不到数据"
    return result
def get_qa_dict(qa):
    qa_dict = {}
    qa_dict['id'] = qa['_id']
    qa_dict['img_url'] = ""
    qa_dict['title'] = qa['_source']['title']
    qa_dict['labels'] = qa['_source']['labels']
    qa_dict['category'] = qa['_source']['category']
    qa_dict['create_time'] = qa['_source']['create_time']
    return qa_dict
def query_qa_service(content,current_page,item):
    current_page-=1
    start_from = item*current_page
    size = item
    result = return_info(result=False,msg="查询出错,请稍后再试",data=[])
    qa_list,count = dao.query_qa(content,start_from,size)
    result.count = count
    if qa_list != None and len(qa_list)!=0:
        result.result = True
        result.msg = "查询成功"
        for qa in qa_list:
            result.data.append(get_qa_dict(qa))
    else:
        result.result=False
        result.msg="查询不到数据"
    return result
def get_video_dict(video):
    video_dict = {}
    video_dict['id'] = video['_id']
    video_dict['title'] = video['_source']['title']
    video_dict['labels'] = video['_source']['labels']
    video_dict['create_time'] = video['_source']['create_time']
    return video_dict
def query_video_service(content,current_page,item):
    current_page-=1
    start_from = item*current_page
    size = item
    result = return_info(result=False,msg="查询出错,请稍后再试",data=[])
    video_list,count = dao.query_video(content,start_from,size)
    result.count = count
    if video_list != None and len(video_list):
        result.result = True
        result.msg = "查询成功"
        for video in video_list:
            result.data.append(get_video_dict(video))
    else:
        result.result=False
        result.msg="查询不到数据"
    return result
def query_all_by_keywords(content,current_page,item):
    current_page-=1
    start_from = item*current_page
    size = item
    result = return_info(result=False,msg="查询出错,请稍后再试",data=[])
    query_result_item_list,count = dao.query_keywords(content,start_from,size)
    result.count = count
    if query_result_item_list !=None and len(query_result_item_list):
        result.result = True
        result.msg = "查询成功"
        for item in query_result_item_list:
            if item['_index']==dao.qa_index:
                item_dict = get_qa_dict(item)
                item_dict['type']='qa'
            elif item['_index']==dao.article_index:
                item_dict = get_article_dict(item)
                item_dict['type']='article'
            elif item['_index']==dao.video_index:
                item_dict = get_video_dict(item)
                item_dict['type']='video'
            else:
                continue
            result.data.append(item_dict)
    else:
        result.result=False
        result.msg="查询不到数据"
    return result