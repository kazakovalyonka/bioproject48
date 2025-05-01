from Bio import SeqIO
from Bio.Seq import Seq

# Функция для извлечения белковых последовательностей из файла GenBank
def extract_proteins(file_path):
    for record in SeqIO.parse(file_path, "genbank"):
        for feature in record.features:
            if feature.type == "CDS":
                # Локация кодирующей области
                location = feature.location 
                # Нуклеотидная последовательность
                sequence = feature.extract(record.seq)
                 # Трансляция до стоп-кодона 
                translation = sequence.translate(to_stop=True)  
                print(f"{record.id}: {record.description}")
                print(f"Coding sequence location = {location}")
                print(f"Translation =\n{translation}\n")

# Путь к файлу GenBank
genbank_file = "sequence.gb"
extract_proteins(genbank_file)
