__version__ = "0.0.2"
__all__ = list(
    filter((lambda x: x),
           map((lambda x: x[:-3] if x[-3:] == '.py' else None),
               __import__('os').listdir())))
