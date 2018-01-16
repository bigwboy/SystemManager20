# -*- coding: utf-8 -*-


from django.db import models




#cp联系人管理表
class PersonnelTatble(models.Model):
    CDN = models.ForeignKey('Resourcesmanagement.CDNTable',on_delete=models.CASCADE,)
    Name = models.CharField(u'姓名', max_length=40,unique=True)
    Phone = models.CharField(u'电话', max_length=40,null=True,blank=True)
    QQNunmber = models.BigIntegerField(u'QQ号',null=True,unique=True,blank=True)
    Email = models.EmailField(u'邮箱',null=True,blank=True)
    Remarks = models.TextField(u'备注',null=True,blank=True)
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    class Meta:
        verbose_name = '联系人信息'
        verbose_name_plural = '联系人信息'
        ordering = ['Name']

    def __str__(self):
        return self.Name
