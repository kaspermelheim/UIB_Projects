#2
source("populasjon.R")

#3
names(populasjon) <- c("nr", "vekt")

tetthet <- density(populasjon$vekt)
plot(tetthet, main = "", xlab = "Vekt i gram", ylab = "Tetthet")

#4

mean(populasjon$vekt)

qqnorm(populasjon$vekt, main = "Vekt")
qqline(populasjon$vekt, col = "red")

#5
set.seed(1)
n=40
Radutvalg <- sample(1:nrow(populasjon), size = n, replace = FALSE)

mittutvalg <- populasjon [Radutvalg, ]

#6
utvalgtetthet <- density(mittutvalg$vekt)
plot(utvalgtetthet, main = "", xlab = "Vekt i gram", ylab = "Tetthet")

#7
source("utvalg.R")
head(utvalg)

#8
snittene <- colMeans(utvalg)
sdene <- apply(utvalg, 2, sd)
empirisk <- data.frame(snittene = snittene, sdene = sdene)

names(empirisk) <- c("empirisk middelverdi", "standardavvik")

#9
hist(empirisk[,1])

#10
mean(empirisk[,1])
