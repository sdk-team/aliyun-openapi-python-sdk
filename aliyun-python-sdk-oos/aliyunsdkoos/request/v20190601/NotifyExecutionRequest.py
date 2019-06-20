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
class NotifyExecutionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'oos', '2019-06-01', 'NotifyExecution','oos')

	def get_ExecutionId(self):
		return self.get_query_params().get('ExecutionId')

	def set_ExecutionId(self,ExecutionId):
		self.add_query_param('ExecutionId',ExecutionId)

	def get_ExecutionStatus(self):
		return self.get_query_params().get('ExecutionStatus')

	def set_ExecutionStatus(self,ExecutionStatus):
		self.add_query_param('ExecutionStatus',ExecutionStatus)

	def get_NotifyNote(self):
		return self.get_query_params().get('NotifyNote')

	def set_NotifyNote(self,NotifyNote):
		self.add_query_param('NotifyNote',NotifyNote)

	def get_TaskName(self):
		return self.get_query_params().get('TaskName')

	def set_TaskName(self,TaskName):
		self.add_query_param('TaskName',TaskName)

	def get_NotifyType(self):
		return self.get_query_params().get('NotifyType')

	def set_NotifyType(self,NotifyType):
		self.add_query_param('NotifyType',NotifyType)

	def get_Parameters(self):
		return self.get_query_params().get('Parameters')

	def set_Parameters(self,Parameters):
		self.add_query_param('Parameters',Parameters)