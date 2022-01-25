#sample
#031005
#Lager sampler fra "populasjon".
#sample st?rrelse: n
#antall  = m

m <- 100
n <- 50

X<-populasjon[,2]
M<-matrix( rep(0,n*m), ncol=m)
for( j in 1:m) 
{
  M[,j]<-sample(X,n, replace=F)
}	

#_____________Datasettetene lagres:__________	
utvalg<-data.frame(M)
	

#_____________________slutt___________________
