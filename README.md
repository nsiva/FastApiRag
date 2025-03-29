# FastApiRag

FastApiRag is a FastAPI project designed to provide a robust and efficient API service.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Contributing](#contributing)
- [License](#license)

## Installation

To install and run this project locally, follow these steps:

1. Clone the repository:

    ```sh
    git clone https://github.com/nsiva/FastApiRag.git
    cd FastApiRag
    ```

2. Create a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

To start the FastAPI server, run:

```sh
uvicorn app.main:app --reload