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
class ModifyReservedInstancesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2016-03-14', 'ModifyReservedInstances','ecs')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_Configurations(self):
		return self.get_query_params().get('Configurations')

	def set_Configurations(self,Configurations):
		for i in range(len(Configurations)):	
			if Configurations[i].get('ZoneId') is not None:
				self.add_query_param('Configuration.' + str(i + 1) + '.ZoneId' , Configurations[i].get('ZoneId'))
			if Configurations[i].get('ReservedInstanceName') is not None:
				self.add_query_param('Configuration.' + str(i + 1) + '.ReservedInstanceName' , Configurations[i].get('ReservedInstanceName'))
			if Configurations[i].get('InstanceType') is not None:
				self.add_query_param('Configuration.' + str(i + 1) + '.InstanceType' , Configurations[i].get('InstanceType'))
			if Configurations[i].get('Scope') is not None:
				self.add_query_param('Configuration.' + str(i + 1) + '.Scope' , Configurations[i].get('Scope'))
			if Configurations[i].get('InstanceAmount') is not None:
				self.add_query_param('Configuration.' + str(i + 1) + '.InstanceAmount' , Configurations[i].get('InstanceAmount'))


	def get_Tags(self):
		return self.get_query_params().get('Tags')

	def set_Tags(self,Tags):
		for i in range(len(Tags)):	
			if Tags[i].get('Key') is not None:
				self.add_query_param('Tag.' + str(i + 1) + '.Key' , Tags[i].get('Key'))
			if Tags[i].get('Value') is not None:
				self.add_query_param('Tag.' + str(i + 1) + '.Value' , Tags[i].get('Value'))


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

	def get_ReservedInstanceIds(self):
		return self.get_query_params().get('ReservedInstanceIds')

	def set_ReservedInstanceIds(self,ReservedInstanceIds):
		for i in range(len(ReservedInstanceIds)):	
			if ReservedInstanceIds[i] is not None:
				self.add_query_param('ReservedInstanceId.' + str(i + 1) , ReservedInstanceIds[i]);