"""
Micro Code 6.0.1
Author Merwin

In normal mode:
    1,20,000 chrs in 200x200 Image -15
    3 chrs in 1x1 image
In safe mode:
    1,20,000/3 chrs in 200x200 Image -15/3
    1 chrs in 1x1 image
"""

import numpy as np
import cv2
import random


class MicroCode:
    def encryptor_n(self,raw):
        final = ""
        pattern = {'a': 'E', 'b': 'n', 'c': 'e', 'd': 'u', 'e': 'o', 'f': '4', 'g': '9', 'h': 'x', 'i': '1', 'j': 'z', 'k': 'I', 'l': 'S', 'm': '7', 'n': '5', 'o': 'T', 'p': 'd', 'q': 't', 'r': 's', 's': '3', 't': 'v', 'u': 'P', 'v': 'C', 'w': 'J', 'x': 'A', 'y': 'X', 'z': '2', 'A': 'K', 'B': 'O', 'D': '0', 'E': 'Q', 'F': 'y', 'G': '6', 'H': 'H', 'I': 'N', 'J': 'p', 'K': 'L', 'L': 'a', 'M': 'k', 'N': 'q', 'O': 'F', 'P': 'U', 'Q': '8', 'R': 'w', 'S': 'G', 'T': 'j', 'U': 'h', 'V': 'i', 'W': 'm', 'X': 'W', 'Y': 'b', 'Z': 'r', '0': 'M', '1': 'V', '2': 'g', '3': 'Z', '4': 'Y', '5': 'f', '6': 'R', '7': 'l', '8': 'B', '9': 'D'}
        for each in raw:
            final+=pattern.get(each,each)
        return final
    def decryptor_n(self,raw):
        final = ""
        new_pattern = {'E': 'a', 'n': 'b', 'e': 'c', 'u': 'd', 'o': 'e', '4': 'f', '9': 'g', 'x': 'h', '1': 'i', 'z': 'j', 'I': 'k', 'S': 'l', '7': 'm', '5': 'n', 'T': 'o', 'd': 'p', 't': 'q', 's': 'r', '3': 's', 'v': 't', 'P': 'u', 'C': 'v', 'J': 'w', 'A': 'x', 'X': 'y', '2': 'z', 'K': 'A', 'O': 'B', None: 'C', '0': 'D', 'Q': 'E', 'y': 'F', '6': 'G', 'H': 'H', 'N': 'I', 'p': 'J', 'L': 'K', 'a': 'L', 'k': 'M', 'q': 'N', 'F': 'O', 'U': 'P', '8': 'Q', 'w': 'R', 'G': 'S', 'j': 'T', 'h': 'U', 'i': 'V', 'm': 'W', 'W': 'X', 'b': 'Y', 'r': 'Z', 'M': '0', 'V': '1', 'g': '2', 'Z': '3', 'Y': '4', 'f': '5', 'R': '6', 'l': '7', 'B': '8', 'D': '9'}
        for each  in raw:
            final+=new_pattern.get(each,each)
        return final
    def auto_encryption_pattern(self):
        pattern = {}
        chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
         'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
         'U', 'V', 'W', 'X', 'Y', 'Z',"0","1","2","3","4","5","6","7","8","9"]
        for each in chars:
            while True:
                guess = random.choice(chars)
                checked = True
                for each_ in pattern.values():
                    if each_ == guess:
                       checked = False
                if checked:
                    pattern.setdefault(each,guess)
                    break
        return pattern
    def read(self,file_name,password,mode="normal",start_pos=(0,0),dimed_brightness=0,brightness=0,):
        pos_x = start_pos[0]
        pos_y = start_pos[1]
        if mode == "normal":
            result = False
            data = ""
            try:
                file = cv2.imread(file_name)
                file = np.array(file)
                file = file.tolist()
            except:
                return False,data
            ascii_list = []
            pos_cal_x = 0
            pos_cal_y = 0
            for each in file:
                if pos_cal_y == pos_y:
                    for each_ in each:
                        if pos_cal_x == pos_x:
                            for each__ in each_:
                                if each__ == 0:
                                    pass
                                else:
                                    ascii_list.append(each__+dimed_brightness-brightness)
                        else:
                            pos_cal_x+=1
                else:
                    pos_cal_y+=1
            data = self.convert_ascii_list_to_chr(ascii_list)
            data = self.decryptor_n(data)
            real_password = data.split("///+++///")
            if password == real_password[1]:
                result = True
                return result,real_password[0]
            else:
                data = None
                return result,data
        else:
            result = False
            data = ""
            try:
                file = cv2.imread(file_name)
                file = np.array(file)
                file = file.tolist()
            except:
                return False,data
            ascii_list = []
            pos_cal_x = 0
            pos_cal_y = 0
            for each in file:
                if pos_cal_y == pos_y:
                    for each_ in each:
                        if pos_cal_x == pos_x:
                            for each__ in each_:
                                if each__ == 0:
                                    pass
                                else:
                                    ascii_list.append(each__+dimed_brightness-brightness)
                        else:
                            pos_cal_x+=1
                else:
                    pos_cal_y+=1
            data = self.convert_ascii_list_to_chr(ascii_list)
            data = self.decryptor_n(data)
            real_password = data.split("///+++///")
            if password == real_password[1]:
                result = True
                return result,real_password[0]
            else:
                data = None
                return result,data
    def to_ascii(self,raw_data):
        pre_final = []
        for each in raw_data:
            pre_final.append(ord(each))
        return pre_final
    def convert_ascii_list_to_chr(self,ascii_list):
        final = []
        for each in ascii_list:
            if each == 0:
                pass
            else:
                a = str(chr(int(each)))
                final.append(a)
        final_ = ""
        for each in final:
            final_+=each
        return final_
    def list_to_str_ascii(self,list_):
        final_data = ""
        for each in list_:
            len_of_char = len(str(each))
            if len_of_char == 3:
                final_data += str(each)
            else:
                if len_of_char == 0:
                    pass
                elif len_of_char == 1:
                    final_data += "00" + str(each)
                elif len_of_char == 2:
                    final_data += "0" + str(each)
        return final_data
    def encryptor(self,raw,pattern):
        final = ""
        for each in raw:
            final+=pattern.get(each,each)
        return final
    def inversed_pattern(self,raw):
        final = {}
        raw = dict(raw)
        keys = raw.keys()
        values = raw.values()
        c = 0
        keys = list(keys)
        for each in values:
            final.setdefault(str(each), str(keys[c]))
            c += 1
        return final
    def decryptor(self,raw,pattern):
        final = ""
        new_pattern = self.inversed_pattern(pattern)
        for each  in raw:
            final+=new_pattern.get(each,each)
        return final
    def write(self,file_name,data_,password,mode="normal",size=(200,200),start_pos=(0,0),dim_brightness=0,brightness=0,vertical_spacing=0,spacing=0,):
        x_size = size[0]
        y_size = size[1]
        pos_x = start_pos[0]
        pos_y = start_pos[1]
        if mode == "normal":
            file_name = file_name
            data = ""
            data__ = ""
            micro_code  = np.zeros((x_size, y_size, 3), dtype=np.uint8)
            data__+=data_
            data__+="///+++///"
            data__+=password
            data += data__
            data = self.encryptor_n(data)
            data = self.to_ascii(data)
            pointer = 0
            pointer_ = 0+pos_x
            pointer__ = 0+pos_y
            for each in data:
                each = int(each)
                pointer_ = pointer_+spacing
                micro_code[pointer__][pointer_][pointer] = each-dim_brightness+brightness
                if pointer == 2:
                    pointer=0
                    pointer_+=1
                else:
                    pointer+=1
                if pointer_ == x_size:
                    pointer_ = 0
                    pointer__+=1
                if pointer__ == y_size-1:
                    break
            cv2.imwrite(file_name,micro_code)
        else:
            file_name = file_name
            data = ""
            data__ = ""
            micro_code  = np.zeros((x_size,y_size, 3), dtype=np.uint8)
            data__+=data_
            data__+="///+++///"
            data__+=password
            data += data__
            data = self.encryptor_n(data)
            data = self.to_ascii(data)
            pointer = 0
            pointer_ = 0+pos_x
            pointer__ = 0+pos_y
            for each in data:
                each = int(each)
                if pointer_+spacing < x_size:
                    pointer_=pointer_+spacing
                    pointer__ = pointer__ + vertical_spacing
                micro_code[pointer__][pointer_][pointer] = each-dim_brightness+brightness
                pointer_+=1
                if pointer_ == x_size:
                    pointer_ = 0
                    pointer__+=1
                if pointer__ == y_size-1:
                    break
            cv2.imwrite(file_name,micro_code)

if __name__ == '__main__':
    mc = MicroCode()

    mc.write("Hello_world.png","HI","b61bdja",)
    print(mc.read("Hello_world.png","b61bdja",))
