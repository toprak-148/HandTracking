
import speech_recognition as sr
import time

def main():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Dinleniyor... (çıkmak için sifir demelisin)")
            try:
                # Mikrofonun en fazla 5 saniye içinde ses algılamasını bekler
                audio = r.listen(source, timeout=3, phrase_time_limit=10)
                voice = r.recognize_google(audio, language='tr-TR')
                print("Tanınan ses:", voice)
                
                if voice.lower() == "sifir":
                    print("Çıkış komutu alındı. Program sonlandırılıyor.")
                    break
            except sr.WaitTimeoutError:
                print("Zaman aşımı: Mikrofon 5 saniye içinde ses algılayamadı.")
            except sr.UnknownValueError:
                print("Tanımlanamayan ses: Ses tanıma başarısız oldu.")
            except sr.RequestError as e:
                print("İstek hatası; Google Web Speech API'ye ulaşılamadı; {0}".format(e))

if __name__ == "__main__":
    main()
