<div align="center">
  <a href="https://mseep.ai/app/adityanarayan001-gitmind-mcp">
    <img src="https://mseep.net/pr/adityanarayan001-gitmind-mcp-badge.png" alt="MseeP.ai Security Assessment Badge">
  </a>
</div>

# GitMind-MCP(Model Context Protocol) Server 🧠 📊

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

## How to Use

### Pre-requisites
- <b>Python</b>
- <b>GitHub account with a ```personal-access-token```</b>
- <b>Ollama</b>

1. Clone the repository:
   ```bash
   git clone https://github.com/AdityaNarayan001/GitMind-MCP.git
   ```
2. Install the ```requirements.txt```:
    ```bash
    pip install -r requirements.txt
    ```

### Server Side
The ```server``` directory contains the server-side implementation of the MCP layer. To run the server, follow these steps:
1. Move to server directory:
    ```bash
    cd GitMind-MCP/server
    ```
2. Start the server:
    ```bash
    python3 server.py
    ```
    or
    ```bash
    python server.py
    ```

### Client Side
The ```client``` directory contains the client-side implementation. To run the client, follow these steps:
1. Move to server directory:
    ```bash
    cd GitMind-MCP/client
    ```
2. Start the server:
    ```bash
    python3 client.py
    ```
    or
    ```bash
    python client.py
    ```
