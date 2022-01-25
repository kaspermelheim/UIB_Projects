#Les in krabbedate
library("readxl")
krabber <- read_excel("krabbe.xlsx")

#Kontigenstabell krabber
telling <- table(krabber$Gender, krabber$Location)

#Stolpediagram krabber
barplot(
  telling, beside = TRUE, main = "Krabbetelling", sub = "Krabbetelling", legend = c("f", "m")
  )

#Konstruere krabbeM og krabbeF vektor
Gender <- krabber$Gender
Size <- krabber$Size
TypeM <- Gender == "m"
krabbeM <- Size[TypeM]
TypeF <- Gender == "f"
krabbeF <- Size[TypeF]

#Kvantitativ oppsummering av data
summary(krabbeM)
summary(krabbeF)

#Kvantitativ oppsummering av data i mm
krabbeM.mm <- krabbeM * 10
summary(krabbeM.mm)

# Skalert Histogram
hist(krabbeM, freq = FALSE, breaks = 10, main = "Hanner")
hist(krabbeF, freq = FALSE, breaks = 10, main = "Hunner")

# Boxplot
boxplot(krabbeM, krabbeF, names = c("krabbeM", "krabbeF"))

# normalplott:
qqnorm(krabbeM, main = "hanner")
qqline(krabbeM, col = "red")