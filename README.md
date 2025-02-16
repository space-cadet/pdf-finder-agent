# PDF-Agent GUI

This project is a graphical user interface (GUI) for the PDF-Agent application, built using Kivy. The GUI allows users to easily search for and download academic papers using their titles or DOIs.

## Project Structure

```
pdf-agent-gui
├── pdf_agent_gui
│   ├── __init__.py
│   ├── main.py
│   ├── pdf_agent.py
│   ├── kv
│   │   └── main.kv
│   └── assets
├── requirements.txt
└── README.md
```

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd pdf-agent-gui
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command in your terminal:
```
python -m pdf_agent_gui.main
```

## Features

- Search for papers by title or DOI.
- Download PDFs directly from Sci-Hub.
- User-friendly interface built with Kivy.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.