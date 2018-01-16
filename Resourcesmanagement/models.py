# -*- coding: utf-8 -*-


from django.db import models




#cdn表
class CDNTable(models.Model):
    CDN = models.CharField(u'CDN名称', max_length=30)
    CDN_Remarks = models.TextField(u'备注', null=True, blank=True)
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    class Meta:
        verbose_name = 'CDN表'
        verbose_name_plural = 'CDN表'
        #确保唯一
        unique_together = ['CDN']
        ordering = ['CDN']

    def __str__(self):
        return self.CDN

#域表
class RegionTable(models.Model):
    region = models.CharField(u'域', max_length=30)
    CDN = models.ForeignKey('CDNTable',on_delete=models.CASCADE,)
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    class Meta:
        verbose_name = 'CDN域表'
        verbose_name_plural = 'CDN域表'
        #确保唯一
        unique_together = ['region']
        ordering = ['region']

    def __str__(self):
        return self.region

#应用表
class ApplicationTable(models.Model):
    app = models.CharField(u'应用', max_length=30)
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    class Meta:
        verbose_name = '应用表'
        verbose_name_plural = '应用表'
        # 确保唯一
        unique_together = ['app']
        ordering = ['app']

    def __str__(self):
        return self.app

#应用域名表
class ApplicationDomainTable(models.Model):
    domain = models.CharField(u'域名', max_length=50)
    app = models.ForeignKey('ApplicationTable', verbose_name='应用',on_delete=models.CASCADE,)
    region = models.ForeignKey('RegionTable',verbose_name='域',on_delete=models.CASCADE,)
    res_type = models.ForeignKey('restype',verbose_name='类型',on_delete=models.CASCADE,)
    resoucescover=models.ForeignKey('CoverTable', verbose_name='覆盖情况',null=True,on_delete=models.CASCADE,)
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    class Meta:
        verbose_name = '应用域名表'
        verbose_name_plural = '应用域名表'
        # 确保域名。应用。域三个组合唯一，单独或其中两个可相同
        unique_together = ['domain','region','app']
        ordering = ['domain']

    def __str__(self):
        return  self.domain

#调度控制域名表
class ControlDomainTable(models.Model):
    ControlDomain=models.CharField(u'调度控制域名',max_length=30)
    CDN = models.ForeignKey('CDNTable',on_delete=models.CASCADE,)
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    class Meta:
        verbose_name = '调度控制域名表'
        verbose_name_plural = '调度控制域名表'
        # 确保唯一
        unique_together = ['ControlDomain']
        ordering = ['ControlDomain']

    def __str__(self):
        return self.ControlDomain


#调度IP表
class ControlIpTable(models.Model):
    ControlIp = models.GenericIPAddressField(u'调度ip',protocol='ipv4')
    CDN = models.ForeignKey('CDNTable',on_delete=models.CASCADE,)
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)
    class Meta:
        verbose_name = '调度控制ip表'
        verbose_name_plural = '调度控制ip表'
        # 确保唯一
        unique_together = ['ControlIp']
        ordering = ['ControlIp']
    def __str__(self):
        return self.ControlIp + '\n' + self.CDN.CDN

#域名类型
class restype(models.Model):
   restype=models.CharField(u'类型',max_length=50)
   pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
   update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

   class Meta:
       verbose_name = '域名类型表'
       verbose_name_plural = '域名类型表'

   def __str__(self):
       return self.restype

#覆盖情况表
class CoverTable(models.Model):
    cover = models.CharField(u'覆盖情况', max_length=50)
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    class Meta:
        verbose_name = '覆盖情况'
        verbose_name_plural = '覆盖情况'

    def __str__(self):
        return self.cover