from libratom.lib.pff import PffArchive
import mailbox
from email import message_from_string
from pathlib import Path

# Richiedi all'utente il percorso del file PST da convertire
pst_file = input("Inserisci il percorso del file PST da convertire: ")

# Verifica se il file PST esiste
if not Path(pst_file).is_file():
    print("Il file PST specificato non esiste.")
    exit()

output_mbox_file = "output.mbox"

archive = PffArchive(pst_file)

# Crea un oggetto Mbox per scrivere i messaggi convertiti
mbox = mailbox.mbox(output_mbox_file)

for folder in archive.folders():
    if folder.get_number_of_sub_messages() != 0:
        for message in folder.sub_messages:
            eml_message = archive.format_message(message)  # Ottieni il messaggio in formato EML
            email_message = message_from_string(eml_message)  # Converti il messaggio EML in un oggetto EmailMessage
            
            # Estrai il testo del messaggio come stringa UTF-8
            message_text = email_message.as_string().encode('utf-8')
            
            # Aggiungi il messaggio all'oggetto Mbox
            mbox.add(message_text)

# Salva l'oggetto Mbox nel formato MBOX
mbox.flush()

print(f"Conversione da PST a MBOX completata. I messaggi sono stati salvati in {output_mbox_file}")
