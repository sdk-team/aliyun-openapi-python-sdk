# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class QueryPriceForTempUpgradeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'QueryPriceForTempUpgrade','rds')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_CountryCode(self):
		return self.get_query_params().get('CountryCode')

	def set_CountryCode(self,CountryCode):
		self.add_query_param('CountryCode',CountryCode)

	def get_CurrencyCode(self):
		return self.get_query_params().get('CurrencyCode')

	def set_CurrencyCode(self,CurrencyCode):
		self.add_query_param('CurrencyCode',CurrencyCode)

	def get_DBInstanceId(self):
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self,DBInstanceId):
		self.add_query_param('DBInstanceId',DBInstanceId)

	def get_BusinessInfo(self):
		return self.get_query_params().get('BusinessInfo')

	def set_BusinessInfo(self,BusinessInfo):
		self.add_query_param('BusinessInfo',BusinessInfo)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_CommodityCode(self):
		return self.get_query_params().get('CommodityCode')

	def set_CommodityCode(self,CommodityCode):
		self.add_query_param('CommodityCode',CommodityCode)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_UsedTime(self):
		return self.get_query_params().get('UsedTime')

	def set_UsedTime(self,UsedTime):
		self.add_query_param('UsedTime',UsedTime)

	def get_DBInstanceClass(self):
		return self.get_query_params().get('DBInstanceClass')

	def set_DBInstanceClass(self,DBInstanceClass):
		self.add_query_param('DBInstanceClass',DBInstanceClass)

	def get_PromotionCode(self):
		return self.get_query_params().get('PromotionCode')

	def set_PromotionCode(self,PromotionCode):
		self.add_query_param('PromotionCode',PromotionCode)

	def get_OrderType(self):
		return self.get_query_params().get('OrderType')

	def set_OrderType(self,OrderType):
		self.add_query_param('OrderType',OrderType)