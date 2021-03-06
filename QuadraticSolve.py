
from math import sqrt as r_sqrt

#rSqrt is the real number version of the square root function

from cmath import sqrt as c_sqrt

#rSqrt is the complex number version of the square root function


def evaluate_quadratic(a, b, c, x):

    quad_result = a*(x**2) + b*x + c

    return quad_result


def get_second_derivative(a):
    return 2*float(a)


def print_first_derivative(a, b):

    sec_der = get_second_derivative(a)

    print("The first derivative of the quadratic is " + str(sec_der)  + "x" + " " "+" + " " + b)


def print_second_derivative(a):

    print("The second derivative of the quadratic is " + str(get_second_derivative(a)))



def get_axis_of_symmetry(a, b):

    if float(a) != 0:

        return -b / (2*a)

    else:
        pass


def get_vertex(a, b, c):

    v_x = get_axis_of_symmetry(a,b)  # x coordinate of vertex

    v_y = evaluate_quadratic(a, b, c,v_x)  # y coordinate of vertex

    vertex = (v_x, v_y)  # create a tuple of the x and y coordinates for the vertex of the parabola

    return vertex


def is_concave_up(a_coefficient):

    if a_coefficient > 0:
        return True
    else:
        return False


def print_min_or_max(a, b, c):

    vertex = get_vertex(a, b, c)

    if is_concave_up(a):

        print("The quadratic reaches a minimum at x = " + str(vertex[0]))

        print("The minimum value that the quadratic achieves is" + " " + str(vertex[1]))

    else:

        print("The quadratic reaches a maximum at x = " + str(vertex[0]) + "\n")

        print("The maximum value that the quadratic achieves is" + " " + str(vertex[1]))


def print_vertex(a, b, c):

    print("The vertex of the corresponding parabola is " + " " + str(get_vertex(float(a),float(b),float(c))))


def sum_of_roots(a, b, c):

    if b**2 - 4*a*c > 0:
        return -b / a

    elif b**2 - 4*a*c == 0:
        return -b / a

    else:
        pass


def product_of_roots(a, b, c):

    if b**2 - 4*a*c > 0:
        return c / a

    elif b**2 - 4*a*c == 0:
        return c / a

    else:
        pass


def print_sum_of_roots(a, b, c):

    if b**2 - 4*a*c > 0:
        sum_rts = sum_of_roots(a, b, c)
        print("The sum of the roots are: " + str(sum_rts))

    elif b**2 - 4*a*c == 0:
        sum_rts = sum_of_roots(a, b, c)
        print("The sum of the roots are: " + str(sum_rts))

    else:
        pass


def print_prod_of_roots(a, b, c):

    if b**2 - 4*a*c > 0:
        prod_rts = product_of_roots(a, b, c)
        print("The product of the roots are: " + str(prod_rts))

    elif b**2 - 4*a*c == 0:
        prod_rts = product_of_roots(a, b, c)
        print("The product of the roots are: " + str(prod_rts))

    else:
        pass


def print_sum_and_prod_roots(a, b, c):

    if b**2 - 4*a*c > 0:

        print("\n")
        print("Sum and Product of Roots")
        print_sum_of_roots(a, b, c)
        print_prod_of_roots(a, b, c)

    elif b**2 - 4*a*c == 0:

        print("\n")
        print("Sum and Product of Roots")
        print_sum_of_roots(a, b, c)
        print_prod_of_roots(a, b, c)

    else:
        pass


def quad_formula(a, b, c):

    roots = []

    if a == 0:

        return list('')

    else:
        axis_sym = get_axis_of_symmetry(a, b)
        #axis_sym = -b/(2*a)  # axis of symmetry: the x-value of the vertex of the parabola represented by the quadratic
                        # and is a term in the quadratic formula

        discriminant = (b**2) - (4*a*c) # b^2 - 4ac is the discriminant and is a term that is part of the quadratic formula

    #Use the real number square root if the discriminant is positive
        if discriminant > 0:
            first_root = axis_sym + r_sqrt(discriminant)/(2*a)
            second_root = axis_sym - r_sqrt(discriminant)/(2*a)

    #If the discriminant is zero, there is only one distinct real root and so only one root needs to be calculated
        elif discriminant == 0:
            first_root = axis_sym + r_sqrt(discriminant)/(2*a)

    #If the discriminant is negative, use the complex number version of the square root function
        elif discriminant < 0:
            first_root = axis_sym + c_sqrt(discriminant)/(2*a)
            second_root = axis_sym - c_sqrt(discriminant)/(2*a)

        roots.append(first_root)

        if discriminant != 0:
            roots.append(second_root)

    #roots.sort() #sort the roots by smallest to largest

    return roots

