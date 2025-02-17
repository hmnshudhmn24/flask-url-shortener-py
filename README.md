# URL Shortener

This is a simple URL shortener built with Flask. It allows users to shorten long URLs and redirect them using a generated short link.

## Features
- Generate short URLs using an MD5 hash function.
- Allow users to specify custom aliases for shortened URLs.
- Redirect users from short URLs to their original long URLs.
- Track the total number of shortened URLs.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/url-shortener.git
   cd url-shortener
   ```

2. Install dependencies:
   ```sh
   pip install flask
   ```

3. Run the application:
   ```sh
   python url_shortener.py
   ```

## API Endpoints

- `POST /shorten` – Shortens a long URL. 
  - **Request Body:** `{ "url": "https://example.com", "alias": "custom" }`
  - **Response:** `{ "short_url": "http://localhost:5000/custom" }`

- `GET /<short_url>` – Redirects to the original long URL.

- `GET /stats` – Returns statistics about shortened URLs.

## License
This project is licensed under the MIT License.
