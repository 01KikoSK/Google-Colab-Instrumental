# prompt: create me instrumental

# This code requires the music21 library. Install it if you haven't already:
# !pip install music21

from music21 import *

def create_simple_instrumental():
  """Creates a simple instrumental piece using music21."""

  # Create a stream to hold the music
  score = stream.Stream()

  # Create a melody (example: C major scale)
  melody = stream.Part()
  melody.insert(0, instrument.Piano())  # Specify the instrument

  notes = [note.Note("C4"), note.Note("D4"), note.Note("E4"), note.Note("F4"),
           note.Note("G4"), note.Note("A4"), note.Note("B4"), note.Note("C5")]
  for n in notes:
      melody.append(n)

  # Add some chords (example: C major chord)
  chords = stream.Part()
  chords.insert(0, instrument.AcousticGuitar()) #Specify the instrument

  c_major_chord = chord.Chord(["C3", "E3", "G3"])
  chords.append(c_major_chord)
  chords.append(c_major_chord) # Repeat the chord for simplicity
  chords.append(c_major_chord)


  # Add the melody and chords to the score
  score.insert(0, melody)
  score.insert(0, chords)
  
  # Show the score (in a new window)
  score.show()

  # Or save it as a MIDI file:
  # score.write('midi', fp='my_instrumental.mid')

create_simple_instrumental()