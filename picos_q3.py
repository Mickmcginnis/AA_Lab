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


p.add_constraint(64*x11 + 0.64*x13 + 0.64*x14 + 0.64*x15 + 0.36*x16 - 0.36*y11 - 0.36*y13-0.36*y14 - 0.36*y15 - 0.36*y16 - 0.36*z11 - 0.36*z13 - 0.36*z14 - 0.36*z15 - 0.36*z16 <= 0)
p.add_constraint(0.7*x11 + 0.7*x13 + 0.7*x14 + 0.7*x15 + 0.7*x16 - 0.3*y11 - 0.3*y13-0.3*y14 - 0.3*y15 - 0.3*y16 - 0.3*z11 - 0.3*z13 - 0.3*z14 - 0.3*z15 - 0.3*z16 >= 0)
p.add_constraint(0.64*x21 + 0.64*x22 + 0.64*x23 + 0.64*x24 + 0.36*x26 - 0.36*y21 - 0.36*y22 - 0.36*y23-0.36*y24 - 0.36*y26 - 0.36*z21 - 0.36*z22 - 0.36*z23 - 0.36*z24 - 0.36*z26 <= 0)
p.add_constraint(0.7*x21 + 0.7*x22 + 0.7*x23 + 0.7*x24 + 0.7*x26 - 0.3*y21 - 0.3*y22 - 0.3*y23-0.3*y24 - 0.3*y26 - 0.3*z21 - 0.3*z22 - 0.3*z23 - 0.3*z24 - 0.3*z26 >= 0)
p.add_constraint(0.64*x31 + 0.64*x32 + 0.64*x33 + 0.64*x35 + 0.64*x36 - 0.36*y31 - 0.36*y32 - 0.36*y33-0.36*y35 - 0.36*y36 - 0.36*z31 - 0.36*z32 - 0.36*z33 - 0.36*z35 - 0.36*z36 <= 0)
p.add_constraint(0.7*x31 + 0.7*x32 + 0.7*x33 + 0.7*x35 + 0.7*x36 - 0.3*y31 - 0.3*y32 - 0.3*y33-0.3*y35 - 0.3*y36 - 0.3*z31 - 0.3*z32 - 0.3*z33 - 0.3*z35 - 0.3*z36 >= 0)
p.add_constraint(0.64*y11 + 0.64*y13 + 0.64*y14 + 0.64*y15 + 0.64*y16 - 0.36*x11 - 0.36*x13-0.36*x14 - 0.36*x15 - 0.36*x16 - 0.36*z11 - 0.36*z13 - 0.36*z14 - 0.36*z15 - 0.36*z16 <= 0)
p.add_constraint(0.7*y11 + 0.7*y13 + 0.7*y14 + 0.7*y15 + 0.7*y16 - 0.3*x11 - 0.3*x13-0.3*x14 - 0.3*x15 - 0.3*x16 - 0.3*z11 - 0.3*z13 - 0.3*z14 - 0.3*z15 - 0.3*z16 >= 0)
p.add_constraint(0.64*y21 + 0.64*y22 + 0.64*y23 + 0.64*y24 + 0.64*y26 - 0.36*x21 - 0.36*x22 - 0.36*x23-0.36*x24 - 0.36*x26 - 0.36*z21 - 0.36*z22 - 0.36*z23 - 0.36*z24 - 0.36*z26 <= 0)
p.add_constraint(0.7*y21 + 0.7*y22 + 0.7*y23 + 0.7*y24 + 0.7*y26 - 0.3*x21 - 0.3*x22 - 0.3*x23-0.3*x24 - 0.3*x26 - 0.3*z21 - 0.3*z22 - 0.3*z23 - 0.3*z24 - 0.3*z26 >= 0)
p.add_constraint(0.64*y31 + 0.64*y32 + 0.64*y33 + 0.64*y35 + 0.64*y36 - 0.36*x31 - 0.36*x32 - 0.36*x33-0.36*x35 - 0.36*x36 - 0.36*z31 - 0.36*z32 - 0.36*z33 - 0.36*z35 - 0.36*z36 <= 0)
p.add_constraint(0.7*y31 + 0.7*y32 + 0.7*y33 + 0.7*y35 + 0.7*y36 - 0.3*x31 - 0.3*x32 - 0.3*x33-0.3*x35 - 0.3*x36 - 0.3*z31 - 0.3*z32 - 0.3*z33 - 0.3*z35 - 0.3*z36 >= 0)
p.add_constraint(0.64*z11 + 0.64*z13 + 0.64*z14 + 0.64*z15 + 0.64*z16 - 0.36*x11 - 0.36*x13-0.36*x14 - 0.36*x15 - 0.36*x16 - 0.36*y11 - 0.36*y13 - 0.36*y14 - 0.36*y15 - 0.36*y16 <= 0)
p.add_constraint(0.7*z11 + 0.7*z13 + 0.7*z14 + 0.7*z15 + 0.7*z16 - 0.3*x11 - 0.3*x13-0.3*x14 - 0.3*x15 - 0.3*x16 - 0.3*y11 - 0.3*y13 - 0.3*y14 - 0.3*y15 - 0.3*y16 >= 0)
p.add_constraint(0.64*z21 + 0.64*z22 + 0.64*z23 + 0.64*z24 + 0.64*z26 - 0.36*x21 - 0.36*x22 - 0.36*x23-0.36*x24 - 0.36*x26 - 0.36*y21 - 0.36*y22 - 0.36*y23 - 0.36*y24 - 0.36*y26 <= 0)
p.add_constraint(0.7*z21 + 0.7*z22 + 0.7*z23 + 0.7*z24 + 0.7*z26 - 0.3*x21 - 0.3*x22 - 0.3*x23-0.3*x24 - 0.3*x26 - 0.3*y21 - 0.3*y22 - 0.3*y23 - 0.3*y24 - 0.3*y26 >= 00.)
p.add_constraint(0.64*z31 + 0.64*z32 + 0.64*z33 + 0.64*z35 + 0.64*z36 - 0.36*x31 - 0.36*x32 - 0.36*x33-0.36*x35 - 0.36*x36 - 0.36*y31 - 0.36*y32 - 0.36*y33 - 0.36*y35 - 0.36*y36 <= 0)
p.add_constraint(0.7*z31 + 0.7*z32 + 0.7*z33 + 0.7*z35 + 0.7*z36 - 0.3*x31 - 0.3*x32 - 0.3*x33-0.3*x35 - 0.3*x36 - 0.3*y31 - 0.3*y32 - 0.3*y33 - 0.3*y35 - 0.3*y36 >= 0)


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
p.add_constraint(x11 + x13 + x14 + x15 + x16 + y11 + y13 + y14 + y15 + y16 + z11 + z13 + z14 + z15 + z16 <= 977)
p.add_constraint(x21 + x22 + x23 + x24 + x26 + y21 + y22 + y23 + y24 + y26 + z21 + z22 + z23 + z24 + z26 <= 951)
p.add_constraint(x31 + x32 + x33 + x35 + x36 + y31 + y32 + y33 + y35 + y36 + z31 + z32 + z33 + z35 + z36 <= 972)


# Objective function: 3x + 4y.
p.set_objective('min',
                300*x11 + 300*y11 + 300*z11 + 600*x13 + 600*y13 + 600*z13 + 200*x14 + 200*y14 + 200*z14 +
                500*x16 + 500*y16 + 500*z16 + 400*x22 + 400*y22 + 400*z22 + 300*x23 + 300*y23 + 300*z23 +
                500*x24 + 500*y24 + 500*z24 + 300*x26 + 300*y26 + 300*z26 + 700*x31 + 700*y31 + 700*z31 +
                500*x32 + 500*y32 + 500*z32 + 200*x33 + 200*y33 + 200*z33 + 400*x35 + 400*y35 + 400*z35)


solution = p.solve(verbosity=0, solver='cvxopt', primals=False)

print(solution.primals)
