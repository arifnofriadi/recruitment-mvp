# Recruitment MVP

A minimal dashboard for recruitment teams to manage candidates and clients. This application consists of a Flask backend API and a Vue.js frontend interface.

## Prerequisites

Before installing and running this application, ensure you have the following installed on your system:

- Python 3.8 or higher
- Node.js 14 or higher
- npm (comes with Node.js)
- Git

## Installation

### Backend Setup

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```
   - On Windows:
     ```
     venv\Scripts\activate
     ```

4. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

5. Initialise the database:
   ```
   flask seed-db
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```
   cd ../frontend
   ```

2. Install the required Node.js packages:
   ```
   npm install
   ```

## Running the Application

### Backend

1. Ensure the virtual environment is activated (from the backend directory):
   ```
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate     # On Windows
   ```

2. Run the Flask development server:
   ```
   python run.py
   ```

The backend will be available at `http://127.0.0.1:5000`.

### Frontend

1. From the frontend directory, run the Vue.js development server:
   ```
   npm run serve
   ```

The frontend will be available at `http://localhost:8080`.

## Usage

- Open your web browser and navigate to `http://localhost:8080`.
- Use the interface to view, create, update, and delete candidates.
- Select candidates or clients to view their details in the panel.

## API Endpoints

The backend provides the following API endpoints:

- `GET /api/candidates` - Retrieve all candidates
- `GET /api/candidates/<id>` - Retrieve a specific candidate
- `POST /api/candidates` - Create a new candidate
- `PUT /api/candidates/<id>` - Update a candidate
- `DELETE /api/candidates/<id>` - Delete a candidate
- `GET /api/clients` - Retrieve all clients
- `GET /api/clients/<id>` - Retrieve a specific client

## Contributing

1. Fork the repository.
2. Create a new branch for your feature.
3. Make your changes and commit them.
4. Push to your fork and submit a pull request.

## Licence

This project is licensed under the MIT Licence.