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


This script automates the download of Tableau dashboards from a Tableau Server using a Personal Access Token (PAT). The downloaded dashboards will have a suffix in the format of `_<current_date>` attached to their names, making it easy to track when they were downloaded.

#### Use Cases

In Tableau Server, a "Dashboard Version" is only created when a dashboard is republished, overwriting the previous one. However, if you only refresh the data extract, no version of the dashboard with the old data is retained. This can be problematic if you need to revert the dashboard to a previous data state.

To avoid this, you can use this script to download the dashboard before refreshing the extract. If the latest version after the refresh is unsatisfactory, you can simply republish the downloaded version, saving significant time and effort compared to requesting a data engineer to restore snapshots and rebuild the data.

## Additional Features and Notes

- **Extensibility**: The script is designed with a class structure, allowing for additional functions to be added in the future.
- **Backup Capability**: You can extend the script to store the downloaded dashboards as a backup or for development history in locations such as SharePoint, S3, etc.
- **Automation**: The script can be scheduled to run automatically or integrated into a data pipeline, ensuring that dashboards are backed up immediately after a data extract refresh.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

The script was created with the following versions:
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

