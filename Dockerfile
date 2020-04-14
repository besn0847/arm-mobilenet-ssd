FROM besn0847/arm-tf-cv2:latest
MAINTAINER franck@besnard.mobi

RUN mkdir /ssd

COPY tensorflow-1.15.0-cp35-cp35m-linux_armv7l.whl /ssd/

RUN pip3 uninstall -y tensorflow && \
        pip3 install flask

RUN cd /ssd/ && \
	pip3 install tensorflow-1.15.0-cp35-cp35m-linux_armv7l.whl && \
	rm tensorflow-1.15.0-cp35-cp35m-linux_armv7l.whl

COPY frozen_inference_graph.pb /ssd/
COPY coco_labels.txt /ssd/
COPY app.py /ssd/
COPY startup.sh /

RUN chmod +x /startup.sh 

EXPOSE 5000

ENTRYPOINT ["/startup.sh"]

