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

This will start the server at http://127.0.0.1:8000.

## Endpoints
Here are some of the main endpoints provided by this project:

GET /: Root endpoint
GET /items/{item_id}: Get an item by ID
POST /items/: Create a new item
Refer to the OpenAPI docs at http://127.0.0.1:8000/docs for a full list of endpoints and their details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.