#4
# Les inn krabbedata
library("xlsx")
krabber <- read.xlsx(file = "krabbe.xlsx", sheetIndex = 1)

#5
# Konstruere krabbeM og krabbeF vektor
Gender <- krabber$Gender
Size <- krabber$Size
TypeM <- Gender == "m"
TypeF <- Gender == "f"
krabbeM <- Size[TypeM]
krabbeF <- Size[TypeF]

#6
# Transformere dataene
log.krabbeM <- log(krabbeM)
log.krabbeF <- log(krabbeF)

#7
# Skalert Histogram for ordinære og log-transformerte verdier
par(mfrow = c(2,2))
hist(krabbeM, freq = FALSE, breaks = 10, main = "Hanner")
hist(krabbeF, freq = FALSE, breaks = 10, main = "Hunner")
hist(log.krabbeM, freq = FALSE, breaks = 10, main = "log(Hanner)")
hist(log.krabbeF, freq = FALSE, breaks = 10, main = "log(Hunner)")

par(mfrow = c(2,2))
qqnorm(krabbeM, main = "Hanner")
qqline(krabbeM, col = "red")

qqnorm(krabbeF, main = "Hanner")
qqline(krabbeF, col = "red")

qqnorm(log.krabbeM, main = "Hanner")
qqline(log.krabbeM, col = "red")

qqnorm(log.krabbeM, main = "Hanner")
qqline(log.krabbeM, col = "red")

#8
test <- t.test(log.krabbeM, log.krabbeF, alternative = "two.sided")
test

#9
# Gjennomsnitt,standardavvik og antall i hver gruppe
x1 <- mean(log.krabbeM)
x2 <- mean(log.krabbeF)
s1 <- sd(log.krabbeM)
s2 <- sd(log.krabbeF)
n1 <- length(log.krabbeM)
n2 <- length(log.krabbeF)

# t-observator for to-utvalgs t-test
T.observator <- (x1 - x2)/sqrt(s1^2/n1 + s2^2/n2)

# Ta en titt p˚a de forskjellige størrelsene
x1
x2
s1
s2
n1
n2
T.observator

#10
# pverdi
a = n1 - 1
b = n2 - 1
min_ab = min(a,b)

frihetsgrader <- min_ab
pverdi <- 2*(1 - pt(abs(T.observator), df = frihetsgrader))
pverdi



