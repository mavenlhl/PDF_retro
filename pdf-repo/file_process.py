import os

class process(object):
    def __init__(self,filepath:str):
        self.filepath = filepath
        self.suffix = ".pdf"
        self.leng = len(self.filepath+"//")
    
    def __get_file_name(self):
        list_file_name = []
        for each_name in os.listdir(self.filepath):
            file = os.path.join(self.filepath,each_name)
            list_file_name.append(file)

        return list_file_name 
    
    def sort_file(self):
        
        for i in self.__get_file_name():
            print(i)
            af_name = input("输入改变后的名称")#必须是数字：1~999
            k = os.rename(i,os.path.join(self.filepath,af_name+self.suffix))
            print("转换后的名字{}".format(k))

    def final_name(self):
        list_tmp = []
        final_name_list=[]
        for i in self.__get_file_name():
            num = int(i[self.leng-1:].split(".")[0])
            list_tmp.append(num)
        
        list_tmp.sort()
        for j in range(len(list_tmp)):
            final_name_list.append(os.path.join(self.filepath,str(list_tmp[j])+self.suffix))
        return final_name_list
 

if __name__ == "__main__":
    x = process(filepath="pdf-data").final_name()
    print(x)
    pass
        