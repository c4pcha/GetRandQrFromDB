import qrcode
from random import randint


test_db = ["test0","test1","test2","test3","test4"]


class QrUtils:
    def __init__(self):
        pass
    
    def get_qr(self,ids:list=[]):
        
        qrs=[]
        for i in ids:
            qrs.append(qrcode.make(self.database[i]))
            
        return qrs,ids
    
    
    def get_rand_qr(self,cantity:int=0):
        ids=[]
        for i in range(cantity):
            ids.append(randint(0,len(self.database)-1))

        qrs=[]
        for i in ids:
            qrs.append(qrcode.make(self.database[i]))
            
        return qrs,ids
    
    def config(self,database):
        self.database= database

    
    def __del__(self):
        pass

if __name__ == "__main__":
    
    #Example of use.
    #Getting 6 random Qr from the test database
    qrutils = QrUtils()
    qrutils.config(database=test_db)
    qrs,ids= qrutils.get_rand_qr(6)
    qrs_iter= iter(qrs)
    name = 0
    for i in ids:
        next(qrs_iter).save(str(name)+" - random.jpg")
        name += 1
        
    #Other Example of use
    #Getting 2 specific Qr from database
    
    qrutils = QrUtils()
    qrutils.config(database=test_db)
    qrs,ids= qrutils.get_qr([0,4])
    qrs_iter= iter(qrs)
    name = 0
    for i in ids:
        next(qrs_iter).save(str(name)+" - specific.jpg")
        name += 1
    