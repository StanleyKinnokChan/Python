<!-- PROJECT LOGO -->
<br />
<div align="center">
  <p align="center">
    Consolidating Dashboard Usage Files
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

This tool is a simple utility designed to consolidate multiple `Who Has Seen.xlsx` files, which are downloaded from Tableau dashboards. These files provide usage data and can be quickly merged for a consolidated analysis.

**Note:** For scenarios involving a large number of dashboards, it is more efficient to query the [Tableau server repository database](https://tableau.github.io/tableau-data-dictionary/2022.1/data_dictionary.html) directly. However, if you do not have access to the repository database and need to rely on manually downloading `Who Has Seen.xlsx` files from each dashboard, this tool streamlines the consolidation process, saving time and effort.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

The script was created with the following versions:
* python 3.8.0
* pandas==2.0.3
* openpyxl==3.1.2

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage
1. In Tableau server, go the target workbook. For each dashboard where you need the usage statistics, open "Who Has Seen This View" and download the .xlsx files from the "crosstab" option for the dashbaord. 
![image](https://i.imgur.com/PX1VVZW.png) ![image](https://i.imgur.com/7SHuWTk.png)

2. Open the script `Consolidating Dashboard Usage Files.py`. Change the directory path where `Who Has Seen.xlsx` files are saved
Running the script: `Consolidating Dashboard Usage Files.py'`. A consolidated csv file will be saved in the same directory.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

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

