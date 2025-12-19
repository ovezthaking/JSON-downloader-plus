# JSON Downloader Plus

A Python utility for downloading, managing, and uploading JSON data from and to REST APIs. This project specifically works with [JSONPlaceholder](https://jsonplaceholder.typicode.com/) as a data source, providing a simple interface to perform CRUD operations on posts.

## Features

- **Download Posts**: Fetch individual posts from JSONPlaceholder API
- **Save Data**: Save JSON data to local files with automatic timestamping
- **Read Files**: Load and parse JSON files
- **Upload Posts**: Submit JSON payloads to the API
- **Automatic Logging**: All operations are logged with timestamps
- **Error Handling**: Comprehensive error handling and validation
- **Docker Support**: Full Docker containerization for easy deployment

## Project Structure

```
JSON-downloader-plus/
├── main.py                    # Main application with core functions
├── tests/
│   └── test_main.py          # Unit tests using pytest
├── Dockerfile                 # Docker configuration
├── logs.txt                   # Automatic operation logs
├── post.json                  # Sample JSON payload
└── README.md                  # This file
```

## Installation

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Local Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/JSON-downloader-plus.git
cd JSON-downloader-plus
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

Required packages:
- `requests` - For HTTP requests to the API
- `pytest` - For running tests

## Usage

### Core Functions

#### 1. `get_post(index)`
Retrieves a single post from JSONPlaceholder API.

```python
from main import get_post

post = get_post(1)
print(post)  # Returns post with id=1
```

**Parameters:**
- `index` (int): The post ID to retrieve

**Returns:** Dictionary containing the post data or error message

---

#### 2. `save_file(filename, title='', body='')`
Saves a post to a local file with automatic timestamp suffix.

```python
from main import save_file

save_file('my_post', title='Hello World', body='This is my first post')
# Creates file: my_post_<timestamp>
```

**Parameters:**
- `filename` (str): Base name for the output file
- `title` (str, optional): Post title. If empty, user is prompted
- `body` (str, optional): Post content. If empty, user is prompted

---

#### 3. `save_json(filename, get_payload)`
Saves JSON data to a file with .json extension and timestamp.

```python
from main import save_json

data = {"title": "Test", "body": "Content", "userId": 1}
save_json('output', data)
# Creates file: output_<timestamp>.json
```

**Parameters:**
- `filename` (str): Base name for the output file
- `get_payload` (dict): Dictionary to save as JSON

---

#### 4. `read_file(filename)`
Reads and parses a JSON file.

```python
from main import read_file

content = read_file('post.json')
print(content)
```

**Parameters:**
- `filename` (str): Path to the JSON file

**Returns:** Parsed JSON data as dictionary or error message

---

#### 5. `upload_post(filename)`
Uploads JSON data from a file to the JSONPlaceholder API.

```python
from main import upload_post

response = upload_post('post.json')
print(response)
```

**Parameters:**
- `filename` (str): Path to the JSON file containing the post data

**Returns:** API response object or error message

---

### Logging

All function calls are automatically logged to `logs.txt` with:
- Timestamp of execution
- Function name
- Operation result
- Completion status

## Testing

Run the unit tests with pytest:

```bash
pytest tests/
```

Or with verbose output:

```bash
pytest tests/ -v
```

### Test Coverage

- **test_get_post()**: Verifies API retrieval of post #1
- **test_save_file()**: Validates file creation and content integrity

## Docker Usage

### Build Image

```bash
docker build -t json-downloader-plus .
```

### Run Container

```bash
docker run -v $(pwd):/app json-downloader-plus
```

Or on Windows PowerShell:

```powershell
docker run -v ${PWD}:/app json-downloader-plus
```

The Docker image includes:
- Python 3.x environment
- All dependencies (pytest, requests)
- Main application and tests

## Example Workflow

```python
from main import get_post, save_json, upload_post

# Step 1: Fetch a post from the API
post = get_post(5)

# Step 2: Save it locally
save_json('downloaded_post', post)

# Step 3: Modify and upload
modified_post = post
modified_post['title'] = 'Updated Title'
save_json('modified_post', modified_post)

# Step 4: Upload back to API
response = upload_post('modified_post_<timestamp>.json')
```

## Error Handling

All functions include comprehensive error handling:

- **TypeError**: Raised when invalid parameter types are provided
- **FileNotFoundError**: Raised when file operations fail
- **RuntimeError**: Raised for API communication errors
- **Timeout**: Handled for requests exceeding 10 seconds

## API Reference

### JSONPlaceholder Base URL
```
https://jsonplaceholder.typicode.com/posts
```

### Expected JSON Format
```json
{
  "title": "Post title",
  "body": "Post content",
  "userId": 1
}
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Author

Created by ovezthaking

## Changelog

### Version 1.0
- Initial release
- Core CRUD operations
- Automatic logging
- Docker support
- Unit tests

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'requests'"
**Solution**: Install dependencies with `pip install -r requirements.txt`

### Issue: "Error: Connection timeout"
**Solution**: Check your internet connection and JSONPlaceholder API availability

### Issue: Files not being created
**Solution**: Ensure you have write permissions in the application directory

## Support

For issues and questions, please open an issue on GitHub or contact the project maintainer.

---

**Happy JSON downloading! 🚀**
