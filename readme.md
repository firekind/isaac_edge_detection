# Edge Detection in Nvidia Isaac using Python

As it says on the tin.

![](res/example.png)

## Setup

Pull the docker image [`firekind/isaac:2020.2`](https://hub.docker.com/repository/docker/firekind/isaac) and start a container using:

```
$ $ docker run --mount source=isaac-sdk-build-cache,target=/root -v <path to project directory>:/workspace -w /workspace --runtime=nvidia --device <path to camera, if used. eg: /dev/video2> -it firekind/isaac:2020.2 /bin/bash
```

## Run

### Using V4L2 Camera
To run the application using a V4L2 camera, attach the camera and note its device id. Edit the `device_id` under the `config` section of [`app/graphs/edge_detection.app.json`](https://github.com/firekind/isaac_edge_detection/blob/master/app/graphs/edge_detection.app.json#L81) file. Then, run:

```
$ bazel run //app:edge_detection
```

and open `localhost:3000` on the browser to see the results.

### Using Isaac Sim (Unity 3d)

Make sure Isaac Sim (Unity 3d) is downloaded, and a scene from isaac sim is running. A scene can be started using:

```
~/isaac-sim-unity3d/builds$ ./sample.x86_64 --scene small_warehouse
```

And then run the application using:

```
$ bazel run //app:edge_detection -- --simulate
```

and open `localhost:3000` on the browser to see the results.
