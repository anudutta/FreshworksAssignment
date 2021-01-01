import time
import json
import os
from os import path
import sys


class fileDataStore:

    data = {}

    def __init__(self, file_dir=None):

        # If file name is incorrect or it does not exist then program terminate
        if file_dir != None and not os.path.isfile(file_dir):
            print('OSError: Error Occured during loading file')

        if file_dir == None:  # getting current working directory
            file_dir = os.getcwd()

        self.path = file_dir
        try:
            with open(self.path, 'r') as json_file:
                self.data = json.load(json_file)
        except:
            pass

    def create(self,key, value, timeout=0):
            if key in self.data:
                print("error: this key already exists")
            else:
                if key.isalpha():
                    print(os.path.getsize(self.path))
                    print(sys.getsizeof(value))
                    if os.path.getsize(self.path) <= 2**30 and sys.getsizeof(value) <= (16 * 1024 * 1024):
                        if timeout == 0:
                            l = [value, timeout]
                        else:
                            l = [value, time.time() + timeout]
                        if len(key) <= 32:  # constraints for input key_name capped at 32chars
                            self.data[str(key)] = l
                        else:
                            print("error: Memory limit exceeded!! ")
                        with open(self.path, 'w') as json_file:
                            json.dump(self.data, json_file)
                    else:
                        if(os.path.getsize(self.path) >= 2**30):
                            print("error: File size is greter or equal to its limit(1GB)! ")
                        else:
                            print("error: JSON size is greter or equal to 16 KB! ")
                else:
                    print(
                        "error: Invalid key_name!! key_name must contain only alphabets and no special characters or numbers")

    def read(self,key):
            if str(key) not in self.data:
                print(
                    "error: given key does not exist in database. Please enter a valid key")
            else:
                b = self.data[str(key)]
            if b[1] != 0:
                if time.time() < b[1]:  # comparing the present time with expiry time
                    stri = str(key) + ":" + str(
                        b[0])  # to return the value in the format of JasonObject i.e.,"key_name:value"
                    return stri
                else:
                    print("error: time-to-live of", key, "has expired")
            else:
                stri = str(key) + ":" + str(b[0])
                return stri

    def delete(self,key):
            if str(key) not in self.data:
             # error message4
                print(
                    "error: given key does not exist in database. Please enter a valid key")
            else:
                b = self.data[str(key)]
                if b[1] != 0:
                    if time.time() < b[1]:  # comparing the current time with expiry time
                        del self.data[key]
                        print("key is successfully deleted")
                    else:
                        print("error: time-to-live of", key,
                              "has expired")  # error message5
                else:
                    del self.data[key]
                    with open(self.path, 'w') as json_file:
                            json.dump(self.data, json_file)
                    print("key is successfully deleted")
