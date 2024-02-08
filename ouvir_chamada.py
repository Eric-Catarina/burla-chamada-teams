import pvporcupine
import pyaudio
import struct
import subprocess
import os
from dotenv import load_dotenv
load_dotenv()


def main():
    # Inicializar Porcupine com a palavra-chave personalizada
    porcupine = pvporcupine.create(
    access_key = os.getenv("ACCESS_KEY"), 
    keyword_paths=['./Chamada_pt_linux_v3_0_0.ppn'],
    model_path='./porcupine_params_pt.pv' # Atualize este caminho conforme necessário
)

    
    # Inicializar PyAudio e abrir o fluxo de áudio
    pa = pyaudio.PyAudio()
    audio_stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )
    
    print("Ouvindo a palavra 'Chamada'...")

    try:
        while True:
            # Ler dados do microfone
            pcm = audio_stream.read(porcupine.frame_length)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
            
            # Processar o frame de áudio
            result = porcupine.process(pcm)
            if result >= 0:
                print("Palavra 'Chamada' detectada, executando script.py...")
                # Substitua 'script.py' pelo caminho do seu script
                subprocess.run(['python3', './marcar_presenca.py'])
    except KeyboardInterrupt:
        print("Finalizando...")
    finally:
        # Limpeza
        audio_stream.close()
        pa.terminate()
        porcupine.delete()

if __name__ == "__main__":
    main()
