

[![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/staneykinnok-chan/)



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://i.imgur.com/4x6hd0i.png" target="_blank" rel="noreferrer"> <img src="https://i.imgur.com/4x6hd0i.png" alt="Diagram" width="1000" height="321"/></a>
  <h3 align="center"></h3>

  <p align="center">
    REST API Application with FLASK and Postgres DB
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
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project demostrated my ability to build a REST API using Flask. The API interacted with the postgres DB hosted locally using docker.

After running the script `1. load data into postgres.py`, a new table `fashion_product` was created in the Postgres DB and the [csv data](https://www.kaggle.com/datasets/bhanupratapbiswas/fashion-products) related to the fashion product list was inserted into the table. 

When the application script `2. Flask API application.ipynb` is running, you can send GET/POST/PUT/DELETE request one by one by using the script `3. API request.ipynb`.

You can also query the data in Postgres DB using the PGadmin, which was hosted in localhost:5050.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* [docker](https://docs.docker.com/desktop/install/windows-install/) & [docker-compose](https://docs.docker.com/compose/install/) 
* python 3.8.0

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Clone the repo
   ```sh
   git clone https://github.com/StanleyKinnokChan/Python/tree/main/Restful%20API
   ```
2. If you use your own environment, install the package in requirements.txt
   ```sh
   py -m pip install -r requirements.txt
   ```
3. Run the Postgres DB & PGadain with docker
   ```sh
   docker compose up -d
   ```
4. Insert the sample dataset into Postgres
   ```py
   python "1. load data into postgres.py"
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

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



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Flask official documentation](https://flask.palletsprojects.com/en/3.0.x/api/)
* [Kaggle dataset](https://www.kaggle.com/datasets/bhanupratapbiswas/fashion-products)
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members

