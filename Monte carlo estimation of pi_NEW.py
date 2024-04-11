import random
total_points=[10,100,1000,10000,100000,1000000]



number_of_points_inside_the_circle= 0
number_of_points_inside_the_square = 0
for j in range(len(total_points)):
    for i in range(total_points[j]):
        rand_x = random.uniform(-1, 1)
        rand_y = random.uniform(-1, 1)
        origin_dist = rand_x ** 2 + rand_y ** 2
        if origin_dist <= 1:
            number_of_points_inside_the_circle += 1
            number_of_points_inside_the_square += 1
            pi = 4 * number_of_points_inside_the_circle / number_of_points_inside_the_square
    print("Final Estimation of Pi=", pi)
    difference = (3.141592653589793238-pi)
    print(difference)
    sd=[]
    for i in range (len(total_points)):
        standard_deviation = print(((difference**2)/total_points[i])**(1/2))
        sd.append(standard_deviation)
    print(number_of_points_inside_the_circle)
    import math
    a=math.log(number_of_points_inside_the_circle)
    print(a)









































