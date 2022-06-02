#4

#Find all entities involved in the chain of trust:

#Finding the entities involved with the sertificate for uib.no we find that these are the four entities involed:
#p1masterlb.uib.no -> GEANT OV RSA CA 4 -> USERTrust RSA Certification Authority -> Sectigo (AAA)


#What digital signature algorithm was used to authenticate them?

# p1masterlb.uib.no -> sha384RSA
# GEANT OV RSA CA 4 -> sha384RSA
# USERTrust RSA Certification Authority -> sha384RSA
# Sectigo (AAA) -> sha1RSA


#What is their public key?

# p1masterlv.uib.no -> RSA (2048 bits): 30 82 01 0a 02 82 01 01 00 e8 84 2b c8 af 51 e6 b0 89 99 d4 f7 2a bf 86 b6 43 57 7c ec 04 a2 51 01 23 26 cb db a1 35 77 61 0a eb 20 0f 61 2d f3 a2 42 80 b6 6c ac bc c4 2a 16 21 34 2c f8 98 67 56 55 0d 4a d0 21 e6 50 8a 1a e8 06 bd 3f ec 03 23 ea a5 c0 a0 ff 39 fb bf 54 fe 9c 1c 97 c3 b5 f3 14 ad 5b 68 9f f3 6f 39 be a2 18 ad 1f 91 be d7 e1 4c f7 fe 09 ca 4b 14 83 3e 7d f2 4b d0 c5 37 1a 29 6a 0b 3d 3b a2 70 3f 14 3a 2f da 6f a6 22 64 13 f5 44 88 a1 d9 4c b3 21 f5 73 e1 d9 98 7e 32 df 06 25 cf ac 06 01 74 c3 0e 46 ec 1a df 51 af 13 e9 a1 b2 94 81 a4 5d 16 7a 13 c9 4e d3 59 5f cd 7b 0d 1d c8 30 24 18 43 b6 ff 4e c6 4a 52 59 98 7b 7c 97 92 bc 53 ae 59 1e 05 33 c9 d7 4a 56 9c 8c 82 13 1e e2 bc 60 a2 c3 a5 d7 10 0a 65 9e c5 eb 42 0f 74 03 98 2f 7f 98 c5 89 d5 04 e8 c2 8b d8 82 7b 27 d7 5f 02 03 01 00 01
# GEANT OV RSA CA 4 & USERTrust RSA Certification Authority -> RSA (4096 bits): 30 82 02 0a 02 82 02 01 00 a5 88 62 d5 a1 22 3e c8 3d 64 a4 4c 03 0f 50 af c3 2d 86 ca fa 47 6d 15 49 f1 5e 87 b4 e0 c2 d2 d0 8b a4 52 44 b3 a1 e2 8a f8 10 c1 bf d6 d8 7c 96 28 ef ef 19 c1 31 56 64 4f 2b 05 88 f9 93 3e 22 ce 7e fc fe 43 03 b5 37 08 ef 81 8f 89 ae ce df 4a 85 40 fd 34 24 5f 37 31 bb 84 e5 dd 61 e2 fa a2 66 28 b2 55 bb f2 4e b8 7b 9d ea 63 a9 2d 69 08 6e 13 83 4b 33 b1 00 d2 76 e0 81 8f c7 d8 78 39 70 f2 cb af f7 e3 67 84 e9 43 d7 0a d2 7c 03 37 ae 99 31 ba 0d fb f9 29 5c 76 e2 50 85 4c 65 33 1d 40 7e 8f e8 34 95 22 a0 fd 27 f5 3b 38 02 6a 32 55 f5 e9 e6 67 ff 38 c9 d8 78 f3 03 e9 ea f6 d6 7f 51 f4 3b 74 5d dc b8 69 31 25 67 4e a1 53 2c a6 52 6d 07 8b 73 1f e5 f4 33 8a 65 f0 42 0b d8 21 5b 1b 20 4e a5 bd 81 0e ef dd 3d da 21 f4 9a 54 2f 6b 9f 05 71 3b 45 63 98 37 4f 14 d6 dd a3 19 e1 d3 36 30 7f 8e 67 57 54 10 82 94 70 64 9f 77 c9 67 9d 86 9e 1c 87 56 ba 02 3c 2a b3 ec 2f e2 66 73 98 14 a3 a2 fb 55 d2 62 b0 77 e0 90 6d 24 e8 6a 51 14 3f 84 1e 26 ae 14 77 3e 56 36 63 4c 23 83 98 3f a7 20 ae 79 49 e7 46 9a d0 36 4f 94 9a ab 29 03 c6 2f af 4a 41 0c f5 d9 68 31 be 10 ae 55 4e f4 cb a6 56 00 fa 29 05 ad 72 91 bb 2d b6 92 f1 00 36 6b 7b 97 07 e7 bd e5 22 e2 c7 76 3c 7b 36 3a 58 21 74 71 db e4 09 51 19 d7 da ac 77 ed e6 48 c5 85 f3 f2 08 0c fb 05 c7 e9 10 db 53 75 76 a3 90 cf eb b8 57 3c 74 80 6c 0f a9 d2 8a e3 02 87 29 93 6a 2c c4 72 a8 35 21 37 2c 28 cd c7 c5 95 77 19 d7 be e4 36 f2 d2 9d 68 ae bd 92 77 e6 dd b0 7b c6 97 5f b0 d3 53 3c 7f 44 95 c8 ec 71 66 71 a5 e6 79 22 28 fc 97 2a c2 1b 5c f4 bd 25 ad 48 1b 20 4a 75 32 1b fb 02 03 01 00 01
# Sectigo (AAA) -> RSA (2048 bits): 30 82 01 0a 02 82 01 01 00 be 40 9d f4 6e e1 ea 76 87 1c 4d 45 44 8e be 46 c8 83 06 9d c1 2a fe 18 1f 8e e4 02 fa f3 ab 5d 50 8a 16 31 0b 9a 06 d0 c5 70 22 cd 49 2d 54 63 cc b6 6e 68 46 0b 53 ea cb 4c 24 c0 bc 72 4e ea f1 15 ae f4 54 9a 12 0a c3 7a b2 33 60 e2 da 89 55 f3 22 58 f3 de dc cf ef 83 86 a2 8c 94 4f 9f 68 f2 98 90 46 84 27 c7 76 bf e3 cc 35 2c 8b 5e 07 64 65 82 c0 48 b0 a8 91 f9 61 9f 76 20 50 a8 91 c7 66 b5 eb 78 62 03 56 f0 8a 1a 13 ea 31 a3 1e a0 99 fd 38 f6 f6 27 32 58 6f 07 f5 6b b8 fb 14 2b af b7 aa cc d6 63 5f 73 8c da 05 99 a8 38 a8 cb 17 78 36 51 ac e9 9e f4 78 3a 8d cf 0f d9 42 e2 98 0c ab 2f 9f 0e 01 de ef 9f 99 49 f1 2d df ac 74 4d 1b 98 b5 47 c5 e5 29 d1 f9 90 18 c7 62 9c be 83 c7 26 7b 3e 8a 25 c7 c0 dd 9d e6 35 68 10 20 9d 8f d8 de d2 c3 84 9c 0d 5e e8 2f c9 02 03 01 00 01

