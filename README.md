# GraphRAG testing

## File Requirements
- File type: `.txt` only

## Execution Steps
### 1. Install Dependency
```bash
pip install -r requirements.txt
```

### 2. Initial Structure (We use ragtest as folder name)
No API key required for this step.
```bash
python -m graphrag.index --init --root ./ragtest
```

### 3. Make input folder
```bash
mkdir ./ragtest/input
```

### 4. Put your file inside input folder (.txt only)
You can convert .pdf to .txt using convert.py, also calculate tokens

### 5. Set Your OpenAI API Key and Settings
Set your OpenAI APIkey in .env
```bash
GRAPHRAG_API_KEY=""
```
Also configure your settings.yaml with parameters like chunk size, model, embedding, etc.

### 6. Embedding
```bash
python -m graphrag.index --root ./ragtest
```
After Embedding, output will be saved in ragtest/output

### 7. Ask question
Global level
```bash
python -m graphrag.query --root ./ragtest --method global "your question"
```

Local level (Specific character or terminology)
```bash
python -m graphrag.query --root ./ragtest --method local "your question"
```

## Cost of Embedding
- Number of tokens in the txt file: 13,592
- Price: $1.62

# Cost of single query
- Price: $0.07


