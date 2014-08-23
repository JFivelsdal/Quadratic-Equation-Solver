
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

#def quad_max_or_min(a,b,c):


a_val = raw_input("Enter a value for the a coefficient: ")

b_val = raw_input("Enter a value for the b coefficient: ")

c_val = raw_input("Enter a value for the c coefficient: ")

print("\n")
#Checks to see if the 'a' coefficient is not 1, if the 'a' coefficient is  not 1 then the value
#will be printed in front of x^2

if float(a_val) != 1:

# Cases: a+ b+ c+  and a- b+ c+

# b and c terms get a plus sign

    if (float(b_val) > 0) & (float(c_val) > 0):
        print("The solution to the quadratic equation " + a_val + "x^2 " + "+ " + b_val + "x " + "+ " + c_val + " is: ")

#Cases: a+ b+ c- and a- b+ c-

# b term get a plus sign

    if (float(b_val) > 0) & (float(c_val) < 0):
        print("The solution to the quadratic equation " + a_val + "x^2 "
              + "+ " + b_val + "x " + "- " + str(abs(float(c_val))) + " is: ")

#Cases: a+ b- c+ and a- b- c+

# c term get a plus sign

    if (float(b_val) < 0) & (float(c_val) > 0):
        print("The solution to the quadratic equation " + a_val + "x^2 " + "- " + str(abs(float(b_val))) + "x " + "+ " + c_val + " is: ")

#Cases: a+ b- c- and a- b- c-

#neither b or c terms get a plus sign

    if (float(b_val) < 0) & (float(c_val) < 0):
        print("The solution to the quadratic equation " + a_val + "x^2 " + "- " + str(abs(float(b_val))) + "x " + "- "
              + str(abs(float(c_val))) + " is: ")

#Checks to see if the 'a' coefficient is 1, if the 'a' coefficient is 1 then the value
#will not be printed in front of x^2

if float(a_val) == 1:

    if (float(b_val) > 0) & (float(c_val) > 0):
        print("The solution to the quadratic equation " + "x^2 " + "+ " + b_val + "x " + "+ " + c_val + " is: ")

#Cases: a+ b+ c- and a- b+ c-

# b term get a plus sign

    if (float(b_val) > 0) & (float(c_val) < 0):
        print("The solution to the quadratic equation " + "x^2 " + "+ " + b_val + "x " + "- " + str(abs(float(c_val))) + " is: ")

#Cases: a+ b- c+ and a- b- c+

# c term get a plus sign

    if (float(b_val) < 0) & (float(c_val) > 0):
        print("The solution to the quadratic equation " + "x^2 " "- " + str(abs(float(b_val))) + "x " + "+"
              + c_val + " is: ")

#Cases: a+ b- c- and a- b- c-

#neither b or c terms get a plus sign

    if (float(b_val) < 0) & (float(c_val) < 0):
        print("The solution to the quadratic equation " + "x^2 " "- " + str(abs(float(b_val))) + "x " + "- "
              + str(abs(float(c_val))) + " is: ")


root1 = quad_formula(float(a_val), float(b_val), float(c_val))[0]

#checks to see if there is more than one distinct root
if len(quad_formula(float(a_val),float(b_val), float(c_val))) > 1:
    root2 = quad_formula(float(a_val),float(b_val), float(c_val))[1]

#If there is only one distinct root (a repeated root), then only print the one root that exists in the root list
if len(quad_formula(float(a_val),float(b_val), float(c_val))) == 1:
    print("x = " + str(root1) + " (with multiplicity 2)")

elif len(quad_formula(float(a_val),float(b_val), float(c_val))) > 1:
    print("x1 = " + str(root1) + " and " + "x2 = " + str(root2))





#if float(c_val) > 0:
    #print("The solution to the quadratic equation " + a_val + "x^2 " + "+" + b_val + "x " + "+" + c_val + " is: ")

#if float(c_val) < 0:
     #print("The solution to the quadratic equation " + a_val + "x^2 " + "+" + b_val + "x " + c_val + " is: ")


#print(quad_formula(float(a_val),float(b_val),float(c_val)))