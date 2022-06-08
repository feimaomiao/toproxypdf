try:
    from .funcs import mainfunc as main
except ModuleNotFoundError:
    from funcs import mainfunc as main
