# JanataWifiTask
## URL: [Visit the Janata WiFi website](http://dip008.pythonanywhere.com/)

# Project Overview

This project aimed to build a basic web application using Python and Django for visualizing data from a JSON source, implementing CRUD functionalities, and creating visualizations using charts.

## Tasks Completed

### 1. Basic Web App with Django and JSON Data:
- Developed a web application displaying data from a JSON source in a tabular format on the home page.

### 2. Integration with SQL Server and CRUD Functionality:
- Loaded the data into an SQL server.
- Implemented CRUD functionalities allowing editable table rows.
- Separated JSON and SQL models, maintaining a clear distinction between the two.
- Version control via Git: Created 'jsonModel' branch for the initial step and 'sqlModel' branch for subsequent steps.

### 3. Enhanced Visualization:
- Added a line chart above the table, showcasing the 'close' column against sorted dates (X-axis).
- mImplemented a bar chart representing the 'volume' column (Y-axis) alongside the line chart.
- Incorporated a search option by the 'Trade Code', dynamically altering the charts' displayed data.

### 4. Additional Functionalities:
- Added the "Paginator" functionality to show 50 rows of the table at a time.
- As the total amount of data was huge, if the paginator was not used, it would take a long time to load the homepage.
- Added a "Add New Data" button to add new data.

## Learning and Challenges

### Learning:
- **Python and Django:** Strengthened proficiency in Python web development and Django framework.
- **SQL Integration:** Acquired knowledge of integrating data with an SQL server and managing separate models.
- **Chart Visualization:** Expanded skills in chart visualization libraries for creating interactive charts and multi-axis displays.
- **CRUD Implementation:** Learned to implement CRUD functionalities within a web application.

### Challenges:
- **Adapting to New Technologies:** Adapting to Python and Django for web development, especially if lacking prior experience in this stack.
- **SQL Integration:** Overcoming challenges in setting up and synchronizing data between Django and SQL servers.
- **Chart Customization:** Navigating the complexities of chart customization.

## Conclusion

This project was a significant learning experience, demonstrating adaptability in learning new technologies and leveraging existing programming skills to create a functional web application. It highlighted challenges in integrating different technologies while emphasizing the importance of clean code and efficient problem-solving.
