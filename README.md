# GitMind-MCP

## Overview

GitMind-MCP is an AI-powered middleware that connects an Ollama-based LLM with the GitHub API. It enables intelligent interaction with GitHub repositories by leveraging natural language understanding and automated API calls.

## How It Works

### Client (Ollama LLM)

1. Processes user queries and generates structured responses.

2. Sends requests to the MCP server for GitHub-related actions.

### Server (MCP Layer)

1. Receives queries from the LLM client.

2. Determines the necessary GitHub API calls.

3. Fetches and processes GitHub data.

4. Returns results to the client.