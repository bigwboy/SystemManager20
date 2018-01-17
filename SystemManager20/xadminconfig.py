import xadmin
import xadmin.views
#全局设置
class GlobalSetting(object):
    # 设置base_site.html的Title
    site_title = '系统管理平台1.1'
    # 设置base_site.html的Footer
    site_footer  = '浙江华通云科技有限公司' +\
                   '\n'+'        -----系统运维部'
    #设置右边折叠
    menu_style = "accordion"
    apps_label_title = {
        'auth' : u'权限管理',
        'resourcesmanagement':u'资源管理',
        'personnelmanagement':u'联系人管理',
        'ipaddrmanagement': u'地址库管理',
        'returnchecklogmanagement':'返回日志',
        'userupload':'上传文件管理',
        'computerroommanagerment':u'机房管理',
    }
xadmin.site.register(xadmin.views.CommAdminView, GlobalSetting)

