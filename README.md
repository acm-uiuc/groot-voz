# groot-voz
> 🗣 Alexa, Burn Down the Office

[![Build Status](https://travis-ci.org/acm-uiuc/groot-voz.svg?branch=master)](https://travis-ci.org/acm-uiuc/groot-voz)

`groot-voz` is the basis for ACM's "office of the future" project. This client allows users to access services of the ACM intranet with a intuitive voice interface using Amazon Alexa.

With `groot-voz` you will be able to...

* Adjust ACM's custom office lighting system
* Control the music playing in the office
* Request items from our vending machine


[![Join the chat at https://acm-uiuc.slack.com/messages/C6XGZD212/](https://img.shields.io/badge/slack-groot-724D71.svg)](https://acm-uiuc.slack.com/messages/C6XGZD212/)

## Installation

1. Clone the repo.

    ```
    git clone https://github.com/acm-uiuc/groot-voz
    cd groot-voz
    ```

2. Install dependencies.

    ```
    pip install -r requirements.txt
    ```

3. Copy secrets template.

    ```
    cp secrets.template.py secrets.py
    ```

4. Fill out `GROOT_URL` and `GROOT_ACCESS_TOKEN` in secrets.py
5. Run the app.

    ```
    python app.py
    ```

## Setting Up the Alexa Skill
Follow [this](https://developer.amazon.com/blogs/post/Tx14R0IYYGH3SKT/Flask-Ask-A-New-Python-Framework-for-Rapid-Alexa-Skills-Kit-Development) tutorial on setting up the skill. You can find the speech assets necessary for setting up the Alexa Interaction Model in `speech_assets/`.

## Supported Commands
See [Sample Utterances](speech_assets/SampleUtterances.txt)


## Acknowledgment
We are thankful to [Amazon](https://github.com/amzn), especially to the [AWS](https://github.com/aws) team and the [Alexa](https://github.com/alexa) team for supporting this project.

[Amazon](https://www.amazon.com/) is a [proud sponsor](https://acm.illinois.edu/sponsors/sponsors_list) of ACM@UIUC. 
