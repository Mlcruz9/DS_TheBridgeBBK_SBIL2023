import pickle
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
hola_mundo = pickle.load(open('data/hola_mundo.pkl', 'rb'))
print(hola_mundo)