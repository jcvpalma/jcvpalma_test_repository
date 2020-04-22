require("stats")

# base directory
setwd("~/Projetos/c19graphs/covid19r")

# read the dataset
df_covid <- read.csv("covid19_sus_dataset_r0.csv", sep=";")

# KPIs 
# 1st How many case we have per states
View(df_covid)

# 1st. create new df with amount of cases
df <- data.frame(row.names = c("regiao", "uf", "total_obitos", "total_casos"))

#summary
summary(df_covid)

#grpah
plot(type="n",
     x=df_covid$data, 
     y=df_covid$obitosNovos, 
     xlab="Data", ylab="Qtde Obitos",
     main="Covid-19 Brasil")



