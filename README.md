<h1 align="center">Сервис по покупке сертификатов</h1>
<p align="center">
<img src="https://img.shields.io/badge/python-v3.8-blue?style=for-the-badge">
<img src="https://img.shields.io/badge/django-3.0-blue?style=for-the-badge" alt="">
<img src="https://img.shields.io/badge/SQL-MS--2019-blue?style=for-the-badge" alt="">
<img src="https://img.shields.io/badge/HTML-blue?style=for-the-badge" alt="">
<img src="https://img.shields.io/badge/CSS-blue?style=for-the-badge" alt="">
</p>
<p>
    В проекте есть следующие модули:
</p>
<ol>
    <li>Отправка почты</li>
    <li>Генерация Qr-кодов</li>
    <li>Взаимодействие с БД SQL 2019 MS</li>
    <li>Работа с эквайринговой системой электронных платежей Paykiper</li>
    <li>Публикация и редактирование информации по сертификата (в виде постов)</li>
</ol>
<p>
    pip list
</p>
    <li>Django</li>
    <li>django-ckeditor</li>
    <li>django-debug-toolbar</li>
    <li>gunicorn</li>
    <li>Pillow</li>
    <li>pyodbc</li>
    <li>qrcode</li>
    <li>requests</li>
</ul>

<p>
    Установка драйверов для взаимодействия с SQL Server-2019 MS
</p>
    sudo su
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

    #Download appropriate package for the OS version
    #Choose only ONE of the following, corresponding to your OS version

    #Ubuntu 16.04
    curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

    #Ubuntu 18.04
    curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

    #Ubuntu 20.04
    curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

    #Ubuntu 21.04
    curl https://packages.microsoft.com/config/ubuntu/21.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

    exit
    sudo apt-get update
    sudo ACCEPT_EULA=Y apt-get install -y msodbcsql17
    # optional: for bcp and sqlcmd
    sudo ACCEPT_EULA=Y apt-get install -y mssql-tools
    echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
    source ~/.bashrc
    # optional: for unixODBC development headers
    sudo apt-get install -y unixodbc-dev
