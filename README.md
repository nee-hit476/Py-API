# Flask Books API (MVC Pattern)

A simple RESTful Books API built with **Flask** using the **MVC (Model-View-Controller)** architecture.  
CRUD operations (Create, Read, Update, Delete) on an in-memory book list.
Will implement DB next.
---

## 🏗 Project Structure

```bash
books_api/
├── app.py                 # Main entry point of the app
├── models/
│   └── book.py            # Book model (data & logic)
├── controllers/
│   └── book_controller.py # Controller (logic handling)
└── routes/
    └── book_routes.py     # Route definitions (URL endpoints)
```
### API Endpoints
| Method | Endpoint      | Description         |
| ------ | ------------- | ------------------- |
| GET    | `/books`      | Get all books       |
| GET    | `/books/<id>` | Get a specific book |
| POST   | `/books`      | Add a new book      |
| PUT    | `/books/<id>` | Update book details |
| DELETE | `/books/<id>` | Delete a book       |

## ⚙️ Setup Steps

### 1. Clone the Repository

```bash
git clone https://github.com/nee-hit476/Py-API.git
cd flask-books-api
```

### 2. Initialize the virtual enviroment
```bash
python -m venv venv
source venv/bin/activate     # On macOS/Linux
venv\Scripts\activate        # On Windows
```

### 3. Install the dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the API
```bash
python app.py
```


