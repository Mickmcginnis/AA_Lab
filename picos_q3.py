import picos as pic
from picos import RealVariable

p = pic.Problem()

x11 = RealVariable('x11')
x13 = RealVariable('x13')
x14 = RealVariable('x14')
x15 = RealVariable('x15')
x16 = RealVariable('x16')
x21 = RealVariable('x21')
x22 = RealVariable('x22')
x23 = RealVariable('x23')
x24 = RealVariable('x24')
x26 = RealVariable('x26')
x31 = RealVariable('x31')
x32 = RealVariable('x32')
x33 = RealVariable('x33')
x35 = RealVariable('x35')
x36 = RealVariable('x36')

y11 = RealVariable('y11')
y13 = RealVariable('y13')
y14 = RealVariable('y14')
y15 = RealVariable('y15')
y16 = RealVariable('y16')
y21 = RealVariable('y21')
y22 = RealVariable('y22')
y23 = RealVariable('y23')
y24 = RealVariable('y24')
y26 = RealVariable('y26')
y31 = RealVariable('y31')
y32 = RealVariable('y32')
y33 = RealVariable('y33')
y35 = RealVariable('y35')
y36 = RealVariable('y36')

z11 = RealVariable('z11')
z13 = RealVariable('z13')
z14 = RealVariable('z14')
z15 = RealVariable('z15')
z16 = RealVariable('z16')
z21 = RealVariable('z21')
z22 = RealVariable('z22')
z23 = RealVariable('z23')
z24 = RealVariable('z24')
z26 = RealVariable('z26')
z31 = RealVariable('z31')
z32 = RealVariable('z32')
z33 = RealVariable('z33')
z35 = RealVariable('z35')
z36 = RealVariable('z36')




# Constraint 0: x + 2y <= 14.
# p.add_constraint(x11 + 2 * y11 <= 14.0)
# TODO 30% stuff
n = x11 + x13 + x14 + x15 + x16 + x21 + x22 + x23 + x24 + x26 + x31 + x32 + x33 + x35 + x36 + y11 + y13 + y14 + y15 + y16 + y21 + y22 + y23 + y24 + y26 + y31 + y32 + y33 + y35 + y36 + z11 + z13 + z14 + z15 + z16 + z21 + z22 + z23 + z24 + z26 + z31 + z32 + z33 + z35 + z36

# denominators
h1_denom = x11 + x13 + x14 + x15 + x16 + y11 + y13 + y14 + y15 + y16 + z11 + z13 + z14 + z15 + z16 # hub 1
h2_denom = x21 + x22 + x23 + x24 + x26 + y21 + y22 + y23 + y24 + y26 + z21 + z22 + z23 + z24 + z26 # hub 2
h3_denom = x31 + x32 + x33 + x35 + x36 + y31 + y32 + y33 + y35 + y36 + z31 + z32 + z33 + z35 + z36 # hub 3

# x numerators
x_h1_num = x11 + x13 + x14 + x15 + x16 # hub 1
x_h2_num = x21 + x22 + x23 + x24 + x26 # hub 2
x_h3_num = x31 + x32 + x33 + x35 + x36 # hub 3

# y numerators
y_h1_num = y11 + y13 + y14 + y15 + y16 # hub 1
y_h2_num = y21 + y22 + y23 + y24 + y26 # hub 2
y_h3_num = y31 + y32 + y33 + y35 + y36 # hub 3

# z numerators
z_h1_num = z11 + z13 + z14 + z15 + z16 # hub 1
z_h2_num = z21 + z22 + z23 + z24 + z26 # hub 2
z_h3_num = z31 + z32 + z33 + z35 + z36 # hub 3

# # add x constraints
# p.add_constraint(0.3 * (h1_denom) <= x_h1_num <= 0.36 * (h1_denom)) # hub 1
# p.add_constraint(0.3 * (h2_denom) <= x_h2_num <= 0.36 * (h2_denom)) # hub 2
# p.add_constraint(0.3 * (h3_denom) <= x_h3_num <= 0.36 * (h3_denom)) # hub 3

# # add y constraints
# p.add_constraint(0.3 * (h1_denom) <= y_h1_num <= 0.36 * (h1_denom)) # hub 1
# p.add_constraint(0.3 * (h2_denom) <= y_h2_num <= 0.36 * (h2_denom)) # hub 2
# p.add_constraint(0.3 * (h3_denom) <= y_h3_num <= 0.36 * (h3_denom)) # hub 3

# # add z constraints
# p.add_constraint(0.3 * (h1_denom) <= z_h1_num <= 0.36 * (h1_denom)) # hub 1
# p.add_constraint(0.3 * (h2_denom) <= z_h2_num <= 0.36 * (h2_denom)) # hub 2
# p.add_constraint(0.3 * (h3_denom) <= z_h3_num <= 0.36 * (h3_denom)) # hub 3

