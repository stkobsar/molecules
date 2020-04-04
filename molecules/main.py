import moses
from rdkit import Chem
from rdkit.Chem import Draw
import numpy as np
from tqdm import tqdm


train = moses.get_dataset('train')
test = moses.get_dataset('test')
dataset = np.hstack([train, test]) #sumar los dos arrays que tenemos
#test_scaffolds = moses.get_dataset('test_scaffolds')

print("Number of molecules to train: ", len(train), "Number of molecules to test: ", len(test))

smiles_train = train[0]



def image_molecule(smiles, title = "molecule.png"):
    mol_train = Chem.MolFromSmiles(smiles)
    Draw.MolToFile(mol_train, title)
    return title

def smiles_number_to_smiles_string(input_molecule, dict):
    smile_char = [dict_number_to_char[number] for number in smile ]
    smile_string = "".join(smile_char)
    return smile_string


molecule1 = image_molecule(smiles_train)

####Generative model####

print(smiles_train)

#crear Input --> [CCCS(=O)c1ccc2[nH]c(=NC(=O)OC)[nH]c2c1] --> [11123456..] X

one_sentece_of_smiles = "".join(dataset) #juntar todas las strings en una sola. tiene que ser lista de strings, sino falla
characters = set(one_sentece_of_smiles) #no es una lista pero se comporta como una lista
dict_char_to_number = { char:idx for idx, char in enumerate(characters) }
dict_number_to_char = { idx:char for idx, char in enumerate(characters) }

list_smile_numbers = []
for smile in dataset:
    numeric_smile = [dict_char_to_number[letter] for letter in smile ]
    list_smile_numbers.append(numeric_smile)


###TENEMOS: LIsta SMILES numerica


# Initial: CCCS --> --CCS  / [C,2]-- CCS - C, 2
# CCCCCSSO ..> 111111223 --> 1111123
## [21232321,




list_input = []
list_output = []
for smile in tqdm(list_smile_numbers):
    #for atom in enumerate(smile):
    mol = None
    while mol == None:
        idx = np.random.randint(0, len(smile))
        input_molecule = smile.copy() #.copy() es para crear una copia independiente de la original
        del input_molecule[idx]
        input_string = smiles_number_to_smiles_string(input_molecule, dict_number_to_char)
        mol = Chem.MolFromSmiles(input_string) #Si mol == None --> no valida si mol != None es valida
    list_input.append(input_string)
    list_output.append([smile[idx], idx]) #append para mas de un elemento en una misma lista.


np.save("input", list_input)
np.save("output", list_output)


if __name__ == "__main__:
#########
#   train, test = ...
##  create_input_output(train, test):
#   if not os.path.exists("input") and not os.path.exists("output"):
#       create_input_output(train, test)
#
#
#############


# Outputs --> CCCS ---> CCS (input) --> ("S", 2) (output)