def y_intercept(a, b, c):

    if float(a) != 0:

        y_int = evaluate_quadratic(a, b, c, 0)

        print("The y intercept occurs at " + "(" + "0" + "," + y_int + ")")

    else:
        print("")


def print_quadratic(a_val, b_val, c_val):

    if float(a_val) == 0:
        print("This is not a quadratic equation")


#If the a coefficient is non-zero, continue with the program
    else:
        if (float(a_val) != 1) & (float(a_val) != -1):  # The cases when a = 1 or a = -1 are dealt with separately

#if b and c are both positive
            if (float(b_val) > 0) & (float(c_val) > 0): # b > 0 and c > 0 (b+ and c+) - Case # 1
                if float(b_val) == 1: # if b value is 1 don't print the 1
                    print("The solution to the quadratic equation " + a_val + "x^2 " + "+ " + "x " + "+ " + c_val + " is: ")
                else:
                    print("The solution to the quadratic equation " + a_val + "x^2 " + "+ " + b_val + "x " + "+ " + c_val + " is: ")
# b is negative

            if float(b_val) < 0:

                if float(c_val) == 0:  # b < 0 and c = 0  (b- and c = 0) - Case # 2
                    if float(b_val) == -1:
                        print("The solution to the quadratic equation " + a_val + "x^2 " + "- " + "x " + " is: ")
                    else:
                        print("The solution to the quadratic equation " + a_val + "x^2 " + "- " + str(abs(float(b_val))) + "x " + " is: ")

                elif float(c_val) > 0:  # b < 0 and c > 0 ( b- and c+) - Case # 3
                    if float(b_val) == -1:
                        print("The solution to the quadratic equation " + a_val + "x^2 " + "- " + "x " + "+ " + c_val + " is: ")
                    else:
                        print("The solution to the quadratic equation " + a_val + "x^2 " + "- " + str(abs(float(b_val))) + "x " + " + " + c_val + " is: ")

# c is negative

            if float(c_val) < 0:

                if float(b_val) == 0:  # b = 0 and c < 0 (c- and b = 0) - Case # 4
                    print("The solution to the quadratic equation " + a_val + "x^2 " + "- " + str(abs(float(c_val))) + " is: ")

                elif float(b_val) > 0:  # b > 0 and c < 0 ( c- and b+) - Case # 5
                    if float(b_val) == 1:
                        print("The solution to the quadratic equation " + a_val + "x^2 " + "+ " + "x " + "- " + str(abs(float(c_val))) + " is: ")
                    else:
                        print("The solution to the quadratic equation " + a_val + "x^2 " + "+ " + b_val + "x " + "- " + str(abs(float(c_val))) + " is: ")

# if b and c are both negative
            if (float(b_val) < 0) & (float(c_val) < 0):  # b < 0 and c < 0 (b- and c-) - Case #6
                if float(b_val) == -1:
                    print("The solution to the quadratic equation " + a_val + "x^2 " + "-x " + "- " + str(abs(float(c_val))) + " is: ")
                else:
                    print("The solution to the quadratic equation " + a_val + "x^2 " + "- " + str(abs(float(b_val))) + "x " + "- " + str(abs(float(c_val))) + " is: ")

 #if b > 0 and c = 0 (b+ and c = 0)
            if float(b_val) > 0:

                if float(c_val) == 0:  # b > 0 and c = 0 (b+ and c = 0) - Case #7
                    if float(b_val) == 1:
                        print("The solution to the quadratic equation " + a_val + "x^2" + " + " "x " + " is: ")
                    else:
                        print("The solution to the quadratic equation " + a_val + "x^2" + " + " + b_val + "x " + " is: ")

 #if b = 0 and c > 0

            if float(c_val) > 0:

                if float(b_val) == 0:  # b = 0 and c > 0 (b = 0 and c+) - Case #8
                    print("The solution to the quadratic equation " + a_val + "x^2 " + "+ " + c_val + " is: ")

 #if b = 0 and c = 0
            if (float(b_val) == 0) & (float(c_val) == 0): # b = 0 and c = 0  - Case #9
                print("The solution to the quadratic equation " + a_val + "x^2" + " is: ")

    #Checks to see if the 'a' coefficient is 1, if the 'a' coefficient is 1 then the value
    #will not be printed in front of x^2

        elif float(a_val) == -1:  # When a = -1

        #if b and c are both positive
            if (float(b_val) > 0) & (float(c_val) > 0):  # b > 0 and c > 0 (b+ and c+) - Case # 1

                if float(b_val) == 1:
                    print("The solution to the quadratic equation " + "-x^2 " + "+ " + "x " + "+ " + c_val + " is: ")

                else:

                    print("The solution to the quadratic equation " + "-x^2 " + "+ " + b_val + "x " + "+ " + c_val + " is: ")
