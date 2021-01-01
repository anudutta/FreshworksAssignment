from threading import Thread
exec(open("E:\\Projects\\FileDataStore.py").read())
import FileDataStore

a = FileDataStore.fileDataStore('E:\\Projects\\abc.txt')

a.create('ab', '{"name": "Anu", "email_id": "anu@gmail.com", "m_no": "11"}')     #to create a key with key_name,value given and with time-to-live property value given(number of seconds)

a.create("cd",  "name": "Chintu", "email_id": "chintu@gmail.com", "m_no": None,  5000)   #to create a key with key_name,value given and with time-to-live property value given(number of seconds)

a.create("ef",  "name": "Tom", "email_id": "tom@gmail.com", "m_no": None)    #to create a key with key_name,value given and with no time-to-live property

a.create("ab",  "name": "Chintu", "email_id": "chintu@gmail.com", "m_no": None,  5000) #it returns an ERROR since the key_name already exists in the database

print(a.read("ab")) #it returns the value of the respective key in Jasonobject format 'key_name:value'

print(a.read("xy")) # it returns error as the given key does not exist in database

a.delete("ab")   #it deletes the respective key and its value from the database(memory is also freed)
a.delete("xy")   #it returns error as the given key does not exist in database




#we can access these using multiple threads like
#t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
#t1.start()
#t1.sleep()
#t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
#t2.start()
#t2.sleep()
#and so on upto tn

