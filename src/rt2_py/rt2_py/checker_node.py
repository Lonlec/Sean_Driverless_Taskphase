
import rclpy
from rclpy.node import Node
from rt2_interfaces.msg import RT2String
from std_msgs.msg import Int32


class PalindromeChecker(Node):
    def __init__(self):
        super().__init__('palindrome_checker')

        self.result_publisher = self.create_publisher(
            Int32, '/palindrome_result', 10
        )

        self.string_subscription = self.create_subscription(
            RT2String,
            '/rt2_string',
            self.check_string,
            10
        )

        self.reply_subscription = self.create_subscription(
            RT2String,
            '/palindrome_reply',
            self.receive_reply,
            10
        )

    def check_string(self, msg):
        text = msg.data
        result = Int32()
        result.data = int(text == text[::-1])

        self.get_logger().info(
            f'Checking "{text}": {result.data}'
        )
        self.result_publisher.publish(result)

    def receive_reply(self, msg):
        self.get_logger().info(
            f'Palindrome result: {msg.data}'
        )


def main(args=None):
    rclpy.init(args=args)
    node = PalindromeChecker()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
