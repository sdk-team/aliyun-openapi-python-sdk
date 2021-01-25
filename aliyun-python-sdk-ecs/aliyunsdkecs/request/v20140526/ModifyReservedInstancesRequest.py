# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest

class ModifyReservedInstancesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'ModifyReservedInstances')
		self.set_method('POST')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_Configuration(self):
		return self.get_query_params().get('Configuration')

	def set_Configuration(self, Configurations):
		for depth1 in range(len(Configurations)):
			if Configurations[depth1].get('ZoneId') is not None:
				self.add_query_param('Configuration.' + str(depth1 + 1) + '.ZoneId', Configurations[depth1].get('ZoneId'))
			if Configurations[depth1].get('ReservedInstanceName') is not None:
				self.add_query_param('Configuration.' + str(depth1 + 1) + '.ReservedInstanceName', Configurations[depth1].get('ReservedInstanceName'))
			if Configurations[depth1].get('InstanceType') is not None:
				self.add_query_param('Configuration.' + str(depth1 + 1) + '.InstanceType', Configurations[depth1].get('InstanceType'))
			if Configurations[depth1].get('Scope') is not None:
				self.add_query_param('Configuration.' + str(depth1 + 1) + '.Scope', Configurations[depth1].get('Scope'))
			if Configurations[depth1].get('InstanceAmount') is not None:
				self.add_query_param('Configuration.' + str(depth1 + 1) + '.InstanceAmount', Configurations[depth1].get('InstanceAmount'))

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_ReservedInstanceId(self):
		return self.get_query_params().get('ReservedInstanceId')

	def set_ReservedInstanceId(self, ReservedInstanceIds):
		for depth1 in range(len(ReservedInstanceIds)):
			if ReservedInstanceIds[depth1] is not None:
				self.add_query_param('ReservedInstanceId.' + str(depth1 + 1) , ReservedInstanceIds[depth1])