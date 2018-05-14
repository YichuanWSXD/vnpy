# encoding: UTF-8

from __future__ import absolute_import
from vnpy.trader import vtConstant
from .ksgoldGateway import KsgoldGateway

gatewayClass = KsgoldGateway
gatewayName = 'KSGOLD'
gatewayDisplayName = u'金仕达黄金'
gatewayType = vtConstant.GATEWAYTYPE_FUTURES
gatewayQryEnabled = True