# b is negative

            if float(b_val) < 0:

                if float(c_val) == 0:  # b < 0 and c = 0  (b- and c = 0) - Case # 2

                    if float(b_val) == -1:
                        print("The solution to the quadratic equation " + "-x^2 " + "-x " + " is: ")
                    else:
                        print("The solution to the quadratic equation " + "-x^2 " + "- " + str(abs(float(b_val))) + "x " + " is: ")

                elif float(c_val) > 0:  # b < 0 and c > 0 ( b- and c+) - Case # 3
                    if float(b_val) == -1:
                        print("The solution to the quadratic equation " + "-x^2 " + "-x " + " + " + c_val + " is: ")
                    else:
                        print("The solution to the quadratic equation " + "-x^2 " + "- " + str(abs(float(b_val))) + "x " + " + " + c_val + " is: ")

# c is negative

            if float(c_val) < 0:

                if float(b_val) == 0:  # b = 0 and c < 0 (c- and b = 0) - Case # 4
                    print("The solution to the quadratic equation " + "-x^2 " + "- " + str(abs(float(c_val))) + " is: ")

                elif float(b_val) > 0:  # b > 0 and c < 0 ( c- and b+) - Case # 5

                    if float(b_val) == 1:
                        print("The solution to the quadratic equation " + "-x^2 " + "+ " + "x " + "- " + str(abs(float(c_val))) + " is: ")

                    else:
                        print("The solution to the quadratic equation " + "-x^2 " + "+ " + b_val + "x " + "- " + str(abs(float(c_val))) + " is: ")

