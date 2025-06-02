# SESSION 4 - NUMERICAL OPTIMIZATION


##########################################
##########################################
## PART 1: FUNCTIONS OF 1 VARIABLE

# define the function
f <- function (x) -(1/6)*x^6 + x^2 + 2*x + 1

# plot the function over a specific interval
x_interval <- seq(0, 2, by = 0.1)
plot(x_interval, f(x_interval), type = "l")

## The R function "optimize" find minimums: we apply it to -f. 
minusf <- function (x) -f(x)
xmin <- optimize(minusf, c(0, 10), tol = 0.0001)

# you can "print" the result in a sentence for more clarity
cat("Function f is at a max in x=",xmin$minimum,"over the interval [0,2].", "\n")

# add a vertical line showing the maximum
abline(v=xmin$minimum, col="red")

# this algorithm implements the "golden section search" 
# simply takes 3 points, then a fourth and reselect an interval
# it works for specific functions (stricly unimodal)

# QUESTION:
############


##########################################
##########################################
## PART 2: FUNCTIONS OF 2 VARIABLES

# Output price
p <- 1
# p is a global variable


# Cobb-Douglas production function
Q <- function(k,l,a,b){
	# these arguments are local variables
	(k^a)*(l^b)
}

# you can evaluate this function at any point
Q(.2,.3,.5,.5)


# QUESTION 1:
############


# QUESTION 2:
############


# QUESTION 3:
############


# QUESTION 4:
############


# PLOTTING THE FUNCTION
############

# Plot the function
range_pi1 <- outer(range_k, range_l, Pi1)
persp(range_k, range_l, range_pi1,col = "lightblue", shade = 0.1, theta = 30, phi = 30)

# FINDING THE OPTIMUM
############
# the optimization function take a vector of 2 elements as argument
opp_Pi1 <- function(inputs){
	k <- inputs[1]
	l <- inputs[2]
	- Pi1(k,l) # add a minus to get max
}

result <- optim(c(1,1),fn=opp_Pi1,method="Nelder-Mead")

# add the maximum on the 3D graph
point_2d <- persp(range_k, range_l, range_pi1,col = "lightblue", shade = 0.1, theta = 30, phi = 30)
points(trans3d(result$par[1], result$par[2], -result$value, pmat = point_2d), col = "red", pch = 19)


##########################################
##########################################
## PART 3: CONSTRAINED MAXIMIZATION - THE CES-UTILITY CONSUMER CASE

# QUESTION 1:
############


# QUESTION 2:
############


# CES exponent parameter
r1 <- .5
# consumer's income
m1 <- 10
# vector of prices
p1 <- c(2,1)


# QUESTION 3:
############



########### OPTIMIZATION
result=constrOptim(c(0,0), minus_utility_1, NULL, ui = t(-p1), ci = -m1)
cat("x*=",result$par[1]," & y*=",result$par[2])

# QUESTION 4:
############
# how close are we to the constraint?




##########################################
##########################################
## INTRODUCTION TO LOOPS
# how do the optimal ratio of good (x/y) vary with the ratio of prices (p/q) ?

# define the sequence of prices (of good 1) over which we'll iterate
p1_sequence <- seq(0.5, 2, by = 0.1) 

# prepare lists to save results of each iteration
ratios_xovery <- numeric()

for (p1 in p1_sequence) {
	# define the new price vector
	p <- c(p1,1)
	# compute optimal consumption
	result=constrOptim(c(0,0), minus_utility, NULL, ui = t(-p), ci = -m)
	# append results to lists
	ratios_xovery <- append(ratios_xovery,result$par[1]/result$par[2])
}

plot(p1_sequence, ratios_xovery, type = "l")

# we find a decreasing relationship, but we know it depends on r!


# QUESTION :
############
# run the previous approach for different values of r using 2 nested loops
