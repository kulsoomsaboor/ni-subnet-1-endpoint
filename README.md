# Bittensor Text-to-Text API | Subnet 1 | Text Prompting

This FastAPI application utilizes the Bittensor network to provide a decentralized API that allows validators to easily host an API for other services to prompt the Bittensor Subnet 1 network.

## Features

- **Conversational AI**: A Text-to-Text goal-driven behaviour to drive human-like conversations.


## Installation

Ensure you have Python 3.8+ installed on your system. To install the required dependencies, follow these steps:

Clone the repository:

   ```
   git clone https://github.com/kulsoomsaboor/ni-subnet-1-endpoint.git
   cd ni-subnet-1-endpoint
   ```
   Install the required Python packages:
   
```
pip install -r requirements.txt
```

Configure the necessary environment variables:

hotkey_mnemonic: Your Bittensor wallet mnemonic for authentication.
This can be set in your shell or included in an .env file.

Running the API
To run the FastAPI application aka your endpoint, use the following command from the directory that contains your main.py file:

```
uvicorn main:app --host 0.0.0.0 --port 8001
```
