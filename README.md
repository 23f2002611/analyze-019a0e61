# Data Processing and Reporting Project

This project demonstrates a simple data processing pipeline using Python and Pandas, with automated execution and reporting via GitHub Actions and GitHub Pages.

## Project Overview

The core of this project is a Python script (`execute.py`) that reads sales data from `data.csv`, performs several analytical calculations, and outputs the results in JSON format.

Key features:
- **Data Analysis**: Calculates total sales, average order value, top 5 products by sales, and total revenue by region.
- **Automated Workflow**: A GitHub Actions workflow (`.github/workflows/ci.yml`) automates the following:
    - Code linting with Ruff.
    - Execution of the `execute.py` script.
    - Publication of the generated `result.json` file to GitHub Pages.
- **Static Site**: A minimal `index.html` page is provided to serve as a landing page for the project, linking to the generated `result.json`.

## Files in this Repository

- `execute.py`: The Python script responsible for data processing. It reads `data.csv` and outputs a JSON summary.
- `data.csv`: The input data file, converted from `data.xlsx`.
- `.github/workflows/ci.yml`: The GitHub Actions workflow definition.
- `README.md`: This README file.
- `LICENSE`: The MIT License for this project.
- `index.html`: A simple HTML page deployed to GitHub Pages.
- `styles.css`: A CSS file for basic styling.
- `app.js`: An empty JavaScript file (for completeness).

## How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd <your-repo-name>
    ```
2.  **Set up a Python 3.11+ environment:**
    It's recommended to use a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows: `venv\Scripts\activate`
    ```
3.  **Install dependencies:**
    ```bash
    pip install pandas==2.3.0 ruff
    ```
4.  **Run the data processing script:**
    ```bash
    python execute.py > result.json
    ```
    This will generate `result.json` in your current directory.

5.  **Run Ruff linter:**
    ```bash
    ruff check .
    ```

## GitHub Actions Workflow

The `.github/workflows/ci.yml` workflow is triggered on every `push` to the `main` branch. It performs the following steps:

1.  **Checkout repository**: Fetches the code.
2.  **Set up Python 3.11**: Configures the Python environment.
3.  **Install dependencies**: Installs `pandas` and `ruff`.
4.  **Run Ruff**: Lints the Python code.
5.  **Execute Python script**: Runs `execute.py` and redirects its output to `result.json`.
6.  **Setup Pages**: Configures the GitHub Pages environment.
7.  **Upload Pages artifact**: Uploads all relevant files (including `index.html`, `styles.css`, `app.js`, and `result.json`) as an artifact for GitHub Pages.
8.  **Deploy to GitHub Pages**: Publishes the artifact to your repository's GitHub Pages site.

## Accessing the Results

After a successful CI/CD run, the `result.json` file and the `index.html` page will be published to GitHub Pages.

You can typically find the published content at:
`https://<YOUR_GITHUB_USERNAME>.github.io/<YOUR_REPOSITORY_NAME>/`

And the generated JSON result at:
`https://<YOUR_GITHUB_USERNAME>.github.io/<YOUR_REPOSITORY_NAME>/result.json`

Replace `<YOUR_GITHUB_USERNAME>` and `<YOUR_REPOSITORY_NAME>` with your actual GitHub details.