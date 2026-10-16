"""Replace rough prototype voice with a CloneVoice MP3 or WAV export.
Usage: python render_with_clonevoice.py /path/to/voiceover.mp3
Requires ffmpeg, ffprobe and the prototype silent footage at /mnt/data/poppy_mockery/silent.mp4.
Retimes visuals to audio; does not lip-sync.
"""
import subprocess, sys, pathlib, json
p = pathlib.Path('/mnt/data')
if len(sys.argv) != 2:
    raise SystemExit('Usage: python render_with_clonevoice.py <CloneVoice MP3 or WAV>')
audio = pathlib.Path(sys.argv[1]).resolve()
video = p / 'poppy_mockery/silent.mp4'
if not audio.is_file() or not video.is_file():
    raise SystemExit('Both CloneVoice audio and the existing silent video are needed.')
def duration(f):
    value = subprocess.check_output(['ffprobe','-v','error','-show_entries',
         'format=duration','-of','json',str(f)])
    return float(json.loads(value)['format']['duration'])
v,a=duration(video),duration(audio)
out=p/'poppy_vs_stickmen_clonevoice_rough_cut.mp4'
subprocess.run(['ffmpeg','-y','-v','error','-i',str(video),'-i',str(audio),
    '-filter_complex',f'[0:v]setpts={a/v:.8f}*PTS[v]','-map','[v]',
    '-map','1:a:0','-c:v','libx264','-preset','medium','-crf','21',
    '-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-movflags',
    '+faststart','-shortest',str(out)],check=True)
print('ROUGH CUT:',out)
print('Voice retimed, not lip synced.')
