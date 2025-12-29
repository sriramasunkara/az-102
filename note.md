AI - 102

Exam Focus: concise study notes for core AI-102 domains — key concepts, Azure services, and common tasks.

1. Develop generative AI apps in Azure
- Key services: Azure OpenAI Service, Azure AI Studio, Azure Cognitive Services integration.
- Concepts: model selection (capabilities vs cost), prompt engineering, safety filters, output post-processing.
- Tasks: deploy/host models, integrate via REST/SDK, manage keys and endpoints, implement rate-limiting and retries.
- Best practices: chain-of-thought sparingly, use system/user prompts, validate outputs, log examples for model tuning.

2. Develop AI agents on Azure
- Key services: Azure AI Studio (agents), Orchestration with Azure Functions or WebJobs, Bot Framework for conversational flows.
- Concepts: tool use, action chaining, state management, memory strategies, agent security and access control.
- Tasks: design tools/actions, implement tool connectors (APIs, search, databases), manage conversational context.

3. Develop natural language solutions in Azure
- Key services: Azure Cognitive Services for Language, Text Analytics, Language Service (NER, sentiment, summarization), Azure OpenAI.
- Concepts: NER, intent classification, sentiment analysis, summarization, question answering, retrieval-augmented generation (RAG).
- Tasks: build pipelines for ingestion, index content (vector store), implement retriever + generator, evaluate with precision/recall and human review.

4. Develop computer vision solutions in Azure
- Key services: Azure Computer Vision, Custom Vision, Face, Video Analyzer, Cognitive Services Containers for edge.
- Concepts: image classification, object detection, OCR, image/video analysis, model training vs custom models.
- Tasks: prepare datasets, train/customize models, deploy endpoints, handle scaling and latency, ensure privacy and consent.

5. Develop AI information extraction solutions in Azure
- Key services: Form Recognizer / Document Intelligence, Text Analytics for key-phrase extraction, OCR + custom models.
- Concepts: structured extraction, templates vs supervised models, confidence scores, data normalization.
- Tasks: label training data, configure extraction models, validate/parsing outputs, integrate into downstream workflows (databases, search).

Study tips
- Hands-on: build small end-to-end sample for each domain (ingest → process → serve).
- Security: learn authentication (managed identity, keys), data protection, and privacy controls.
- Monitoring: telemetry, metrics, and guarding against model drift and hallucinations.
- Resources: Azure docs, Microsoft Learn AI-102 learning path, practice labs, and sample repos.

Next steps: create flashcards and 2–3 practice labs (RAG Q&A, image classifier, form extractor).
