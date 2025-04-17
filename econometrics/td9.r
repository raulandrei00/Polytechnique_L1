# Load necessary library
library(readr)

# Read the CSV file into a dataframe
lfs_women <- read_csv("/users/eleves-a/2024/raul-andrei.pop/lfs_women.csv")

# Save the dataframe to the current working directory
save(lfs_women, file = "/users/eleves-a/2024/raul-andrei.pop/Desktop/econometrics/lfs_women.RData")

summary(lfs_women)

# Linear regression: mne1 explains ntravail
model_ntravail <- lm(ntravail ~ mne1, data = lfs_women)
summary(model_ntravail)

# Linear regression: mne1 explains ntpp
model_ntpp <- lm(ntpp ~ mne1, data = lfs_women)
summary(model_ntpp)

model_ntpp_extended <- lm(ntpp ~ mne1 + same_sexe + hh_twin_after, data = lfs_women)
summary(model_ntpp_extended)

library(dplyr)
library(plm)


est_sample = lfs_women %>% 
    mutate (lfs = ifelse(ntravail == 1,1,0),
        mother = ifelse (nsexe == 2 & mne1 > 0,1,0),
        large_family = ifelse(mne1 > 2, 1, 0),
        full_time = ifelse (ntpp == 2, 1, 0),
        high_skilled = ifelse (ndiplo >= 5, 1,0)) %>%
    mutate (mother_x_large_family = mother * large_family) %>%
    mutate (iv_twins = mother*hh_twin_after, 
            iv_ssex = mother*same_sexe)

summary(lm(lfs ~ mother + large_family + mother_x_large_family, data= est_sample))

summary(lm(lfs ~ mother + large_family + mother_x_large_family + high_skilled + log(nag), data= est_sample))

 