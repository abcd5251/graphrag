# GraphRAG testing

## File Requirements
- File type: `.txt` only

## Execution Steps
### 1. Install Dependency
```bash

```

### 1. Initial Structure
No API key required for this step.
```bash
python -m graphrag.index --init --root ./ragtest
```

### 2. Set Your OpenAI API Key and Settings
Configure your settings.yaml with parameters like chunk size, model, embedding, etc.

### 3. Embedding
```bash
python -m graphrag.index --root ./ragtest
```
After Embedding, output will be saved in ragtest/output

### 4. Ask question
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


