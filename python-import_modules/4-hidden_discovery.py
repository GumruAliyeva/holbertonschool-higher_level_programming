#!/usr/bin/python3
import importlib.util

if __name__ == "__main__":
    # .pyc faylının yolu
    file_path = "/tmp/hidden_4.pyc"
    
    # Modulun yükənməsi
    spec = importlib.util.spec_from_file_location("hidden_4", file_path)
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)
    
    # Modulun adlarını çıxartmaq
    names = dir(hidden_4)
    
    # __ ilə başlayanları çıxartmaq və sırala
    for name in sorted([n for n in names if not n.startswith("__")]):
        print(name)
