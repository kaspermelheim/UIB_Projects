#Populajon
#031005
#
#Dette skriptet lager populasjon.
#idealistisk ønske: forventing 3.4 og standardavvik 4.8
#Vi har laget  mu= 3050 * 0.3 + 3750* 0.7
# Dette gir for stor varians.


#________________størrelse på populasjonen______________
N <- 30000

#_________________frø______________
set.seed(31005)

#_________________blandingsmodell__________
p<-0.3

mu1 <- 3000
mu2 <- 3800

si1 <- 300
si2 <- 550



#__________________________genererer blandingsmodell___________
x1<- rnorm(N,mu1,si1)
x2<- rnorm(N,mu2,si2)
z<-rbinom(N,1,p)
x1<-round(x1)
x2<-round(x2)
x<- x1*z + x2*(1-z)


#___________________________Plasserer data i en dataramme.
no<-1:N
M<-matrix( rep(0,2*N),ncol=2)
M[,1]<-no
M[,2] <-x
populasjon<-data.frame(M)

#_____________________slutt_________________________
