# arm-mobilenet-ssd
A microservice for Raspberry PI running a MobileNet SSD v2 neural network to detect object in pictures 

To start the container with default config :
```bash
docker run -d --name arm-mobilenet-ssd -p 5000:5000 arm-mobilenet-ssd
```

Alternatively you can specify a conf diretory so you can change model weights easily :
```bash
docker run -d --name arm-mobilenet-ssd -v <conf_dir>:/conf -p 5000:5000 arm-mobilenet-ssd
```

To test an image with the MobileNet SSD WebService : 
```bash
curl -X PUT -F image_file=@./soccer.jpeg http://localhost:5000/process
```

#### Result is something like :
```bash
 Class: person with confidence: 0.984648585319519
 Class: person with confidence: 0.950616717338562
 Class: person with confidence: 0.9479445815086365
 Class: sports ball with confidence: 0.8936725854873657
 Class: person with confidence: 0.7434501647949219
 Class: baseball glove with confidence: 0.46374112367630005
 Class: sports ball with confidence: 0.35583359003067017
 Class: sports ball with confidence: 0.33586207032203674
```
 
Based on Alpine Linux 3.8, Python 3.5, Tensorflow Lite 1.15 and OpenCV 3.4.4.

#### Tributes
1. https://www.hackster.io/news/benchmarking-tensorflow-lite-on-the-new-raspberry-pi-4-model-b-3fd859d05b98 
2. https://medium.com/@aallan/benchmarking-edge-computing-ce3f13942245 

