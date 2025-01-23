import logging
from app import create_app
from waitress import serve

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("waitress")

app = create_app()

if __name__ == "__main__":
    host = "0.0.0.0" 
    port = 5000
    logger.info(f"Serving on http://127.0.0.1:{port}")
    serve(app, host=host, port=port, threads=2)