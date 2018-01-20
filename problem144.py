from math import sqrt, tan, atan

def eq(a, b):
    return abs(a-b) < 1e-10

def intersect_x(slope, old_x, old_y, ysect):
    a, b = 5, 10
    m, k = slope, ysect
    
    A = a**2 * m**2 + b**2
    B = 2 * a**2 * m * k
    C = a**2 * (k**2 - b**2)
    
    x = (-B + sqrt(B**2 - 4 * A * C)) / (2 * A)
    
    if eq(x, old_x):
        return (-B - sqrt(B**2 - 4 * A * C)) / (2 * A)
    else:
        return x
    
def intersect_y(x, slope, b):
    return slope * x + b
    
def new_beam_slope_with_intersection_point(beam_slope, x, y):
    normal_slope = slope_of_normal(x, y)
    normal_angle = atan(normal_slope)
    beam_angle = atan(beam_slope)
    new_beam_angle = 2 * normal_angle - beam_angle
    return tan(new_beam_angle)
    
def slope_of_normal(x, y):
    return y / (4 * x)    
    
def intersection_is_at_open_area(x, y):
    return -0.01 <= x and y >= 9.99998 or x <= 0.01 and y >= 9.99998

def solve():
    inside = True
    count = 1
    beam_slope = (-9.6 - 10.1) / 1.4
    xsect, ysect = 1.4, -9.6
    
    while inside:
        new_beam_slope = new_beam_slope_with_intersection_point(beam_slope, xsect, ysect)
        
        b = ysect - (new_beam_slope * xsect)
        
        xsect = intersect_x(new_beam_slope, xsect, ysect, b)
        ysect = intersect_y(xsect, new_beam_slope, b)
        
        if intersection_is_at_open_area(xsect, ysect):
            inside = False
        else:
            count += 1
            
        beam_slope = new_beam_slope
        
    return count

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
