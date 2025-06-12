import pandas as pd
import numpy as np

textos = ['Agua mole em pedra dura, tanto bate até que fura', 'Quem não tem cão, caça com gato', 'Soneto de Fidelidade', 'Os lusiadas']

classes = ['ditado', 'ditado', 'poema', 'poema']

df = pd.DataFrame({'texto': textos, 'classe': classes})

print(df)