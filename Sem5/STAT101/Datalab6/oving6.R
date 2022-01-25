#Del 2
#a
qnorm(0.90, mean = 12, sd = 6)

#b
giftmålinger <- c(8.2, 20.2, 19.9, 13.2, 12.2)
mean_g <- mean(giftmålinger)
sd_g <- sd(giftmålinger)

#c
qnorm(0.95, mean_g, 6)
konfidens_95 <- cbind(mean_g - 1.96 * (6 / sqrt(5)), mean_g + 1.96 * (6 / sqrt(5)))

#d
set.seed(1011)

# Trekke 5 x 10000 observasjoner fra normalfordeling:
normalfordelt.utvalg <- rnorm(50000, mean = 12, sd = 6)
# Gruppere de sammen i grupper på 5 (som rader i en matrise med fem kolonner):
x <- matrix(normalfordelt.utvalg, ncol = 5)

#e
snitt <- rowMeans(x)
a = 1.96 * (6 / sqrt(5))
konfidensintervall <- cbind(snitt - a , snitt + a )

#f
inneholder18 <- intersect(which(konfidensintervall[,1]<18),
                          which(konfidensintervall[,2]>18))
inneholder18

length(inneholder18)/10000
