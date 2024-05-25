from pydub import AudioSegment

def split_audio(file_path, output1, output2):
    # Carregar o arquivo de áudio
    audio = AudioSegment.from_file(file_path, format="wav")
    
    # Calcular o ponto de divisão
    mid_point = len(audio) // 2
    
    # Dividir o áudio em duas partes
    first_half = audio[:mid_point]
    second_half = audio[mid_point:]
    
    # Exportar as duas partes como novos arquivos WAV
    first_half.export(output1, format="wav")
    second_half.export(output2, format="wav")

# Caminho para o seu arquivo de áudio WAV
file_path = "Rua Professor Picarolo.wav"

# Nomes dos arquivos de saída
output1 = "Rua Professor Picarolo_part1.wav"
output2 = "Rua Professor Picarolo_part2.wav"

# Dividir o arquivo
split_audio(file_path, output1, output2)

