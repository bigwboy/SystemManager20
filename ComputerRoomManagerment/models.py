
# -*- coding: utf-8 -*-
from django.db import models




#机房管理表
class ComputerRoomTable(models.Model):
    ComputerRoomName = models.CharField(u'机房名称', max_length=40)
    ComputerRoomAddress = models.CharField(u'机房位置', max_length=200)
    ComputerRoomPhone = models.CharField(u'联系电话', max_length=40)
    Remarks = models.TextField(u'备注', null=True, blank=True)
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    class Meta:
        verbose_name = '机房信息'
        verbose_name_plural = '机房信息'
        #ordering = ['']

    def __unicode__(self):
        return self.ComputerRoomName

#服务器信息表
class ServerMachineTable(models.Model):
    ManufacturersName=models.ForeignKey('EquipmentManufacturersTable',on_delete=models.CASCADE,)
    ManufacturersType=models.CharField(u'机器型号', max_length=100)
    SNNumber= models.CharField(u'SN号', max_length=100)
    DiskType = models.CharField(u'硬盘类型', max_length=20)
    DiskSize= models.CharField(u'硬盘大小', max_length=20)
    RAMSize=models.CharField(u'内存大小', max_length=20)
    CDN = models.ForeignKey('Resourcesmanagement.CDNTable',on_delete=models.CASCADE,)
    CabinetName = models.ForeignKey('CabinetTable',on_delete=models.CASCADE,)
    NetworkMachineName=models.ForeignKey('NetworkMachineTable',on_delete=models.CASCADE,)
    Remarks = models.TextField(u'备注', null=True, blank=True)
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    class Meta:
        verbose_name = '服务器信息'
        verbose_name_plural = '服务器信息'
        #ordering = ['']

    def __unicode__(self):
        return self.pub_date


#网络设备信息表
class NetworkMachineTable(models.Model):
    NetworkMachineName=models.CharField(u'机器名', max_length=100)
    CabinetName = models.ForeignKey('CabinetTable',on_delete=models.CASCADE,)
    NetworkMachineType=models.CharField(u'机器型号', max_length=100)
    PortSize=models.CharField(u'端口数', max_length=100)
    Remarks = models.TextField(u'备注', null=True, blank=True)
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)
    class Meta:
        verbose_name = '网络设备信息'
        verbose_name_plural = '网络设备信息'
        #ordering = ['']

    def __unicode__(self):
        return self.NetworkMachineName

#机柜信息表
class CabinetTable(models.Model):
    CabinetName = models.CharField(u'机柜名称', max_length=40)
    ComputerRoomName = models.ForeignKey('ComputerRoomTable',on_delete=models.CASCADE,)
    CabinetSize = models.CharField(u'机柜高度', max_length=40)
    Remarks = models.TextField(u'备注', null=True, blank=True)
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    class Meta:
        verbose_name = '机柜信息'
        verbose_name_plural = '机柜信息'
        #ordering = ['']

    def __unicode__(self):
        return self.CabinetName

#设备厂商表
class EquipmentManufacturersTable(models.Model):
    ManufacturersName= models.CharField(u'厂商名称', max_length=40)
    Remarks = models.TextField(u'备注', null=True, blank=True)
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    class Meta:
        verbose_name = '设备厂商'
        verbose_name_plural = '设备厂商'
        # ordering = ['']

    def __unicode__(self):
        return self.ManufacturersName