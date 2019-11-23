import cv2
import numpy as np
import os

#def store_raw_images():
#    pic_num = 1
#    
#    if not os.path.exists('pos'):
#        os.makedirs('pos')
#        
#    if pic_num == 1:
#        try:
#            print(pic_num)
#            img = cv2.imread("pos/"+str(pic_num)+".jpg")
#            # should be larger than samples / pos pic (so we can place our image on it)
#            resized_image = cv2.resize(img, (100, 400))
#            cv2.imwrite("pos/"+str(pic_num)+".jpg",resized_image)
#            
#        except Exception as e:
#            print(str(e)) 
            
def create_pos_n_neg():
    for file_type in ['neg']:
        
        for img in os.listdir(file_type):

            if file_type == 'pos':
                line = file_type+'/'+img+' 1 0 0 50 50\n'
                with open('info.dat','a') as f:
                    f.write(line)
            elif file_type == 'neg':
                line = file_type+'/'+img+'\n'
                with open('bg.txt','a') as f:
                    f.write(line)
                    
create_pos_n_neg()
#store_raw_images()