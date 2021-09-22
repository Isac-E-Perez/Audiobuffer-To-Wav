import os
import ffmpy

ff = ffmpy.FFmpeg(
    inputs={'Isac.m4a': None},
    outputs={'Isac.wav': None}
)

ff.run()
