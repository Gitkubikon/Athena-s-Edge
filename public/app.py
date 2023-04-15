import logging
import sys
import time

from flask import Flask, render_template, request

app = Flask(__name__)

# Configure logging
log_file = "app.log"
logging.basicConfig(filename=log_file, level=logging.INFO)

# Enable debugging
app.config["DEBUG"] = True

# Define error handlers
@app.errorhandler(404)
def page_not_found(error):
    logging.error("Page not found: %s", request.url)
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server_error(error):
    logging.error("Server error: %s", error)
    return render_template("500.html"), 500

# Define routes
@app.route("/")
def index():
    return render_template("index.html")

# Define CLI commands
@app.cli.command("start")
def start_server():
    app.run(debug=app.config["DEBUG"])

@app.cli.command("monitor")
def monitor_server():
    while True:
        logging.info("Server is running")
        time.sleep(60)

@app.cli.command("stop")
def stop_server():
    func = request.environ.get("werkzeug.server.shutdown")
    if func is None:
        logging.error("Not running with the Werkzeug Server")
        sys.exit(1)
    func()
    logging.info("Server shut down gracefully")

if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])
