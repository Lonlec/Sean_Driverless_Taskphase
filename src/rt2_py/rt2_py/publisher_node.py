
import rclpy
from rclpy.node import Node
from rt2_interfaces.msg import RT2String


class StringPublisher(Node):
    def __init__(self):
        super().__init__('string_publisher')
        self.publisher = self.create_publisher(
            RT2String, '/rt2_string', 10
        )

    def publish_string(self, text):
        msg = RT2String()
        msg.data = text
        self.publisher.publish(msg)
        self.get_logger().info(f'Published: {text}')


def main(args=None):
    rclpy.init(args=args)
    node = StringPublisher()

    try:
        while rclpy.ok():
            text = input(
                'Enter a string (or type exit to stop): '
            )

            if text.lower() == 'exit':
                break

            node.publish_string(text)
            rclpy.spin_once(node, timeout_sec=0.1)

    except (KeyboardInterrupt, EOFError):
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
