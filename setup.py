from cx_Freeze import setup, Executable

setup(
    name = "SSH-Client",
    version = "0.1",
    description = "Windows SSH client",
    executables = [Executable("start.py")]
)