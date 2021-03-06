#!/usr/bin/python
#
# Copyright 2016 BMC Software, Inc.
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
#
class Animal(object):

    def __init__(self):
        self.voice = "???"

    def speak(self):
        print('{0} says "{1}"'.format(self.__class__.__name__, self.voice))

class Cat(Animal):

    def __init__(self):
        super(Cat, self).__init__()
        self.voice = 'Meow!'

class Dog(Animal):

    def __init__(self):
        super(Dog, self).__init__()
        self.voice = 'Woof!'


if __name__ == '__main__':
    animal = Animal()
    animal.speak()

    cat = Cat()
    cat.speak()

    dog = Dog()
    dog.speak()
