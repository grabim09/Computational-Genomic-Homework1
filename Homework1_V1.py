#!/usr/bin/env python
# coding: utf-8

# In[1]:


#All Necessary Library
import streamlit as st
import numpy as np
import pandas as pd
import random as rand


# In[14]:


Genetic_Code = {
    0: {
        "Amino Acid": "Isoleucine",
        "Single_Letter": "I",
        "3-Letter Code": "Iso",
        "Codon": ['ATT', 'ATC', 'ATA']
    },
    1: {
        "Amino Acid": "Leucine",
        "Single_Letter": "L",
        "3-Letter Code": "Leu",
        "Codon": ['CTT', 'CTC', 'CTA', 'CTG', 'TTA', 'TTG']
    },
    2: {
        "Amino Acid": "Valine",
        "Single_Letter": "V",
        "3-Letter Code": "Val",
        "Codon": ['GTT', 'GTC', 'GTA', 'GTG']
    },
    3: {
        "Amino Acid": "Phenylalanine",
        "Single_Letter": "F",
        "3-Letter Code": "Phe",
        "Codon": ['TTT', 'TTC']
    },
    4: {
        "Amino Acid": "Methionine",
        "Single_Letter": "M",
        "3-Letter Code": "Met (Start)",
        "Codon": ['ATG']
    },
    5: {
        "Amino Acid": "Cysteine",
        "Single_Letter": "C",
        "3-Letter Code": "Cys",
        "Codon": ['TGT', 'TGC']
    },
    6: {
        "Amino Acid": "Alanine",
        "Single_Letter": "A",
        "3-Letter Code": "Ala",
        "Codon": ['GCT', 'GCC', 'GCA', 'GCG']
    },
    7: {
        "Amino Acid": "Glycine",
        "Single_Letter": "G",
        "3-Letter Code": "Gly",
        "Codon": ['GGT', 'GGC', 'GGA', 'GGG']
    },
    8: {
        "Amino Acid": "Proline",
        "Single_Letter": "P",
        "3-Letter Code": "Pro",
        "Codon": ['CCT', 'CCC', 'CCA', 'CCG']
    },
    9: {
        "Amino Acid": "Threonine",
        "Single_Letter": "T",
        "3-Letter Code": "Thr",
        "Codon": ['ACT', 'ACC', 'ACA', 'ACG']
    },
    10: {
        "Amino Acid": "Serine",
        "Single_Letter": "S",
        "3-Letter Code": "Ser",
        "Codon": ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC']
    },
    11: {
        "Amino Acid": "Tyrosine",
        "Single_Letter": "Y",
        "3-Letter Code": "Tyr",
        "Codon": ['TAT', 'TAC']
    },
    12: {
        "Amino Acid": "Tryptophan",
        "Single_Letter": "V",
        "3-Letter Code": "Trp",
        "Codon": ['TGG']
    },
    13: {
        "Amino Acid": "Glutamine",
        "Single_Letter": "Q",
        "3-Letter Code": "Glu",
        "Codon": ['CAA', 'CAG']
    },
    14: {
        "Amino Acid": "Asparagine",
        "Single_Letter": "N",
        "3-Letter Code": "Asn",
        "Codon": ['AAT', 'AAC']
    },
    15: {
        "Amino Acid": "Histidine",
        "Single_Letter": "H",
        "3-Letter Code": "His",
        "Codon": ['CAT', 'CAC']
    },
    16: {
        "Amino Acid": "Glutamic Acid",
        "Single_Letter": "E",
        "3-Letter Code": "Glu",
        "Codon": ['GAA', 'GAG']
    },
    17: {
        "Amino Acid": "Aspartic Acid",
        "Single_Letter": "D",
        "3-Letter Code": "Asp",
        "Codon": ['GAT', 'GAC']
    },
    18: {
        "Amino Acid": "Lysine",
        "Single_Letter": "K",
        "3-Letter Code": "Lys",
        "Codon": ['AAA', 'AAG']
    },
    19: {
        "Amino Acid": "Arginine",
        "Single_Letter": "R",
        "3-Letter Code": "Arg",
        "Codon": ['CGT', 'CGC', 'CGA', 'AGA', 'AGG']
    },
    20: {
        "Amino Acid": "Stop Codon",
        "Single_Letter": "Stop",
        "3-Letter Code": "Termination",
        "Codon": ['TAA', 'TAG', 'TGA']
    }
}


# In[15]:


GC = pd.DataFrame(Genetic_Code).T


# ## Soal 1

# In[2]:


Nucleic_Acid = {"DNA","RNA"}


# In[3]:


Nitrogen_Base = {
    "Purines": {
        "Adenine",
        "Guanine"
    },
    "Pyrimidines": {
        "Cytosine",
        "Thymine",
        "Uracile"
    }
}


# In[4]:


