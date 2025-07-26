# Prayer of the Moment

Christian prayer and devotion application for creating short prayers to full devotion sessions.

## Features

- CLI-based interface for prayer management
- PDF parsing for liturgical documents
- Database integration for prayer storage
- Print functionality for physical copies

## Development

### Prerequisites
- Python 3.13+
- uv package manager
- asdf version manager

### Setup
```bash
# Install dependencies
uv sync

# Run tests
uv run pytest tests/ -v

# Run application
uv run main.py --help
```

## Usage

```bash
# Show help
uv run main.py --help

# Run hello command
uv run main.py hello --name "Your Name"
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.
