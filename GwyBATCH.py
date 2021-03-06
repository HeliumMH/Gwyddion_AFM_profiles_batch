import pandas as pd
import os
from datetime import datetime

file_dir=input('---Gwy AFM line profiles batch processing program--- \nPlease enter the dir of the csv file\n')

while file_dir != []:
    if file_dir=='quit':
        quit()
    elif os.path.exists(file_dir)==False:
        print('File not exists or No directory detected')
        file_dir = input('---Gwy AFM line profiles batch processing program--- \nPlease enter the dir of the csv file\n')
        continue
    else:
        #read data
        data = pd.read_csv(file_dir,sep=';',header=None)
        df=pd.DataFrame(data)
        #print(df)
        #print(df.count())
        nline = df.shape[1]
        with open('AFM thickness merge.txt', 'a+') as f:
            print('--- %s write at' %file_dir,datetime.now(),' ---',file=f)
        #processing
        n = 1
        nProfile = 1
        while n<nline-1:
            y0=df.iloc[0,n]
            y1=df.iloc[df.count()[n]-1,n]
            #print(y0,y1)
            height=abs(y0-y1)*1000000000
            print(height)
            with open('AFM thickness merge.txt','a+') as f:
                print(nProfile,'%.2f' %height,sep='   ',file=f)
            height=0
            n+=2
            nProfile+=1

        file_dir = input('Gwy AFM line profiles batch processing program. Please enter the dir of the csv file\n')
        continue




