# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import CDNTable,RegionTable,ApplicationTable,ApplicationDomainTable,ControlDomainTable,ControlIpTable
from .models import restype,CoverTable
import xadmin

from SystemManager20 import xadminconfig





#域显示行
class regioninline(object):
    model = RegionTable
#调度控制域名显示行
class ControlDomainline(object):
    model = ControlDomainTable
#调度控制ip显示行
class ControlIpline(object):
    model = ControlIpTable
#域名显示行
class ApplicationDomainline(object):
    model = ApplicationDomainTable


#cdn管理显示
class CDNTableXAdmin(object):
    list_display = ('CDN','pub_date', 'update_time',)
    search_fields = ('CDN',)
    inlines = [regioninline,ControlDomainline,ControlIpline]
    show_bookmarks = False
xadmin.site.register(CDNTable,CDNTableXAdmin)


#应用表
class ApplicationTableXAdmin(object):
    list_display = ('app','pub_date','update_time',)
    # 不显示书签
    search_fields = ('app',)
    show_bookmarks = False
    #inlines=[regioninline]
xadmin.site.register(ApplicationTable,ApplicationTableXAdmin)



#域管理显示
class RegionTableXAdmin(object):
   list_display = ('region','CDN',)
   search_fields = ('region','CDN__CDN',)
   list_filter = ('CDN',)
   # 不显示书签
   inlines = [ApplicationDomainline]
   show_bookmarks = False
xadmin.site.register(RegionTable,RegionTableXAdmin)


#应用资源域名管理显示
class ApplicationDomainTableXAdmin(object):
    def CDN(self,ApplicationDomainTable):
        return  ApplicationDomainTable.region.CDN.CDN
    list_display = ('domain','app','CDN','region','res_type','resoucescover')
    search_fields = ('domain','app__app','region__region',)
    list_filter = ('res_type','region__CDN','resoucescover')
    #不显示书签
    show_bookmarks = False
xadmin.site.register(ApplicationDomainTable,ApplicationDomainTableXAdmin)


#调度控制域名表管理显示
class ControlDomainTableXAdmin(object):
    list_display = ('ControlDomain', 'CDN',)
    search_fields = ('ControlDomain', 'CDN__CDN')
    list_filter = ('CDN',)
    # 不显示书签
    show_bookmarks = False
xadmin.site.register(ControlDomainTable, ControlDomainTableXAdmin)

#调度控制ip管理显示
class ControlIpTableXAdmin(object):
    list_display = ('ControlIp', 'CDN',)
    search_fields = ('ControlIp', 'CDN__CDN')
    show_bookmarks = False
xadmin.site.register(ControlIpTable, ControlIpTableXAdmin)

#域名类型表管理显示
class restypeXADMIN(object):
    list_display = ('restype',)
xadmin.site.register(restype, restypeXADMIN)

#覆盖情况管理显示
class CoverTableXADMIN(object):
     list_display = ('cover',)
xadmin.site.register(CoverTable, CoverTableXADMIN)
