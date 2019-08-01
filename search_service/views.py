
from django.shortcuts import HttpResponse
from search_service.service.elasticsearch_service import *
from search_service.bean.return_data import *
from django.views.decorators.csrf import csrf_exempt
import json
import logging
import traceback
logger = logging.getLogger("django")

# Create your views here.
@csrf_exempt
def test(request):
    return HttpResponse("test_cmai_all_media", content_type="application/json")
@csrf_exempt
def search_key_word(request):
    result = return_info(result=False,msg="查询出错,请稍后再试",data=[])
    try:
        if request.method == "GET":
            content = request.GET.get('content',"")
            item = int(request.GET.get('item',10))
            current_page = int(request.GET.get("current_page",1))
            logger.info(content+str(item)+str(current_page))
            result = query_all_by_keywords(content,current_page,item)
            logger.info(json.dumps(result,default=result2dict))
    except:
        logger.error(traceback.format_exc())
    return HttpResponse(json.dumps(result,default=result2dict),content_type="application/json")
@csrf_exempt
def search_article_key_word(request):
    result = return_info(result=False,msg="查询出错,请稍后再试",data=[])
    try:
        if request.method == "GET":
            content = request.GET.get('content',"")
            item = int(request.GET.get('item',10))
            current_page = int(request.GET.get("current_page",1))
            logger.info(content+str(item)+str(current_page))
            result = query_article_service(content,current_page,item)
            logger.info(json.dumps(result,default=result2dict))
    except:
        logger.error(traceback.format_exc())
    return HttpResponse(json.dumps(result,default=result2dict),content_type="application/json")
def search_video_key_word(request):
    result = return_info(result=False,msg="查询出错,请稍后再试",data=[])
    try:
        if request.method == "GET":
            content = request.GET.get('content',"")
            item = int(request.GET.get('item',10))
            current_page = int(request.GET.get("current_page",1))
            logger.info(content+str(item)+str(current_page))
            result = query_video_service(content,current_page,item)
            logger.info(json.dumps(result,default=result2dict))
    except:
        logger.error(traceback.format_exc())
    return HttpResponse(json.dumps(result,default=result2dict),content_type="application/json")
def search_qa_key_word(request):
    result = return_info(result=False,msg="查询出错,请稍后再试",data=[])
    try:
        if request.method == "GET":
            content = request.GET.get('content',"")
            item = int(request.GET.get('item',10))
            current_page = int(request.GET.get("current_page",1))
            logger.info(content+str(item)+str(current_page))
            result = query_qa_service(content,current_page,item)
            logger.info(json.dumps(result,default=result2dict))
    except:
        logger.error(traceback.format_exc())
    return HttpResponse(json.dumps(result,default=result2dict),content_type="application/json")