#Para RSA-OAEP y PSS
from Crypto.PublicKey import RSA
from Crypto.PublicKey.RSA import generate
from Crypto.Cipher import PKCS1_OAEP

#Para RSA-PSS
from Crypto.Signature import pkcs1_15, pss

#Para generación de cadenas
import string
import random

#Para calculo de tiempo, tablas y graficas
import timeit
from time import time
import pandas as pd
import matplotlib.pyplot as plt

num_global = 0
tiempos = []
tiempos2 = []
cadena = []

class rsa():
	def cadenas():
	  cadena = []
	  num_global = 0
	  length_of_string = random.randint(50, 50)
	  for i in range(0,500,1):
	    cadena.append(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))
	  return(cadena)

	def cifrado():
	  externalkey = generate(1024, randfunc=None, e=17)
	  message = bytes(cadena[num_global],'utf8')
	  key = RSA.importKey(externalkey.exportKey())
	  cipher = PKCS1_OAEP.new(key)
	  ciphertext = cipher.encrypt(message)

	def decifrado():
	  global tiempos2
	  externalkey = generate(1024, randfunc=None, e=17)
	  message = bytes(cadenas[num_global],'utf8')
	  key = RSA.importKey(externalkey.exportKey())
	  cipher = PKCS1_OAEP.new(key)
	  ciphertext = cipher.encrypt(message)
	  ####Decrypt
	  tiempo_inicial = time() 
	  key = RSA.importKey(externalkey.exportKey())
	  cipher = PKCS1_OAEP.new(key)
	  message_decrypt = cipher.decrypt(ciphertext)
	  tiempo_final = time() 
	  tiempo = tiempo_final - tiempo_inicial
	  tiempos2.append(tiempo)
	  return(tiempos2)

	def time_cifrar():
	  global num_global
	  global tiempos
	  tiempo_inicial = time() 
	  rsa.cifrado()
	  tiempo_final = time() 
	  num_global += 1
	  tiempo = tiempo_final - tiempo_inicial
	  tiempos.append(tiempo)
	  return(tiempos)