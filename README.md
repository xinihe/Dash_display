# Tailong Finance School Data Visualization Project

## Purpose

The purpose of this project is to develop a series of screen displays in the form of a web application to illustrate and visualize data from the Tailong Finance School of Zhejiang Gongshang University. This project leverages MySQL for data storage, Python for data processing, and Dash for data visualization and web application development.

## Tools and Technologies

- **MySQL**: For storing and managing the data.
- **Python**: For data processing and analysis.
- **Dash**: For creating interactive web applications to display the data.

## Project Structure

The project is organized into the following folders:

- **Assets**: Contains materials, figures, and other useful resources.
- **Code**: Contains the code developed for the screen displays.
- **Data**: Contains some sample data and data descriptions.

## Installation

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.x
- MySQL
- pip (Python package installer)

### Python Libraries

Install the required Python libraries using pip:

```bash
pip install dash plotly pandas sqlalchemy mysql-connector-python
```

### MySQL Database

Set up a MySQL database and import your data. Update the database connection details in your code as necessary.

## Usage

### Running the Application

1. **Set Up the Database**:

   - Ensure your MySQL database is running and contains the required data.
   - Update the database connection details in the code files.
2. **Run the Dash Application**:

   - Navigate to the `Code` directory.
   - Run the main application file (e.g., `app.py`):
     ```bash
     python app.py
     ```
3. **Access the Application**:

   - Open a web browser and navigate to `http://127.0.0.1:8050/` or `http://localhost:8050/` to view the application.

## Folder Details

### Assets

This folder contains materials, figures, and other useful resources used in the project. This may include images, icons, and other media files that are displayed in the web application.

### Code

This folder contains the Python code developed for the screen displays. Each file in this directory corresponds to different parts of the web application. Below is a brief description of key files:

- `app.py`: The main application file that initializes and runs the Dash app.
- `data_processing.ipynb`: Contains functions and scripts for processing data from the MySQL database.
- `dash_trial.ipynb`: Contains functions for generating various plots and visualizations using Dash and Plotly.

### Data

This folder contains sample data and data descriptions. It is used for testing and demonstration purposes. Below is a brief description of key files:

- `sample_data.csv`: A sample dataset used for initial testing and development.
- `data_access.ipynb`: A text file describing the sample data and its structure.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributors

For any questions or further information, please contact:

- Xinyu Song, Kun Yu, He Ni
- Tailong Finance School, Zhejiang Gongshang University
