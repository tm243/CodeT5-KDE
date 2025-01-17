
# CodeT5 KDE

This model is a CodeT5 model fine-tuned with an example dataset from KDE-C++ code. You can find the dataset here:

https://www.opendocstring.com/tool/ 

and select _full-dataset-KDE-kdeconnect-C++_

You are encouraged to improve and extend the dataset.

## Demo

Follow this link to try out the live model: https://www.opendocstring.com/#demo

## Setup

Make yourself a folder and install the required Python packages (Python 3.13):

```virtualenv .env```

```source .env/bin/activate```

```pip install -r requirements.txt```

In case you run into problems installing Pytorch on MacOS, you can try this:

```pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cpu```

and then continue with install -r requirements.txt

Now, before you run the model you need to download the weights and unpack them.
You can use the script:

./download_weights.sh

or do it manually:

```wget https://www.opendocstring.com/downloads/weights/codet5/saved-pretrained-kde-cpp-multisum-2023-05-10-06.tar.gz```

The weights will be in api/saved-pretrained-kde-...

## Run Inference

### Inference Test

A python code example for inference:

```python inference.py```

## Local Server

You can connect to this model via the REST api.

Run the local server:

```uvicorn api.rest:app --port 7999 --reload```

Make a POST request to get the summary of some code.

### Browser

Open demo.html in your browser and paste some code. It will make requests to the local server you just started.

### Python

```
import requests

result = requests.post('http://localhost:7999/summary', json={ 'code' : code })
summary = json.loads(result.text)['summary']
```

