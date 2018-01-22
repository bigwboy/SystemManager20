# SystemManager20
#系统管理平台，移植为python3.6。django2.0.1平台，xadmin2.0
##新增django-rest-framework接口调试


爬坑说：
  1、 centos7.0,安装python3.6，命令 ./configure --enable-optimizations --with-ssl 默认新版本pip 安装程序 需要ssl模块，所有必须在安装时候默认连接为ssl。然后make make install 如旧。
  2、由于采用xadmin2.0模块，目前该模版有一定bug，已经清楚，需要调整/xadmin/widgets.py 79行添加  
        #guanguang20180117
        input_html=re.split('\>',input_html[0])
     87行调整为
        #guanguang20180117
        '</i></span>%s<span class="input-group-btn"><button class="btn btn-default" type="button">%s</button></span></div></div>' % (input_html[0]+'>', _(u'Today'), input_html[1]+'>', _(u'Now'))

