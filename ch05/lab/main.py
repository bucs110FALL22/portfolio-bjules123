#Part A and B
import pygame 
pygame.init()
display = pygame.display.set_mode()
display.fill("blue")
count = 0
upper_limit = 20
iters={} 
x = []
y = []
for start in range(2,upper_limit+1,1):
 n = start
 count = 0
 while n>1:
   count = count+1
   max_so_far = 0
   if count>max_so_far:
     max_so_far = count
   if n%2==0:
    n = int(n/2)
    print(n)
   else:
    n = int(3*n + 1) 
    print(n)
 iters[start]=count
 
 
max_val = max_so_far
print(iters)
iters = iters.items()
#Part C
font = pygame.font.Font(None, 30)
if len(iters)>1:
 pygame.draw.lines(display, "black", True, [(x[0],y[0]),(x[1],y[1])])
pygame.display.flip()
new_display = pygame.transform.flip(display, False, True)
display.blit(new_display , (0, 0))

msg = font.render("The largest number is", True, "blue")
display.blit(msg, (10,10))



  