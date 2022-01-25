set.seed(9999)
BinomialSamples <- rbinom(10000,10, 0.5)

hist(BinomialSamples, freq=TRUE)

mean(BinomialSamples)
var(BinomialSamples)

#Første 10
mean(BinomialSamples[0:10])
var(BinomialSamples[0:10])

#Første 20
mean(BinomialSamples[0:20])
var(BinomialSamples[0:20])

#Første 100
mean(BinomialSamples[0:100])
var(BinomialSamples[0:100])

#Første 1000
mean(BinomialSamples[0:1000])
var(BinomialSamples[0:1000])

 #Første 10000
mean(BinomialSamples[0:10000])
var(BinomialSamples[0:10000])

n=10
p=1/2
x=0:10
p=dbinom(x,size=n,prob=p)
plot(x,p,type="h",xlim=c(0,10),ylim=c(0,0.3),lwd=2,col="blue",
     ylab="Probability mass",xlab="Number of successes")
points(x,p,pch=16,cex=2,col="dark red")

#Hypergeometrisk
m <- 10
n <- 10
k <- 10
HypergeometricSamples <- rhyper(10000,m,n,k)

mean(HypergeometricSamples)
var(HypergeometricSamples)

x <- 0:m
p=dhyper(x,m,n,k,log=FALSE)
plot(x,p,type="h",xlim=c(0,10),ylim=c(0,0.4),lwd=2,col="blue",
     ylab="Probability mass",xlab="Number of successes", main="Hypergeometric")
points(x,p,pch=16,cex=2,col="dark red")

