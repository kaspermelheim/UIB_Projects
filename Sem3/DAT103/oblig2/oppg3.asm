    
; konstanter    
    SYS_EXIT  equ 1
    SYS_READ  equ 3
    SYS_WRITE equ 4
    STDIN     equ 0
    STDOUT    equ 1
    STDERR    equ 2


section .bss
	num resb 10
	
section .text
	global _start

_start:
	mov ecx, 0

loop1:
	inc ecx
	cmp ecx, 10
	jl loop1
	je loop2

loop2:
	dec ecx
	cmp ecx, 0
	jg loop2
	je Finished
	
skrivsiffer:
; Skriver ut sifferet lagret i ecx. Ingen sjekk på verdiområde.
	push eax
	push ebx
	push ecx
	push edx
	add ecx,'0'; converter tall til ascii.
	mov [num],ecx
	mov ecx,num
	mov edx,1
	mov ebx,STDOUT
	mov eax,SYS_WRITE
	int 80h
	pop edx
	pop ecx
	pop ebx
	pop eax
	ret	
			
Finished:
	call skrivsiffer
	mov eax,1
	mov ebx,0
	int 80h	
	
	
