#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Copyright (c) 2002-2017 "Neo Technology,"
# Network Engine for Objects in Lund AB [http://neotechnology.com]
#
# This file is part of Neo4j.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# tag::hello-world-import[]
from neo4j.v1 import GraphDatabase
from base_application import BaseApplication
# end::hello-world-import[]

# tag::hello-world[]
class HelloWorldExample(BaseApplication):
    def __init__(self, uri, user, password):
        super(HelloWorldExample, self).__init__(uri, user, password)

    def _create_and_return_greeting(self, tx, message):
        record_list = list(tx.run("CREATE (a:Greeting) " +
                                  "SET a.message = $message " +
                                  "RETURN a.message + ', from node ' + id(a)",
                                  {"message": message}))
        return str(record_list[0][0])
        
    def print_greeting(self, message):
        with self._driver.session() as session:
            greeting = session.write_transaction(lambda tx: self._create_and_return_greeting(tx, message))
            print(greeting)
# end::hello-world[]

# tag::hello-world-output[]
# hello, world, from node 1234
# end::hello-world-output[]
