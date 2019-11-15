import cx_Freeze

executables = [cx_Freeze.Executable("Pong.py")]

cx_Freeze.setup(
    name="Pong",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["padelCollide.ogg","point.ogg","wallCollide.ogg"]}},
    executables = executables

    )