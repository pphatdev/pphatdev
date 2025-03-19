# GitHub Status Readme

## Overview
This project provides a real-time update of your GitHub status. It interacts with the GitHub API to fetch and display the current status of a specified repository.

## Features
- Fetches the current status of a GitHub repository.
- Updates the status in real-time.
- Easy to configure and use.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/github-status-readme.git
   cd github-status-readme
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables by copying `.env.example` to `.env` and filling in the necessary values.

## Usage

To run the application, execute the following command:
```bash
python src/main.py
```

## Running Tests

To run the unit tests, use:
```bash
pytest tests/test_github_api.py
```

## Contributing

Feel free to submit issues and pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License. See the LICENSE file for details.