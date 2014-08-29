
import QuadraticSolve as qs

#Get the quadratic equation coefficients from user input

a_value = raw_input("Enter a value for the a coefficient: ")

b_value = raw_input("Enter a value for the b coefficient: ")

c_value = raw_input("Enter a value for the c coefficient: ")

print("\n") # prints a new line to separate input and output

qs.print_quadratic(a_value, b_value, c_value)  # prints the quadratic based on the input provided earlier

qs.print_quad_roots(a_value, b_value, c_value) # prints the roots from that solve the corresponding quadratic

print("\n")

qs.y_intercept(a_value,b_value,c_value)

print("\n")

qs.print_min_or_max(float(a_value),float(b_value),float(c_value))


qs.print_vertex(a_value,b_value,c_value)
#Test Cases


# 3 cases a = 1, a != 1, and a != 1 and a ! = -1

# 3 cases b = 1, b = -1, b ! = -1 and b != 1

# b +, c non-negative  (c > 0 and c = 0)



##########################################

# a = 1 cases

#####################################

####################################

# b positive cases where c is positive negative or zero



##############################
# b positive cases  for  a = 1 case

# b+ , c +  b! = 1 and b!= - 1

## qs.print_quadratic("1", "2", "3")

## Result: The solution to the quadratic equation x^2 + 2x + 3 is:


# b = 1, c +

## qs.print_quadratic("1", "1", "3")


## Result: The solution to the quadratic equation x^2 + x + 3 is:


#b+, c- and c = 0

## qs.print_quadratic("1", "2", "-3")

## Result: The solution to the quadratic equation x^2 + 2x - 3.0 is:



# b = 1, c -

## qs.print_quadratic("1", "1", "-3")

## Result: The solution to the quadratic equation x^2 + x - 3.0 is:


#b+, c = 0

## qs.print_quadratic("1", "2", "0")

## Result: The solution to the quadratic equation x^2 + 2x  is:

# b = 1, c = 0

## qs.print_quadratic("1", "1", "0")

## Result: The solution to the quadratic equation x^2 + x  is:



####################################

# b negative cases where c is positive negative or zero (when a = 1)



##############################
# b negative cases

# b- , c +  b! = 1 and b!= - 1

## qs.print_quadratic("1", "-2", "3")

## Result: The solution to the quadratic equation x^2 - 2.0x + 3 is:


# b = -1, c +

## qs.print_quadratic("1", "-1", "3")

## Result: The solution to the quadratic equation x^2 - x + 3 is:


#b-, c- and c = 0

## qs.print_quadratic("1", "-2", "-3")

## Result: The solution to the quadratic equation x^2 - 2.0x - 3.0 is:



# b = -1, c -

## qs.print_quadratic("1", "-1", "-3")

## Result: The solution to the quadratic equation x^2 - x - 3.0 is:

#b-, c = 0

## qs.print_quadratic("1", "-2", "0")

## Result: The solution to the quadratic equation x^2 - 2.0x  is:

# b = -1, c = 0

## qs.print_quadratic("1", "-1", "0")

## Result: The solution to the quadratic equation x^2 - x is:



###########################################

# Cases when b = 0   when a = 1

# b = 0 and c > 0

## qs.print_quadratic("1", "0", "2")

## Result: The solution to the quadratic equation x^2 + 2 is:


# b = 0 and c < 0

## qs.print_quadratic("1", "0", "-1")

## Result: The solution to the quadratic equation x^2 - 1.0 is:

# b = 0 and c = 0

## qs.print_quadratic("1", "0", "0")

## Result: The solution to the quadratic equation x^2 is:


#########################################



####################################

# b positive cases where c is positive negative or zero


#a = -1
##############################
# b positive cases  for  a = -1 case

# b+ , c +  b! = 1 and b!= - 1

## qs.print_quadratic("-1", "2", "3")

## Result: The solution to the quadratic equation -x^2 + 2x + 3 is:

# b = 1, c +

## qs.print_quadratic("-1", "1", "3")

## Result: The solution to the quadratic equation -x^2 + x + 3 is:




#b+, c- and c = 0

# qs.print_quadratic("-1", "2", "-3")

## Result: The solution to the quadratic equation -x^2 + 2x  is:  (wrong output) [c term missing]


# b = 1, c -

# qs.print_quadratic("-1", "1", "-3")

## Result: The solution to the quadratic equation -x^2 + x  is: (wrong output) [c term missing]

#b+, c = 0

# qs.print_quadratic("-1", "2", "0")

## Result: The solution to the quadratic equation -x^2 + 2x  is:

# b = 1, c = 0

# qs.print_quadratic("-1", "1", "0")

## Result: The solution to the quadratic equation -x^2 + x  is:

####################################

# b negative cases where c is positive negative or zero (when a != 1 and a != 1)



##############################
# b negative cases

# b- , c +  b! = 1 and b!= - 1

# qs.print_quadratic("-1", "-2", "3")

## Result: The solution to the quadratic equation -x^2 - 2.0x  + 3 is:



# b = -1, c +

# qs.print_quadratic("-1", "-1", "3")

## Result: The solution to the quadratic equation -x^2 -x  + 3 is:   (weird spacing, probably replace negative sign with minus sign)

#b-, c- and c = 0

# qs.print_quadratic("-1", "-2", "-3")

## Result: The solution to the quadratic equation -x^2 - 2.0x - 3.0 is:



##

# b = -1, c -

# qs.print_quadratic("-1", "-1", "-3")

## Result: The solution to the quadratic equation -x^2 - x - 3.0 is:

#b-, c = 0

# qs.print_quadratic("-1", "-2", "0")

## Result: The solution to the quadratic equation -x^2 - 2.0x  is:

# b = -1, c = 0

# qs.print_quadratic("-1", "-1", "0")

## Result: The solution to the quadratic equation -x^2 -x  is:  (Weird spacing again and replace negative sign with minus sign)

###########################################

# Cases when b = 0   when a = -1
# b = 0 and c > 0

# qs.print_quadratic("-1", "0", "2")

## Result: The solution to the quadratic equation -x^2 + 2 is:


# b = 0 and c < 0

# qs.print_quadratic("-1", "0", "-1")

## Result: The solution to the quadratic equation -x^2 - 1.0 is:

# b = 0 and c = 0

# qs.print_quadratic("-1", "0", "0")

## Result: The solution to the quadratic equation -x^2 is:




#########################################

####################################

# b positive cases where c is positive negative or zero



##############################
# b positive cases  for  a  != 1  and a != -1 case

# b+ , c +  b! = 1 and b!= - 1

# qs.print_quadratic("2", "2", "3")

## Result: The solution to the quadratic equation 2x^2 + 2x + 3 is:

# b = 1, c +

# qs.print_quadratic("2", "1", "3")

## Result: The solution to the quadratic equation 2x^2 + x + 3 is:


#b+, c- and c = 0

# qs.print_quadratic("2", "2", "-3")

## Result: The solution to the quadratic equation 2x^2 + 2x - 3.0 is:


# b = 1, c -

# qs.print_quadratic("2", "1", "-3")

## Result: The solution to the quadratic equation 2x^2 + x - 3.0 is:

#b+, c = 0

#

# b = 1, c = 0

# qs.print_quadratic("2", "1", "0")

## Result: The solution to the quadratic equation 2x^2 + x  is:



####################################

# b negative cases where c is positive negative or zero (when a != 1 and a != -1)



##############################
# b negative cases

# b- , c +  b! = 1 and b!= - 1

# qs.print_quadratic("2", "-2", "3")

## Result: The solution to the quadratic equation 2x^2 - 2.0x  + 3 is:



# b = -1, c +

# qs.print_quadratic("2", "-1", "3")

## Result: The solution to the quadratic equation 2x^2 - x + 3 is:



#b-, c- and c = 0

# qs.print_quadratic("2", "-2", "-3")

## Result: The solution to the quadratic equation 2x^2 - 2.0x - 3.0 is:


# b = -1, c -

# qs.print_quadratic("2", "-1", "-3")

## Result: The solution to the quadratic equation 2x^2 -x - 3.0 is:  [weird spacing - change the negative sign to a minus sign]

#b-, c = 0

# qs.print_quadratic("2", "-2", "0")

## Result: The solution to the quadratic equation 2x^2 - 2.0x  is:


# b = -1, c = 0

# qs.print_quadratic("2", "-1", "0")

## Result: The solution to the quadratic equation 2x^2 - x  is:



###########################################

# Cases when b = 0   when a != 1 and a != -1

# b = 0 and c > 0

# qs.print_quadratic("2", "0", "2")

## Result: The solution to the quadratic equation 2x^2 + 2 is:


# b = 0 and c < 0

# qs.print_quadratic("2", "0", "-1")

## Result: The solution to the quadratic equation 2x^2 - 1.0 is:

# b = 0 and c = 0

# qs.print_quadratic("2", "0", "0")

## Result: The solution to the quadratic equation 2x^2 is:





#########################################

#########################################