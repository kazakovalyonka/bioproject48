from Bio import SeqIO

# Функция для расчёта GC-состава
def calculate_gc_content(sequence):
    g = sequence.count("G")
    c = sequence.count("C")
    total = len(sequence)
    return (g + c) / total

# Основная часть программы
def sort_by_gc_content(file_path):
    records = []

    # Чтение записей из файла GenBank
    for record in SeqIO.parse(file_path, "genbank"):
        seq = str(record.seq)
        gc_content = calculate_gc_content(seq)
        records.append((record.id, record.description, gc_content))

    # Сортировка записей по GC-составу
    records.sort(key=lambda x: x[2])

    # Вывод результатов
    for record_id, description, gc_content in records:
        print(f"{record_id}: {description}, GC = {gc_content}")

# Указание пути к файлу
genbank_file = "sequence.gb"
sort_by_gc_content(genbank_file)
