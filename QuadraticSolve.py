
from math import sqrt as r_sqrt

#rSqrt is the real number version of the square root function

from cmath import sqrt as c_sqrt

#rSqrt is the complex number version of the square root function


def quad_formula(a, b, c):

    roots = []

    axis_sym = -b/(2*a)  # axis of symmetry: the x-value of the vertex of the parabola represented by the quadratic
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

def is_concave_up(a_coefficient):

    if a_coefficient > 0:
        return True
    else:
        return False


a_val = raw_input("Enter a value for the a coefficient: ")

b_val = raw_input("Enter a value for the b coefficient: ")

c_val = raw_input("Enter a value for the c coefficient: ")

print("\n")
#Checks to see if the 'a' coefficient is not 1, if the 'a' coefficient is  not 1 then the value
#will be printed in front of x^2

#First Check that if the value of the a coefficient is set equal to zero

#consider the cases where a = 1 and a = -1  and also when b = 1 and b = -1

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
                    print("The solution to the quadratic equation " + a_val + "x^2 " + "- " + "x " + " + " + c_val + " is: ")
                else:
                    print("The solution to the quadratic equation " + a_val + "x^2 " + "- " + str(abs(float(b_val))) + "x " + " + " + c_val + " is: ")

# c is negative

        if float(c_val) < 0:

            if float(b_val) == 0:  # b = 0 and c < 0 (c- and b = 0) - Case # 4
                print("The solution to the quadratic equation " + a_val + "x^2 " + "- " + str(abs(float(c_val))) + " is: ")

            elif float(b_val) > 0:  # b > 0 and c < 0 ( c- and b+) - Case # 5
                if float(b_val) == 1:
                    print("The solution to the quadratic equation " + a_val + "x^2 " + "+ " + "x " + " is: ")
                else:
                    print("The solution to the quadratic equation " + a_val + "x^2 " + "+ " + b_val + "x " + " is: ")

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
                    print("The solution to the quadratic equation " + a_val + "x^2" + "x " + " is: ")
                else:
                    print("The solution to the quadratic equation " + a_val + "x^2" + "+ " + b_val + "x " + " is: ")

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
                    print("The solution to the quadratic equation " + "-x^2 " + "+ " + "x " + " is: ")

                else:
                    print("The solution to the quadratic equation " + "-x^2 " + "+ " + b_val + "x " + " is: ")

# if b and c are both negative
        if (float(b_val) < 0) & (float(c_val) < 0):  # b < 0 and c < 0 (b- and c-) - Case #6

            if float(b_val) == -1:
                print("The solution to the quadratic equation " + "-x^2 " + "-x " + "- " + str(abs(float(c_val))) + " is: ")

            else:
                print("The solution to the quadratic equation " + "-x^2 " + "- " + str(abs(float(b_val))) + "x " + "- " + str(abs(float(c_val))) + " is: ")

 #if b > 0 and c = 0
        if float(b_val) > 0:

            if float(c_val) == 0:  # b > 0 and c = 0 (b+ and c = 0) - Case #7
                if float(b_val) == 1:
                    print("The solution to the quadratic equation " + "-x^2" + "+ " + "x " + " is: ")
                else:
                    print("The solution to the quadratic equation " + "-x^2" + "+ " + b_val + "x " + " is: ")

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
                        print("The solution to the quadratic equation " + "x^2 " + "-x " + " is: ")
                    else:
                        print("The solution to the quadratic equation " + "x^2 " + "- " + str(abs(float(b_val))) + "x " + " is: ")

                elif float(c_val) > 0:  # b < 0 and c > 0 ( b- and c+) - Case # 3

                    if float(b_val) == -1:
                        print("The solution to the quadratic equation " + "x^2 " + "-x " + " + " + c_val + " is: ")

                    else:
                        print("The solution to the quadratic equation " + "x^2 " + "- " + str(abs(float(b_val))) + "x " + " + " + c_val + " is: ")

        # c is negative

            if float(c_val) < 0:

                if float(b_val) == 0:  # b = 0 and c < 0 (c- and b = 0) - Case # 4
                    print("The solution to the quadratic equation " + "x^2 " + "- " + str(abs(float(c_val))) + " is: ")

                elif float(b_val) > 0:  # b > 0 and c < 0 ( c- and b+) - Case # 5
                    if float(b_val) == 1:
                        print("The solution to the quadratic equation " + "x^2 " + "+ " + "x " + " is: ")
                    else:
                        print("The solution to the quadratic equation " + "x^2 " + "+ " + b_val + "x " + " is: ")

             # if b and c are both negative
                    if (float(b_val) < 0) & (float(c_val) < 0):  # b < 0 and c < 0 (b- and c-) - Case #6

                        if float(b_val) == -1:
                            print("The solution to the quadratic equation "  + "x^2 " + "-x " + "- " + str(abs(float(c_val))) + " is: ")
                        else:
                            print("The solution to the quadratic equation "  + "x^2 " + "- " + str(abs(float(b_val))) + "x " + "- " + str(abs(float(c_val))) + " is: ")

             #if b > 0 and c = 0
            if float(b_val) > 0:

                if float(c_val) == 0:  # b > 0 and c = 0 (b+ and c = 0) - Case #7

                    if float(b_val) == 1:
                        print("The solution to the quadratic equation " + "x^2" + "+ " + "x " + " is: ")
                    else:
                        print("The solution to the quadratic equation " + "x^2" + "+ " + b_val + "x " + " is: ")

        #if b = 0 and c > 0

            if float(c_val) > 0:

                if float(b_val) == 0:  # b = 0 and c > 0 (b = 0 and c+) - Case #8
                    print("The solution to the quadratic equation " + "x^2 " + "+ " + c_val + " is: ")

         #if b = 0 and c = 0
            if (float(b_val) == 0) & (float(c_val) == 0): # b = 0 and c = 0  - Case #9
                print("The solution to the quadratic equation " + "x^2" + " is: ")

    root1 = quad_formula(float(a_val), float(b_val), float(c_val))[0]

    #checks to see if there is more than one distinct root
    if len(quad_formula(float(a_val),float(b_val), float(c_val))) > 1:
        root2 = quad_formula(float(a_val),float(b_val), float(c_val))[1]

    #If there is only one distinct root (a repeated root), then only print the one root that exists in the root list
    if len(quad_formula(float(a_val),float(b_val), float(c_val))) == 1:
        print("x = " + str(root1) + " (with multiplicity 2)")

    elif len(quad_formula(float(a_val),float(b_val), float(c_val))) > 1:
        print("x1 = " + str(root1) + " and " + "x2 = " + str(root2))


class Quadratic:
    """ This class provides a framework for creating a quadratic equation
    """
a = 0
b = 0
c = 0

second_derivative = 2*a

def __init__(self,a, b, c):
    """(Quadratic, a coefficient, b coefficient, c coefficient)"""

    self.a = a
    self.b = b
    self.c = c





