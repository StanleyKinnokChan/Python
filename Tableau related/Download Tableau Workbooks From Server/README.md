<!-- PROJECT LOGO -->
<br />
<div align="center">
  <p align="center">
    Download Tableau Workbooks From Server
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

This script helps download a list of Tableau dashboard from tableau Server via Personal access token (PAT).The downloaded dashboard will have "_<current_date>" suffix attached to the dashboard name. 

Usage cases:
In Tableau server, "Dashboard version" only will be created if a dashboard is re-published and overwrite the previous one. However, if you fully refresh data extract, no version of the dashbaord with the old extract will be kept. If you want to revert the data back to previous version connected the dashboard, you need to ask the data engineer to repopulate the data from the snapshot, re-extract the data, reset the parameter, re-validate the data rendered in the dashboard. What we can do is to download the dashbaord before the refresh take place. If the latest version is not satisfied, we can just republish the downloaded dashboard. 

P.S. I write the functions inside a class so that more function may be added in the futher if I have time.

P.S.2 You can add the function so that the downloaded dashboards can be then saved in somewhere else as backup and development history (e.g. SharePoint, S3...)  

P.S.3 You can schedule the run of the script or set to be a part of data pipeline so that the dashboards are backuped after the extract refresh is done. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

These are the versions of python and packages when I crteated the script.
* python 3.8.0
* pandas==2.0.3
* tableauserverclient==0.32
* pathlib==1.0.1

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage
1. First, you need a Personal access token (PAT) to connect to your Tableau server. In Tableau server, go to Settings (you can access by clicking your personal icon on the top right conner - "My Account Settings"). In the Personal Access Tokens section, type in your token name and copy the generated secret. The secret should only be known by yourself. Use into system variables or other secret management system if it is share.
![image](https://i.imgur.com/Qu6JcCx.png)

2. Open the script `Download Tableau Workbooks From Server.py`. Here are 6 info you need to input in the script:
   1. directory path for saving the dashboard
   2. workbook_list
   3. token_name
   4. personal_access_token (the secret)
   5. site_id
   6. server_url

![image](https://i.imgur.com/FHxgi3z.png)

3. Run the script `py 'Download Tableau Workbooks From Server.py'`. The dashboards specified in the list within the script will be downloaded to to target location. 

Extra:
If you are using [virtual environment](!https://docs.python.org/3/library/venv.html) in Window, you can just put the script and setyp.bat in your virtual environment folder and click the setup.bat to run your script directly everytime you need it. If the application is stale, just press Enter button to resume. 
![image](https://i.imgur.com/1tf0xAf.png)

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

