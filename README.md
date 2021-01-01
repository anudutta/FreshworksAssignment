# FreshworksAssignment
# FreshworksAssignment
This is created for Freshworks Assignment.

It is a file based key value data store. This supports the basic  create,read,delete(CRD) operations. The data will be stored as a local storage for an single process on one laptop. The data must be exposed as library to clients than can instantiate a class and work with the data store. The size of the file storing data must never exceed 1GB and more than one client will not be able to use the same file as a data store at any given time.

The data store will support the following :

1. It can be initialized using an optional file path. If one is not provided, it will reliably create itself in a reasonable location on the laptop.
2. A new key-value pair can be added to the data store using the Create operation. The key is always a string - capped at 32chars. The value is always a JSON object - capped at 16KB.
3. If Create is invoked for an existing key, an appropriate error must be returned.
4. A Read operation on a key can be performed by providing the key, and receiving the value in response, as a JSON object.
5. A Delete operation can be performed by providing the key.
6. Every key supports setting a Time-To-Live property when it is created. This property is optional. If provided, it will be evaluated as an integer defining the number of seconds the key must be retained in the data store. Once the Time-To-Live for a key has expired, the key will no longer be available for Read or Delete operations.
7. Appropriate error responses must always be returned to a client if it uses the data store in unexpected ways or breaches any limits
8. The file size never exceeds 1GB
9. The file is accessed by multi-threading

Usage:-

Create an Instance:-
import FileDataStore
a = FileDataStore.fileDataStore()

Create Data:-
a.create('ab', '{"name": "Anu", "email_id": "anu@gmail.com", "m_no": "11"}')     #to create a key with key_name,value given and with time-to-live property value given(number of seconds)

Read:-
a.read("ab") #it returns the value of the respective key in Jasonobject format 'key_name:value'

Delete:-
a.delete("ab")   #it deletes the respective key and its value from the database(memory is also freed)
