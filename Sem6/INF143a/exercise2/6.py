#Construct a LFSR with a max of 1073741823

#We find out that 2^30 = max + 1 = 1073741823
#This means we need to create a LFSR with 30 cells
#Since it is primitive we will end up with a maximum cycle of 2^30 - 1 (every state except zero-state: [0,0,0,0,0,...,0] etc])

#We can use a online generator to find a LFSR with 30 cells:

#x^30 + x^27 + x^25 + x^24 + x^23 + x^22 + x^19 + x^16 + x^12 + x^10 + x^8 + x^7 + x^6 + x^1 + 1