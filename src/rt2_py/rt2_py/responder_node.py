
import rclpy
from rclpy.node import Node
from rt2_interfaces.msg import RT2String
from std_msgs.msg import Int32


class ResultResponder(Node):
    def __init__(self):
        super().__init__('result_responder')

        self.reply_publisher = self.create_publisher(
            RT2String, '/palindrome_reply', 10
        )

        self.result_subscription = self.create_subscription(
            Int32,
            '/palindrome_result',
            self.respond,
            10
        )

    def respond(self, msg):
        reply = RT2String()
        reply.data = 'Yes' if msg.data == 1 else 'No'
        self.reply_publisher.publish(reply)

        self.get_logger().info(
            f'Received {msg.data}; replying "{reply.data}"'
        )


def main(args=None):
    rclpy.init(args=args)
    node = ResultResponder()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
