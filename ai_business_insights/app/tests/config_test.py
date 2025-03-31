import pytest
from app import create_app

@pytest.fixture
def app():
    """Create and configure the app for testing."""
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app

@pytest.fixture
def client(app):
    """Create a test client."""
    return app.test_client()

@pytest.fixture
def runner(app):
    """Create a test runner."""
    return app.test_cli_runner()
