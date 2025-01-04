from flask import Flask, request, render_template, jsonify, send_file
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import ollama
import pickle
import os
from datetime import datetime
from fpdf import FPDF

# Initialiser Flask
app = Flask(__name__)

# Modèle d'encodage
model = SentenceTransformer('all-MiniLM-L6-v2')

# Chemins des fichiers PDF
DOCUMENTS = {
    'code_travail': 'data/code_travail.pdf',
    'code_obligations_contrats': 'data/code_obligations_contrats.pdf',
    'code_penal': 'data/code_penal.pdf',
    'moudawana': 'data/moudawana.pdf',
    'procedure_penale': 'data/procedure_penale.pdf',
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

# Fonction pour charger un index
def load_index(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            data = pickle.load(f)
            return data['index'], data['sentences']
    return None, None

# Indexer tous les documents
for doc_name, pdf_path in DOCUMENTS.items():
    index_file = f'data/{doc_name}_index.pkl'
    if not os.path.exists(index_file):
        print(f"Indexation de {doc_name}...")
        text = extract_text_from_pdf(pdf_path)
        index, sentences = index_text(text, model)
        save_index(index, sentences, index_file)
        print(f"Index de {doc_name} sauvegardé dans {index_file}.")
    else:
        print(f"Index de {doc_name} déjà existant.")

# Fonction pour rechercher et générer une réponse
def search_and_answer(question, index, sentences, model, top_k=3):
    question_embedding = model.encode([question])
    distances, indices = index.search(question_embedding, top_k)
    relevant_sentences = [sentences[i] for i in indices[0]]
    context = "\n".join(relevant_sentences)
    response = ollama.generate(model='mistral', prompt=f"Contexte:\n{context}\n\nQuestion: {question}\nRéponse:")
    return response['response'], relevant_sentences

# Route pour la page d'accueil
@app.route('/')
def home():
    return render_template('index.html', documents=DOCUMENTS.keys())

# Route pour poser une question
@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question', '').strip()
    selected_doc = data.get('document', '').strip()
    
    if not question or not selected_doc:
        return jsonify({'error': 'Veuillez fournir une question et sélectionner un document.'}), 400
    
    if selected_doc not in DOCUMENTS:
        return jsonify({'error': 'Document invalide.'}), 400
    
    # Charger l'index du document sélectionné
    index, sentences = load_index(f'data/{selected_doc}_index.pkl')
    
    # Générer une réponse
    answer, relevant_articles = search_and_answer(question, index, sentences, model)
    return jsonify({'answer': answer, 'articles': relevant_articles})

# Route pour télécharger la conversation en PDF
@app.route('/download', methods=['POST'])
def download():
    data = request.json
    chat_history = data.get('history', [])
    
    # Créer un PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    for entry in chat_history:
        pdf.cell(200, 10, txt=f"Vous: {entry['question']}", ln=True)
        pdf.cell(200, 10, txt=f"Bot: {entry['answer']}", ln=True)
        pdf.cell(200, 10, txt="", ln=True)  # Espace entre les entrées
    
    pdf_path = "data/conversation.pdf"
    pdf.output(pdf_path)
    
    return send_file(pdf_path, as_attachment=True)

# Démarrer l'application Flask
if __name__ == '__main__':
    app.run(debug=True)