#What are the public parameters used in the algorithm (e.g. the prime number p for RSA)?
# Information about key:
# Algorithm: RSA
# Key-size: 2048
# Eksponent: 65537
# Modulus: E8:84:2B:C8:AF:51:E6:B0:89:99:D4:F7:2A:BF:86:B6:43:57:7C:EC:04:A2:51:01:23:26:CB:DB:A1:35:77:61:0A:EB:20:0F:61:2D:F3:A2:42:80:B6:6C:AC:BC:C4:2A:16:21:34:2C:F8:98:67:56:55:0D:4A:D0:21:E6:50:8A:1A:E8:06:BD:3F:EC:03:23:EA:A5:C0:A0:FF:39:FB:BF:54:FE:9C:1C:97:C3:B5:F3:14:AD:5B:68:9F:F3:6F:39:BE:A2:18:AD:1F:91:BE:D7:E1:4C:F7:FE:09:CA:4B:14:83:3E:7D:F2:4B:D0:C5:37:1A:29:6A:0B:3D:3B:A2:70:3F:14:3A:2F:DA:6F:A6:22:64:13:F5:44:88:A1:D9:4C:B3:21:F5:73:E1:D9:98:7E:32:DF:06:25:CF:AC:06:01:74:C3:0E:46:EC:1A:DF:51:AF:13:E9:A1:B2:94:81:A4:5D:16:7A:13:C9:4E:D3:59:5F:CD:7B:0D:1D:C8:30:24:18:43:B6:FF:4E:C6:4A:52:59:98:7B:7C:97:92:BC:53:AE:59:1E:05:33:C9:D7:4A:56:9C:8C:82:13:1E:E2:BC:60:A2:C3:A5:D7:10:0A:65:9E:C5:EB:42:0F:74:03:98:2F:7F:98:C5:89:D5:04:E8:C2:8B:D8:82:7B:27:D7:5F