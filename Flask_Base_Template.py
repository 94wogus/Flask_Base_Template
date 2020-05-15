from app import create_app

app = create_app()

@app.route('/')
def index():
    return "<h1>This is FanRep Base Template Server<h1>"