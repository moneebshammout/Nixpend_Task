from project import createApp
from dotenv import load_dotenv
from os import getenv

# load environment variables.
load_dotenv()

app = createApp()

if __name__ == "__main__":
    app.run(debug=True, port=getenv("PORT"))
