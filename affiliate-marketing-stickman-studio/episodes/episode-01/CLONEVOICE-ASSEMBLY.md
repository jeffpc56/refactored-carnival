# CloneVoice video assembly

The preferred voice is **Teacher Explaining Patiently** (Jeff's saved CloneVoice preset).

CloneVoice output must be exported as MP3 or WAV through Jeff's authorized account. No public API or access to his signed-in browser was available here. Do NOT substitute an unrelated voice and call it CloneVoice.

Production assembly script: `render_with_clonevoice.py` (in this folder).

Requires existing first-scene visual clip `poppy_mockery/silent.mp4` from the local prototype, and a CloneVoice audio export. Run:

```bash
python render_with_clonevoice.py /path/to/voiceover.mp3
```

Produces `poppy_vs_stickmen_clonevoice_rough_cut.mp4`.

This only retimes visual playback to the full audio length. It does not produce genuine lip sync, gesture timing, or scene-by-scene alignment. Proper lip sync requires a talking-character video generation step. This is a technical starting point, not the finished video.

Scene composition rules:
- Poppy is the foreground speaker.
- The television/whiteboard remains physically behind him.
- Stickmen silently mock him on that screen.
- Use Poppy's selected voice for all narration.
