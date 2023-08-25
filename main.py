import speech_recognition as sVoice
import pyttsx3
import pywhatkit as kit
import openai
import subprocess
import os

# Setup kunci API
openai.api_key = "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"

def speech_to_text():
    recognizer = sVoice.Recognizer()
    microphone = sVoice.Microphone()

    with microphone as source:
        print('Mendengarkan...')
        audio = recognizer.listen(source, phrase_time_limit=7)
        try:
            print('Memproses...')
            teks = recognizer.recognize_google(audio, language='id-ID')
            print('Anda mengatakan:', teks)
            return teks
        except sVoice.UnknownValueError:
            print("Maaf, tidak dapat mengerti suara.")
            return None
        except sVoice.RequestError:
            print("Tidak dapat meminta hasil. Periksa koneksi jaringan Anda.")
            return None

def text_to_speech(teks):
    engine = pyttsx3.init()
    engine.say(teks)
    engine.runAndWait()

def chat_dengan_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2000
    )
    return response.choices[0].text.strip()

def wait_for_trigger(trigger_phrase):
    recognizer = sVoice.Recognizer()
    microphone = sVoice.Microphone()

    while True:
        print("Menunggu perintah...")
        trigger_input = speech_to_text()

        if trigger_input and trigger_phrase.lower() in trigger_input.lower():
            print("Perintah terdeteksi:", trigger_phrase)
            break

if __name__ == "__main__":
    while True:
        print("Menunggu trigger")
        wait_for_trigger("Halo Siesta")
        print("Bot Diaktifkan...")
        text_to_speech("Halo, Selamat Datang Kembali. Erlang!")

        while True:
            print("Silakan berkata sesuatu...")
            input_pengguna = speech_to_text()

            if input_pengguna:
                if "stop" in input_pengguna.lower():
                    print("Menghentikan sistem.")
                    text_to_speech("Selamat tinggal!")
                    wait_for_trigger("Halo Siesta")  # Menunggu trigger untuk mengaktifkan kembali
                elif "buka spotify" in input_pengguna.lower():
                    print("Membuka Spotify...")
                    text_to_speech("Membuka Spotify...")
                    kit.playonyt("Spotify")  # Membuka Spotify di YouTube
                elif "buka youtube" in input_pengguna.lower():
                    print("Membuka YouTube...")
                    text_to_speech("Membuka YouTube...")
                    kit.playonyt("YouTube")  # Membuka YouTube di browser
                elif "buka instagram" in input_pengguna.lower():
                    print("Membuka Instagram...")
                    text_to_speech("Membuka Instagram...")
                    kit.search("Instagram")  # Mencari Instagram di browser

            else:
                print("Berbincang dengan AI...")
                respons_gpt = chat_dengan_gpt(input_pengguna)
                print("Respons AI:", respons_gpt)
                text_to_speech(respons_gpt)


























# def speech_to_text():
#     recognizer = sVoice.Recognizer()
#     microphone = sVoice.Microphone()

#     with microphone as source:
#         print('Mendengarkan...')
#         audio = recognizer.listen(source, phrase_time_limit=5)
#         try:
#             print('Memproses...')
#             text = recognizer.recognize_google(audio, language='id-ID')
#             print('Anda mengatakan:', text)
#             return text
#         except sVoice.UnknownValueError:
#             print("Maaf, tidak dapat mengerti suara.")
#             return None
#         except sVoice.RequestError:
#             print("Tidak dapat meminta hasil. Periksa koneksi jaringan Anda.")
#             return None

# def text_to_speech(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()

# def search_wikipedia(query):
#     try:
#         summary = wikipedia.summary(query, sentences=2)
#         return summary
#     except wikipedia.exceptions.PageError:
#         return "Maaf, saya tidak dapat menemukan informasi tentang itu."
#     except wikipedia.exceptions.DisambiguationError:
#         return "Terdapat beberapa kemungkinan hasil. Mohon berikan informasi yang lebih spesifik."
#     except wikipedia.exceptions.HTTPTimeoutError:
#         return "Waktu pencarian di Wikipedia habis. Mohon coba lagi nanti."

# if __name__ == "__main__":
#     while True:
#         print("Silakan berkata sesuatu...")
#         user_input = speech_to_text()

#         if user_input:
#             if "berhenti" in user_input.lower():
#                 print("Menghentikan sistem.")
#                 text_to_speech("Sampai jumpa, Erlang!")
#                 break
            
#             print("Mencari di Wikipedia untuk:", user_input)
#             wiki_result = search_wikipedia(user_input)
#             print("Ringkasan Wikipedia:", wiki_result)
#             text_to_speech(wiki_result)























# def perintah():
#     dengar = sVoice.Recognizer() #Mengambil atribut Objek sVoice
#     with sVoice.Microphone() as src: #Membuat sebuah Perintah
#         print('Listening . . .')
#         suara = dengar.listen(src, phrase_time_limit=5)
#         try:
#             print('Processing. . .')
#             Service = dengar.recognize_google(suara, language='id-ID')
#             print(Service)
#         except:
#             pass
#         return Service

# def knowledge():
#     In = 
#     voice = pyt.init()
#     result = wikipedia.summary

# def bicara(self):
#     teks = (self) 
#     bahasa = 'id'
#     namaFile = 'bicara.mp3'
#     def read():
#         suara = gTTS(text=teks, lang=bahasa, slow=False)
#         suara.save(namaFile)
#         os.system(f'start {namaFile}')
#     read( )

# def startSiesta():
#     Service = perintah()
#     bicara(Service)

# startSiesta()