# Komunikator

Verzija pythona: 3.8 (preverjeno deluje tudi v verziji 3.7)
Struktura map:
- komunikator:
  - app:
    - template
 
 Za pravilno delovanje programa, ga je potrebno zagnati na ravni "komunikator", ne na ravni "app".

Pred dodajanjem na Docker je potrebno v datotekah "output_to_user.py" in "user_input_acquisition" spremeniti naslavljanje datotek "app/ssml.xml" -> "/app/ssml.xml"; "app/intents2.json" -> "/app/intents2.json" in 'app/vaja-stqi-a94d4033cbd5.json' -> '/app/vaja-stqi-a94d4033cbd5.json'. 
