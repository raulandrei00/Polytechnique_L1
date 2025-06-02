#hello

#P3
#P3.1

U <- function(x , y , r) {
    (x^r + y^r)^(1/r)
}

minus_utility <- function(x) {
    -U(x[1], x[2], r1)
}

# CES ex p onen t parame ter
r1 <- .5
# consumer ’ s income
m1 <- 10
# v e c t o r o f p r i c e s
p1 <- c ( 2 , 1 )


result = constrOptim(c(0,0), minus_utility, NULL, ui = t(-p1), ci = -m1)
cat("x*=",result$par[1]," & y*=",result$par[2],"\n")

p_y <- 1
px_list <- seq(0.5, 2, by = 0.1)

ratios_xovery <- numeric()

for (p1 in px_list) {
    # define the new price vector
    p <- c(p1, p_y)
    # compute optimal consumption
    result = constrOptim(c(0,0), minus_utility, NULL, ui = t(-p), ci = -m1)
    # append results to lists
    ratios_xovery <- append(ratios_xovery, result$par[1]/result$par[2])
}

ratios_xovery

plot(px_list, ratios_xovery, type = "l", xlab = "Price of Good 1", ylab = "Optimal Ratio of x/y", main = "Optimal Ratio of x/y vs Price of Good 1")

r_values <- c(0.1, 0.5)
ratios_xovery_list <- list()

for (r in r_values) {
    ratios_xovery <- numeric()
    for (p1 in px_list) {
        # define the new price vector
        p <- c(p1, p_y)
        # compute optimal consumption
        r1 <- r  # Update the CES parameter for each iteration
        result = constrOptim(c(0,0), minus_utility, NULL, ui = t(-p), ci = -m1)
        # append results to lists
        ratios_xovery <- append(ratios_xovery, result$par[1]/result$par[2])
    }
    ratios_xovery_list[[as.character(r)]] <- ratios_xovery
}

library(plotly)
# install.packages("plotly")
# Prepare data for 3D plot
r_values_rep <- rep(r_values, each = length(px_list))
px_list_rep <- rep(px_list, times = length(r_values))
ratios <- unlist(ratios_xovery_list)

# Create a data frame for plotting
data <- data.frame(r = r_values_rep, p1 = px_list_rep, ratio = ratios)
library(dplyr)
# install.packages("dplyr")
# Create 3D plot
plot_ly(data, x = ~p1, y = ~r, z = ~ratio, type = "scatter3d", mode = "lines") %>%
    layout(
        scene = list(
            xaxis = list(title = "Price of Good 1 (p1)"),
            yaxis = list(title = "r (CES parameter)"),
            zaxis = list(title = "Optimal Ratio of x/y")
        )
    )