Nucleic_Acid_Nitrogen_Base = {
    "DNA":{
        "Purines": Nitrogen_Base["Purines"],
        "Pyrimidines": Nitrogen_Base["Pyrimidines"] - {'Uracile'},
        "Nitrogen Base Name": Nitrogen_Base["Purines"] | (Nitrogen_Base["Pyrimidines"] - {'Uracile'}),
        "Nitrogen Base Code": set()
    },
    "RNA":{
        "Purines": Nitrogen_Base["Purines"],
        "Pyrimidines": Nitrogen_Base["Pyrimidines"] - {'Thymine'},
        "Nitrogen Base Name": Nitrogen_Base["Purines"] | (Nitrogen_Base["Pyrimidines"] - {'Thymine'}),
        "Nitrogen Base Code": set()
    }
}
for code in Nucleic_Acid_Nitrogen_Base["DNA"]["Nitrogen Base Name"]:
    Nucleic_Acid_Nitrogen_Base["DNA"]["Nitrogen Base Code"].add(code[0])
for code in Nucleic_Acid_Nitrogen_Base["RNA"]["Nitrogen Base Name"]:
    Nucleic_Acid_Nitrogen_Base["RNA"]["Nitrogen Base Code"].add(code[0])


# In[5]:


def nitrogen_base1(molecule):
    mol = Nucleic_Acid_Nitrogen_Base.get(molecule)
#     print('Molecule Type: ' + molecule)
#     print('Purines: ' + ', '.join(sorted(mol.get("Purines"))))
#     print('Pyrimidines: ' + ', '.join(sorted(mol.get("Pyrimidines"))))
#     print('Nitrogen Base Name: ' + ', '.join(sorted(mol.get("Nitrogen Base Name"))))
#     print('Nitrogen Base Code: ' + ', '.join(sorted(mol.get("Nitrogen Base Code"))))
    st.write('Molecule Type: ' + molecule)
    st.write('Purines: ' + ', '.join(sorted(mol.get("Purines"))))
    st.write('Pyrimidines: ' + ', '.join(sorted(mol.get("Pyrimidines"))))
    st.write('Nitrogen Base Name: ' + ', '.join(sorted(mol.get("Nitrogen Base Name"))))
    st.write('Nitrogen Base Code: ' + ', '.join(sorted(mol.get("Nitrogen Base Code"))))


# In[6]:


def nitrogen_base2(molecule):
    Purines = Nitrogen_Base["Purines"]
    Pur = Purines
    Pyrimidines = Nitrogen_Base["Pyrimidines"]
    if molecule == 'DNA':
        Pyr = Pyrimidines - {'Uracile'}
    elif molecule == 'RNA':
        Pyr = Pyrimidines - {'Thymine'}
    NBF = Pur | Pyr
    NBC = set()
    for code in NBF:
        NBC.add(code[0])
#     print('Molecule Type: ' + molecule)
#     print('Purines: ' + str(Pur))
#     print('Pyrimidines: ' + str(Pyr))
#     print('Nitrogen Base Name: ' + str(NBF))
#     print('Nitrogen Base Code: ' + str(NBC))
    st.write('Molecule Type: ' + molecule)
    st.write('Purines: ' + str(Pur))
    st.write('Pyrimidines: ' + str(Pyr))
    st.write('Nitrogen Base Name: ' + str(NBF))
    st.write('Nitrogen Base Code: ' + str(NBC))


# In[16]:


def generate_random_codon(molecule,length):
    code = list(Nucleic_Acid_Nitrogen_Base[molecule]["Nitrogen Base Code"])
    random_codon = ''.join(rand.choice(code) for i in range(length))
    st.write(random_codon)


# In[9]:


def main():
    st.title("07311940000046_Agra Bima Yuda_Genomics Computation_Homework 1")
    st.divider()
    acid = st.radio(
        "Select one nucleic acid below:",
        sorted(Nucleic_Acid),
        captions = ["Deoxyribonucleic Acid","Ribonucleic Acid"])
    st.write(acid)
    st.divider()
    st.header("Problem 1. Using concept of set and related commands in Programming Language, write a program to list the nitrogen base of DNA and RNA")
    st.subheader("Nitrogen base of selected Nucleic Acid")
    nitrogen_base1(acid)
    st.divider()
    st.header("Problem 2. Write a program that lists all the DNA and RNA sequences that encode a given protein sequences")
    sequences_count = st.number_input("Enter the number of sequences: ", min_value=3, step=3)
    st.write(sequences_count)
    st.subheader("Generated Random Codon")
    generate_random_codon(acid,sequences_count)
    
if __name__ == "__main__":
    main()


# In[19]:


code = list(Nucleic_Acid_Nitrogen_Base["DNA"]["Nitrogen Base Code"])
random_codon = ''.join(rand.choice(code) for i in range(9))
random_codon


# In[13]:


generate_random_codon("RNA",9)


# In[13]:


print(enumerate(GC.loc[:,'Codon']))


# In[14]:


print(list(enumerate(GC.loc[:,'Codon'])))


# In[15]:


for count, ele in enumerate(GC.loc[:,'Codon']):
    if 'GTT' in ele:
        print (count)
        break


# In[16]:


GC.loc[count]['Amino Acid']


# In[15]:


for count, ele in enumerate(GC.loc[:,'Codon']):
    print (count, ele)

