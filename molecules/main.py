import moses
from rdkit import Chem
from rdkit.Chem import Draw
import numpy as np


train = moses.get_dataset('train')
test = moses.get_dataset('test')
dataset = np.hstack([train, test]) #sumar los dos arrays que tenemos
#test_scaffolds = moses.get_dataset('test_scaffolds')

print("Number of molecules to train: ", len(train), "Number of molecules to test: " , len(test))

smiles_train = train[0]



def image_molecule(smiles, title = "molecule.png"):
    mol_train = Chem.MolFromSmiles(smiles)
    Draw.MolToFile(mol_train, title)
    return title


molecule1 = image_molecule(smiles_train)

####Generative model####

print(smiles_train)

#crear Input --> [CCCS(=O)c1ccc2[nH]c(=NC(=O)OC)[nH]c2c1] --> [11123456..] X

one_sentece_of_smiles = "".join(dataset) #juntar todas las strings en una sola. tiene que ser lista de strings, sino falla
characters = set(one_sentece_of_smiles) #no es una lista pero se comporta como una lista
dict_char = { char:idx for idx, char in enumerate(characters) }

list_smile_numbers = []
for smile in dataset:
    numeric_smile = [ dict_char[letter] for letter in smile ]
    list_smile_numbers.append(numeric_smile)





numeric_smile = []
for letter in smile:
    numeric_smile.append(dict_char[letter])


# Outputs --> CCCS ---> CCS (input) --> ("S", 2) (output)




# 1) Todas training y test --> vocabulario: (lista de caracteres unicos) y assignamos un numero --> dictionario {"C":1, "S": 2}

# 2) Usando dictionario de antes cambiar strings por numeros CCC... --> 111...

#crear Output --> [tipoatom, posicion] --> [C, 1] --> [1, 1] Y

#modelo = Arquitecture.train(X, Y)

