from lib_pianoroll import get_pianoroll_encoder_decoder
from lib_hparams import get_hparams_object
import pretty_midi

# Define the hyperparameters
hparams = {}
hparams["shortest_duration"] = 0.125
hparams["min_pitch"] = 36
hparams["max_pitch"] = 81
hparams["separate_instruments"] = True
hparams["num_instruments"] = 4
hparams["quantization_level"] = 0.125

hparams_obj = get_hparams_object(hparams)

encoder_decoder = get_pianoroll_encoder_decoder(hparams_obj)
midi_melody_file = pretty_midi.PrettyMIDI("../data/322_SuperMarioBros__17_18SavedthePrincess.mid")
midi_fullvoices_file = pretty_midi.PrettyMIDI("../data/322_SuperMarioBros__17_18SavedthePrincess_full_voices.mid")

pianoroll_melody_result = encoder_decoder.encode_midi_melody_to_pianoroll(midi_melody_file)
pianoroll_fullvoices_result = encoder_decoder.encode_midi_to_pianoroll(midi_fullvoices_file, (1, 16, 46, 3))