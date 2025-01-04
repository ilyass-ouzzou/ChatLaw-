import PyPDF2
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle
import os

# Modèle d'encodage
model = SentenceTransformer('all-MiniLM-L6-v2')

# Chemins des fichiers PDF
DOCUMENTS = {
    'code_travail': r'C:\Users\pc\Desktop\ChatLaw\data\code de travail.pdf',
    'code_obligations_contrats': r'C:\Users\pc\Desktop\ChatLaw\data\Code des obligations et des contrats.pdf',
    'code_penal': r'C:\Users\pc\Desktop\ChatLaw\data\code_penal.pdf',
    'moudawana': r'C:\Users\pc\Desktop\ChatLaw\data\LA MOUDAWANA.pdf',
    'procedure_penale': r'C:\Users\pc\Desktop\ChatLaw\data\procédure pénale.pdf',
}

# Fonction pour extraire le texte du PDF
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text

# Fonction pour indexer le texte
def index_text(text, model):
    sentences = text.split('\n')
    sentence_embeddings = model.encode(sentences)
    dimension = sentence_embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(sentence_embeddings)
    return index, sentences

# Fonction pour sauvegarder l'index
def save_index(index, sentences, file_path):
    with open(file_path, 'wb') as f:
        pickle.dump({'index': index, 'sentences': sentences}, f)

# Indexer tous les documents
for doc_name, pdf_path in DOCUMENTS.items():
    index_file = f'{doc_name}_index.pkl'
    if not os.path.exists(index_file):
        print(f"Indexation de {doc_name}...")
        text = extract_text_from_pdf(pdf_path)
        index, sentences = index_text(text, model)
        save_index(index, sentences, index_file)
        print(f"Index de {doc_name} sauvegardé dans {index_file}.")
    else:
        print(f"Index de {doc_name} déjà existant.")