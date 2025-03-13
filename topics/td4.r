# install.packages('readxl')

library('readxl')

df = read_xlsx("/users/eleves-a/2024/raul-andrei.pop/MRW_QJE1992.xlsx")

print(df)

library('ggplot2')

g1 <- ggplot(data = df, mapping = aes(x = gdpgrowth, y = log(rgdpw60))) +
  geom_point() +
  theme_minimal()

g1

group = c()

for (i in 1:nrow(df)) {
    if (is.na(df[i, 'n']) || df[i , 'n'] == 0) group[i] = NA
    else if (df[i , 'o'] == 1) {
        group[i] = 'o'
    }
    else if (df[i , 'i'] == 1) {
        group[i] = 'i'

    }
    else {
        group[i] = 'n'
    }
}

group

df$group = group

df$group


library('dplyr')


df_filter = df %>% filter(number != 0 & !is.na(gdpgrowth))

constant = 0.05

reg0 = lm(formula = log(rgdpw85) ~ 1 + log(i_y) + log(popgrowth + constant), 
    data = df_filter)

reg0

reg1 = lm(formula = log(rgdpw85) ~ 1 + school + log(i_y) + log(popgrowth + constant), 
    data = df_filter)

reg1

summary(reg0)
summary(reg1)
testt = lm (log(gdpgrowth) ~ log(n + 0.05) + i_y , data= df_filter)

testt


reg1_o = lm(formula= log(rgdpw85) ~ 1 + school + log(i_y) + log(popgrowth + constant), 
        data = df_filter %>% filter(group == 'o'))

reg1_o

summary(reg1_o)




linearHypothesis 

