par(las=2) # make label text perpendicular to axis
par(mar=c(4,7,3,1))
par(mfrow=c(1,2))

Ita = read.table("Ita.txt", head=T)
data= rbind(Ita$Art, Ita$Poss)
barplot(as.matrix(data), main="Italian", col=c("black","grey"), names.arg=Ita$Noun, xlim=c(0,1), cex.names=0.7, cex.main = 2, horiz=TRUE) 
abline(v=0.4, col="white")

Eng = read.table("Eng.txt", head=T)
data= rbind(Eng$Art, Eng$Poss)
barplot(as.matrix(data), main="English", col=c("black","grey"), names.arg=Eng$Noun, xlim=c(0,1), cex.names=0.7, cex.main = 2, horiz=TRUE) 
abline(v=0.4, col="white")

table(Ita$Art<0.40)
table(Eng$Art<0.40)

