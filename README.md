# AI Language Learning Chatbot

An AI-powered chatbot designed to help users **learn English through conversation**.

The chatbot allows users to communicate naturally in written English while the AI silently corrects their **grammar, spelling, and punctuation mistakes** and continues the conversation.

## Working

The user chats with the AI normally. If the user's message contains mistakes, the chatbot:

1. Identifies grammar, spelling, and punctuation errors.
2. Rewrites the user's sentence correctly.
3. Continues the conversation naturally without explicitly pointing out the mistakes.

### Example

**User:**

> i goed to markey yesturday

**AI:**

> *I went to the market yesterday.*

> That sounds like a productive trip! What did you buy at the market?

The corrected sentence is shown to the user, but the AI does not explicitly say that the user made a mistake. This keeps the conversation natural while allowing the user to learn from the correction.

## Session Memory

The chatbot currently remembers what the user has talked about **within the current session**.

Cross-session memory is not implemented, hence the conversation context is lost once the user ends the session.

The grammar mistakes and their corrections are currently stored in a Python dictionary, for example:


{
    "goed": "went",
    "yesturday": "yesterday"
}


Forlarge user base, a proper SQL database would be efficient wihc can contain:

* User mistakes and corrected words
* Grammar error categories
* Session history
* Long term progress 

## Learning Progress

if the user stays inactive for a certain amount of time(1.5 hours) ,it automatically generates the summary :

the summary focuses on **areas where the user is struggling grammatically**.

For example, if the user repeatedly makes mistakes with verb tenses, the summary could identify:

> **Weak area: Tenses**

## Architecture

The basic flow of the application is:

```text
User
  ↓
Visual UI
  ↓
User Input (English Sentence)
  ↓
Prompt Builder
  ↓
AI API
  ↓
AI Generated Response
  ↓
Frontend UI
  ↓
Summary Generator
```

The architecture separates the major responsibilities of the application into different components.

## Design Principle

The project follows the **Single Responsibility Principle (SRP)**.

Each file/module is responsible for a specific task rather than handling multiple unrelated responsibilities.

This makes the project:

* Easier to understand
* Easier to debug
* Easier to maintain
* Easier to extend

## Current Technology

* **Language:** Python
* **AI Model:** GPT-4o mini
* **AI API:** OpenAI API
* **Current Storage:** Python dictionary
* **Future Storage:** SQL database

## Current Limitations

* Cross-session memory is not implemented.
* Grammar data is currently stored in memory rather than a persistent database.
* The system is currently designed for **English learning** only.
* Database-backed learning analytics are planned for future development.

## Future Improvements

Possible future improvements include:

* Persistent cross-session memory
* SQL database integration
* User-specific learning profiles
* Grammar progress tracking
* More detailed error categorization
* Personalized exercises based on recurring mistakes
* Support for additional languages
* Improved frontend experience
* summary generating button for anytime summary generation
