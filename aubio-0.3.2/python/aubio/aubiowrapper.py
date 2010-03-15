# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.36
#
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _aubiowrapper
import new
new_instancemethod = new.instancemethod
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


new_fvec = _aubiowrapper.new_fvec
del_fvec = _aubiowrapper.del_fvec
fvec_read_sample = _aubiowrapper.fvec_read_sample
fvec_write_sample = _aubiowrapper.fvec_write_sample
fvec_get_channel = _aubiowrapper.fvec_get_channel
fvec_put_channel = _aubiowrapper.fvec_put_channel
fvec_get_data = _aubiowrapper.fvec_get_data
new_cvec = _aubiowrapper.new_cvec
del_cvec = _aubiowrapper.del_cvec
cvec_write_norm = _aubiowrapper.cvec_write_norm
cvec_write_phas = _aubiowrapper.cvec_write_phas
cvec_read_norm = _aubiowrapper.cvec_read_norm
cvec_read_phas = _aubiowrapper.cvec_read_phas
cvec_put_norm_channel = _aubiowrapper.cvec_put_norm_channel
cvec_put_phas_channel = _aubiowrapper.cvec_put_phas_channel
cvec_get_norm_channel = _aubiowrapper.cvec_get_norm_channel
cvec_get_phas_channel = _aubiowrapper.cvec_get_phas_channel
cvec_get_norm = _aubiowrapper.cvec_get_norm
cvec_get_phas = _aubiowrapper.cvec_get_phas
new_aubio_sndfile_ro = _aubiowrapper.new_aubio_sndfile_ro
new_aubio_sndfile_wo = _aubiowrapper.new_aubio_sndfile_wo
aubio_sndfile_info = _aubiowrapper.aubio_sndfile_info
aubio_sndfile_write = _aubiowrapper.aubio_sndfile_write
aubio_sndfile_read = _aubiowrapper.aubio_sndfile_read
del_aubio_sndfile = _aubiowrapper.del_aubio_sndfile
aubio_sndfile_channels = _aubiowrapper.aubio_sndfile_channels
aubio_sndfile_samplerate = _aubiowrapper.aubio_sndfile_samplerate
aubio_fft_getnorm = _aubiowrapper.aubio_fft_getnorm
aubio_fft_getphas = _aubiowrapper.aubio_fft_getphas
new_aubio_mfft = _aubiowrapper.new_aubio_mfft
aubio_mfft_do = _aubiowrapper.aubio_mfft_do
aubio_mfft_rdo = _aubiowrapper.aubio_mfft_rdo
del_aubio_mfft = _aubiowrapper.del_aubio_mfft
new_aubio_filter = _aubiowrapper.new_aubio_filter
new_aubio_adsgn_filter = _aubiowrapper.new_aubio_adsgn_filter
new_aubio_cdsgn_filter = _aubiowrapper.new_aubio_cdsgn_filter
aubio_filter_do = _aubiowrapper.aubio_filter_do
aubio_filter_do_outplace = _aubiowrapper.aubio_filter_do_outplace
aubio_filter_do_filtfilt = _aubiowrapper.aubio_filter_do_filtfilt
new_aubio_biquad = _aubiowrapper.new_aubio_biquad
aubio_biquad_do = _aubiowrapper.aubio_biquad_do
aubio_biquad_do_filtfilt = _aubiowrapper.aubio_biquad_do_filtfilt
new_aubio_hist = _aubiowrapper.new_aubio_hist
del_aubio_hist = _aubiowrapper.del_aubio_hist
aubio_hist_do = _aubiowrapper.aubio_hist_do
aubio_hist_do_notnull = _aubiowrapper.aubio_hist_do_notnull
aubio_hist_dyn_notnull = _aubiowrapper.aubio_hist_dyn_notnull
aubio_win_rectangle = _aubiowrapper.aubio_win_rectangle
aubio_win_hamming = _aubiowrapper.aubio_win_hamming
aubio_win_hanning = _aubiowrapper.aubio_win_hanning
aubio_win_hanningz = _aubiowrapper.aubio_win_hanningz
aubio_win_blackman = _aubiowrapper.aubio_win_blackman
aubio_win_blackman_harris = _aubiowrapper.aubio_win_blackman_harris
aubio_win_gaussian = _aubiowrapper.aubio_win_gaussian
aubio_win_welch = _aubiowrapper.aubio_win_welch
aubio_win_parzen = _aubiowrapper.aubio_win_parzen
aubio_window = _aubiowrapper.aubio_window
aubio_unwrap2pi = _aubiowrapper.aubio_unwrap2pi
vec_mean = _aubiowrapper.vec_mean
vec_max = _aubiowrapper.vec_max
vec_min = _aubiowrapper.vec_min
vec_min_elem = _aubiowrapper.vec_min_elem
vec_max_elem = _aubiowrapper.vec_max_elem
vec_shift = _aubiowrapper.vec_shift
vec_sum = _aubiowrapper.vec_sum
vec_local_energy = _aubiowrapper.vec_local_energy
vec_local_hfc = _aubiowrapper.vec_local_hfc
vec_alpha_norm = _aubiowrapper.vec_alpha_norm
vec_dc_removal = _aubiowrapper.vec_dc_removal
vec_alpha_normalise = _aubiowrapper.vec_alpha_normalise
vec_add = _aubiowrapper.vec_add
vec_adapt_thres = _aubiowrapper.vec_adapt_thres
vec_moving_thres = _aubiowrapper.vec_moving_thres
vec_median = _aubiowrapper.vec_median
vec_quadint = _aubiowrapper.vec_quadint
aubio_quadfrac = _aubiowrapper.aubio_quadfrac
vec_peakpick = _aubiowrapper.vec_peakpick
aubio_bintomidi = _aubiowrapper.aubio_bintomidi
aubio_miditobin = _aubiowrapper.aubio_miditobin
aubio_bintofreq = _aubiowrapper.aubio_bintofreq
aubio_freqtobin = _aubiowrapper.aubio_freqtobin
aubio_freqtomidi = _aubiowrapper.aubio_freqtomidi
aubio_miditofreq = _aubiowrapper.aubio_miditofreq
aubio_silence_detection = _aubiowrapper.aubio_silence_detection
aubio_level_detection = _aubiowrapper.aubio_level_detection
aubio_autocorr = _aubiowrapper.aubio_autocorr
new_aubio_scale = _aubiowrapper.new_aubio_scale
aubio_scale_set = _aubiowrapper.aubio_scale_set
aubio_scale_do = _aubiowrapper.aubio_scale_do
del_aubio_scale = _aubiowrapper.del_aubio_scale
new_aubio_resampler = _aubiowrapper.new_aubio_resampler
aubio_resampler_process = _aubiowrapper.aubio_resampler_process
del_aubio_resampler = _aubiowrapper.del_aubio_resampler
aubio_onset_energy = _aubiowrapper.aubio_onset_energy
aubio_onset_specdiff = _aubiowrapper.aubio_onset_specdiff
aubio_onset_hfc = _aubiowrapper.aubio_onset_hfc
aubio_onset_complex = _aubiowrapper.aubio_onset_complex
aubio_onset_phase = _aubiowrapper.aubio_onset_phase
aubio_onset_kl = _aubiowrapper.aubio_onset_kl
aubio_onset_mkl = _aubiowrapper.aubio_onset_mkl
new_aubio_onsetdetection = _aubiowrapper.new_aubio_onsetdetection
aubio_onsetdetection = _aubiowrapper.aubio_onsetdetection
aubio_onsetdetection_free = _aubiowrapper.aubio_onsetdetection_free
aubio_onsetdetection_energy = _aubiowrapper.aubio_onsetdetection_energy
aubio_onsetdetection_hfc = _aubiowrapper.aubio_onsetdetection_hfc
aubio_onsetdetection_complex = _aubiowrapper.aubio_onsetdetection_complex
aubio_onsetdetection_phase = _aubiowrapper.aubio_onsetdetection_phase
aubio_onsetdetection_specdiff = _aubiowrapper.aubio_onsetdetection_specdiff
aubio_onsetdetection_kl = _aubiowrapper.aubio_onsetdetection_kl
aubio_onsetdetection_mkl = _aubiowrapper.aubio_onsetdetection_mkl
new_aubio_pvoc = _aubiowrapper.new_aubio_pvoc
del_aubio_pvoc = _aubiowrapper.del_aubio_pvoc
aubio_pvoc_do = _aubiowrapper.aubio_pvoc_do
aubio_pvoc_rdo = _aubiowrapper.aubio_pvoc_rdo
aubio_pitch_yin = _aubiowrapper.aubio_pitch_yin
aubio_pitch_mcomb = _aubiowrapper.aubio_pitch_mcomb
aubio_pitch_schmitt = _aubiowrapper.aubio_pitch_schmitt
aubio_pitch_fcomb = _aubiowrapper.aubio_pitch_fcomb
aubio_pitch_yinfft = _aubiowrapper.aubio_pitch_yinfft
aubio_pitchm_freq = _aubiowrapper.aubio_pitchm_freq
aubio_pitchm_midi = _aubiowrapper.aubio_pitchm_midi
aubio_pitchm_cent = _aubiowrapper.aubio_pitchm_cent
aubio_pitchm_bin = _aubiowrapper.aubio_pitchm_bin
aubio_pitchdetection = _aubiowrapper.aubio_pitchdetection
aubio_pitchdetection_set_yinthresh = _aubiowrapper.aubio_pitchdetection_set_yinthresh
del_aubio_pitchdetection = _aubiowrapper.del_aubio_pitchdetection
new_aubio_pitchdetection = _aubiowrapper.new_aubio_pitchdetection
new_aubio_pitchmcomb = _aubiowrapper.new_aubio_pitchmcomb
aubio_pitchmcomb_detect = _aubiowrapper.aubio_pitchmcomb_detect
aubio_pitch_cands = _aubiowrapper.aubio_pitch_cands
del_aubio_pitchmcomb = _aubiowrapper.del_aubio_pitchmcomb
aubio_pitchyin_diff = _aubiowrapper.aubio_pitchyin_diff
aubio_pitchyin_getcum = _aubiowrapper.aubio_pitchyin_getcum
aubio_pitchyin_getpitch = _aubiowrapper.aubio_pitchyin_getpitch
aubio_pitchyin_getpitchfast = _aubiowrapper.aubio_pitchyin_getpitchfast
new_aubio_pitchschmitt = _aubiowrapper.new_aubio_pitchschmitt
aubio_pitchschmitt_detect = _aubiowrapper.aubio_pitchschmitt_detect
del_aubio_pitchschmitt = _aubiowrapper.del_aubio_pitchschmitt
new_aubio_pitchfcomb = _aubiowrapper.new_aubio_pitchfcomb
aubio_pitchfcomb_detect = _aubiowrapper.aubio_pitchfcomb_detect
del_aubio_pitchfcomb = _aubiowrapper.del_aubio_pitchfcomb
new_aubio_peakpicker = _aubiowrapper.new_aubio_peakpicker
aubio_peakpick_pimrt = _aubiowrapper.aubio_peakpick_pimrt
aubio_peakpick_pimrt_getval = _aubiowrapper.aubio_peakpick_pimrt_getval
aubio_peakpick_pimrt_wt = _aubiowrapper.aubio_peakpick_pimrt_wt
del_aubio_peakpicker = _aubiowrapper.del_aubio_peakpicker
new_aubio_tss = _aubiowrapper.new_aubio_tss
del_aubio_tss = _aubiowrapper.del_aubio_tss
aubio_tss_do = _aubiowrapper.aubio_tss_do
new_aubio_beattracking = _aubiowrapper.new_aubio_beattracking
aubio_beattracking_do = _aubiowrapper.aubio_beattracking_do
del_aubio_beattracking = _aubiowrapper.del_aubio_beattracking
NOTE_OFF = _aubiowrapper.NOTE_OFF
NOTE_ON = _aubiowrapper.NOTE_ON
KEY_PRESSURE = _aubiowrapper.KEY_PRESSURE
CONTROL_CHANGE = _aubiowrapper.CONTROL_CHANGE
PROGRAM_CHANGE = _aubiowrapper.PROGRAM_CHANGE
CHANNEL_PRESSURE = _aubiowrapper.CHANNEL_PRESSURE
PITCH_BEND = _aubiowrapper.PITCH_BEND
MIDI_SYSEX = _aubiowrapper.MIDI_SYSEX
MIDI_TIME_CODE = _aubiowrapper.MIDI_TIME_CODE
MIDI_SONG_POSITION = _aubiowrapper.MIDI_SONG_POSITION
MIDI_SONG_SELECT = _aubiowrapper.MIDI_SONG_SELECT
MIDI_TUNE_REQUEST = _aubiowrapper.MIDI_TUNE_REQUEST
MIDI_EOX = _aubiowrapper.MIDI_EOX
MIDI_SYNC = _aubiowrapper.MIDI_SYNC
MIDI_TICK = _aubiowrapper.MIDI_TICK
MIDI_START = _aubiowrapper.MIDI_START
MIDI_CONTINUE = _aubiowrapper.MIDI_CONTINUE
MIDI_STOP = _aubiowrapper.MIDI_STOP
MIDI_ACTIVE_SENSING = _aubiowrapper.MIDI_ACTIVE_SENSING
MIDI_SYSTEM_RESET = _aubiowrapper.MIDI_SYSTEM_RESET
MIDI_META_EVENT = _aubiowrapper.MIDI_META_EVENT
BANK_SELECT_MSB = _aubiowrapper.BANK_SELECT_MSB
MODULATION_MSB = _aubiowrapper.MODULATION_MSB
BREATH_MSB = _aubiowrapper.BREATH_MSB
FOOT_MSB = _aubiowrapper.FOOT_MSB
PORTAMENTO_TIME_MSB = _aubiowrapper.PORTAMENTO_TIME_MSB
DATA_ENTRY_MSB = _aubiowrapper.DATA_ENTRY_MSB
VOLUME_MSB = _aubiowrapper.VOLUME_MSB
BALANCE_MSB = _aubiowrapper.BALANCE_MSB
PAN_MSB = _aubiowrapper.PAN_MSB
EXPRESSION_MSB = _aubiowrapper.EXPRESSION_MSB
EFFECTS1_MSB = _aubiowrapper.EFFECTS1_MSB
EFFECTS2_MSB = _aubiowrapper.EFFECTS2_MSB
GPC1_MSB = _aubiowrapper.GPC1_MSB
GPC2_MSB = _aubiowrapper.GPC2_MSB
GPC3_MSB = _aubiowrapper.GPC3_MSB
GPC4_MSB = _aubiowrapper.GPC4_MSB
BANK_SELECT_LSB = _aubiowrapper.BANK_SELECT_LSB
MODULATION_WHEEL_LSB = _aubiowrapper.MODULATION_WHEEL_LSB
BREATH_LSB = _aubiowrapper.BREATH_LSB
FOOT_LSB = _aubiowrapper.FOOT_LSB
PORTAMENTO_TIME_LSB = _aubiowrapper.PORTAMENTO_TIME_LSB
DATA_ENTRY_LSB = _aubiowrapper.DATA_ENTRY_LSB
VOLUME_LSB = _aubiowrapper.VOLUME_LSB
BALANCE_LSB = _aubiowrapper.BALANCE_LSB
PAN_LSB = _aubiowrapper.PAN_LSB
EXPRESSION_LSB = _aubiowrapper.EXPRESSION_LSB
EFFECTS1_LSB = _aubiowrapper.EFFECTS1_LSB
EFFECTS2_LSB = _aubiowrapper.EFFECTS2_LSB
GPC1_LSB = _aubiowrapper.GPC1_LSB
GPC2_LSB = _aubiowrapper.GPC2_LSB
GPC3_LSB = _aubiowrapper.GPC3_LSB
GPC4_LSB = _aubiowrapper.GPC4_LSB
SUSTAIN_SWITCH = _aubiowrapper.SUSTAIN_SWITCH
PORTAMENTO_SWITCH = _aubiowrapper.PORTAMENTO_SWITCH
SOSTENUTO_SWITCH = _aubiowrapper.SOSTENUTO_SWITCH
SOFT_PEDAL_SWITCH = _aubiowrapper.SOFT_PEDAL_SWITCH
LEGATO_SWITCH = _aubiowrapper.LEGATO_SWITCH
HOLD2_SWITCH = _aubiowrapper.HOLD2_SWITCH
SOUND_CTRL1 = _aubiowrapper.SOUND_CTRL1
SOUND_CTRL2 = _aubiowrapper.SOUND_CTRL2
SOUND_CTRL3 = _aubiowrapper.SOUND_CTRL3
SOUND_CTRL4 = _aubiowrapper.SOUND_CTRL4
SOUND_CTRL5 = _aubiowrapper.SOUND_CTRL5
SOUND_CTRL6 = _aubiowrapper.SOUND_CTRL6
SOUND_CTRL7 = _aubiowrapper.SOUND_CTRL7
SOUND_CTRL8 = _aubiowrapper.SOUND_CTRL8
SOUND_CTRL9 = _aubiowrapper.SOUND_CTRL9
SOUND_CTRL10 = _aubiowrapper.SOUND_CTRL10
GPC5 = _aubiowrapper.GPC5
GPC6 = _aubiowrapper.GPC6
GPC7 = _aubiowrapper.GPC7
GPC8 = _aubiowrapper.GPC8
PORTAMENTO_CTRL = _aubiowrapper.PORTAMENTO_CTRL
EFFECTS_DEPTH1 = _aubiowrapper.EFFECTS_DEPTH1
EFFECTS_DEPTH2 = _aubiowrapper.EFFECTS_DEPTH2
EFFECTS_DEPTH3 = _aubiowrapper.EFFECTS_DEPTH3
EFFECTS_DEPTH4 = _aubiowrapper.EFFECTS_DEPTH4
EFFECTS_DEPTH5 = _aubiowrapper.EFFECTS_DEPTH5
DATA_ENTRY_INCR = _aubiowrapper.DATA_ENTRY_INCR
DATA_ENTRY_DECR = _aubiowrapper.DATA_ENTRY_DECR
NRPN_LSB = _aubiowrapper.NRPN_LSB
NRPN_MSB = _aubiowrapper.NRPN_MSB
RPN_LSB = _aubiowrapper.RPN_LSB
RPN_MSB = _aubiowrapper.RPN_MSB
ALL_SOUND_OFF = _aubiowrapper.ALL_SOUND_OFF
ALL_CTRL_OFF = _aubiowrapper.ALL_CTRL_OFF
LOCAL_CONTROL = _aubiowrapper.LOCAL_CONTROL
ALL_NOTES_OFF = _aubiowrapper.ALL_NOTES_OFF
OMNI_OFF = _aubiowrapper.OMNI_OFF
OMNI_ON = _aubiowrapper.OMNI_ON
POLY_OFF = _aubiowrapper.POLY_OFF
POLY_ON = _aubiowrapper.POLY_ON
MIDI_COPYRIGHT = _aubiowrapper.MIDI_COPYRIGHT
MIDI_TRACK_NAME = _aubiowrapper.MIDI_TRACK_NAME
MIDI_INST_NAME = _aubiowrapper.MIDI_INST_NAME
MIDI_LYRIC = _aubiowrapper.MIDI_LYRIC
MIDI_MARKER = _aubiowrapper.MIDI_MARKER
MIDI_CUE_POINT = _aubiowrapper.MIDI_CUE_POINT
MIDI_EOT = _aubiowrapper.MIDI_EOT
MIDI_SET_TEMPO = _aubiowrapper.MIDI_SET_TEMPO
MIDI_SMPTE_OFFSET = _aubiowrapper.MIDI_SMPTE_OFFSET
MIDI_TIME_SIGNATURE = _aubiowrapper.MIDI_TIME_SIGNATURE
MIDI_KEY_SIGNATURE = _aubiowrapper.MIDI_KEY_SIGNATURE
MIDI_SEQUENCER_EVENT = _aubiowrapper.MIDI_SEQUENCER_EVENT
AUBIO_MIDI_PLAYER_READY = _aubiowrapper.AUBIO_MIDI_PLAYER_READY
AUBIO_MIDI_PLAYER_PLAYING = _aubiowrapper.AUBIO_MIDI_PLAYER_PLAYING
AUBIO_MIDI_PLAYER_DONE = _aubiowrapper.AUBIO_MIDI_PLAYER_DONE
AUBIO_MIDI_READY = _aubiowrapper.AUBIO_MIDI_READY
AUBIO_MIDI_LISTENING = _aubiowrapper.AUBIO_MIDI_LISTENING
AUBIO_MIDI_DONE = _aubiowrapper.AUBIO_MIDI_DONE
new_aubio_midi_event = _aubiowrapper.new_aubio_midi_event
del_aubio_midi_event = _aubiowrapper.del_aubio_midi_event
aubio_midi_event_set_type = _aubiowrapper.aubio_midi_event_set_type
aubio_midi_event_get_type = _aubiowrapper.aubio_midi_event_get_type
aubio_midi_event_set_channel = _aubiowrapper.aubio_midi_event_set_channel
aubio_midi_event_get_channel = _aubiowrapper.aubio_midi_event_get_channel
aubio_midi_event_get_key = _aubiowrapper.aubio_midi_event_get_key
aubio_midi_event_set_key = _aubiowrapper.aubio_midi_event_set_key
aubio_midi_event_get_velocity = _aubiowrapper.aubio_midi_event_get_velocity
aubio_midi_event_set_velocity = _aubiowrapper.aubio_midi_event_set_velocity
aubio_midi_event_get_control = _aubiowrapper.aubio_midi_event_get_control
aubio_midi_event_set_control = _aubiowrapper.aubio_midi_event_set_control
aubio_midi_event_get_value = _aubiowrapper.aubio_midi_event_get_value
aubio_midi_event_set_value = _aubiowrapper.aubio_midi_event_set_value
aubio_midi_event_get_program = _aubiowrapper.aubio_midi_event_get_program
aubio_midi_event_set_program = _aubiowrapper.aubio_midi_event_set_program
aubio_midi_event_get_pitch = _aubiowrapper.aubio_midi_event_get_pitch
aubio_midi_event_set_pitch = _aubiowrapper.aubio_midi_event_set_pitch
aubio_midi_event_length = _aubiowrapper.aubio_midi_event_length
new_aubio_track = _aubiowrapper.new_aubio_track
del_aubio_track = _aubiowrapper.del_aubio_track
aubio_track_set_name = _aubiowrapper.aubio_track_set_name
aubio_track_get_name = _aubiowrapper.aubio_track_get_name
aubio_track_add_event = _aubiowrapper.aubio_track_add_event
aubio_track_first_event = _aubiowrapper.aubio_track_first_event
aubio_track_next_event = _aubiowrapper.aubio_track_next_event
aubio_track_get_duration = _aubiowrapper.aubio_track_get_duration
aubio_track_reset = _aubiowrapper.aubio_track_reset
aubio_track_count_events = _aubiowrapper.aubio_track_count_events
new_aubio_midi_player = _aubiowrapper.new_aubio_midi_player
del_aubio_midi_player = _aubiowrapper.del_aubio_midi_player
aubio_midi_player_reset = _aubiowrapper.aubio_midi_player_reset
aubio_midi_player_add_track = _aubiowrapper.aubio_midi_player_add_track
aubio_midi_player_count_tracks = _aubiowrapper.aubio_midi_player_count_tracks
aubio_midi_player_get_track = _aubiowrapper.aubio_midi_player_get_track
aubio_midi_player_add = _aubiowrapper.aubio_midi_player_add
aubio_midi_player_load = _aubiowrapper.aubio_midi_player_load
aubio_midi_player_callback = _aubiowrapper.aubio_midi_player_callback
aubio_midi_player_play = _aubiowrapper.aubio_midi_player_play
aubio_midi_player_play_offline = _aubiowrapper.aubio_midi_player_play_offline
aubio_midi_player_stop = _aubiowrapper.aubio_midi_player_stop
aubio_midi_player_set_loop = _aubiowrapper.aubio_midi_player_set_loop
aubio_midi_player_set_midi_tempo = _aubiowrapper.aubio_midi_player_set_midi_tempo
aubio_midi_player_set_bpm = _aubiowrapper.aubio_midi_player_set_bpm
aubio_midi_player_join = _aubiowrapper.aubio_midi_player_join
aubio_track_send_events = _aubiowrapper.aubio_track_send_events
aubio_midi_send_event = _aubiowrapper.aubio_midi_send_event
new_aubio_midi_parser = _aubiowrapper.new_aubio_midi_parser
del_aubio_midi_parser = _aubiowrapper.del_aubio_midi_parser
aubio_midi_parser_parse = _aubiowrapper.aubio_midi_parser_parse
new_aubio_midi_file = _aubiowrapper.new_aubio_midi_file
del_aubio_midi_file = _aubiowrapper.del_aubio_midi_file
aubio_midi_file_read_mthd = _aubiowrapper.aubio_midi_file_read_mthd
aubio_midi_file_load_tracks = _aubiowrapper.aubio_midi_file_load_tracks
aubio_midi_file_read_track = _aubiowrapper.aubio_midi_file_read_track
aubio_midi_file_read_event = _aubiowrapper.aubio_midi_file_read_event
aubio_midi_file_read_varlen = _aubiowrapper.aubio_midi_file_read_varlen
aubio_midi_file_getc = _aubiowrapper.aubio_midi_file_getc
aubio_midi_file_push = _aubiowrapper.aubio_midi_file_push
aubio_midi_file_read = _aubiowrapper.aubio_midi_file_read
aubio_midi_file_skip = _aubiowrapper.aubio_midi_file_skip
aubio_midi_file_read_tracklen = _aubiowrapper.aubio_midi_file_read_tracklen
aubio_midi_file_eot = _aubiowrapper.aubio_midi_file_eot
aubio_midi_file_get_division = _aubiowrapper.aubio_midi_file_get_division
new_aubio_midi_driver = _aubiowrapper.new_aubio_midi_driver
del_aubio_midi_driver = _aubiowrapper.del_aubio_midi_driver
aubio_midi_driver_settings = _aubiowrapper.aubio_midi_driver_settings

