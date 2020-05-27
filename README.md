# eLab Report Downloader

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/ShubhayanS/eLab-Reports-Downloader/graphs/commit-activity) 
[![GitHub issues](https://img.shields.io/github/issues/ShubhayanS/eLab-Reports-Downloader)](https://github.com/ShubhayanS/eLab-Reports-Downloader/issues)
[![GitHub forks](https://img.shields.io/github/forks/ShubhayanS/eLab-Reports-Downloader?style=social)](https://github.com/ShubhayanS/eLab-Reports-Downloader/network) [![GitHub stars](https://img.shields.io/github/stars/ShubhayanS/eLab-Reports-Downloader?style=social)](https://github.com/ShubhayanS/eLab-Reports-Downloader/stargazers)
 [![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)


## What it does?

This script is for downloading reports of eLab automatically thus saving the hassle of individually downloading the reports. However changing the url in the script, this script can work for other eLabs too.

```3rd year``` : OS (C, C++)

## :rocket: Getting Started 

### Disclaimer

Run this script at your own risk. The developers are no way responsible for unforseen issues with  your eLab. However, this script is tested extensively to avoid such circumstances.

### :octocat: Requirements

1. [Python 3](https://www.python.org/downloads/) installed on your system.
2. Python Selenium (It can be installed by opening CMD and running "pip install selenium")
3. Urllib Library (It can be installed by opening CMD and running "pip install urllib")
4. Latest version of Google Chrome (>83.0) installed.
5. Good Internet Connection - Any issues after running the script can be resolved by inproving your connection. Other issues can be accounted for due to server issues of the host.


### :running: Running

1. Clone the repository, and navigate to the downloaded folder `eLab-Reports-Downloader`.
2. Open CMD where the folder is located
3. Open in elab.py in your notepad editor or any editor of your preference. In the user name variable and pw variable type your registration number and password of elab  and dont forget to save the file in same location.
4. Again,in the cmd to run the downloader, type ```python elab.py``` .
5. Your eLab reports will automatically get downloaded and saved in Downloads (default chrome download location) in your PC.The elab reprts downloading starts from backwards i.e Question 100.

### :robot: Debugging

Sometimes due to server overloading the script might stop at certain questio - for instance if your script stops at Question  number 75 by throwing error in CMD, then you can rerun the script by changing the question number i.e if its Question number 75 so 100 - 75 = 25. That is the script can continue from where it stopped by changing from 1 to 25.

`qp = driver.find_element_by_css_selector('#svgChart > g > g:nth-child(4) > path:nth-child(1)')` 

to 

`qp = driver.find_element_by_css_selector('#svgChart > g > g:nth-child(4) > path:nth-child(25)')`


### :stars: Contribute

This project repository was made for personal use. Feel free to fork the repository and make changes corresponding to your eLab to improve support. Some pending work can be :

- [ ] Support for multiple elabs (example - ADA, Python etc)
- [ ] Package the web application also as a native app/ extension/ web-app.
- [ ] Cloud-hosted with full support on Heroku / Ripple / AWS
- [ ] Click-and-go : Allow user to be notified and PDF emailed when report generation is complete

### Current Maintainers

Show love to our work by "Star" or "Forking" this Repo :heart:

[ShubhayanS](https://github.com/ShubhayanS), [Soumya Sinha](https://github.com/Soumyasinha29), [Sagnik Chatterjee](https://github.com/sagnik20)


That's it. :smiley:

