
import QuadraticSolve as qs

#Get the quadratic equation coefficients from user input

a_value = raw_input("Enter a value for the a coefficient: ")

b_value = raw_input("Enter a value for the b coefficient: ")

c_value = raw_input("Enter a value for the c coefficient: ")

print("\n")  # prints a new line to separate input and output

print("Solution and Y-Intercept:")

qs.print_quadratic(a_value, b_value, c_value)  # prints the quadratic based on the input provided earlier

qs.print_quad_roots(a_value, b_value, c_value)  # prints the roots from that solve the corresponding quadratic

qs.y_intercept(a_value, b_value, c_value)

print("\n")

print("Min\Max info and Vertex of Quadratic:")
qs.print_min_or_max(float(a_value), float(b_value), float(c_value))


qs.print_vertex(a_value, b_value, c_value)


qs.print_sum_and_prod_roots(float(a_value), float(b_value), float(c_value))

#qs.print_prod_of_roots(float(a_value), float(b_value), float(c_value))

print("\n")

print("Derivative Information:")

qs.print_first_derivative(a_value, b_value)

qs.print_second_derivative(a_value)


