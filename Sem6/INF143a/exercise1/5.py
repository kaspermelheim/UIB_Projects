cipher = "IVSIKBFDGXQUMNBDVAZY"
key = "BERGEN"

#5x5 PLayfair grid med key BERGEN
B E R G N 
A C D F H 
I K L M O
P Q S T U
V W X Y Z

#Følger steps fra https://www.geeksforgeeks.org/playfair-cipher-with-examples/

#Deler cipher opp i pairs, IV, SI, KB etc
"IV" -> "AP"
"SI" -> "PL"

#Fortsett for alle pairs og du ender opp med:
"APPLIEDCRYPTOGRAPBYX"