letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z" \
          "a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z"
alphabet = ""
letter = letters.split()
letter.append(" ")
crypt_prog = False
language = input("Please chose language 'en' for English: \n"
                 "Lütfen dil seçiniz Türkçe için 'tr' değerini giriniz: ").lower()


def crypt_again():
    global language
    global crypt_prog
    crypt_prog = True
    language = input("Please chose language 'en' for English: \n"
                     "Lütfen dil seçiniz Türkçe için 'tr' değerini giriniz: ").lower()
    if language == "tr":
        crypt_prog = False
        turkish()
    elif language == "en":
        crypt_prog = False
        english()




def turkish():
    global crypt_prog
    global letter
    global alphabet
    while not crypt_prog == True:
        crypt = input("Şifreyi Çözmek için: 'coz', olusturmak için ise 'olustur' değerlerini giriniz: ").lower()
        if crypt == "olustur":
            value = int(input("Şifrenizin kripto sayısının kaç olmasını istersiniz? "))
            message = input("Lütfen şifrelemek istediğiniz mesajı giriniz: ").lower()
            for i in range(len(message)):
                if message[i] == " ":
                    alphabet += " "
                else:
                    indeks = letter.index(message[i])
                    updated_index = (indeks + value) % len(letter)
                    alphabet += letter[updated_index]
            print(f"Oluşturduğunuz şifre aşağıdadır. Karşı tarafın şifreyi çözmesi için lütfen kripto sayısını"
                f" iletmeyi unutmayınız.\nŞifre: {alphabet}")
            crypt_prog = True
        elif crypt == "coz":
            value = int(input("Şifrenizin kripto sayısının kaç olmasını istersiniz? "))
            message = input("Lütfen cozmek istediğiniz istediğiniz şifreyi giriniz: ").lower()
            for i in range(len(message)):
                if message[i] == " ":
                    alphabet += " "
                else:
                    indeks = letter.index(message[i])
                    updated_index = (indeks - value) % len(letter)
                    alphabet += letter[updated_index]
            print(f"Çözülen şifre aşağıdadır.\nÇözülen Şifre: {alphabet}")
            crypt_prog = True
        else:
            again = input("Yanlış bir değer girdiniz. Yeniden başlatmak için 'E', sonlandırmak için 'H' "
                        "değerlerinden birini giriniz.")
            if again == "e":
                crypt_again()
            else:
                crypt_prog = True
                print("Teşekkürler. İyi günler dileriz.")

def english():
    global crypt_prog
    global letter
    global alphabet
    global crypt_again
    while not crypt_prog == True:
        crypt = input("To Decrypt: enter 'decrypt', to generate 'crypty' values: ").lower()
        value = int(input("What number of cryptos do you want your password to be? "))
        if crypt == "crypt":
            message = input("Please enter the message you want to encrypt: ").lower()
            for i in range(len(message)):
                if message[i] == " ":
                    alphabet += " "
                else:
                    indeks = letter.index(message[i])
                    updated_index = (indeks + value) % len(letter)
                    alphabet += letter[updated_index]
            print(f"The password you created is below. Please do not forget to provide the crypto number for the other"
                  f" party to decrypt it.\nCrypt Password: {alphabet}")
            crypt_prog = True
        elif crypt == "decrypt":
            message = input("Please enter the password you want to decrypt: ").lower()
            for i in range(len(message)):
                if message[i] == " ":
                    alphabet += " "
                else:
                    indeks = letter.index(message[i])
                    updated_index = (indeks - value) % len(letter)
                    alphabet += letter[updated_index]
            print(f"The decrypted password is below.\nDecrypt Passowrd: {alphabet}")
            crypt_prog = True
        else:
            again = input("You entered an incorrect value. Enter 'Y' to restart, 'N' to terminate.").lower()
            if again == "y":
                crypt_again()
            else:
                crypt_prog = True
                print("Thanks. Have a nice days.")


if language == "tr":
    turkish()
elif language == "en":
    english()
