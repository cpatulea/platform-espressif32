# Like Meshtastic platformio-custom.py
# https://github.com/meshtastic/firmware/blob/develop/bin/platformio-custom.py

Import("projenv")
projenv.Append(
    CCFLAGS=["-DFLAG_FROM_EXTRA_SCRIPTS"],
)