# if b and c are both negative
            if (float(b_val) < 0) & (float(c_val) < 0):  # b < 0 and c < 0 (b- and c-) - Case #6

                if float(b_val) == -1:
                    print("The solution to the quadratic equation " + "-x^2 " + "- " + "x " + "- " + str(abs(float(c_val))) + " is: ")

                else:
                    print("The solution to the quadratic equation " + "-x^2 " + "- " + str(abs(float(b_val))) + "x " + "- " + str(abs(float(c_val))) + " is: ")

 #if b > 0 and c = 0
            if float(b_val) > 0:

                if float(c_val) == 0:  # b > 0 and c = 0 (b+ and c = 0) - Case #7
                    if float(b_val) == 1:
                        print("The solution to the quadratic equation " + "-x^2" + " + " + "x " + " is: ")
                    else:
                        print("The solution to the quadratic equation " + "-x^2" + " + " + b_val + "x " + " is: ")

 #if b = 0 and c > 0

            if float(c_val) > 0:

                if float(b_val) == 0:  # b = 0 and c > 0 (b = 0 and c+) - Case #8
                    print("The solution to the quadratic equation " + "-x^2 " + "+ " + c_val + " is: ")

 #if b = 0 and c = 0
            if (float(b_val) == 0) & (float(c_val) == 0): # b = 0 and c = 0  - Case #9
                print("The solution to the quadratic equation " + "-x^2" + " is: ")

        elif float(a_val) == 1:

            #if b and c are both positive
                if (float(b_val) > 0) & (float(c_val) > 0):  # b > 0 and c > 0 (b+ and c+) - Case # 1

                    if float(b_val) == 1:
                        print("The solution to the quadratic equation " + "x^2 " + "+ " + "x " + "+ " + c_val + " is: ")
                    else:
                        print("The solution to the quadratic equation " + "x^2 " + "+ " + b_val + "x " + "+ " + c_val + " is: ")
        # b is negative

                if float(b_val) < 0:

                    if float(c_val) == 0:  # b < 0 and c = 0  (b- and c = 0) - Case # 2

                        if float(b_val) == -1:
                            print("The solution to the quadratic equation " + "x^2 " + "-" + " x" + " is: ")
                        else:
                            print("The solution to the quadratic equation " + "x^2 " + "- " + str(abs(float(b_val))) + "x " + " is: ")

                    elif float(c_val) > 0:  # b < 0 and c > 0 ( b- and c+) - Case # 3

                        if float(b_val) == -1:
                            print("The solution to the quadratic equation " + "x^2 "  "- " + "x " + "+ " + c_val + " is: ")

                        else:
                            print("The solution to the quadratic equation " + "x^2 " + "- " + str(abs(float(b_val))) + "x "+ "+ " + c_val + " is: ")

        # c is negative

                if float(c_val) < 0:

                    if float(b_val) == 0:  # b = 0 and c < 0 (c- and b = 0) - Case # 4
                        print("The solution to the quadratic equation " + "x^2 " + "- " + str(abs(float(c_val))) + " is: ")

                    elif float(b_val) > 0:  # b > 0 and c < 0 ( c- and b+) - Case # 5
                        if float(b_val) == 1:
                            print("The solution to the quadratic equation " + "x^2 " + "+ " + "x " + "- " + str(abs(float(c_val))) + " is: ")
                        else:
                            print("The solution to the quadratic equation " + "x^2 " + "+ " + b_val + "x " + "- " + str(abs(float(c_val)))  +" is: ")

             # if b and c are both negative
                if (float(b_val) < 0) & (float(c_val) < 0):  # b < 0 and c < 0 (b- and c-) - Case #6

                    if float(b_val) == -1:
                        print("The solution to the quadratic equation "  + "x^2 " + "- " + "x " + "- " + str(abs(float(c_val))) + " is: ")
                    else:
                        print("The solution to the quadratic equation "  + "x^2 " + "- " + str(abs(float(b_val))) + "x " + "- " + str(abs(float(c_val))) + " is: ")

             #if b > 0 and c = 0
                if float(b_val) > 0:

                    if float(c_val) == 0:  # b > 0 and c = 0 (b+ and c = 0) - Case #7

                        if float(b_val) == 1:
                            print("The solution to the quadratic equation " + "x^2" + " + " + "x " + " is: ")
                        else:
                            print("The solution to the quadratic equation " + "x^2" + " + " + b_val + "x " + " is: ")

        #if b = 0 and c > 0

                if float(c_val) > 0:

                    if float(b_val) == 0:  # b = 0 and c > 0 (b = 0 and c+) - Case #8
                        print("The solution to the quadratic equation " + "x^2 " + "+ " + c_val + " is: ")

         #if b = 0 and c = 0
                if (float(b_val) == 0) & (float(c_val) == 0): # b = 0 and c = 0  - Case #9
                    print("The solution to the quadratic equation " + "x^2" + " is: ")

        # end of print_quadratic method


def print_quad_roots(a_val, b_val, c_val):


        # Calculates the first root for a valid quadratic equation
        if len(quad_formula(float(a_val),float(b_val), float(c_val))) > 0:
            root1 = quad_formula(float(a_val), float(b_val), float(c_val))[0]

    # Checks to see if there is more than one distinct root
        if len(quad_formula(float(a_val),float(b_val), float(c_val))) > 1:
            root2 = quad_formula(float(a_val),float(b_val), float(c_val))[1]


    # If there is only one distinct root (a repeated root), then only print the one root that exists in the root list
        if len(quad_formula(float(a_val),float(b_val), float(c_val))) == 1:
            print("x = " + str(root1) + " (with multiplicity 2)")

    # If there are two distinct roots, print both roots
        elif len(quad_formula(float(a_val),float(b_val), float(c_val))) > 1:
            print("x1 = " + str(root1) + " and " + "x2 = " + str(root2))

    # If you don't have a valid quadratic equation (for example a = 0), then don't print a solution
        elif len(quad_formula(float(a_val),float(b_val), float(c_val))) == 0:
            print("")









