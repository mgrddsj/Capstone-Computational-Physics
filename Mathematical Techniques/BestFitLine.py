#%% 

def getBestFit(x_list, y_list):
    b = sum_x = sum(x_list)
    d = sum_y = sum(y_list)
    a = sum_x_square = sum(x*x for x in x_list)
    c = sum_x_y = sum(map(lambda x,y: x*y, x_list, y_list))
    n = len(x_list)

    A = (c*n-b*d)/(a*n-b*b)
    B = (a*d-b*c)/(a*n-b*b)
    return A,B

xx = [1,2,3,4,5,6,7,8,9]
yy = [1,2,3,4,5,6,7,8,9] #[2,4,6,8,10,12,14,16,18]
print(getBestFit(xx, yy))