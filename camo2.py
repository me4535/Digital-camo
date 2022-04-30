# CÀI ĐẦY ĐỦ THƯ VIỆN ĐỂ KHÔNG BỊ LỖI :( 
#LƯU Ý : CÀI THƯ VIỆN Ở CÙNG 1 THƯ MỤC VỚI THƯ MỤC ĐẶT FILE CODE NÀY
# NÊN THAM KHẢO CÁCH CÀI PYTHON VÀ THƯ VIÊN TRÊN MANG TRƯỚC KHI DÙNG
import cv2
import numpy as np
import random 
from random import randint
from PIL import Image, ImageDraw
# Tạo khung trống
image_path_output = 'đặt đường dẫn để lưu ảnh nền vào đây' # theo mẫu 'C:/Users/ten file/ ten file/ ten file'
image_name_output = 'anhnen.png' # ghi tên của file ảnh nền
mode = 'RGB' 
size = (200,200) #thay đổi size của bức ảnh chứa camo tại đây lưu khí khi đổi xong phải thay đổi 2 dòng 27 và 28 thành random.randint(0, số đã nhập - 2)
color = (7, 36, 1) 
im = Image.new(mode, size, color)
im.save(image_path_output + image_name_output )
""" tạo ngẫu nhiên điểm ảnh
"""
img = cv2.imread("anhnen.png")
"""nhập màu vào các list chú ý : định dạng màu là RGB, dùng color picker pick ra màu RGB thì cần đổi lại vị trí của các giá trị cho phù hợp 
    ví dụ RGB :[255,0,0] thì phải đổi thành BGR [0,0,255]
    nhập tối thiểu 7 màu
"""
B = ["75","71","146","13","5","0","6"]
G = ["56","91","181","23","105","87","84"]
R = ["60","81","160","54","20","48","22"]
i=0
while (True):
    i = i+1
    x = random.randint(0,197)
    y = random.randint(0,197)  
    a = random.randint(0,6) # đây là biến chọn random màu từ list màu được nhập bên trên để chỉnh lại đúng số lượng màu đã nhập chỉ cần thay đổi từ (0,6) thành (0, số màu đã nhập - 2)
    b=int(B[a])
    g=int(G[a])
    r=int(R[a])
    img[x][y] = [b,g,r]
    img[x+1][y] = [b,g,r]
    img[x-1][y+1] = [b,g,r]
    img[x-1][y-1] = [b,g,r]
    img[x+1][y-1] = [b,g,r] 
    if i == 9000: # thay đổi giá trị này sẽ thay đổi độ lộn xộn của các pixel màu 
        break
"""opencv sử dụng hệ màu BGR không phải RGB ví dụ RGB :[255,0,0] thì phải đổi thành BGR [0,0,255]"""
cv2.imwrite('anh2.png', img)
""" """










