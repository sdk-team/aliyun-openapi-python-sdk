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

class ReleaseInstancesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'R-kvstore', '2015-01-01', 'ReleaseInstances','r-kvstore')

	def get_async(self):
		return self.get_query_params().get('async')

	def set_async(self,async):
		self.add_query_param('async',async)

	def get_instanceName(self):
		return self.get_query_params().get('instanceName')

	def set_instanceName(self,instanceName):
		self.add_query_param('instanceName',instanceName)

	def get_instanceID(self):
		return self.get_query_params().get('instanceID')

	def set_instanceID(self,instanceID):
		self.add_query_param('instanceID',instanceID)

	def get_channel(self):
		return self.get_query_params().get('channel')

	def set_channel(self,channel):
		self.add_query_param('channel',channel)

	def get_force(self):
		return self.get_query_params().get('force')

	def set_force(self,force):
		self.add_query_param('force',force)

	def get_aliUID(self):
		return self.get_query_params().get('aliUID')

	def set_aliUID(self,aliUID):
		self.add_query_param('aliUID',aliUID)

	def get_resourceName(self):
		return self.get_query_params().get('resourceName')

	def set_resourceName(self,resourceName):
		self.add_query_param('resourceName',resourceName)

	def get_operator(self):
		return self.get_query_params().get('operator')

	def set_operator(self,operator):
		self.add_query_param('operator',operator)