#---------------------------------------------#
#| DATA PREPARATION SCRIPT FOR ECO102 PROJECT  |
 #---------------------------------------------#

install.packages("rvest")

# Load required library
library(rvest)

setwd(dirname(normalizePath(sys.frame(1)$ofile)))
# Read the HTML file
html <- read_html("location_data_raw.html")
# this file contains a div extracted from a website's source code
# https://developers.google.com/public-data/docs/canonical/countries_csv?utm_source=chatgpt.com

# Extract the table
tbl <- html %>%
  html_node("table") %>%
  html_table(fill = TRUE)

 #---------------------------------------------#
#| IMPORTING DATA                              |
 #---------------------------------------------#

# Write to CSV
write.csv(tbl, "countries.csv", row.names = FALSE)
# this sequence converts the div to a csv

# List all CSV files in the current directory
csv_files <- list.files(pattern = "\\.csv$", ignore.case = TRUE)

# Read all CSV files into a named list of data frames
csv_data <- lapply(csv_files, read.csv, stringsAsFactors = FALSE)
names(csv_data) <- csv_files

names(csv_data)

# access table: csv_data[["countries.csv"]]

 #--------------------------------------------#
#| DATA CLEANING                              |
 #--------------------------------------------#

# Remove rows with NA values
csv_data <- lapply(csv_data, na.omit)



# # Convert character columns to factors
# csv_data <- lapply(csv_data, function(df) {
#   df[] <- lapply(df, function(col) {
#     if (is.character(col)) {
#       as.factor(col)
#     } else {
#       col
#     }
#   })
#   return(df)
# })


library(dplyr)
# Read countries.csv as reference
countries_ref <- read.csv("countries.csv", stringsAsFactors = FALSE)

# Helper: function to standardize a table
standardize_country <- function(df, country_col) {
  df <- df %>%
    left_join(countries_ref, by = setNames("name", country_col)) %>%
    mutate(country = country) # ISO code from countries.csv
  return(df)
}

# Standardize each table
csv_data_std <- list()

for (name in names(csv_data)) {
  df <- csv_data[[name]]
  # Try to detect the country column
  if ("country" %in% names(df)) {
    # If it's already ISO code, keep as is
    df$country <- df$country
  } else if ("Region" %in% names(df)) {
    df <- df %>%
      left_join(countries_ref, by = c("Region" = "name"))
    df$country <- df$country
  } else if ("Country/Region" %in% names(df)) {
    df <- df %>%
      left_join(countries_ref, by = c("Country/Region" = "name"))
    df$country <- df$country
  } else if ("name" %in% names(df)) {
    df <- df %>%
      left_join(countries_ref, by = "name")
    df$country <- df$country
  }
  # Standardize year column if needed
  if ("Year" %in% names(df)) names(df)[names(df) == "Year"] <- "year"
  if ("year" %in% names(df)) df$year <- df$year
  csv_data_std[[name]] <- df
}

# Now you can join using 'country' and 'year'
central_table <- csv_data_std[[1]]
for (i in 2:length(csv_data_std)) {
  central_table <- full_join(central_table, csv_data_std[[i]],
                             by = c("country", "year"))
}

# View the resulting centralised table
head(central_table)

write.csv(central_table, "central_table.csv", row.names = FALSE)
# central data seems bad
# to do 
# 1) redo central data
# 2) run regression Pollution ~ vaci + control(loc , temp)
# 3) run IV: vaci ~ muslimi + cost_prod
