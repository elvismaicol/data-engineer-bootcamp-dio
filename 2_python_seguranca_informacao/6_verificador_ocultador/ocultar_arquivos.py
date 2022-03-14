import ctypes

# cód hexadecimal para ocultar
atributo_oculto = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW('ocultar.txt', atributo_oculto)

if retorno:
    print("Arquivo foi ocultado")
else:
    print("Arquivo não foi ocultado")