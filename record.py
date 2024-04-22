import io
import typing
import time
import wave
from pathlib import Path

import pyaudio
from rhasspysilence import WebRtcVadRecorder, VoiceCommand, VoiceCommandResult

pa = pyaudio.PyAudio()


def speech_to_text() -> None:
    """
    Records audio until silence is detected
    Saves audio to audio/recording.wav
    """
    recorder = WebRtcVadRecorder(
        vad_mode=3,
        silence_seconds=4,
    )
    recorder.start()

    # Directory to save WAV files
    wav_dir = Path("audio")
    wav_filename = "recording"

    audio_source = pa.open(
        rate=16000,
        format=pyaudio.paInt16,
        channels=1,
        input=True,
        frames_per_buffer=960,
    )
    audio_source.start_stream()

    def buffer_to_wav(buffer: bytes) -> bytes:
        """Wraps a buffer of raw audio data in a WAV"""
        rate = 16000
        width = 2  # Bytes per sample
        channels = 1

        with io.BytesIO() as wav_buffer:
            with wave.open(wav_buffer, mode="wb") as wav_file:
                wav_file.setframerate(rate)
                wav_file.setsampwidth(width)
                wav_file.setnchannels(channels)
                wav_file.writeframesraw(buffer)

            return wav_buffer.getvalue()

    try:
        chunk = audio_source.read(960)
        while chunk:
            # Look for speech/silence
            voice_command = recorder.process_chunk(chunk)

            if voice_command:
                # Reset
                audio_data = recorder.stop()
                if wav_dir:
                    # Write WAV to directory
                    wav_path = (wav_dir / f"{wav_filename}_{int(time.time())}.wav")
                    wav_bytes = buffer_to_wav(audio_data)
                    wav_path.write_bytes(wav_bytes)
                    break

            # Next audio chunk
            chunk = audio_source.read(960)

    finally:
        try:
            audio_source.stop_stream()
            audio_source.close()
        except Exception:
            pass


if __name__ == "__main__":
    speech_to_text()
