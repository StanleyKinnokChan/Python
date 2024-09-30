<!-- PROJECT LOGO -->
<br />
<div align="center">
  <p align="center">
    Visualizing Tableau Calculation Dependencies and exporting list of fields 
    <br />
    <br />
    <a href="https://github.com/StanleyKinnokChan/Python/issues">Report Bug</a>
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

When working with numerous fields in Tableau, keeping track of field relationships and dependencies can be challenging. Opening each calculation manually to examine the formulas is time-consuming and inefficient. This script automates the process by generating a CSV file that lists all the calculations, and HTML files that visualize calculation dependencies as a network graph for each data source.

### Features

- **CSV Output**: Automatically generates a CSV file that lists all calculations across your Tableau workbook, allowing for quick inspection of formulas.
- **Dependency Visualization**: Creates interactive HTML files for each data source that visualize calculation dependencies as a network graph, providing a clear and comprehensive overview.
- **Field Statistics**: Provides additional statistics for fields, helping you better understand field usage and relationships within the workbook.
- **Impact Evaluation**: Enables you to evaluate the impact of changing a calculation on other related calculations by visualizing dependencies, helping you assess potential ripple effects throughout the workbook.

### Use Cases

- **Manage Complex Workbooks**: Easily track and manage field dependencies in workbooks with numerous calculated fields and data sources.
- **Save Time**: Avoid the hassle of opening each calculation manually to inspect its formula. Quickly view all necessary information in the CSV file or explore dependencies visually through the network graph.
- **Impact Analysis**: If you modify a calculation, this tool helps you understand how the change will affect other dependent calculations, making it easier to predict and mitigate any downstream issues.
- **Optimize Workflows**: Gain insights into your field structure and dependencies to optimize your Tableau workbook design, making it easier to debug and enhance performance.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

The script was created with the following versions:
* python 3.8.0
* pandas==2.0.3
* xml.etree.ElementTree==1.3.0
* pyvis==0.3.2

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage
1. Open the script `Tableau Calculation Dependencies.py` and change the workbook path in the script. Noted that the workbook must be in .twb format instead of .twbx.
![image](https://i.imgur.com/9XGfh8o.png)

2. Running the script: ``` py 'Tableau Calculation Dependencies.py'```. The field_csv and the HTMLs file will be saved in the directory where the workbook file located.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

Examples of HTML:
![image](https://i.imgur.com/GfqcA3W.png)

Examples of csv:
![image](https://i.imgur.com/bU3klRU.png)


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Stanley Chan - [LinkedIn](https://www.linkedin.com/in/staneykinnok-chan/) - stanleykinnok.chan@gmail.com

Project Link: [https://github.com/StanleyKinnokChan/Python/tree/main/Restful%20API](https://github.com/StanleyKinnokChan/Python/tree/main/Restful%20API)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members

