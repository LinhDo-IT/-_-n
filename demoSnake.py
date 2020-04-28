import pygame
import time
import random

pygame.init() #Khởi tạo môi trường

white = (255,255,255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)



dis_width = 700
dis_heigth = 400

dis = pygame.display.set_mode((dis_width, dis_heigth)) #kích thước

score_font = pygame.font.SysFont("consolas", 20)
font_style = pygame.font.SysFont('consolas', 25)

mss1 = 'Game Over!'
mss2 = 'Press C_Continue or Q_Quit ?'
mss3 = 'You Have Score: '
clock = pygame.time.Clock() #Hàm time.clock() trả về CPU time hiện tại dưới dạng số giây dạng số thực

snake_block = 10
snake_speed = 15

#Chữ
def message(msg, color):
    mess =  font_style.render(msg, True, color) #hàm render() vẽ và hiễn thị chữ lên màn hình
    dis.blit(mess, [70, 150]) #hàm blit in ra dòng mes tại vị trí[x1,y1]

#con rắn
def our_snake(snake_block, snake_list):
    for i in snake_list:
        pygame.draw.rect(dis, black, [i[0], i[1], snake_block, snake_block])

#Điểm
def Score(score):
    value = score_font.render("Score: "+ str(score), True, red) 
    dis.blit(value, [600,0])

#Màn hình
def gameLoop():
    game_Over = False 
    game_close = False

    x1 = dis_width / 2
    y1 = dis_heigth / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    #Tạo thức ăn
    foodx = round(random.randrange(0, dis_width - snake_block)/10.0)*10.0 #randrange(): trả về 1 phần tử được lựa chọn ngẫu nhiên từ dãy(start, stop step)
    foody = round(random.randrange(0, dis_heigth - snake_block)/10.0)*10.0
    
    game_Over = False
    while not game_Over:

        while game_close == True:
            dis.fill(blue)
            message(mss1 +" "+ mss2, green)
            Score(Length_of_snake - 1)
            pygame.display.update()

            #Tạo nút cho dòng mess
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_Over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get(): #Hàm get() trả về tham số đc truyền vào
            if event.type == pygame.QUIT: #Hàm type() trả về đối tượng được truyền dưới dạng tham số
                game_Over = True
            if event.type == pygame.KEYDOWN: #Hàm di chuyển rắn
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                if event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= dis_width or x1 < 0 or y1 >= dis_heigth or y1 < 0:
            game_close = True
        
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue) #Xóa trắng màn hình
        pygame.draw.rect(dis,yellow,[foodx, foody, snake_block, snake_block]) #Vẽ (lại) con rắn
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head) #thêm snake_Head vào ds đc trỏ bởi snake_List
        if len(snake_List) > Length_of_snake:
            del snake_List[0] #xóa snake_List tại vị trí 0
        
        for i in snake_List[:-1]:
            if i == snake_Head: #Nếu đầu con rắn trùng khối ở phần thân thì game kết thúc
                game_close = True

        our_snake(snake_block, snake_List)
        Score(Length_of_snake - 1)

        pygame.display.update() 

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0)*10.0
            foody = round(random.randrange(0, dis_heigth - snake_block) / 10.0)*10.0
            Length_of_snake += 1
        
        clock.tick(snake_speed) #Số dấu phẩy động tính bằng đơn vị giây trong Tick

    pygame.quit() #Kết thúc môi trường

gameLoop()
