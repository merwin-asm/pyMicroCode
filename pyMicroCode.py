"""
Micro Code 7.0.0
Author Merwin Mathew
"""


from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import numpy as np
import base64
import zlib
import cv2


class MicroCode:
    def compress(self,data):
        data_ = data.encode()
        data_ = zlib.compress(data_)
        if len(data_) < len(data):
            final = data_.decode(encoding='latin1')
        else:
            final = data
        return final
    def de_compress(self,data):
        try:
            data_ = data.encode(encoding='latin1')
            data_ = zlib.decompress(data_)
            return data_.decode()
        except:
            return data
    def encrypt_(self,data,password):
        f = Fernet(password)
        return f.encrypt(data)
    def encrypt(self,data,password,diff):
        key = self.password_to_key(password)
        data = data.encode()
        for e in range(0,diff):
            data = self.encrypt_(data,key)
        return data.decode()
    def decrypt_(self,data,password):
        f = Fernet(password)
        return f.decrypt(data)
    def decrypt(self,data,password,diff):
        key = self.password_to_key(password)
        data = data.encode()
        try:
            for e in range(0, diff):
                data = self.decrypt_(data, key)
            data = data.decode()
        except:
            data = False
        return data
    def password_to_key(self, password):
        salt = b'.-Kh)ura/)\xcef\xc8\x88u\xc2'
        password = password.encode()
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend())
        key = base64.urlsafe_b64encode(kdf.derive(password))
        return key
    def read(self, file_name, password, mode="normal", start_pos=(0, 0), dimed_brightness=0, brightness=0, difficulty=1):
        pos_x = start_pos[0]
        pos_y = start_pos[1]
        if mode == "normal":
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
            data = self.decrypt(data,password,difficulty)
            data = self.de_compress(data)
            return data
        else:
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
            data = self.decrypt(data,password,difficulty)
            data = self.de_compress(data)
            return data
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
    def write(self,file_name,data_,password,mode="normal",size=(200,200),start_pos=(0,0),dim_brightness=0,brightness=0,vertical_spacing=0,spacing=0,difficulty=1):
        x_size = size[0]
        y_size = size[1]
        pos_x = start_pos[0]
        pos_y = start_pos[1]
        data_ = self.compress(data_)
        if mode == "normal":
            micro_code  = np.zeros((x_size, y_size, 3), dtype=np.uint8)
            data = self.encrypt(data_,password,difficulty)
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
            micro_code  = np.zeros((x_size,y_size, 3), dtype=np.uint8)
            data = self.encrypt(data_,password,difficulty)
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
    mc.write("Hello_world_1.png","hello","hi") #writing microcode
    print(mc.read("Hello_world_1.png","hi"))#reading microcode
