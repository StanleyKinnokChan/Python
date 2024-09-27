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

This is only a very simple gidget that I used to cosolidate the dashabord usage files `Who Has Seen.xlsx` downloaded from the server. Noted that if you have large number of dashboards, a better way should be querying the [Tableau server repository database](https://tableau.github.io/tableau-data-dictionary/2022.1/data_dictionary.html). The use case here is when you don't have the access right to the Tableau server repository database, and you download `Who Has Seen.xlsx` files from each of the dashboard for a quick analysis. Here is the consolidating tools. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

These are the versions of python and packages when I crteated the script.
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

