from rsagestion import RsaGestion
from aesgestion import AesGestion
from hashgestion import HashGestion


hash_gestion = HashGestion()
message = "message secret"
empreinte = hash_gestion.calculate_sha256(message)
print(f"Message  : {message}")
print(f"Empreinte SHA-256 : {empreinte}")



empreinte_fichier = hash_gestion.calculate_file_sha256( "test.txt")
print(" Test SHA-256 d'un fichier ")
print(f"Empreinte SHA-256  : {empreinte_fichier}\n")



#AES
aes_gestion = AesGestion()
aes_gestion.generate_aes_key()

texte = "test"
texte_chiffre = aes_gestion.encrypt_string_to_base64("peorpeor")
texte_dechiffre = aes_gestion.decrypt_string_from_base64(texte_chiffre)

print("Test AES d'une chaine")
print(f"Texte dechiffre: {texte_dechiffre}\n")


