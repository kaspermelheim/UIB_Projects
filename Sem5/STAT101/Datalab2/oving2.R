data <- read.table("fatherSon.txt", header = TRUE)

#Vektor
father <- data$Father
son <- data$Son
summary(father)
summary(son)

#Gjør om til cm og rund av
father.cm <- father * 2.54
son.cm <- son * 2.54
father.round = round(father.cm)
son.round = round(son.cm)
summary(father.round)
summary(son.round)

#Spredningsplott
plot(father, son)

#Gjennomsnitt og standardavvik
father.mean = mean(father)
son.mean = mean(son)
father.sd = sd(father)
son.sd = sd(son)

#Nye observasjoner
neighbour = rnorm(1078, father.mean, father.sd)
data$neighbour = neighbour

#Korrelasjonsmatrise
kor <- cor(data)
kor

#Linær regresjon
regresjon <- lm(son~father, data=data)
summary(regresjon)

#Plot with regresjonslinje
plot(father,son)
abline(regresjon, col = "red")

#Spredningsplott
regresjon.residualer = regresjon$residuals
plot(father, regresjon.residualer, xlab="Father", ylab="Residualer")
abline(0,0)

#Normalfordelingsplott
qqnorm(regresjon.residualer)
qqline(regresjon.residualer)