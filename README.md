# AI-Powered Code Generation System

An advanced AI-powered code generation system that converts natural language requirements into working code using multiple specialized agents.

## Features

- Natural language requirement analysis
- Automated architectural design
- Code generation with best practices
- Code integration and build system
- Web interface for easy interaction
- Redis-based memory management
- Comprehensive error handling

## Prerequisites

- Python 3.11 or higher
- Redis server
- OpenRouter API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-code-generator.git
cd ai-code-generator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
Create a `.env` file in the project root and add:
```
FLASK_SECRET_KEY=your-secret-key
OPENROUTER_API_KEY=your-openrouter-api-key
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0
```

## Redis Setup

1. Install Redis:
   - For Ubuntu/Debian: `sudo apt-get install redis-server`
   - For macOS: `brew install redis`
   - For Windows: Download from [Redis Windows](https://github.com/microsoftarchive/redis/releases)

2. Start Redis server:
   - Linux/macOS: `redis-server`
   - Windows: Start Redis service

## OpenRouter API Setup

1. Sign up at [OpenRouter](https://openrouter.ai/)
2. Create an API key
3. Add the API key to your `.env` file

## Usage

1. Start the application:
```bash
python app.py
```

2. Open your browser and navigate to `http://localhost:5000`

3. Enter your requirements in natural language

4. The system will:
   - Analyze requirements
   - Generate architecture
   - Create code
   - Build the final output

5. Find generated code in the `output` directory

## Project Structure

```
.
├── agents/             # Specialized AI agents
├── static/            # Static files (CSS, JS)
├── templates/         # HTML templates
├── utils/            # Utility functions
├── app.py            # Main application
├── config.py         # Configuration
└── routes.py         # Route handlers
```

## Configuration

The application can be configured through environment variables or `config.py`:

- `FLASK_SECRET_KEY`: Secret key for Flask sessions
- `OPENROUTER_API_KEY`: API key for OpenRouter
- `REDIS_HOST`: Redis server host
- `REDIS_PORT`: Redis server port
- `REDIS_DB`: Redis database number

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details
