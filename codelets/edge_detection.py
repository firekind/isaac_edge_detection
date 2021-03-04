import cv2
from isaac import Codelet


class EdgeDetector(Codelet):
    def start(self):
        self.input_image = self.isaac_proto_rx("ImageProto", "input_image")
        self.output_image = self.isaac_proto_tx("ImageProto", "output_image")

        self.tick_on_message(self.input_image)

    def tick(self):
        image_tensor = self.input_image.message.tensor

        kernel_size = 3

        blurred = cv2.GaussianBlur(
            image_tensor,
            (kernel_size, kernel_size),
            sigmaX=0,
            sigmaY=0,
            borderType=cv2.BORDER_DEFAULT,
        )
        blurred = cv2.cvtColor(blurred, cv2.COLOR_RGB2GRAY)

        gradient_x = cv2.Sobel(blurred, cv2.CV_16S, 1, 0, ksize=kernel_size)
        gradient_y = cv2.Sobel(blurred, cv2.CV_16S, 0, 1, ksize=kernel_size)

        abs_gradient_x = cv2.convertScaleAbs(gradient_x)
        abs_gradient_y = cv2.convertScaleAbs(gradient_y)

        res_image = cv2.addWeighted(abs_gradient_x, 0.5, abs_gradient_y, 0.5, 0)

        tx_builder = self.output_image.init()
        tx_builder.proto.elementType = "uint8"
        tx_builder.proto.rows = res_image.shape[0]
        tx_builder.proto.cols = res_image.shape[1]
        tx_builder.proto.channels = 1
        tx_builder.proto.dataBufferIndex = 0
        tx_builder.buffers = [res_image]

        self.output_image.publish()
