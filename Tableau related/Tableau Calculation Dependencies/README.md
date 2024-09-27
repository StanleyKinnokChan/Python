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

When working with numerous fields in Tableau, keeping track of the fields and their dependencies can be quite challenging. It's also time-consuming to open each calculation individually just to examine the formulas and understand their function. This script generates a CSV file listing all the calculations, as well as HTML files for each data source that visualize calculation dependencies as a network graph, along with other statistics.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

These are the versions of python and packages when I crteated the script.
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

