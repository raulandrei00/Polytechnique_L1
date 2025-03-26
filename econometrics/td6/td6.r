# install.packages("haven")
# install.packages("hash")

library("hash")
library("haven")
library("dplyr")
library("ggplot2")

df = read_dta ("/users/eleves-a/2024/raul-andrei.pop/Desktop/econometrics/td6/thermal_week_mort_0411.dta")

df_filter = df %>% filter(!is.na(w_tmp_mean) & !is.na(w_precip) & !is.na(w_cloud) & !is.na(w_evap) & !is.na(w_invterm))

print(df_filter)

df_filter = df_filter %>% filter (w_tmp_impute != 1)


avg_invterm = hash()
avg_w_tmp_mean = hash()


avg_month_df = df_filter %>% group_by(month) %>% 
                summarize (avg_tmp = mean(w_tmp_mean))

print(avg_month_df)

avg_invterm = df_filter %>% group_by(month) %>%
            summarize (avg_invt = mean(w_invterm))


avg_invterm

# for (crt_month in month.name) {
#     crt_month_df = df_filter %>% filter (month == crt_month)
#     avg_invterm[crt_month] <- mean(crt_month_df$w_invterm)
#     avg_w_tmp_mean[crt_month] <- mean (crt_month_df$w_tmp_mean) 
#     print (sum(crt_month_df$w_invterm) / nrow(crt_month_df))
# }

# print (avg_invterm)


# print(df)


avg_death_mexico = df_filter %>% group_by(month) %>%
            summarize (avg_d_m = mean(rw_infant_1y))

avg_death_guadaa = df_filter %>% group_by(month) %>%
            summarize (avg_d_g = mean(grw_infant_1y))


avg_death_guadaa
avg_death_mexico

graph_data = merge (avg_invterm , avg_death_mexico , by = "month")

graph_data

graph_data = merge (graph_data , avg_death_guadaa , by = "month")

graph_data

install.packages("tidyr")
library("tidyr")

graph_long <- graph_data %>% select(month , avg_invt , avg_d_m , avg_d_g) %>%
                gather (key = "variable" , value = "value" , avg_invt , avg_d_m , avg_d_g)

graph_long

graf = ggplot (graph_long , mapping = aes (x = month , y = value , color = variable)) + 
        geom_line() 

graf


# fixed effect = 1) individual fixed effect -> control for charact that do not evolve across time
#                2) time fixed effect -> varies across time
#                3) joint fixed effect