# # add x constraints
# p.add_constraint(0.3 <= x_h1_num <= 0.36) # hub 1
# p.add_constraint(0.3 <= x_h2_num <= 0.36) # hub 2
# p.add_constraint(0.3  <= x_h3_num <= 0.36) # hub 3

# # add y constraints
# p.add_constraint(0.3 <= y_h1_num <= 0.36) # hub 1
# p.add_constraint(0.3 <= y_h2_num <= 0.36) # hub 2
# p.add_constraint(0.3<= y_h3_num <= 0.36) # hub 3

# # add z constraints
# p.add_constraint(0.3 <= z_h1_num <= 0.36) # hub 1
# p.add_constraint(0.3 <= z_h2_num <= 0.36 ) # hub 2
# p.add_constraint(0.3 <= z_h3_num <= 0.36) # hub 3

# add x constraints
p.add_constraint(0.3 <= x_h1_num) # hub 1
p.add_constraint(0.3 <= x_h2_num) # hub 2
p.add_constraint(0.3  <= x_h3_num) # hub 3
p.add_constraint(x_h1_num <= 0.36) # hub 1
p.add_constraint(x_h2_num <= 0.36) # hub 2
p.add_constraint(x_h3_num <= 0.36) # hub 3

# add y constraints
p.add_constraint(0.3 <= y_h1_num) # hub 1
p.add_constraint(0.3 <= y_h2_num) # hub 2
p.add_constraint(0.3<= y_h3_num) # hub 3
p.add_constraint(y_h1_num <= 0.36) # hub 1
p.add_constraint(y_h2_num <= 0.36) # hub 2
p.add_constraint(y_h3_num <= 0.36) # hub 3

# add z constraints
p.add_constraint(0.3 <= z_h1_num) # hub 1
p.add_constraint(0.3 <= z_h2_num) # hub 2
p.add_constraint(0.3 <= z_h3_num) # hub 3
p.add_constraint(z_h1_num <= 0.36) # hub 1
p.add_constraint(z_h2_num <= 0.36 ) # hub 2
p.add_constraint(z_h3_num <= 0.36) # hub 3


# all goods to hubs
p.add_constraint(x11 + x21 + x31 == 144)
p.add_constraint(y11 + y21 + y31 == 171)
p.add_constraint(z11 + z21 + z31 == 135)

p.add_constraint(x22 + x32 == 222)
p.add_constraint(y22 + y32 == 168)
p.add_constraint(z22 + z32 == 210)

p.add_constraint(x13 + x23 + x33 == 165)
p.add_constraint(y13 + y23 + y33 == 176)
p.add_constraint(z13 + z23 + z33 == 209)

p.add_constraint(x14 + x24 == 98)
p.add_constraint(x14 + y24 == 140)
p.add_constraint(z14 + z24 == 112)

p.add_constraint(x15 + x35 == 195)
p.add_constraint(y15 + y35 == 170)
p.add_constraint(z15 + z35 == 135)

p.add_constraint(x16 + x26 + x36 == 153)
p.add_constraint(y16 + y26 + y36 == 126)
p.add_constraint(z16 + z26 + z36 == 171)


# final set of constraints
p.add_constraint(x13 + x23 + x33 + x14 + x24 + x15 + x35 + x16 + x26 + x36 == 977)
p.add_constraint(y13 + y23 + y33 + y14 + y24 + y15 + y35 + y16 + y26 + y36 == 951)
p.add_constraint(z13 + z23 + z33 + z14 + z24 + z15 + z35 + z16 + z26 + z36 == 972)



# Objective function: 3x + 4y.
p.set_objective('min',
                300 * x11 + 600 * x13 + 200 * x14 + 0 * x15 + 500 * x16 +
                0 * x21 + 400 * x22 + 300 * x23 + 500 * x24 + 300 * x26 +
                700 * x31 + 500 * x32 + 200 * x33 + 400 * x35 + 0 * x36 +
                300 * y11 + 600 * y13 + 200 * y14 + 0 * y15 + 500 * y16 +
                0 * y21 + 400 * y22 + 300 * y23 + 500 * y24 + 300 * y26 +
                700 * y31 + 500 * y32 + 200 * y33 + 400 * y35 + 0 * y36 +
                300 * z11 + 600 * z13 + 200 * z14 + 0 * z15 + 500 * z16 +
                0 * z21 + 400 * z22 + 300 * z23 + 500 * z24 + 300 * z26 +
                700 * z31 + 500 * z32 + 200 * z33 + 400 * z35 + 0 * z36)


solution = p.solve(verbosity=0, solver='cvxopt', primals=False)

print(solution.primals)
