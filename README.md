# Comparing OpenAI API and LangChain Integrations

This repository provides code examples of using both the OpenAI API directly and the LangChain wrapper to request a completion from an AI assistant. Here are the key differences observed:

## OpenAI API Directly

- It makes a **direct call** to OpenAI's `ChatCompletion` API
- It **returns the full JSON response** from OpenAI, allowing you to inspect fields like usage, tokens, and more.
- **A bit more complex** to use due to the need to format the prompt, handle API keys, etc.
- **Prints the full JSON response** for comprehensive inspection.

## LangChain

- It uses LangChain's `OpenAI` class to **wrap the OpenAI API**, simplifying the interface.
- It **just returns the generated text**, without the full response JSON.
- Provides a simpler `predict()` method to generate text, simplifying usage.
- Doesn't provide access to usage statistics or other metadata from the response.
- Primarily prints the generated text, providing less information than direct OpenAI API usage.

## Summary:

- **OpenAI direct** gives full control and visibility into the response, making it excellent for complex uses or in-depth inspection, albeit with a bit higher complexity.
- On the other hand, using **LangChain** simplifies the interaction and makes it much easier to integrate OpenAI into an application. However, it comes at the cost of less visibility into the response apart from the generated text.

This repository provides a code sample where a user can choose either approach via a simple terminal interface and check the respective output and estimated cost. This tool serves as a proof-of-concept for comparing the different methods of interaction with OpenAI's powerful language model, and it can act as a foundational point for more robust applications built on top of these services.