from auth import create_app

import os
from dotenv import load_dotenv

load_dotenv()

app = create_app()  

if __name__ == '__main__':
    app.run(host=os.getenv("HOST_URI"), port=os.getenv("PORT_URI"), debug=True)