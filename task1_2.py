import simple_draw as sd
import random
list_of_point = []
temp_list = []
list_of_angle = []
temp_angle = []
sd.resolution = (1800, 1000)
# def branch(point, angle, lenght=100):
#     if lenght<3:
#         return
#     v = sd.get_vector(start_point=point, angle=angle, length=lenght)
#     v.draw(color=(0,255,0))
#     lenght *=0.75
#     branch(v.end_point,angle-30,lenght)
#     branch(v.end_point,angle+30,lenght)
# branch(sd.get_point(600, 0),90,100)
point = sd.get_point(900, 0)
angle = 90
lenght = 200
width = 6
color1 = (102,51,0)
v = sd.vector(start=point,angle=angle,length=lenght,color=color1,width=7)
temp_list.append(v)
temp_angle.append(angle)
list_of_point.append(temp_list)
list_of_angle.append(temp_angle)

for i in range(15):
    temp_angle=[]
    temp_list = []
    lenght *=0.75
    if width>1:
        width-=1
    for j in range(pow(2,i)):
            if i==0 or i==1:
                color1=(102,51,0)
            if i==2 or i==3:
                color1=(204,102,0)
            if i>3 and i<=6:
                color1=(0,255,0)
            if i>6:
                colorrand = random.randint(0,6)
                if colorrand==0:
                    color1=(255,210,0)
                if colorrand==1:
                    color1=(156,87,8)
                if colorrand==2:
                    color1=(244,123,32)
                if colorrand==3:
                    color1=(247,151,98)
                if colorrand==4:
                    color1=(240,81,51)
                if colorrand==5:
                    color1=(86,24,24)
            delta_a = random.randint(25,40)
            delta_l = random.randint(0,20)
            lenght_d = lenght * delta_l / 100
            v = sd.vector(start=list_of_point[i][j],angle=list_of_angle[i][j]+delta_a,length=lenght-lenght_d,color=color1,width=width)
            temp_list.append(v)
            temp_angle.append(list_of_angle[i][j]+delta_a)
            delta_a = random.randint(25, 40)
            delta_l = random.randint(0, 20)
            lenght_d = lenght * delta_l / 100
            v = sd.vector(start=list_of_point[i][j], angle=list_of_angle[i][j] - delta_a, length=lenght-lenght_d, color=color1,width=width)
            temp_list.append(v)
            temp_angle.append(list_of_angle[i][j] - delta_a)
    list_of_angle.append(temp_angle)
    list_of_point.append(temp_list)
sd.pause()

