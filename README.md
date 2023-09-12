
# PST to MBOX Converter

Questo script Python è stato progettato per convertire file PST (Microsoft Outlook Personal Storage Table) in file MBOX (formato utilizzato da molti client di posta elettronica).

## Requisiti

- Python 3.x
- Libreria `libratom` per l'accesso ai file PST
- Libreria `mailbox` per la gestione dei file MBOX

Puoi installare le librerie necessarie eseguendo:
pip install libratom mailbox

## Utilizzo

1. Assicurati di avere il file PST che desideri convertire nella stessa directory dello script o specifica il percorso del file PST come argomento al momento dell'esecuzione dello script.

2. Esegui lo script:
3. python pst_to_mbox.py
4. alla richiesta   "Inserisci il percorso del file PST da convertire:"  inserisci nomefile.pst

5. Una volta completata la conversione, il file MBOX risultante conterrà i messaggi precedentemente presenti nel file PST. Puoi utilizzare client di posta elettronica compatibili con il formato MBOX per aprire e visualizzare i messaggi.


