article_index = "article"
def add_article(data_list,es):
    for data in data_list:
        es.index(index=article_index,id=str(data['id'])+'_'+str(data['version']),body=data)
    pass
def delete_article(data_list,es):
    for data in data_list:
        es.delete(index=article_index,id=str(data['id'])+'_'+str(data['version']))
    pass
def update_article(data_list,es):
    for data in data_list:
        es.update(index=article_index,id=str(data['id'])+'_'+str(data['version']),body ={"doc":data})
    pass