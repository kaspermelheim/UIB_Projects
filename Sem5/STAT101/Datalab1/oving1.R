#Les in krabbedate
library("readxl")
krabber <- read_excel("krabbe.xlsx")

#Kontigenstabell krabber
telling <- table(krabber$Gender, krabber$Location)

#Stolpediagram krabber
barplot(
  telling, beside = TRUE, main = "Krabbetelling", sub = "Krabbetelling", legend = c("f", "m")
  )
